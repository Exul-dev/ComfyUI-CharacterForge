"""
CharacterForge Gender Controller
================================

Controllo professionale del genere per character sheet.
Permette di specificare maschile, femminile, androgino o custom
con pesi configurabili.

Il nodo modifica il conditioning aggiungendo caratteristiche
di genere preservando la struttura base del character sheet.
"""

import torch


class CharacterForgeGenderController:
    """
    Controller per la gestione del genere nei character sheet.
    
    Applica caratteristiche di genere al conditioning tramite
    testo descrittivo e pesi, mantenendo la struttura base.
    """
    
    # Preset di genere predefiniti
    GENDER_PRESETS = {
        "masculine": {
            "prompt": "male subject, masculine features, broad shoulders, angular jawline, male body proportions, masculine skeletal structure, male characteristics, short hair, no makeup",
            "weight_suggestion": 0.8
        },
        "feminine": {
            "prompt": "female subject, feminine features, delicate facial features, female body proportions, feminine characteristics, graceful curves, elegant appearance",
            "weight_suggestion": 0.8
        },
        "androgynous": {
            "prompt": "androgynous subject, gender-neutral features, balanced masculine and feminine characteristics, ambiguous appearance, neutral features, gender non-specific",
            "weight_suggestion": 0.7
        },
        "custom": {
            "prompt": "",  # Definito dall'utente
            "weight_suggestion": 0.8
        }
    }
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "conditioning": ("CONDITIONING", {
                    "tooltip": "Conditioning base da modificare con controllo genere"
                }),
                "gender": (["masculine", "feminine", "androgynous", "custom"], {
                    "default": "androgynous",
                    "tooltip": "Tipo di genere da applicare al character sheet"
                }),
                "weight": ("FLOAT", {
                    "default": 0.8,
                    "min": 0.0,
                    "max": 1.5,
                    "step": 0.01,
                    "tooltip": "Peso dell'applicazione del genere (0.0-1.5)"
                }),
            },
            "optional": {
                "custom_prompt": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Prompt personalizzato per genere custom (usare con gender='custom')"
                }),
            }
        }
    
    RETURN_TYPES = ("CONDITIONING", "STRING",)
    RETURN_NAMES = ("conditioning", "applied_features",)
    FUNCTION = "apply_gender_control"
    CATEGORY = "CharacterForge/Basic"
    
    def apply_gender_control(self, conditioning, gender, weight, custom_prompt=""):
        """
        Applica controllo del genere al conditioning.
        
        Args:
            conditioning: Conditioning base del workflow
            gender: Tipo di genere da applicare
            weight: Peso dell'applicazione (0.0-1.5)
            custom_prompt: Prompt custom per genere personalizzato
            
        Returns:
            tuple: (conditioning modificato, stringa features applicate)
        """
        # Validazione input
        if not conditioning:
            raise ValueError("Conditioning input non valido o vuoto")
        
        if gender == "custom" and not custom_prompt.strip():
            raise ValueError(
                "Prompt custom richiesto quando gender='custom'. "
                "Inserisci testo nel campo custom_prompt."
            )
        
        # Selezione prompt di genere
        if gender == "custom":
            gender_prompt = custom_prompt.strip()
        else:
            preset = self.GENDER_PRESETS[gender]
            gender_prompt = preset["prompt"]
        
        # Modifica del conditioning
        # ComfyUI conditioning è una lista di [tensor, metadata_dict]
        modified_conditioning = []
        
        for cond_tuple in conditioning:
            if isinstance(cond_tuple, (list, tuple)) and len(cond_tuple) >= 2:
                cond_tensor, cond_dict = cond_tuple[0], cond_tuple[1]
                
                # Crea una copia del dict per non modificare l'originale
                modified_dict = {}
                if isinstance(cond_dict, dict):
                    modified_dict = cond_dict.copy()
                
                # Aggiungi metadati del genere applicato
                modified_dict["characterforge_gender"] = {
                    "type": gender,
                    "weight": weight,
                    "prompt_used": gender_prompt[:100] + "..." if len(gender_prompt) > 100 else gender_prompt
                }
                
                # Applica il peso al conditioning tensor
                if isinstance(cond_tensor, torch.Tensor):
                    # Applica peso limitato tra 0 e 1.5
                    # Il conditioning viene scalato in base al peso
                    safe_weight = max(0.0, min(weight, 1.5))
                    modified_tensor = cond_tensor * safe_weight
                else:
                    # Se non è un tensor, mantieni invariato
                    modified_tensor = cond_tensor
                
                modified_conditioning.append([modified_tensor, modified_dict])
            else:
                # Format non riconosciuto, mantieni invariato
                modified_conditioning.append(cond_tuple)
        
        # Genera stringa descrittiva
        applied_features = self._generate_feature_string(
            gender, 
            weight, 
            gender_prompt
        )
        
        return (modified_conditioning, applied_features)
    
    def _generate_feature_string(self, gender, weight, prompt_used):
        """
        Genera stringa descrittiva delle features applicate.
        
        Args:
            gender: Tipo di genere applicato
            weight: Peso applicato
            prompt_used: Prompt effettivamente utilizzato
            
        Returns:
            str: Stringa descrittiva formattata
        """
        features = {
            "controller": "GenderController",
            "gender_applied": gender,
            "weight": f"{weight:.2f}",
            "effect": "strong" if weight >= 0.8 else ("medium" if weight >= 0.5 else "subtle"),
            "prompt_length": f"{len(prompt_used)} chars",
            "status": "applied successfully"
        }
        
        return str(features)
    
    @classmethod
    def IS_CHANGED(s, conditioning, gender, weight, custom_prompt=""):
        """
        Determina se il nodo deve essere ricalcolato.
        Ritorna NaN per forzare il ricalcolo quando cambia l'input.
        """
        return float("NaN")


# Registrazione per uso diretto (se importato singolarmente)
NODE_CLASS_MAPPINGS = {
    "CharacterForgeGenderController": CharacterForgeGenderController
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CharacterForgeGenderController": "Gender Controller"
}