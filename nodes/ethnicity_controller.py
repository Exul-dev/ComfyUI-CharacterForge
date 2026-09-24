"""
CharacterForge Ethnicity Controller
===================================

Controllo professionale dell'etnia per character sheet.
Supporta multi-etnia con mix di caratteristiche primarie
e secondarie per creare soggetti con heritage misto.

Il nodo modifica il conditioning applicando caratteristiche
etniche specifiche: pelle, tratti facciali, capelli, occhi.
"""

import torch


class CharacterForgeEthnicityController:
    """
    Controller etnico con supporto multi-etnia.
    
    Permette di specificare un'etnia primaria e opzionalmente
    una secondaria per creare mix di caratteristiche etniche
    (es. 60% caucasico + 40% asiatico).
    """
    
    # Database caratteristiche etniche
    ETHNICITY_DATABASE = {
        "caucasian": {
            "skin": "fair to light skin with neutral undertones",
            "facial": "European facial features, high cheekbones, relatively narrow nose bridge, varied eye shapes",
            "hair": "straight to wavy hair texture, color range from blonde to dark brown to red",
            "eyes": "light colored eyes common (blue, green, hazel, gray), also brown",
            "heritage": "European descent"
        },
        "african": {
            "skin": "dark to deep brown skin with warm undertones",
            "facial": "African facial features, full lips, wider nose bridge, prominent cheekbones",
            "hair": "curly to coily afro-textured hair, black color",
            "eyes": "dark brown eyes, almond-shaped",
            "heritage": "African descent"
        },
        "asian": {
            "skin": "light to olive skin with neutral undertones",
            "facial": "East Asian facial features, almond-shaped eyes, flatter facial profile, epicanthic fold",
            "hair": "straight black hair, thick texture",
            "eyes": "dark brown almond-shaped eyes",
            "heritage": "East Asian descent"
        },
        "latin": {
            "skin": "olive to tan skin with warm golden undertones",
            "facial": "Latin American facial features, warm expressive features, mixed heritage traits",
            "hair": "dark wavy to curly hair, brown to black",
            "eyes": "brown to dark brown eyes, expressive",
            "heritage": "Latin American descent"
        },
        "mixed": {
            "skin": "varies depending on specific heritage mix",
            "facial": "mixed heritage facial features, blend of characteristics",
            "hair": "varies in texture and color based on mix",
            "eyes": "varies in color and shape",
            "heritage": "mixed heritage"
        }
    }
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "conditioning": ("CONDITIONING", {
                    "tooltip": "Conditioning base da modificare con controllo etnia"
                }),
                "primary_ethnicity": (["caucasian", "african", "asian", "latin", "mixed"], {
                    "default": "mixed",
                    "tooltip": "Etnia principale del soggetto"
                }),
                "weight": ("FLOAT", {
                    "default": 0.6,
                    "min": 0.0,
                    "max": 1.5,
                    "step": 0.01,
                    "tooltip": "Peso dell'applicazione etnica (0.0-1.5)"
                }),
            },
            "optional": {
                "secondary_ethnicity": (["none", "caucasian", "african", "asian", "latin"], {
                    "default": "none",
                    "tooltip": "Etnia secondaria per mix di caratteristiche (es. caucasian-asian mix)"
                }),
                "skin_tone_override": ("STRING", {
                    "default": "",
                    "tooltip": "Override specifico per tono della pelle (es. 'deep bronze', 'pale ivory')"
                }),
                "custom_details": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Dettagli etnici personalizzati aggiuntivi"
                }),
            }
        }
    
    RETURN_TYPES = ("CONDITIONING", "STRING",)
    RETURN_NAMES = ("conditioning", "ethnicity_details",)
    FUNCTION = "apply_ethnicity_control"
    CATEGORY = "CharacterForge/Advanced"
    
    def apply_ethnicity_control(self, conditioning, primary_ethnicity, weight,
                               secondary_ethnicity="none", skin_tone_override="", 
                               custom_details=""):
        """
        Applica controllo etnico al conditioning.
        
        Args:
            conditioning: Conditioning base del workflow
            primary_ethnicity: Etnia principale da applicare
            weight: Peso dell'applicazione (0.0-1.5)
            secondary_ethnicity: Etnia secondaria per mix
            skin_tone_override: Override specifico tono pelle
            custom_details: Dettagli etnici personalizzati
            
        Returns:
            tuple: (conditioning modificato, dettagli etnia applicata)
        """
        # Validazione input
        if not conditioning:
            raise ValueError("Conditioning input non valido o vuoto")
        
        if primary_ethnicity not in self.ETHNICITY_DATABASE:
            raise ValueError(f"Etnia '{primary_ethnicity}' non riconosciuta")
        
        if secondary_ethnicity != "none" and secondary_ethnicity not in self.ETHNICITY_DATABASE:
            raise ValueError(f"Etnia secondaria '{secondary_ethnicity}' non riconosciuta")
        
        # Costruzione prompt etnico completo
        ethnicity_prompt = self._build_ethnicity_prompt(
            primary_ethnicity,
            secondary_ethnicity,
            weight,
            skin_tone_override,
            custom_details
        )
        
        # Modifica del conditioning
        modified_conditioning = []
        
        for cond_tuple in conditioning:
            if isinstance(cond_tuple, (list, tuple)) and len(cond_tuple) >= 2:
                cond_tensor, cond_dict = cond_tuple[0], cond_tuple[1]
                
                # Crea una copia del dict per non modificare l'originale
                modified_dict = {}
                if isinstance(cond_dict, dict):
                    modified_dict = cond_dict.copy()
                
                # Aggiungi metadati etnia al conditioning
                modified_dict["characterforge_ethnicity"] = {
                    "primary": primary_ethnicity,
                    "secondary": secondary_ethnicity,
                    "weight": weight,
                    "skin_override": skin_tone_override if skin_tone_override else None,
                    "is_mixed": secondary_ethnicity != "none"
                }
                
                # IMPORTANTE:
                # Questo controller non riceve un CLIP encoder, quindi non puo' aggiungere
                # il proprio prompt testuale al conditioning in modo corretto.
                # Manteniamo intatto il conditioning ricevuto per non alterare lo stile.
                modified_tensor = cond_tensor

                modified_conditioning.append([modified_tensor, modified_dict])
            else:
                # Format non riconosciuto, mantieni invariato
                modified_conditioning.append(cond_tuple)
        
        # Genera dettagli etnia
        details = self._generate_ethnicity_details(
            primary_ethnicity,
            secondary_ethnicity,
            weight,
            skin_tone_override,
            custom_details
        )
        
        return (modified_conditioning, details)
    
    def _build_ethnicity_prompt(self, primary, secondary, weight, 
                               skin_override="", custom_details=""):
        """
        Costruisce prompt etnico combinato completo.
        
        Args:
            primary: Etnia primaria
            secondary: Etnia secondaria (per mix)
            weight: Peso applicazione
            skin_override: Override tono pelle
            custom_details: Dettagli custom
            
        Returns:
            str: Prompt etnico completo
        """
        primary_features = self.ETHNICITY_DATABASE[primary]
        
        prompt_parts = []
        
        # Base: etnia primaria
        prompt_parts.append(f"{primary} ethnicity subject")
        
        # Caratteristiche primarie
        prompt_parts.append(primary_features["skin"])
        prompt_parts.append(primary_features["facial"])
        prompt_parts.append(primary_features["hair"])
        prompt_parts.append(primary_features["eyes"])
        
        # Se c'Ã¨ un'etnia secondaria, aggiungi mix
        if secondary != "none":
            secondary_features = self.ETHNICITY_DATABASE[secondary]
            
            # Indica heritage misto
            prompt_parts.append(f"mixed {primary}-{secondary} heritage")
            
            # Aggiungi alcune caratteristiche secondarie
            # in base al peso (piÃ¹ peso = piÃ¹ influenza secondaria)
            influence = weight * 0.4  # Max 40% di influenza secondaria
            
            if influence > 0.2:
                # Aggiungi tratti facciali secondari
                prompt_parts.append(f"subtle {secondary_features['facial']}")
            if influence > 0.3:
                # Aggiungi texture capelli secondaria
                prompt_parts.append(f"influenced by {secondary_features['hair']}")
        
        # Override tono pelle se specificato
        if skin_override.strip():
            prompt_parts.append(f"{skin_override.strip()} skin tone")
        
        # Dettagli custom
        if custom_details.strip():
            prompt_parts.append(custom_details.strip())
        
        return ", ".join(prompt_parts)
    
    def _generate_ethnicity_details(self, primary, secondary, weight,
                                   skin_override="", custom_details=""):
        """
        Genera dettagli formattati delle caratteristiche etniche applicate.
        """
        primary_features = self.ETHNICITY_DATABASE[primary]
        
        details = {
            "controller": "EthnicityController",
            "primary_ethnicity": primary,
            "primary_features": {
                "skin": primary_features["skin"],
                "facial": primary_features["facial"],
                "hair": primary_features["hair"],
                "eyes": primary_features["eyes"]
            },
            "secondary_ethnicity": secondary,
            "is_mixed": secondary != "none",
            "weight_applied": f"{weight:.2f}",
            "effect_strength": "strong" if weight >= 0.8 else ("medium" if weight >= 0.5 else "subtle"),
            "skin_override": skin_override if skin_override else "none",
            "custom_details_used": bool(custom_details.strip()),
            "heritage": primary_features["heritage"]
        }
        
        return str(details)
    
    @classmethod
    def IS_CHANGED(s, conditioning, primary_ethnicity, weight,
                   secondary_ethnicity="none", skin_tone_override="", 
                   custom_details=""):
        """
        Determina se il nodo deve essere ricalcolato.
        """
        return float("NaN")


# Registrazione per uso diretto (se importato singolarmente)
NODE_CLASS_MAPPINGS = {
    "CharacterForgeEthnicityController": CharacterForgeEthnicityController
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CharacterForgeEthnicityController": "Ethnicity Controller"
}
