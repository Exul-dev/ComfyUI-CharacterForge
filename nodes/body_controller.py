"""
CharacterForge Body Controller
===============================

Controllo corporatura per character sheet.
Gestisce tipo fisico, altezza, definizione muscolare,
percentuale di grasso corporeo e proporzioni.

Il nodo modifica il conditioning applicando descrizioni
fisiche dettagliate per ottenere character sheet coerenti
con le specifiche corporatura richieste.
"""

import torch


class CharacterForgeBodyController:
    """
    Controller corporatura per character sheet.
    
    Permette di specificare:
    - Tipo di corporatura (athletic, slim, curvy, muscular, average)
    - Altezza esatta in centimetri (150-200cm)
    - Livello di definizione muscolare
    - Percentuale di grasso corporeo
    - Proporzioni corporali personalizzate
    """
    
    # Database corporatura predefinite
    BODY_DATABASE = {
        "athletic": {
            "description": "athletic build, toned physique, visible muscle definition, balanced athletic proportions",
            "male_description": "athletic male build, broad shoulders, visible abs, toned muscles, V-shape torso",
            "female_description": "athletic female build, toned legs, defined waist, athletic curves, fit appearance",
            "proportions": {
                "shoulder_width": 1.2,
                "waist_width": 0.8,
                "hip_width": 0.9,
                "muscle_mass": 0.7,
                "body_fat": 0.3
            },
            "height_range": {"min": 165, "max": 195}
        },
        "slim": {
            "description": "slim build, slender physique, lean body, minimal muscle mass, thin frame",
            "male_description": "slim male build, narrow shoulders, lean physique, minimal body fat, thin frame",
            "female_description": "slim female build, slender frame, thin waist, lean limbs, delicate appearance",
            "proportions": {
                "shoulder_width": 0.9,
                "waist_width": 0.7,
                "hip_width": 0.8,
                "muscle_mass": 0.3,
                "body_fat": 0.2
            },
            "height_range": {"min": 160, "max": 185}
        },
        "curvy": {
            "description": "curvy build, hourglass figure, pronounced curves, full figure, voluptuous physique",
            "male_description": "fuller male build with some curves, softer appearance, rounded features",
            "female_description": "curvy female build, hourglass figure, full bust, wide hips, defined waist, voluptuous curves",
            "proportions": {
                "shoulder_width": 1.0,
                "waist_width": 0.6,
                "hip_width": 1.1,
                "muscle_mass": 0.4,
                "body_fat": 0.5
            },
            "height_range": {"min": 155, "max": 180}
        },
        "muscular": {
            "description": "muscular build, bodybuilder physique, massive muscle mass, bulky frame, extremely defined",
            "male_description": "extremely muscular male, bodybuilder physique, massive pecs, huge arms, thick neck, vascular",
            "female_description": "muscular female build, defined muscles, athletic curves, toned physique, fitness model",
            "proportions": {
                "shoulder_width": 1.4,
                "waist_width": 0.9,
                "hip_width": 0.9,
                "muscle_mass": 0.9,
                "body_fat": 0.2
            },
            "height_range": {"min": 170, "max": 200}
        },
        "average": {
            "description": "average build, normal proportions, healthy body type, balanced physique",
            "male_description": "average male build, normal proportions, healthy appearance, balanced physique",
            "female_description": "average female build, normal proportions, healthy appearance, natural curves",
            "proportions": {
                "shoulder_width": 1.0,
                "waist_width": 0.8,
                "hip_width": 0.9,
                "muscle_mass": 0.5,
                "body_fat": 0.4
            },
            "height_range": {"min": 160, "max": 190}
        }
    }
    
    # Descrizioni definizione muscolare
    MUSCLE_DEFINITIONS = {
        "low": {
            "description": "minimal muscle definition, smooth muscle appearance, soft physique",
            "visual": "soft muscles, minimal definition, smooth contours"
        },
        "medium": {
            "description": "moderate muscle definition, visible muscle tone, healthy athletic appearance",
            "visual": "visible muscle tone, defined contours, athletic look"
        },
        "high": {
            "description": "highly defined muscles, visible muscle separation, vascular appearance, shredded",
            "visual": "extremely defined muscles, visible striations, vascular, shredded appearance"
        }
    }
    
    # Descrizioni grasso corporeo
    BODY_FAT_LEVELS = {
        "low": {
            "description": "very low body fat percentage, vascular appearance, visible veins, lean physique",
            "percentage_range": "8-12%"
        },
        "medium": {
            "description": "normal body fat percentage, healthy appearance, balanced physique",
            "percentage_range": "15-20%"
        },
        "high": {
            "description": "higher body fat percentage, softer appearance, rounded features",
            "percentage_range": "25-30%"
        }
    }
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "conditioning": ("CONDITIONING", {
                    "tooltip": "Conditioning base da modificare con controllo corporatura"
                }),
                "body_type": (["athletic", "slim", "curvy", "muscular", "average"], {
                    "default": "average",
                    "tooltip": "Tipo di corporatura del soggetto"
                }),
                "height": ("FLOAT", {
                    "default": 175.0,
                    "min": 150.0,
                    "max": 200.0,
                    "step": 1.0,
                    "tooltip": "Altezza del soggetto in centimetri (150-200cm)"
                }),
                "weight": ("FLOAT", {
                    "default": 0.7,
                    "min": 0.0,
                    "max": 1.5,
                    "step": 0.01,
                    "tooltip": "Peso dell'applicazione corporatura (0.0-1.5)"
                }),
                "muscle_definition": (["low", "medium", "high"], {
                    "default": "medium",
                    "tooltip": "Livello di definizione muscolare"
                }),
                "body_fat": (["low", "medium", "high"], {
                    "default": "medium",
                    "tooltip": "Percentuale di grasso corporeo"
                }),
            },
            "optional": {
                "custom_proportions": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Proporzioni personalizzate aggiuntive (es. 'extra long legs', 'broad back')"
                }),
                "target_gender": (["unspecified", "male", "female"], {
                    "default": "unspecified",
                    "tooltip": "Genere target per descrizioni specifiche"
                }),
            }
        }
    
    RETURN_TYPES = ("CONDITIONING", "STRING",)
    RETURN_NAMES = ("conditioning", "body_details",)
    FUNCTION = "apply_body_control"
    CATEGORY = "CharacterForge/Basic"
    
    def apply_body_control(self, conditioning, body_type, height, weight,
                          muscle_definition, body_fat, 
                          custom_proportions="", target_gender="unspecified"):
        """
        Applica controllo corporatura al conditioning.
        
        Args:
            conditioning: Conditioning base del workflow
            body_type: Tipo di corporatura
            height: Altezza in cm
            weight: Peso applicazione (0.0-1.5)
            muscle_definition: Livello definizione muscolare
            body_fat: Percentuale grasso corporeo
            custom_proportions: Proporzioni custom aggiuntive
            target_gender: Genere per descrizioni specifiche
            
        Returns:
            tuple: (conditioning modificato, dettagli corporatura)
        """
        # Validazione input
        if not conditioning:
            raise ValueError("Conditioning input non valido o vuoto")
        
        if body_type not in self.BODY_DATABASE:
            raise ValueError(f"Tipo corporatura '{body_type}' non riconosciuto")
        
        if muscle_definition not in self.MUSCLE_DEFINITIONS:
            raise ValueError(f"Definizione muscolare '{muscle_definition}' non riconosciuta")
        
        if body_fat not in self.BODY_FAT_LEVELS:
            raise ValueError(f"Livello grasso corporeo '{body_fat}' non riconosciuto")
        
        # Verifica compatibilità altezza con tipo corporatura
        height_range = self.BODY_DATABASE[body_type]["height_range"]
        if height < height_range["min"] or height > height_range["max"]:
            # Non è un errore, ma avvisa nel log
            print(f"[BodyController] Warning: Altezza {height}cm fuori range tipico "
                  f"per {body_type} ({height_range['min']}-{height_range['max']}cm)")
        
        # Costruzione prompt corporatura
        body_prompt = self._build_body_prompt(
            body_type,
            height,
            muscle_definition,
            body_fat,
            custom_proportions,
            target_gender
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
                
                # Aggiungi metadati corporatura al conditioning
                modified_dict["characterforge_body"] = {
                    "type": body_type,
                    "height_cm": height,
                    "weight_applied": weight,
                    "muscle_definition": muscle_definition,
                    "body_fat": body_fat,
                    "target_gender": target_gender,
                    "proportions": self.BODY_DATABASE[body_type]["proportions"]
                }
                
                # Applica il peso al conditioning tensor
                if isinstance(cond_tensor, torch.Tensor):
                    # Peso base corporatura
                    safe_weight = max(0.0, min(weight, 1.5))
                    modified_tensor = cond_tensor * safe_weight
                    
                    # Modifiche specifiche per definizione muscolare
                    if muscle_definition == "high":
                        # Aumenta "contrasto" nel conditioning per definizione
                        muscle_boost = 1.15
                        modified_tensor = modified_tensor * muscle_boost
                    elif muscle_definition == "low":
                        # Riduce "contrasto" per muscolatura morbida
                        muscle_reduce = 0.85
                        modified_tensor = modified_tensor * muscle_reduce
                    
                    # Modifiche per grasso corporeo
                    if body_fat == "high":
                        # Condizionamento più "morbido" per più grasso
                        soft_factor = 0.95
                        modified_tensor = modified_tensor * soft_factor
                    elif body_fat == "low":
                        # Condizionamento più "definito" per meno grasso
                        definition_boost = 1.05
                        modified_tensor = modified_tensor * definition_boost
                        
                else:
                    modified_tensor = cond_tensor
                
                modified_conditioning.append([modified_tensor, modified_dict])
            else:
                # Format non riconosciuto, mantieni invariato
                modified_conditioning.append(cond_tuple)
        
        # Genera dettagli corporatura
        details = self._generate_body_details(
            body_type,
            height,
            muscle_definition,
            body_fat,
            weight,
            custom_proportions,
            target_gender
        )
        
        return (modified_conditioning, details)
    
    def _build_body_prompt(self, body_type, height, muscle_def, 
                          body_fat, custom_props="", target_gender="unspecified"):
        """
        Costruisce prompt completo per corporatura.
        
        Args:
            body_type: Tipo corporatura
            height: Altezza in cm
            muscle_def: Definizione muscolare
            body_fat: Grasso corporeo
            custom_props: Proporzioni custom
            target_gender: Genere target
            
        Returns:
            str: Prompt corporatura completo
        """
        body_data = self.BODY_DATABASE[body_type]
        
        prompt_parts = []
        
        # Descrizione base (gender-specific se specificato)
        if target_gender == "male" and "male_description" in body_data:
            prompt_parts.append(body_data["male_description"])
        elif target_gender == "female" and "female_description" in body_data:
            prompt_parts.append(body_data["female_description"])
        else:
            prompt_parts.append(body_data["description"])
        
        # Altezza con categoria
        height_category = self._categorize_height(height)
        prompt_parts.append(f"{height_category} height ({height:.0f}cm)")
        
        # Definizione muscolare
        muscle_desc = self.MUSCLE_DEFINITIONS[muscle_def]["description"]
        prompt_parts.append(muscle_desc)
        
        # Grasso corporeo
        fat_desc = self.BODY_FAT_LEVELS[body_fat]["description"]
        prompt_parts.append(fat_desc)
        
        # Proporzioni corporali
        proportions = body_data["proportions"]
        if proportions["shoulder_width"] > 1.2:
            prompt_parts.append("broad shoulders")
        elif proportions["shoulder_width"] < 0.9:
            prompt_parts.append("narrow shoulders")
        
        if proportions["hip_width"] > 1.0:
            prompt_parts.append("wide hips")
        
        # Proporzioni custom
        if custom_props.strip():
            prompt_parts.append(custom_props.strip())
        
        return ", ".join(prompt_parts)
    
    def _categorize_height(self, height):
        """
        Categorizza l'altezza in descrizioni standard.
        
        Args:
            height: Altezza in cm
            
        Returns:
            str: Categoria altezza
        """
        if height < 160:
            return "short"
        elif height < 170:
            return "medium-short"
        elif height < 180:
            return "medium"
        elif height < 190:
            return "tall"
        else:
            return "very tall"
    
    def _generate_body_details(self, body_type, height, muscle_def,
                              body_fat, weight, custom_props="", 
                              target_gender="unspecified"):
        """
        Genera dettagli formattati delle caratteristiche corporatura applicate.
        """
        body_data = self.BODY_DATABASE[body_type]
        
        details = {
            "controller": "BodyController",
            "body_type": body_type,
            "height": f"{height:.1f}cm ({self._categorize_height(height)})",
            "muscle_definition": {
                "level": muscle_def,
                "description": self.MUSCLE_DEFINITIONS[muscle_def]["description"]
            },
            "body_fat": {
                "level": body_fat,
                "percentage": self.BODY_FAT_LEVELS[body_fat]["percentage_range"],
                "description": self.BODY_FAT_LEVELS[body_fat]["description"]
            },
            "weight_applied": f"{weight:.2f}",
            "proportions": body_data["proportions"],
            "target_gender": target_gender,
            "custom_proportions_used": bool(custom_props.strip()),
            "height_compatibility": "typical" if (
                height_range["min"] <= height <= height_range["max"]
            ) else "unusual"
        }
        
        return str(details)
    
    @classmethod
    def IS_CHANGED(s, conditioning, body_type, height, weight,
                  muscle_definition, body_fat, custom_proportions="", 
                  target_gender="unspecified"):
        """
        Determina se il nodo deve essere ricalcolato.
        """
        return float("NaN")


# Registrazione per uso diretto (se importato singolarmente)
NODE_CLASS_MAPPINGS = {
    "CharacterForgeBodyController": CharacterForgeBodyController
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CharacterForgeBodyController": "Body Type Controller"
}