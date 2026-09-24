"""
CharacterForge Style Transfer Node
===================================

Nodo che prende l'IMMAGINE output dal character sheet
e la trasforma applicando LoRA combinabili.

Il nodo preserva completamente la struttura dell'immagine
(identitÃ , pose, layout) cambiando SOLO lo stile visivo.

CHANGELOG v2.2.0:
- IL MENU style_preset ORA INCLUDE I 128 STILI ANIME
  del database preset_styles/anime oltre agli 11 preset
  storici. Selezionabili direttamente dal menu a tendina
  (digitare per cercare, es. "araki", "toriyama").
- Se uno stile esiste sia come preset storico sia nel
  database anime (es. "ghibli", "retro_80s_anime"),
  vince la versione del DATABASE (quella curata da te).
- Fallback sicuro: se il database non si carica, il nodo
  continua a funzionare con i soli 11 preset storici.

CHANGELOG v2.1.2:
- FIX: _encode_style_prompt delega al nodo core
  CLIPTextEncode di ComfyUI (compatibile con Krea2/Qwen3VL)

Pipeline:
1. Riceve IMMAGINE dal SaveImage precedente
2. Codifica immagine in latent (preservando struttura)
3. Applica stile tramite conditioning + LoRA
4. Calcola denoise ottimizzato automaticamente
5. Output: Conditioning + Latent + Denoise per KSampler
"""

import os
import sys
import torch
import numpy as np


# ============================================
# CARICAMENTO DATABASE 128 STILI ANIME
# ============================================

def _load_anime_styles():
    """Carica il database preset_styles/anime con fallback sicuri."""
    # Percorso 1: import relativo (standard quando caricato da ComfyUI)
    try:
        from ..preset_styles.anime import ANIME_STYLES
        return ANIME_STYLES
    except Exception:
        pass
    # Percorso 2: aggiunge la root del pacchetto a sys.path
    try:
        _pkg_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if _pkg_root not in sys.path:
            sys.path.insert(0, _pkg_root)
        from preset_styles.anime import ANIME_STYLES
        return ANIME_STYLES
    except Exception as e:
        print(f"[CharacterForge StyleTransfer] Database anime non disponibile "
              f"({type(e).__name__}: {e}) - uso solo i preset incorporati")
        return {}


ANIME_STYLES = _load_anime_styles()
ANIME_STYLE_NAMES = sorted(ANIME_STYLES.keys()) if ANIME_STYLES else []
# ============================================
# CARICAMENTO DATABASE 202 STILI CINEMATIC
# ============================================

def _load_cinematic_styles():
    """Carica il database cinematic con fallback sicuri."""
    try:
        from ..preset_styles.cinematic import CINEMATIC_STYLES
        return CINEMATIC_STYLES
    except Exception:
        pass

    try:
        _pkg_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if _pkg_root not in sys.path:
            sys.path.insert(0, _pkg_root)

        from preset_styles.cinematic import CINEMATIC_STYLES
        return CINEMATIC_STYLES

    except Exception as e:
        print(
            f"[CharacterForge StyleTransfer] Database cinematic non disponibile "
            f"({type(e).__name__}: {e})"
        )
        return {}


CINEMATIC_STYLES = _load_cinematic_styles()
CINEMATIC_STYLE_NAMES = (
    sorted(CINEMATIC_STYLES.keys())
    if CINEMATIC_STYLES
    else []
)

print(
    f"[CharacterForge StyleTransfer] "
    f"Database cinematic: {len(CINEMATIC_STYLE_NAMES)} stili"
)


def _extract_anime_prompt(style_dict):
    """Estrae la descrizione testuale dello stile dal dict del database."""
    if not style_dict:
        return ""
    parts = []
    for key in ("prompt", "positive_prompt", "style_prompt", "description", "name"):
        val = style_dict.get(key)
        if isinstance(val, str) and val.strip():
            parts.append(val.strip())
            break
    tags = style_dict.get("tags") or style_dict.get("keywords")
    if isinstance(tags, (list, tuple)):
        parts.append(", ".join(str(t) for t in tags))
    elif isinstance(tags, str) and tags.strip():
        parts.append(tags.strip())
    meta = [str(style_dict[k]) for k in ("artist", "studio", "era", "genre")
            if style_dict.get(k)]
    if meta:
        parts.append(", ".join(meta))
    return ", ".join(p for p in parts if p)


