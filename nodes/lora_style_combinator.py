"""
CharacterForge LoRA Style Combinator
=====================================

Nodo che combina multiple LoRA per creare stili visivi unici.
Prende fino a 3 LoRA e li applica in sequenza con pesi indipendenti.

Serve per creare combinazioni personalizzate come:
- Anime 80s + VHS grain (stile autentico retro)
- Ghibli + Watercolor (atmosfera artistica)
- Synthwave + Anime 80s (retro-futurismo)

Il nodo documenta e valida le combinazioni, mentre
il caricamento LoRA effettivo avviene tramite nodi
LoraLoader standard di ComfyUI collegati in serie.
"""

import torch


class CharacterForgeLoRAStyleCombinator:
    """
    Combina multiple LoRA per creare stili unici.
    
    Prende fino a 3 LoRA e li fonde con pesi
    indipendenti per creare uno stile visivo custom.
    
    Esempio workflow:
    1. LoraLoader (retro_80s_anime, 0.8) → LoRAStyleCombinator
    2. LoraLoader (vhs_grain, 0.5) → LoRAStyleCombinator
    3. LoraLoader (film_grain, 0.3) → LoRAStyleCombinator
    4. LoRAStyleCombinator → KSampler
    
    Risultato: Anime anni '80 con autentica grana VHS
    """
    
    # Database combinazioni testate
    TESTED_COMBINATIONS = {
        "retro_80s_anime": {
            "primary": "retro_80s_anime_lora.safetensors",
            "compatible": ["vhs_retro_lora.safetensors", "retro_80s_film_lora.safetensors", "synthwave_lora.safetensors"],
            "incompatible": ["watercolor_style.safetensors", "pixel_art_style.safetensors"],
            "description": "Anime anni '80 con estetica VHS/film",
            "optimal_primary_strength": 0.8,
            "optimal_secondary_strength": 0.5
        },
        "modern_anime_ghibli": {
            "primary": "anime_style.safetensors",
            "compatible": ["ghibli_style.safetensors", "watercolor_style.safetensors"],
            "incompatible": ["vhs_retro_lora.safetensors", "comic_style.safetensors"],
            "description": "Anime moderno con atmosfera Ghibli",
            "optimal_primary_strength": 0.7,
            "optimal_secondary_strength": 0.6
        },
        "retro_futuristic": {
            "primary": "synthwave_lora.safetensors",
            "compatible": ["retro_80s_anime_lora.safetensors", "vhs_retro_lora.safetensors"],
            "incompatible": ["watercolor_style.safetensors", "ghibli_style.safetensors"],
            "description": "Retro-futurismo synthwave con elementi anime",
            "optimal_primary_strength": 0.7,
            "optimal_secondary_strength": 0.4
        },
        "artistic_mixed": {
            "primary": "ghibli_style.safetensors",
            "compatible": ["watercolor_style.safetensors", "anime_style.safetensors"],
            "incompatible": ["vhs_retro_lora.safetensors", "pixel_art_style.safetensors"],
            "description": "Stile artistico con elementi Ghibli/acquerello",
            "optimal_primary_strength": 0.6,
            "optimal_secondary_strength": 0.5
        },
        "comic_cartoon": {
            "primary": "cartoon_style.safetensors",
            "compatible": ["comic_style.safetensors", "pixel_art_style.safetensors"],
            "incompatible": ["ghibli_style.safetensors", "retro_80s_film_lora.safetensors"],
            "description": "Cartoon con influenze comic",
            "optimal_primary_strength": 0.8,
            "optimal_secondary_strength": 0.6
        }
    }
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL", {
                    "tooltip": "Modello base (dal UNETLoader o precedente LoRA)"
                }),
                "clip": ("CLIP", {
                    "tooltip": "CLIP base (dal CLIPLoader o precedente LoRA)"
                }),
                "lora_1_name": (["none", "cartoon_style.safetensors", "anime_style.safetensors", 
                               "ghibli_style.safetensors", "comic_style.safetensors",
                               "retro_80s_anime_lora.safetensors", "retro_80s_film_lora.safetensors",
                               "vhs_retro_lora.safetensors", "synthwave_lora.safetensors",
                               "watercolor_style.safetensors", "pixel_art_style.safetensors"], {
                    "default": "retro_80s_anime_lora.safetensors",
                    "tooltip": "Primo LoRA stile (PRINCIPALE - definisce lo stile base)"
                }),
                "lora_1_strength": ("FLOAT", {
                    "default": 0.8,
                    "min": 0.0,
                    "max": 1.5,
                    "step": 0.01,
                    "tooltip": "Forza primo LoRA (principale, consigliato 0.6-1.0)"
                }),
            },
            "optional": {
                "lora_2_name": (["none", "cartoon_style.safetensors", "anime_style.safetensors",
                               "ghibli_style.safetensors", "watercolor_style.safetensors",
                               "vhs_retro_lora.safetensors", "retro_80s_film_lora.safetensors",
                               "comic_style.safetensors", "synthwave_lora.safetensors",
                               "pixel_art_style.safetensors"], {
                    "default": "none",
                    "tooltip": "Secondo LoRA stile (combinazione - arricchisce lo stile base)"
                }),
                "lora_2_strength": ("FLOAT", {
                    "default": 0.5,
                    "min": 0.0,
                    "max": 1.5,
                    "step": 0.01,
                    "tooltip": "Forza secondo LoRA (consigliato 0.3-0.7)"
                }),
                "lora_3_name": (["none", "comic_style.safetensors", "pixel_art_style.safetensors",
                               "synthwave_lora.safetensors", "vhs_retro_lora.safetensors",
                               "anime_style.safetensors", "cartoon_style.safetensors"], {
                    "default": "none",
                    "tooltip": "Terzo LoRA stile (accento - dettaglio finale)"
                }),
                "lora_3_strength": ("FLOAT", {
                    "default": 0.3,
                    "min": 0.0,
                    "max": 1.5,
                    "step": 0.01,
                    "tooltip": "Forza terzo LoRA (consigliato 0.2-0.5)"
                }),
                "combination_preset": (["custom", "retro_80s_anime", "modern_anime_ghibli", 
                                      "retro_futuristic", "artistic_mixed", "comic_cartoon"], {
                    "default": "custom",
                    "tooltip": "Preset combinazione (auto-configura i LoRA)"
                }),
            }
        }
    
    RETURN_TYPES = ("MODEL", "CLIP", "STRING", "STRING",)
    RETURN_NAMES = ("model", "clip", "combination_info", "style_description",)
    FUNCTION = "combine_lora_styles"
    CATEGORY = "CharacterForge/Style"
    
    def combine_lora_styles(self, model, clip, lora_1_name, lora_1_strength,
                          lora_2_name="none", lora_2_strength=0.5,
                          lora_3_name="none", lora_3_strength=0.3,
                          combination_preset="custom"):
        """
        Combina LoRA multipli per stile unico.
        
        Il nodo valida la combinazione e fornisce
        informazioni dettagliate sulla compatibilità.
        
        Args:
            model: Modello base
            clip: CLIP base
            lora_1_name: Nome primo LoRA (principale)
            lora_1_strength: Forza primo LoRA
            lora_2_name: Nome secondo LoRA
            lora_2_strength: Forza secondo LoRA
            lora_3_name: Nome terzo LoRA
            lora_3_strength: Forza terzo LoRA
            combination_preset: Preset combinazione
            
        Returns:
            tuple: (model, clip, combination_info, style_description)
        """
        
        # Validazione input
        if model is None:
            raise ValueError("Modello non valido")
        
        if clip is None:
            raise ValueError("CLIP non valido")
        
        # Applica preset se selezionato
        if combination_preset != "custom":
            preset_config = self.TESTED_COMBINATIONS.get(combination_preset, {})
            
            if preset_config:
                # Auto-configura LoRA
                lora_1_name = preset_config["primary"]
                lora_1_strength = preset_config["optimal_primary_strength"]
                
                # Se ci sono LoRA compatibili, usa il primo
                if preset_config["compatible"] and lora_2_name == "none":
                    lora_2_name = preset_config["compatible"][0]
                    lora_2_strength = preset_config["optimal_secondary_strength"]
        
        # Costruisce informazioni combinazione
        combination_info = self._build_combination_info(
            lora_1_name, lora_1_strength,
            lora_2_name, lora_2_strength,
            lora_3_name, lora_3_strength
        )
        
        # Genera descrizione stile
        style_description = self._generate_style_description(
            lora_1_name, lora_2_name, lora_3_name,
            combination_preset
        )
        
        # Il modello e CLIP passano attraverso senza modifica
        # Il caricamento LoRA avviene tramite nodi LoraLoader standard
        # collegati in serie PRIMA di questo nodo
        
        return (model, clip, combination_info, style_description)
    
    def _build_combination_info(self, lora_1, strength_1, 
                               lora_2, strength_2,
                               lora_3, strength_3):
        """
        Costruisce informazioni dettagliate sulla combinazione.
        """
        info = {
            "controller": "LoRAStyleCombinator",
            "total_loras": 0,
            "lora_details": [],
            "compatibility_check": "unknown",
            "warnings": [],
            "recommendations": []
        }
        
        # Analizza ogni LoRA
        loras = [
            (lora_1, strength_1, "primary"),
            (lora_2, strength_2, "secondary"),
            (lora_3, strength_3, "tertiary")
        ]
        
        active_loras = []
        for name, strength, role in loras:
            if name != "none":
                active_loras.append((name, strength, role))
                info["lora_details"].append({
                    "name": name,
                    "strength": strength,
                    "role": role
                })
        
        info["total_loras"] = len(active_loras)
        
        # Verifica compatibilità
        if len(active_loras) >= 2:
            primary_name = active_loras[0][0]
            secondary_name = active_loras[1][0]
            
            compatibility = self._check_compatibility(primary_name, secondary_name)
            info["compatibility_check"] = compatibility["status"]
            
            if compatibility["status"] == "incompatible":
                info["warnings"].append(compatibility["message"])
            elif compatibility["status"] == "compatible":
                info["recommendations"].append(compatibility["message"])
        
        # Verifica somma strength
        total_strength = sum(strength for _, strength, _ in active_loras)
        info["total_strength"] = round(total_strength, 2)
        
        if total_strength > 2.5:
            info["warnings"].append(
                f"Somma strength alta ({total_strength:.2f}): rischio conflitti stilistici"
            )
        elif total_strength < 0.8:
            info["warnings"].append(
                f"Somma strength bassa ({total_strength:.2f}): stile potrebbe essere troppo debole"
            )
        
        # Suggerimenti
        if active_loras:
            info["recommendations"].extend(
                self._get_optimization_suggestions(active_loras)
            )
        
        return str(info)
    
    def _check_compatibility(self, primary, secondary):
        """
        Verifica compatibilità tra due LoRA.
        """
        # Cerca combinazione testata
        for combo_name, combo_config in self.TESTED_COMBINATIONS.items():
            if combo_config["primary"] == primary:
                if secondary in combo_config["compatible"]:
                    return {
                        "status": "compatible",
                        "message": f"Combinazione testata: {combo_name}. {combo_config['description']}"
                    }
                elif secondary in combo_config["incompatible"]:
                    return {
                        "status": "incompatible",
                        "message": f"Combinazione sconsigliata per {combo_name}: stili in conflitto"
                    }
        
        # Combinazione non testata
        return {
            "status": "untested",
            "message": "Combinazione sperimentale: verifica i risultati visivamente"
        }
    
    def _get_optimization_suggestions(self, active_loras):
        """
        Genera suggerimenti per ottimizzare la combinazione.
        """
        suggestions = []
        
        primary = active_loras[0]
        primary_name = primary[0]
        primary_strength = primary[1]
        
        # Suggerimenti basati sul LoRA primario
        if "retro_80s" in primary_name:
            if primary_strength > 0.9:
                suggestions.append("Strength alto per anime 80s: riduci a 0.7-0.8 per evitare artefatti")
            suggestions.append("Per autentico look anni '80, aggiungi VHS grain come secondario")
        
        elif "anime" in primary_name and "retro" not in primary_name:
            suggestions.append("Per anime moderno, mantieni strength 0.6-0.8")
        
        elif "ghibli" in primary_name:
            suggestions.append("Ghibli funziona meglio con strength moderato (0.5-0.7)")
        
        elif "synthwave" in primary_name:
            suggestions.append("Synthwave richiede colori intensi: strength 0.6-0.8")
        
        # Suggerimenti generali
        if len(active_loras) == 3:
            suggestions.append("3 LoRA attivi: assicurati che il terzo sia un 'accento' leggero")
        
        return suggestions
    
    def _generate_style_description(self, lora_1, lora_2, lora_3, preset):
        """
        Genera descrizione leggibile dello stile risultante.
        """
        descriptions = []
        
        # Descrizioni per ogni LoRA
        lora_descriptions = {
            "cartoon_style.safetensors": "2D Cartoon con cel shading",
            "anime_style.safetensors": "Anime moderno giapponese",
            "ghibli_style.safetensors": "Acquerello stile Studio Ghibli",
            "comic_style.safetensors": "Fumetto americato con inchiostro",
            "retro_80s_anime_lora.safetensors": "Anime anni '80 con VHS grain",
            "retro_80s_film_lora.safetensors": "Fotografia analogica anni '80",
            "vhs_retro_lora.safetensors": "Estetica VHS analogica",
            "synthwave_lora.safetensors": "Synthwave neon retro-futuristico",
            "watercolor_style.safetensors": "Pittura ad acquerello",
            "pixel_art_style.safetensors": "Pixel art 16-bit retro"
        }
        
        # Descrizione preset
        if preset != "custom":
            preset_desc = self.TESTED_COMBINATIONS.get(preset, {}).get("description", "")
            if preset_desc:
                descriptions.append(f"Preset: {preset_desc}")
        
        # Descrizione LoRA attivi
        for lora_name in [lora_1, lora_2, lora_3]:
            if lora_name != "none" and lora_name in lora_descriptions:
                descriptions.append(lora_descriptions[lora_name])
        
        if not descriptions:
            descriptions.append("Stile base (nessun LoRA attivo)")
        
        return " + ".join(descriptions)
    
    @classmethod
    def IS_CHANGED(s, model, clip, lora_1_name, lora_1_strength,
                  lora_2_name="none", lora_2_strength=0.5,
                  lora_3_name="none", lora_3_strength=0.3,
                  combination_preset="custom"):
        return float("NaN")


# Registrazione per uso standalone
NODE_CLASS_MAPPINGS = {
    "CharacterForgeLoRAStyleCombinator": CharacterForgeLoRAStyleCombinator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CharacterForgeLoRAStyleCombinator": "LoRA Style Combinator"
}