"""
CharacterForge Weighted Conditioning
====================================

Sistema avanzato di combinazione weighted conditioning.
Permette di combinare conditioning multipli (schema, genere,
etnia, corporatura) con pesi individuali configurabili.

Metodi di combinazione disponibili:
- weighted_sum: Somma pesata con normale
- average: Media aritmetica semplice
- concat: Concatenazione sequenziale (tipo ConditioningConcat)
- max: Massimo valore per dimensione
- blend: Interpolazione lineare pesata

Ogni metodo preserva la struttura del conditioning base
se l'opzione preserve_structure Ã¨ attiva.
"""

import torch
import copy


class CharacterForgeWeightedConditioning:
    """
    Sistema di combinazione conditioning con pesi specifici.
    
    Permette di combinare conditioning multipli con pesi
    individuali, simile al sistema di pesi LoRA ma per
    text conditioning.
    
    Combinazione tipica:
    - Base (schema layout): peso 1.0 (sempre)
    - Conditioning 1 (genere): peso 0.8
    - Conditioning 2 (etnia): peso 0.6
    - Conditioning 3 (corporatura): peso 0.7
    """
    
    # Costanti per metodi di combinazione
    COMBINATION_METHODS = {
        "weighted_sum": {
            "description": "Somma pesata con normalizzazione automatica",
            "preserves_base": True,
            "base_influence": 0.5
        },
        "average": {
            "description": "Media aritmetica di tutti i conditioning",
            "preserves_base": False,
            "base_influence": None
        },
        "concat": {
            "description": "Concatenazione sequenziale (massima varietÃ  info)",
            "preserves_base": True,
            "base_influence": 0.0
        },
        "max": {
            "description": "Massimo valore per dimensione tensor",
            "preserves_base": True,
            "base_influence": 0.0
        },
        "blend": {
            "description": "Interpolazione lineare pesata verso il base",
            "preserves_base": True,
            "base_influence": 0.3
        }
    }
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "base_conditioning": ("CONDITIONING", {
                    "tooltip": "Conditioning base (schema layout character sheet)"
                }),
                "conditioning_1": ("CONDITIONING", {
                    "tooltip": "Primo conditioning aggiuntivo (es. genere)"
                }),
                "weight_1": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.5,
                    "step": 0.01,
                    "tooltip": "Peso del primo conditioning (0.0-1.5)"
                }),
                "conditioning_2": ("CONDITIONING", {
                    "tooltip": "Secondo conditioning aggiuntivo (es. etnia)"
                }),
                "weight_2": ("FLOAT", {
                    "default": 0.8,
                    "min": 0.0,
                    "max": 1.5,
                    "step": 0.01,
                    "tooltip": "Peso del secondo conditioning (0.0-1.5)"
                }),
                "conditioning_3": ("CONDITIONING", {
                    "tooltip": "Terzo conditioning aggiuntivo (es. corporatura)"
                }),
                "weight_3": ("FLOAT", {
                    "default": 0.6,
                    "min": 0.0,
                    "max": 1.5,
                    "step": 0.01,
                    "tooltip": "Peso del terzo conditioning (0.0-1.5)"
                }),
                "combination_method": (["weighted_sum", "average", "concat", "max", "blend"], {
                    "default": "weighted_sum",
                    "tooltip": "Metodo di combinazione dei conditioning"
                }),
                "preserve_structure": ("BOOLEAN", {
                    "default": True,
                    "tooltip": "Preserva la struttura del conditioning base (layout character sheet)"
                }),
            },
            "optional": {
                "structure_strength": ("FLOAT", {
                    "default": 0.3,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "tooltip": "Forza con cui preservare la struttura base (0.0-1.0)"
                }),
            }
        }
    
    RETURN_TYPES = ("CONDITIONING", "STRING",)
    RETURN_NAMES = ("conditioning", "combination_info",)
    FUNCTION = "combine_weighted"
    CATEGORY = "CharacterForge/Advanced"
    
    def combine_weighted(self, base_conditioning, conditioning_1, weight_1,
                        conditioning_2, weight_2, conditioning_3, weight_3,
                        combination_method, preserve_structure, 
                        structure_strength=0.3):
        """
        Combina conditioning con pesi specifici.
        
        Args:
            base_conditioning: Conditioning base (schema layout)
            conditioning_1: Primo conditioning aggiuntivo
            weight_1: Peso primo conditioning
            conditioning_2: Secondo conditioning aggiuntivo
            weight_2: Peso secondo conditioning
            conditioning_3: Terzo conditioning aggiuntivo
            weight_3: Peso terzo conditioning
            combination_method: Metodo combinazione
            preserve_structure: Se preservare struttura base
            structure_strength: Forza preservazione struttura
            
        Returns:
            tuple: (conditioning combinato, info combinazione)
        """
        # Validazione input
        if not base_conditioning:
            raise ValueError("Base conditioning non valido o vuoto")
        
        if not conditioning_1 or not conditioning_2 or not conditioning_3:
            raise ValueError("Tutti e tre i conditioning aggiuntivi sono richiesti")
        
        if combination_method not in self.COMBINATION_METHODS:
            raise ValueError(f"Metodo combinazione '{combination_method}' non riconosciuto")
        
        # Validazione pesi
        weights = [weight_1, weight_2, weight_3]
        for i, w in enumerate(weights):
            if w < 0.0 or w > 1.5:
                raise ValueError(f"Peso {i+1} ({w}) fuori range (0.0-1.5)")
        
        # Normalizzazione pesi per weighted_sum
        total_weight = sum(weights)
        if total_weight <= 0:
            raise ValueError("La somma dei pesi deve essere maggiore di 0. Impostare almeno un peso superiore a 0.")
        
        normalized_weights = [w / total_weight for w in weights]
        
        # Esecuzione combinazione in base al metodo
        if combination_method == "weighted_sum":
            combined = self._weighted_sum(
                base_conditioning,
                [conditioning_1, conditioning_2, conditioning_3],
                normalized_weights,
                preserve_structure,
                structure_strength
            )
        elif combination_method == "average":
            combined = self._average(
                base_conditioning,
                [conditioning_1, conditioning_2, conditioning_3]
            )
        elif combination_method == "concat":
            combined = self._concat(
                base_conditioning,
                [conditioning_1, conditioning_2, conditioning_3]
            )
        elif combination_method == "max":
            combined = self._max_combination(
                base_conditioning,
                [conditioning_1, conditioning_2, conditioning_3],
                normalized_weights
            )
        elif combination_method == "blend":
            combined = self._blend(
                base_conditioning,
                [conditioning_1, conditioning_2, conditioning_3],
                normalized_weights,
                structure_strength
            )
        else:
            # Fallback non dovrebbe mai accadere
            combined = base_conditioning
        
        # Applica preservazione struttura finale se richiesto
        if preserve_structure and combination_method not in ["weighted_sum", "blend"]:
            combined = self._apply_structure_preservation(
                combined, 
                base_conditioning, 
                structure_strength
            )
        
        # Genera informazioni combinazione
        info = self._generate_info(
            combination_method, 
            normalized_weights, 
            preserve_structure,
            structure_strength,
            raw_weights=weights
        )
        
        return (combined, info)
    
    def _weighted_sum(self, base, conditionings, weights, 
                     preserve_structure, structure_strength):
        """
        Somma pesata con preservazione opzionale struttura base.
        
        Formula: result = base * base_weight + Î£(cond_i * weight_i)
        dove base_weight = 1.0 - (somma pesi normalizzati * fattore)
        """
        # Estrai tensor dal base
        if not isinstance(base, list):
            base = [base]
        
        result = []
        
        # Calcola influenza base
        method_config = self.COMBINATION_METHODS["weighted_sum"]
        base_influence = method_config["base_influence"]
        
        if preserve_structure:
            # Base ha influenza fissa del 50%, il resto Ã¨ distribuito
            base_weight = base_influence
            cond_weights = [(1.0 - base_influence) * w for w in weights]
        else:
            # Base proporzionale ai pesi
            base_weight = 1.0 / (1.0 + sum(weights))
            cond_weights = [w * base_weight for w in weights]
        
        # Processa ogni elemento del conditioning base
        for base_idx, base_item in enumerate(base):
            if isinstance(base_item, (list, tuple)) and len(base_item) >= 2:
                base_tensor, base_dict = base_item[0], base_item[1]
                
                # Inizializza tensor risultato con base
                if isinstance(base_tensor, torch.Tensor):
                    combined_tensor = base_tensor * base_weight
                else:
                    combined_tensor = base_tensor
                
                # Aggiungi ogni conditioning pesato
                for cond_idx, (cond, weight) in enumerate(zip(conditionings, cond_weights)):
                    if isinstance(cond, list) and cond_idx < len(cond):
                        cond_item = cond[cond_idx]
                        if isinstance(cond_item, (list, tuple)) and len(cond_item) >= 2:
                            cond_tensor = cond_item[0]
                            
                            if isinstance(cond_tensor, torch.Tensor) and isinstance(combined_tensor, torch.Tensor):
                                # Verifica shape compatibility
                                if cond_tensor.shape == combined_tensor.shape:
                                    combined_tensor = combined_tensor + (cond_tensor * weight)
                                else:
                                    print(f"[WeightedConditioning] Warning: Shape mismatch cond_{cond_idx+1}, skip")
                        elif isinstance(cond_item, torch.Tensor):
                            if cond_item.shape == combined_tensor.shape:
                                combined_tensor = combined_tensor + (cond_item * weight)
                
                # Mantieni metadati dal base
                combined_dict = {}
                if isinstance(base_dict, dict):
                    combined_dict = copy.deepcopy(base_dict)
                
                # Aggiungi metadati combinazione
                combined_dict["characterforge_combined"] = {
                    "method": "weighted_sum",
                    "weights_applied": [f"{w:.3f}" for w in cond_weights],
                    "base_influence": f"{base_weight:.3f}",
                    "structure_preserved": preserve_structure
                }
                
                result.append([combined_tensor, combined_dict])
            else:
                # Format non riconosciuto, mantieni invariato
                result.append(base_item)
        
        return result
    
    def _average(self, base, conditionings):
        """
        Media aritmetica di tutti i conditioning.
        
        Formula: result = (base + cond_1 + cond_2 + cond_3) / 4
        """
        all_conditionings = [base] + conditionings
        
        # Determina lunghezza massima
        max_len = max(len(c) if isinstance(c, list) else 1 for c in all_conditionings)
        
        result = []
        
        for i in range(max_len):
            tensors_to_avg = []
            base_dict = {}
            
            # Raccogli tensor da tutti i conditioning
            for cond in all_conditionings:
                if isinstance(cond, list) and i < len(cond):
                    item = cond[i]
                    if isinstance(item, (list, tuple)) and len(item) >= 2:
                        tensor, dict_data = item[0], item[1]
                        if isinstance(tensor, torch.Tensor):
                            tensors_to_avg.append(tensor)
                        # Mantieni il dict del base (primo)
                        if cond is base and isinstance(dict_data, dict):
                            base_dict = copy.deepcopy(dict_data)
                    elif isinstance(item, torch.Tensor):
                        tensors_to_avg.append(item)
                elif isinstance(cond, torch.Tensor) and i == 0:
                    tensors_to_avg.append(cond)
            
            # Calcola media
            if tensors_to_avg:
                # Verifica shape compatibility
                shapes = [t.shape for t in tensors_to_avg]
                if all(s == shapes[0] for s in shapes):
                    avg_tensor = torch.stack(tensors_to_avg).mean(dim=0)
                else:
                    # Se shapes diverse, usa il primo
                    avg_tensor = tensors_to_avg[0]
                    print("[WeightedConditioning] Warning: Shape mismatch in average, uso primo tensor")
                
                # Aggiungi metadati
                combined_dict = base_dict.copy() if base_dict else {}
                combined_dict["characterforge_combined"] = {
                    "method": "average",
                    "sources_count": len(tensors_to_avg)
                }
                
                result.append([avg_tensor, combined_dict])
            else:
                # Mantieni elemento base se esiste
                if isinstance(base, list) and i < len(base):
                    result.append(base[i])
        
        return result
    
    def _concat(self, base, conditionings):
        """
        Concatenazione sequenziale dei conditioning.
        
        Simile a ConditioningConcat nativo di ComfyUI:
        concatena gli embedding tensor per dare al modello
        tutte le informazioni contemporaneamente.
        """
        result = []
        
        # Processa base
        if isinstance(base, list):
            for base_item in base:
                if isinstance(base_item, (list, tuple)) and len(base_item) >= 2:
                    base_tensor, base_dict = base_item[0], base_item[1]
                    
                    # Concatena tensor da tutti i conditioning
                    concat_tensor = base_tensor
                    
                    for cond in conditionings:
                        if isinstance(cond, list) and len(cond) > 0:
                            # Prendi il primo elemento del conditioning
                            cond_item = cond[0]
                            if isinstance(cond_item, (list, tuple)) and len(cond_item) >= 2:
                                cond_tensor = cond_item[0]
                                
                                if isinstance(concat_tensor, torch.Tensor) and isinstance(cond_tensor, torch.Tensor):
                                    # Concatenazione lungo dimensione 0 (batch)
                                    if concat_tensor.dim() == cond_tensor.dim():
                                        try:
                                            concat_tensor = torch.cat([concat_tensor, cond_tensor], dim=0)
                                        except RuntimeError:
                                            # Se cat fallisce, prova stack
                                            print("[WeightedConditioning] Info: cat fallito, mantengo base")
                    
                    # Mantieni metadati
                    combined_dict = {}
                    if isinstance(base_dict, dict):
                        combined_dict = copy.deepcopy(base_dict)
                    
                    combined_dict["characterforge_combined"] = {
                        "method": "concat",
                        "sources_combined": 1 + len(conditionings)
                    }
                    
                    result.append([concat_tensor, combined_dict])
                else:
                    result.append(base_item)
        
        return result
    
    def _max_combination(self, base, conditionings, weights):
        """
        Combinazione basata sul massimo valore per dimensione.
        
        Formula: result[i] = max(base[i], cond_1[i]*w_1, cond_2[i]*w_2, ...)
        """
        result = []
        
        if isinstance(base, list):
            for base_idx, base_item in enumerate(base):
                if isinstance(base_item, (list, tuple)) and len(base_item) >= 2:
                    base_tensor, base_dict = base_item[0], base_item[1]
                    
                    if isinstance(base_tensor, torch.Tensor):
                        max_tensor = base_tensor
                        
                        # Applica max con ogni conditioning pesato
                        for cond_idx, (cond, weight) in enumerate(zip(conditionings, weights)):
                            if isinstance(cond, list) and base_idx < len(cond):
                                cond_item = cond[base_idx]
                                if isinstance(cond_item, (list, tuple)) and len(cond_item) >= 2:
                                    cond_tensor = cond_item[0]
                                    
                                    if isinstance(cond_tensor, torch.Tensor):
                                        # Verifica shape
                                        if cond_tensor.shape == max_tensor.shape:
                                            weighted_cond = cond_tensor * weight
                                            max_tensor = torch.maximum(max_tensor, weighted_cond)
                        
                        # Mantieni metadati
                        combined_dict = {}
                        if isinstance(base_dict, dict):
                            combined_dict = copy.deepcopy(base_dict)
                        
                        combined_dict["characterforge_combined"] = {
                            "method": "max",
                            "weights_applied": [f"{w:.3f}" for w in weights]
                        }
                        
                        result.append([max_tensor, combined_dict])
                    else:
                        result.append(base_item)
                else:
                    result.append(base_item)
        
        return result
    
    def _blend(self, base, conditionings, weights, structure_strength):
        """
        Interpolazione lineare pesata verso il base.
        
        Formula: result = base * (1 - t) + weighted_avg(cond) * t
        dove t = 1.0 - structure_strength
        """
        # Fattore interpolazione (piÃ¹ struttura = meno condizionamento)
        t = 1.0 - structure_strength
        
        result = []
        
        if isinstance(base, list):
            for base_idx, base_item in enumerate(base):
                if isinstance(base_item, (list, tuple)) and len(base_item) >= 2:
                    base_tensor, base_dict = base_item[0], base_item[1]
                    
                    if isinstance(base_tensor, torch.Tensor):
                        # Calcola media pesata dei conditioning
                        weighted_sum = torch.zeros_like(base_tensor)
                        total_weight = sum(weights)
                        
                        if total_weight > 0:
                            for cond_idx, (cond, weight) in enumerate(zip(conditionings, weights)):
                                if isinstance(cond, list) and base_idx < len(cond):
                                    cond_item = cond[base_idx]
                                    if isinstance(cond_item, (list, tuple)) and len(cond_item) >= 2:
                                        cond_tensor = cond_item[0]
                                        
                                        if isinstance(cond_tensor, torch.Tensor) and cond_tensor.shape == base_tensor.shape:
                                            weighted_sum += cond_tensor * (weight / total_weight)
                            
                            # Interpolazione
                            blended_tensor = base_tensor * (1.0 - t) + weighted_sum * t
                        else:
                            blended_tensor = base_tensor
                    else:
                        blended_tensor = base_tensor
                    
                    # Mantieni metadati
                    combined_dict = {}
                    if isinstance(base_dict, dict):
                        combined_dict = copy.deepcopy(base_dict)
                    
                    combined_dict["characterforge_combined"] = {
                        "method": "blend",
                        "structure_strength": f"{structure_strength:.3f}",
                        "interpolation_factor": f"{t:.3f}",
                        "weights_normalized": [f"{w/total_weight:.3f}" for w in weights] if total_weight > 0 else []
                    }
                    
                    result.append([blended_tensor, combined_dict])
                else:
                    result.append(base_item)
        
        return result
    
    def _apply_structure_preservation(self, combined, base, strength):
        """
        Applica preservazione struttura al conditioning combinato.
        
        Blend tra il combinato e il base per mantenere
        le informazioni strutturali del layout.
        """
        if not isinstance(combined, list) or not isinstance(base, list):
            return combined
        
        preserved = []
        
        for i, combined_item in enumerate(combined):
            if i < len(base):
                base_item = base[i]
                
                if (isinstance(combined_item, (list, tuple)) and 
                    isinstance(base_item, (list, tuple)) and
                    len(combined_item) >= 2 and len(base_item) >= 2):
                    
                    combined_tensor, combined_dict = combined_item[0], combined_item[1]
                    base_tensor, base_dict = base_item[0], base_item[1]
                    
                    if (isinstance(combined_tensor, torch.Tensor) and 
                        isinstance(base_tensor, torch.Tensor) and
                        combined_tensor.shape == base_tensor.shape):
                        
                        # Preserva: 70% combinato + 30% base
                        preserved_tensor = combined_tensor * (1.0 - strength) + base_tensor * strength
                        
                        # Mantieni dict combinato
                        preserved_dict = copy.deepcopy(combined_dict) if isinstance(combined_dict, dict) else {}
                        preserved_dict["structure_preservation_applied"] = True
                        preserved_dict["structure_strength"] = f"{strength:.3f}"
                        
                        preserved.append([preserved_tensor, preserved_dict])
                    else:
                        preserved.append(combined_item)
                else:
                    preserved.append(combined_item)
            else:
                preserved.append(combined_item)
        
        return preserved
    
    def _generate_info(self, method, weights, preserve_structure, structure_strength, raw_weights=None):
        """
        Genera stringa informativa dettagliata sulla combinazione.
        """
        method_info = self.COMBINATION_METHODS.get(method, {})
        
        info = {
            "controller": "WeightedConditioning",
            "combination_method": method,
            "method_description": method_info.get("description", "Unknown"),
            "raw_weights": [f"{w:.3f}" for w in (raw_weights if raw_weights is not None else weights)],
            "normalized_weights": [f"{w:.3f}" for w in weights],
            "raw_weights_ratio": f"{weights[0]:.2f}:{weights[1]:.2f}:{weights[2]:.2f}",
            "structure_preserved": preserve_structure,
            "structure_strength": f"{structure_strength:.3f}" if preserve_structure else "N/A",
            "total_conditionings_combined": 4,
            "base_influence": method_info.get("base_influence", "method-dependent"),
            "status": "combination successful"
        }
        
        return str(info)
    
    @classmethod
    def IS_CHANGED(s, base_conditioning, conditioning_1, weight_1,
                  conditioning_2, weight_2, conditioning_3, weight_3,
                  combination_method, preserve_structure, 
                  structure_strength=0.3):
        """
        Determina se il nodo deve essere ricalcolato.
        """
        return float("NaN")


# Registrazione per uso diretto (se importato singolarmente)
NODE_CLASS_MAPPINGS = {
    "CharacterForgeWeightedConditioning": CharacterForgeWeightedConditioning
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CharacterForgeWeightedConditioning": "Weighted Conditioning"
}