class CharacterForgeStyleTransferNode:
    """
    Nodo Style Transfer per CharacterForge.

    Prende l'immagine character sheet e prepara
    conditioning + latent per style transfer con
    preservazione automatica della struttura.

    Calcola AUTOMATICAMENTE il denoise ottimale in base
    allo stile scelto e al livello di preservazione.
    """

    # Configurazioni preset di stile STORICHE (11)
    # (se il nome esiste anche nel database anime, vince il database)
    STYLE_CONFIGS = {
        "cartoon": {
            "description": "2D Cartoon, cel shading, colori piatti",
            "recommended_lora": ["cartoon_style.safetensors"],
            "lora_strength": 0.8,
            "denoise_base": 0.25,
            "structure_weight": 0.9,
            "color_boost": 1.3,
            "prompt": "2D cartoon style, cel shading, clean bold outlines, flat vibrant colors, cartoon character design, animated character aesthetic"
        },
        "anime": {
            "description": "Anime/Manga style, lineart pulito",
            "recommended_lora": ["anime_style.safetensors"],
            "lora_strength": 0.7,
            "denoise_base": 0.30,
            "structure_weight": 0.8,
            "color_boost": 1.4,
            "prompt": "anime style, manga aesthetic, clean lineart, cel shading, expressive anime eyes, Japanese animation quality"
        },
        "ghibli": {
            "description": "Studio Ghibli watercolor, toni caldi",
            "recommended_lora": ["ghibli_style.safetensors"],
            "lora_strength": 0.6,
            "denoise_base": 0.20,
            "structure_weight": 0.9,
            "color_boost": 1.1,
            "prompt": "Studio Ghibli style, hand-painted watercolor background, soft warm lighting, Hayao Miyazaki aesthetic, anime film quality"
        },
        "comic": {
            "description": "American Comic Book, inchiostro forte",
            "recommended_lora": ["comic_style.safetensors"],
            "lora_strength": 0.7,
            "denoise_base": 0.28,
            "structure_weight": 0.85,
            "color_boost": 1.5,
            "prompt": "American comic book style, bold ink outlines, halftone shading, dramatic comic lighting, Marvel DC aesthetic"
        },
        "watercolor": {
            "description": "Watercolor painting, bordi sfumati",
            "recommended_lora": ["watercolor_style.safetensors"],
            "lora_strength": 0.5,
            "denoise_base": 0.18,
            "structure_weight": 0.95,
            "color_boost": 0.9,
            "prompt": "watercolor painting style, soft blended edges, visible brush strokes, muted pastel palette, artistic hand-painted aesthetic"
        },
        "pixel_art": {
            "description": "Retro Pixel Art 16-bit",
            "recommended_lora": ["pixel_art_style.safetensors"],
            "lora_strength": 0.9,
            "denoise_base": 0.22,
            "structure_weight": 1.0,
            "color_boost": 1.2,
            "prompt": "pixel art style, 16-bit retro aesthetic, limited color palette, crisp pixel edges, retro game character design"
        },
        "retro_80s_anime": {
            "description": "1980s Retro Anime, VHS grain, cel animation",
            "recommended_lora": ["retro_80s_anime_lora.safetensors"],
            "lora_strength": 0.8,
            "denoise_base": 0.28,
            "structure_weight": 0.88,
            "color_boost": 1.15,
            "prompt": "1980s retro anime style, vintage cel animation aesthetic, hand-drawn animation quality, VHS grain texture, analog film photography look, retro color grading with warm oranges and cool blues, 80s anime character design with sharp angular features, dramatic 80s lighting with strong contrast, retro anime film grain, 16mm film aesthetic, vintage Japanese animation from the 1980s, reminiscent of Akira and Fist of the North Star era"
        },
        "retro_80s_photography": {
            "description": "1980s Film Photography, analog warmth",
            "recommended_lora": ["retro_80s_film_lora.safetensors"],
            "lora_strength": 0.6,
            "denoise_base": 0.22,
            "structure_weight": 0.92,
            "color_boost": 1.1,
            "prompt": "1980s film photography aesthetic, analog 35mm film grain, vintage Kodachrome colors, warm golden hour lighting, retro color grading with muted highlights and deep shadows, 80s photographic style, VHS home video quality, soft focus background, nostalgic vintage look, old school photography with natural imperfections, film burn effects"
        },
        "vhs_retro": {
            "description": "VHS Retro, analog video aesthetic",
            "recommended_lora": ["vhs_retro_lora.safetensors"],
            "lora_strength": 0.75,
            "denoise_base": 0.25,
            "structure_weight": 0.90,
            "color_boost": 1.2,
            "prompt": "VHS retro aesthetic, analog video tape quality, scan lines, tracking errors, chromatic aberration, 1980s home video look, degraded video quality with authentic imperfections, VHS tape noise, analog distortion, retro CRT television display, vintage video artifacts"
        },
        "synthwave_80s": {
            "description": "Synthwave 80s, neon retro-futurism",
            "recommended_lora": ["synthwave_lora.safetensors"],
            "lora_strength": 0.7,
            "denoise_base": 0.30,
            "structure_weight": 0.85,
            "color_boost": 1.6,
            "prompt": "synthwave 80s aesthetic, neon pink and cyan color palette, retro-futuristic design, 1980s sci-fi anime style, chrome and neon elements, sunset gradient backgrounds, grid floors, retro futuristic character design, cyberpunk 80s aesthetic, Miami Vice color grading"
        },
        "custom_combo": {
            "description": "Combinazione LoRA personalizzata",
            "recommended_lora": ["any_lora.safetensors"],
            "lora_strength": 0.7,
            "denoise_base": 0.25,
            "structure_weight": 0.85,
            "color_boost": 1.2,
            "prompt": ""
        }
    }

    # Lista combinata del menu: preset storici (non duplicati) + stili anime
    _BUILTIN_ORDER = ["cartoon", "anime", "ghibli", "comic", "watercolor",
                      "pixel_art", "retro_80s_anime", "retro_80s_photography",
                      "vhs_retro", "synthwave_80s", "custom_combo"]
    PRESET_CHOICES = (
        [n for n in _BUILTIN_ORDER if n not in ANIME_STYLES]
        + ANIME_STYLE_NAMES
        + CINEMATIC_STYLE_NAMES
    )

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE", {
                    "tooltip": "Immagine character sheet dal SaveImage precedente"
                }),
                "model": ("MODEL", {
                    "tooltip": "Modello con LoRA stile applicati"
                }),
                "clip": ("CLIP", {
                    "tooltip": "CLIP con LoRA stile applicati"
                }),
                "vae": ("VAE", {
                    "tooltip": "VAE per encoding immagine"
                }),
                "style_preset": (s.PRESET_CHOICES, {
                    "default": "retro_80s_anime",
                    "tooltip": "Stile da applicare: 11 preset storici + "
                               "128 stili anime del database. Digita per cercare."
                }),
                "style_intensity": ("FLOAT", {
                    "default": 0.7,
                    "min": 0.0,
                    "max": 1.5,
                    "step": 0.01,
                    "tooltip": "IntensitÃ  applicazione stile (0.0-1.5)"
                }),
                "structure_preservation": ("FLOAT", {
                    "default": 0.9,
                    "min": 0.5,
                    "max": 1.0,
                    "step": 0.01,
                    "tooltip": "Preservazione struttura immagine (0.5-1.0, ALTO consigliato)"
                }),
            },
            "optional": {
                "custom_prompt": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Prompt custom (ha prioritÃ  sul preset). Usare con custom_combo."
                }),
                "extra_style_keywords": ("STRING", {
                    "default": "",
                    "tooltip": "Keywords aggiuntive sommate al prompt dello stile"
                }),
            }
        }

    RETURN_TYPES = ("CONDITIONING", "LATENT", "FLOAT", "STRING",)
    RETURN_NAMES = ("conditioning", "latent", "optimized_denoise", "style_prompt",)
    FUNCTION = "prepare_style_transfer"
    CATEGORY = "CharacterForge/Style"

    def prepare_style_transfer(self, images, model, clip, vae,
                             style_preset, style_intensity,
                             structure_preservation,
                             custom_prompt="", extra_style_keywords=""):
        """
        Prepara tutto per style transfer con preservazione struttura.
        """

        # Validazione input
        if images is None:
            raise ValueError("[CharacterForge StyleTransfer] Immagine non valida o vuota")

        if model is None or clip is None or vae is None:
            raise ValueError("[CharacterForge StyleTransfer] Model, CLIP o VAE non collegati")

        # 1. Risolvi lo stile (il DATABASE anime ha prioritÃ  sui preset storici)
        if style_preset in CINEMATIC_STYLES:
            cinematic_style = CINEMATIC_STYLES[style_preset]
            base_prompt = cinematic_style.get("prompt", "")
            denoise_base = float(cinematic_style.get("denoise", 0.25))
            source = "cinematic_db"

        elif style_preset in ANIME_STYLES:
            anime_style = ANIME_STYLES[style_preset]
            base_prompt = _extract_anime_prompt(anime_style)
            denoise_base = float(anime_style.get("denoise_base",
                                                 anime_style.get("denoise", 0.28)))
            source = "anime_db"


        elif style_preset in self.STYLE_CONFIGS:
            cfg = self.STYLE_CONFIGS[style_preset]
            base_prompt = cfg.get("prompt", "")
            denoise_base = cfg.get("denoise_base", 0.25)
            source = "builtin"
        else:
            raise ValueError(
                f"[CharacterForge StyleTransfer] Stile '{style_preset}' non riconosciuto. "
                f"Disponibili {len(self.PRESET_CHOICES)} stili."
            )

        # 2. Calcola denoise OTTIMIZZATO
        optimized_denoise = self._calculate_optimal_denoise(
            denoise_base,
            style_intensity,
            structure_preservation
        )

        # 3. Costruisci prompt stile
        style_prompt = self._build_style_prompt(
            base_prompt,
            custom_prompt,
            extra_style_keywords,
            structure_preservation
        )

        # 4. Codifica immagine in latent (PRESERVA STRUTTURA)
        latent = self._encode_image_preserving_structure(
            images,
            vae,
            structure_preservation
        )

        # 5. Codifica prompt in conditioning (delega al core ComfyUI)
        conditioning = self._encode_style_prompt(
            clip,
            style_prompt,
            style_intensity
        )

        print(f"[CharacterForge StyleTransfer] stile='{style_preset}' ({source}) "
              f"intensitÃ ={style_intensity} preservazione={structure_preservation} "
              f"-> denoise={optimized_denoise}")

        return (conditioning, latent, optimized_denoise, style_prompt)

    def _calculate_optimal_denoise(self, denoise_base, style_intensity, structure_preservation):
        """
        Calcola il denoise per ottenere un trasferimento stilistico realmente visibile
        mantenendo il controllo sulla struttura.

        style_intensity aumenta direttamente la forza della trasformazione.
        structure_preservation riduce moderatamente il denoise senza annullare lo stile.

        Range sicuro: 0.12 - 0.45
        """
        intensity_factor = 0.75 + (style_intensity * 0.5)
        preservation_factor = 1.0 - (structure_preservation - 0.5) * 0.35

        optimized_denoise = (
            denoise_base
            * intensity_factor
            * preservation_factor
        )

        optimized_denoise = max(0.12, min(0.45, optimized_denoise))
        return round(optimized_denoise, 3)

    def _build_style_prompt(self, base_prompt, custom_prompt,
                          extra_keywords, structure_preservation):
        """Costruisce prompt completo: stile + keywords + preservazione."""
        prompt_parts = []

        if custom_prompt and custom_prompt.strip():
            # Custom prompt ha prioritÃ 
            prompt_parts.append(custom_prompt.strip())
        elif base_prompt:
            prompt_parts.append(base_prompt)

        if extra_keywords and extra_keywords.strip():
            prompt_parts.append(extra_keywords.strip())

        # Preservazione strutturale senza ostacolare il trasferimento stilistico.
        # La struttura viene protetta principalmente dal latent + denoise controllato.
        if structure_preservation >= 0.9:
            prompt_parts.extend([
                "same character identity",
                "same pose and overall composition",
                "same framing and character sheet layout",
                "preserve the original structure while applying the requested art style",
                "preserve recognizable facial features and body proportions"
            ])
        elif structure_preservation >= 0.8:
            prompt_parts.extend([
                "same character identity",
                "same pose and composition",
                "preserve the main character sheet structure",
                "apply the requested art style consistently"
            ])
        elif structure_preservation >= 0.7:
            prompt_parts.extend([
                "recognizable same character",
                "similar composition",
                "strong style adaptation"
            ])
        else:
            prompt_parts.append(
                "creative style interpretation with composition freedom"
            )

        return ", ".join(prompt_parts)

    def _encode_image_preserving_structure(self, images, vae, preservation):
        """Codifica immagine in latent. La preservazione avviene con denoise basso."""
        if not isinstance(images, torch.Tensor):
            raise ValueError(
                f"[CharacterForge StyleTransfer] Formato immagine non supportato: "
                f"{type(images)}. Atteso torch.Tensor IMAGE."
            )

        if images.dim() != 4:
            raise ValueError(
                f"[CharacterForge StyleTransfer] Dimensioni immagine inattese: "
                f"{tuple(images.shape)}. Atteso [B, H, W, C]."
            )

        # Rimuovi canale alpha se presente (il VAE vuole RGB)
        if images.shape[-1] == 4:
            images = images[:, :, :, :3]

        latent_samples = vae.encode(images)
        return {"samples": latent_samples}

    def _encode_style_prompt(self, clip, style_prompt, style_intensity):
        """
        FIX v2.1.2: delega al nodo core CLIPTextEncode di ComfyUI,
        compatibile con TUTTI i tipi di CLIP (Krea2/Qwen3VL incluso).
        Fallback multipli se la delega non riesce.
        """
        # Percorso 1: delega al core
        try:
            from nodes import CLIPTextEncode as _CoreCLIPTextEncode
            result = _CoreCLIPTextEncode().encode(clip, style_prompt)
            if isinstance(result, (tuple, list)) and len(result) > 0:
                return result[0]
            return result
        except Exception as e:
            print(f"[CharacterForge StyleTransfer] Delega a CLIPTextEncode core "
                  f"fallita ({type(e).__name__}: {e}), uso fallback manuale")

        # Percorso 2: encode_from_tokens con pooled
        tokens = clip.tokenize(style_prompt)
        try:
            out = clip.encode_from_tokens(tokens, return_pooled=True)
            if isinstance(out, (tuple, list)) and len(out) == 2:
                cond, pooled = out
                return [[cond, {"pooled_output": pooled}]]
        except Exception:
            pass

        # Percorso 3: scheduled, gestisce 1 o 2 valori
        try:
            out = clip.encode_from_tokens_scheduled(tokens)
            if isinstance(out, (tuple, list)):
                if len(out) >= 2:
                    return [[out[0], {"pooled_output": out[1]}]]
                return [[out[0], {}]]
            return [[out, {}]]
        except Exception:
            pass

        # Percorso 4: ultima spiaggia
        cond = clip.encode_from_tokens(tokens)
        return [[cond, {}]]

    @classmethod
    def IS_CHANGED(s, images, model, clip, vae, style_preset,
                  style_intensity, structure_preservation,
                  custom_prompt="", extra_style_keywords=""):
        return float("NaN")


