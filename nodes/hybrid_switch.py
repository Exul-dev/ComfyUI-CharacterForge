"""
CharacterForge Hybrid Latent Switch
====================================

Switch intelligente per commutazione automatica tra modalità
Text-to-Sheet e Image-to-Sheet.

Gestisce il routing del latent input:
- Text-to-Sheet: usa EmptyLatentImage (generazione da prompt)
- Image-to-Sheet: usa VAEEncode da immagine riferimento

Il nodo include validazione input, logging dettagliato
e gestione errori robusta per un'affidabilità production-ready.
"""

import torch


class CharacterForgeHybridLatentSwitch:
    """
    Switch intelligente per latent input.
    
    Permette di commutare tra:
    - Empty Latent (Text-to-Sheet): generazione completa da prompt
    - VAE Encode da immagine (Image-to-Sheet): mantiene identità
    
    Caratteristiche:
    - Validazione automatica input latent
    - Logging dettagliato modalità attiva
    - Gestione fallback intelligente
    - Metadati tracciabilità per debugging
    """
    
    # Configurazione modalità disponibili
    MODE_CONFIGS = {
        "text_to_sheet": {
            "description": "Generazione character sheet da prompt testuale",
            "uses": "EmptyLatentImage (2048x1024 consigliato)",
            "denoise_suggestion": 1.0,
            "k_sampler_notes": "Generazione completa, nessuna identità di partenza"
        },
        "image_to_sheet": {
            "description": "Generazione character sheet da immagine riferimento",
            "uses": "VAEEncode + IPAdapter per identità",
            "denoise_suggestion": 0.6,
            "k_sampler_notes": "Mantiene 30-40% identità originale"
        }
    }
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "mode": (["text_to_sheet", "image_to_sheet"], {
                    "default": "text_to_sheet",
                    "tooltip": "Modalità del workflow: Text (prompt) o Image (riferimento)"
                }),
                "text_latent": ("LATENT", {
                    "tooltip": "Latent da EmptyLatentImage (usato in modalità text_to_sheet)"
                }),
                "image_latent": ("LATENT", {
                    "tooltip": "Latent da VAEEncode (usato in modalità image_to_sheet)"
                }),
            },
            "optional": {
                "image_reference": ("IMAGE", {
                    "tooltip": "Immagine di riferimento (per debug e visualizzazione)"
                }),
                "auto_validate": ("BOOLEAN", {
                    "default": True,
                    "tooltip": "Valida automaticamente i latent input prima del routing"
                }),
                "debug_mode": ("BOOLEAN", {
                    "default": False,
                    "tooltip": "Attiva logging dettagliato per debugging"
                }),
            }
        }
    
    RETURN_TYPES = ("LATENT", "STRING", "IMAGE",)
    RETURN_NAMES = ("selected_latent", "active_mode_info", "reference_preview",)
    FUNCTION = "switch_latent"
    CATEGORY = "CharacterForge/Hybrid"
    
    def switch_latent(self, mode, text_latent, image_latent, 
                     image_reference=None, auto_validate=True, debug_mode=False):
        """
        Seleziona e instrada il latent appropriato in base alla modalità.
        
        Args:
            mode: Modalità del workflow ("text_to_sheet" o "image_to_sheet")
            text_latent: Latent per Text-to-Sheet (da EmptyLatentImage)
            image_latent: Latent per Image-to-Sheet (da VAEEncode)
            image_reference: Immagine riferimento opzionale
            auto_validate: Se validare automaticamente i latent
            debug_mode: Se attivare logging dettagliato
            
        Returns:
            tuple: (latent selezionato, info modalità, preview immagine)
        """
        # Validazione modalità
        if mode not in self.MODE_CONFIGS:
            error_msg = f"Modalità '{mode}' non riconosciuta. Usare: 'text_to_sheet' o 'image_to_sheet'"
            print(f"[HybridLatentSwitch] ERROR: {error_msg}")
            raise ValueError(error_msg)
        
        # Validazione automatica latent se attivata
        if auto_validate:
            text_valid, text_error = self._validate_latent(text_latent, "text_latent")
            image_valid, image_error = self._validate_latent(image_latent, "image_latent")
            
            if debug_mode:
                print(f"[HybridLatentSwitch] Debug - Validazione:")
                print(f"  text_latent: {'VALID' if text_valid else f'INVALID ({text_error})'}")
                print(f"  image_latent: {'VALID' if image_valid else f'INVALID ({image_error})'}")
            
            # Verifica che il latent per la modalità selezionata sia valido
            if mode == "text_to_sheet" and not text_valid:
                error_msg = f"text_latent non valido: {text_error}"
                print(f"[HybridLatentSwitch] ERROR: {error_msg}")
                raise ValueError(error_msg)
            
            if mode == "image_to_sheet" and not image_valid:
                error_msg = f"image_latent non valido: {image_error}"
                print(f"[HybridLatentSwitch] ERROR: {error_msg}")
                raise ValueError(error_msg)
        
        # Log modalità selezionata
        if debug_mode:
            print(f"[HybridLatentSwitch] Modalità selezionata: {mode}")
            print(f"[HybridLatentSwitch] Descrizione: {self.MODE_CONFIGS[mode]['description']}")
        
        # Routing del latent
        if mode == "text_to_sheet":
            selected = self._prepare_text_latent(text_latent, debug_mode)
            active_mode_info = self._generate_mode_info(
                "text_to_sheet", 
                selected, 
                text_latent,
                None,
                debug_mode
            )
        elif mode == "image_to_sheet":
            selected = self._prepare_image_latent(image_latent, debug_mode)
            active_mode_info = self._generate_mode_info(
                "image_to_sheet", 
                selected, 
                None,
                image_latent,
                debug_mode
            )
        else:
            # Fallback (non dovrebbe mai accadere)
            selected = text_latent
            active_mode_info = self._generate_mode_info(
                "fallback_text", 
                selected, 
                text_latent,
                None,
                debug_mode
            )
        
        return (selected, active_mode_info, image_reference)
    
    def _validate_latent(self, latent, name):
        """
        Valida un latent input.
        
        Args:
            latent: Il latent da validare
            name: Nome per identificazione errori
            
        Returns:
            tuple: (is_valid, error_message)
        """
        # Verifica che non sia None
        if latent is None:
            return False, "Latent è None"
        
        # Verifica formato ComfyUI latent
        # Il formato standard è un dict con 'samples' o un tensor
        if isinstance(latent, dict):
            if "samples" in latent:
                samples = latent["samples"]
                if isinstance(samples, torch.Tensor):
                    if samples.numel() == 0:
                        return False, "Tensor samples vuoto (numel=0)"
                    if samples.dim() < 3:
                        return False, f"Dimensioni tensor insufficienti ({samples.dim()}D, min 3D)"
                    return True, None
                else:
                    return False, f"samples non è un Tensor (tipo: {type(samples).__name__})"
            else:
                return False, "Dict senza chiave 'samples'"
        elif isinstance(latent, torch.Tensor):
            if latent.numel() == 0:
                return False, "Tensor vuoto (numel=0)"
            if latent.dim() < 3:
                return False, f"Dimensioni tensor insufficienti ({latent.dim()}D, min 3D)"
            return True, None
        elif isinstance(latent, (list, tuple)):
            # Alcuni workflow passano latent come liste
            if len(latent) > 0:
                return True, None
            else:
                return False, "Lista latent vuota"
        else:
            return False, f"Formato latent non riconosciuto (tipo: {type(latent).__name__})"
    
    def _prepare_text_latent(self, text_latent, debug_mode=False):
        """
        Prepara il latent per modalità Text-to-Sheet.
        
        Args:
            text_latent: Latent da EmptyLatentImage
            debug_mode: Logging dettagliato
            
        Returns:
            Il latent preparato
        """
        if debug_mode:
            print(f"[HybridLatentSwitch] Preparazione TEXT latent:")
            self._log_latent_info(text_latent, "text_latent")
        
        # Il latent da EmptyLatentImage è già pronto
        # Aggiungi eventuali metadati se in formato dict
        if isinstance(text_latent, dict):
            prepared = text_latent.copy()
            prepared["characterforge_mode"] = "text_to_sheet"
            prepared["characterforge_timestamp"] = "auto"
            return prepared
        else:
            return text_latent
    
    def _prepare_image_latent(self, image_latent, debug_mode=False):
        """
        Prepara il latent per modalità Image-to-Sheet.
        
        Args:
            image_latent: Latent da VAEEncode
            debug_mode: Logging dettagliato
            
        Returns:
            Il latent preparato
        """
        if debug_mode:
            print(f"[HybridLatentSwitch] Preparazione IMAGE latent:")
            self._log_latent_info(image_latent, "image_latent")
        
        # Il latent da VAEEncode è già pronto
        # Aggiungi eventuali metadati se in formato dict
        if isinstance(image_latent, dict):
            prepared = image_latent.copy()
            prepared["characterforge_mode"] = "image_to_sheet"
            prepared["characterforge_timestamp"] = "auto"
            return prepared
        else:
            return image_latent
    
    def _generate_mode_info(self, mode, selected_latent, 
                           text_latent, image_latent, debug_mode=False):
        """
        Genera stringa informativa dettagliata sulla modalità attiva.
        
        Args:
            mode: Modalità attiva
            selected_latent: Latent selezionato
            text_latent: Latent text originale (per confronto)
            image_latent: Latent image originale (per confronto)
            debug_mode: Se includere info extra
            
        Returns:
            str: Stringa JSON-formattata con info modalità
        """
        mode_config = self.MODE_CONFIGS.get(mode, {})
        
        info = {
            "controller": "HybridLatentSwitch",
            "active_mode": mode,
            "mode_description": mode_config.get("description", "Unknown"),
            "uses": mode_config.get("uses", "Unknown"),
            "denoise_suggestion": mode_config.get("denoise_suggestion", 1.0),
            "k_sampler_notes": mode_config.get("k_sampler_notes", ""),
            "routing": "text_latent" if mode in ["text_to_sheet", "fallback_text"] else "image_latent",
            "status": "switched successfully"
        }
        
        # Info aggiuntive in debug mode
        if debug_mode:
            info["debug_details"] = {
                "text_latent_available": text_latent is not None,
                "image_latent_available": image_latent is not None,
                "selected_latent_type": type(selected_latent).__name__,
                "mode_configs_available": list(self.MODE_CONFIGS.keys())
            }
        
        # Info sulla shape del latent selezionato (se disponibile)
        if isinstance(selected_latent, dict) and "samples" in selected_latent:
            samples = selected_latent["samples"]
            if isinstance(samples, torch.Tensor):
                info["latent_shape"] = str(list(samples.shape))
        elif isinstance(selected_latent, torch.Tensor):
            info["latent_shape"] = str(list(selected_latent.shape))
        
        return str(info)
    
    def _log_latent_info(self, latent, name):
        """
        Stampa informazioni dettagliate su un latent (per debug).
        """
        if isinstance(latent, dict):
            print(f"  {name} (dict): keys={list(latent.keys())}")
            if "samples" in latent and isinstance(latent["samples"], torch.Tensor):
                print(f"    samples shape: {latent['samples'].shape}")
                print(f"    samples dtype: {latent['samples'].dtype}")
        elif isinstance(latent, torch.Tensor):
            print(f"  {name} (tensor): shape={latent.shape}, dtype={latent.dtype}")
        else:
            print(f"  {name} (type): {type(latent).__name__}")
    
    @classmethod
    def IS_CHANGED(s, mode, text_latent, image_latent, 
                   image_reference=None, auto_validate=True, debug_mode=False):
        """
        Determina se il nodo deve essere ricalcolato.
        Ritorna il mode per ricalcolo solo quando cambia la modalità.
        """
        return mode


# Registrazione per uso diretto (se importato singolarmente)
NODE_CLASS_MAPPINGS = {
    "CharacterForgeHybridLatentSwitch": CharacterForgeHybridLatentSwitch
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CharacterForgeHybridLatentSwitch": "Hybrid Latent Switch"
}