class CharacterForgeLoRAStyleCombinator:
    """
    Combina multiple LoRA per creare stili unici (documentazione/pianificazione).
    Il caricamento LoRA effettivo avviene con i nodi LoraLoader standard.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL", {
                    "tooltip": "Modello base"
                }),
                "clip": ("CLIP", {
                    "tooltip": "CLIP base"
                }),
                "lora_1_name": (["none", "cartoon_style.safetensors", "anime_style.safetensors",
                               "ghibli_style.safetensors", "comic_style.safetensors",
                               "retro_80s_anime_lora.safetensors", "retro_80s_film_lora.safetensors",
                               "vhs_retro_lora.safetensors", "synthwave_lora.safetensors"], {
                    "default": "retro_80s_anime_lora.safetensors",
                    "tooltip": "Primo LoRA stile (principale)"
                }),
                "lora_1_strength": ("FLOAT", {
                    "default": 0.8,
                    "min": 0.0,
                    "max": 1.5,
                    "step": 0.01,
                    "tooltip": "Forza primo LoRA (principale)"
                }),
            },
            "optional": {
                "lora_2_name": (["none", "cartoon_style.safetensors", "anime_style.safetensors",
                               "ghibli_style.safetensors", "watercolor_style.safetensors",
                               "vhs_retro_lora.safetensors", "retro_80s_film_lora.safetensors"], {
                    "default": "none",
                    "tooltip": "Secondo LoRA stile (combinazione)"
                }),
                "lora_2_strength": ("FLOAT", {
                    "default": 0.5,
                    "min": 0.0,
                    "max": 1.5,
                    "step": 0.01,
                    "tooltip": "Forza secondo LoRA"
                }),
                "lora_3_name": (["none", "comic_style.safetensors", "pixel_art_style.safetensors",
                               "synthwave_lora.safetensors", "vhs_retro_lora.safetensors"], {
                    "default": "none",
                    "tooltip": "Terzo LoRA stile (combinazione)"
                }),
                "lora_3_strength": ("FLOAT", {
                    "default": 0.3,
                    "min": 0.0,
                    "max": 1.5,
                    "step": 0.01,
                    "tooltip": "Forza terzo LoRA"
                }),
            }
        }

    RETURN_TYPES = ("MODEL", "CLIP", "STRING",)
    RETURN_NAMES = ("model", "clip", "combination_info",)
    FUNCTION = "combine_lora_styles"
    CATEGORY = "CharacterForge/Style"

    def combine_lora_styles(self, model, clip, lora_1_name, lora_1_strength,
                          lora_2_name="none", lora_2_strength=0.5,
                          lora_3_name="none", lora_3_strength=0.3):
        combination_info = {
            "controller": "LoRAStyleCombinator",
            "lora_applied": [],
            "status": "ready"
        }

        if lora_1_name != "none":
            combination_info["lora_applied"].append({
                "name": lora_1_name, "strength": lora_1_strength, "role": "primary"
            })
        if lora_2_name != "none" and lora_2_name != lora_1_name:
            combination_info["lora_applied"].append({
                "name": lora_2_name, "strength": lora_2_strength, "role": "secondary"
            })
        if lora_3_name != "none" and lora_3_name != lora_1_name and lora_3_name != lora_2_name:
            combination_info["lora_applied"].append({
                "name": lora_3_name, "strength": lora_3_strength, "role": "tertiary"
            })

        total_strength = lora_1_strength + lora_2_strength + lora_3_strength
        if total_strength > 3.0:
            combination_info["warning"] = "Somma strength alta, rischio conflitti"

        combination_info["suggestions"] = self._get_style_suggestions(
            lora_1_name, lora_2_name, lora_3_name
        )

        return (model, clip, str(combination_info))

    def _get_style_suggestions(self, lora_1, lora_2, lora_3):
        suggestions = []
        tested_combos = {
            ("retro_80s_anime_lora.safetensors", "vhs_retro_lora.safetensors"):
                "Anime 80s autentico con grana VHS",
            ("retro_80s_anime_lora.safetensors", "retro_80s_film_lora.safetensors"):
                "Anime 80s con estetica fotografica",
            ("retro_80s_anime_lora.safetensors", "synthwave_lora.safetensors"):
                "Anime 80s retro-futuristico",
            ("anime_style.safetensors", "ghibli_style.safetensors"):
                "Anime moderno con atmosfera Ghibli",
            ("cartoon_style.safetensors", "comic_style.safetensors"):
                "Cartoon con influenze comic",
        }
        combo_key = (lora_1, lora_2)
        if combo_key in tested_combos:
            suggestions.append(tested_combos[combo_key])
        if not suggestions:
            suggestions.append("Combinazione custom, sperimentale")
        return suggestions

    @classmethod
    def IS_CHANGED(s, model, clip, lora_1_name, lora_1_strength,
                  lora_2_name="none", lora_2_strength=0.5,
                  lora_3_name="none", lora_3_strength=0.3):
        return float("NaN")


# Registrazione nodi per uso standalone
NODE_CLASS_MAPPINGS = {
    "CharacterForgeStyleTransferNode": CharacterForgeStyleTransferNode,
    "CharacterForgeLoRAStyleCombinator": CharacterForgeLoRAStyleCombinator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CharacterForgeStyleTransferNode": "Style Transfer Node",
    "CharacterForgeLoRAStyleCombinator": "LoRA Style Combinator"
}

print(f"[CharacterForge] style_transfer_node v2.2.0 caricato "
      f"({len(ANIME_STYLE_NAMES)} stili anime + {len([n for n in CharacterForgeStyleTransferNode._BUILTIN_ORDER if n not in ANIME_STYLES])} preset)")





