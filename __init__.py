"""
ComfyUI-CharacterForge
=====================

Set professionale di nodi custom per il controllo granulare dei character sheet
con supporto ibrido Text-to-Sheet e Image-to-Sheet.

Ottimizzato per Krea2 e compatibile con l'ultima versione di ComfyUI.

Versione: 2.1.0
Autore: Massimo Bivona
Licenza: MIT

Caratteristiche:
- Controllo granulare genere, etnia, corporatura
- Sistema weighted conditioning con pesi configurabili
- Workflow ibrido Text-to-Sheet / Image-to-Sheet
- Preservazione automatica struttura character sheet
- Style Transfer con preset anni '80 e non solo
- Combinatore LoRA per stili personalizzati
- Database preset stili organizzati per categoria

Categorie Nodi:
- CharacterForge/Basic: Controlli base (genere, corporatura)
- CharacterForge/Advanced: Controlli avanzati (etnia, conditioning)
- CharacterForge/Hybrid: Sistema switch modalità ibrida
- CharacterForge/Style: Style Transfer e combinatore LoRA

Preset Styles Database:
- retro_80s: Anime anni '80, fotografia analogica, VHS, synthwave
- anime: Anime moderno, Studio Ghibli
- western: Cartoon, American Comic
- artistic: Watercolor, Pixel Art
"""

import traceback

__version__ = "2.1.0"
__author__ = "Massimo Bivona"
__license__ = "MIT"

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# ============================================
# CONTROLLI BASE
# ============================================

try:
    from .nodes.gender_controller import CharacterForgeGenderController
    NODE_CLASS_MAPPINGS["CharacterForgeGenderController"] = CharacterForgeGenderController
    NODE_DISPLAY_NAME_MAPPINGS["CharacterForgeGenderController"] = "Gender Controller"
    print("[CharacterForge] Gender Controller OK")

    from .nodes.ethnicity_controller import CharacterForgeEthnicityController
    NODE_CLASS_MAPPINGS["CharacterForgeEthnicityController"] = CharacterForgeEthnicityController
    NODE_DISPLAY_NAME_MAPPINGS["CharacterForgeEthnicityController"] = "Ethnicity Controller"
    print("[CharacterForge] Ethnicity Controller OK")

    from .nodes.body_controller import CharacterForgeBodyController
    NODE_CLASS_MAPPINGS["CharacterForgeBodyController"] = CharacterForgeBodyController
    NODE_DISPLAY_NAME_MAPPINGS["CharacterForgeBodyController"] = "Body Type Controller"
    print("[CharacterForge] Body Controller OK")

    from .nodes.weighted_conditioning import CharacterForgeWeightedConditioning
    NODE_CLASS_MAPPINGS["CharacterForgeWeightedConditioning"] = CharacterForgeWeightedConditioning
    NODE_DISPLAY_NAME_MAPPINGS["CharacterForgeWeightedConditioning"] = "Weighted Conditioning"
    print("[CharacterForge] Weighted Conditioning OK")

    from .nodes.hybrid_switch import CharacterForgeHybridLatentSwitch
    NODE_CLASS_MAPPINGS["CharacterForgeHybridLatentSwitch"] = CharacterForgeHybridLatentSwitch
    NODE_DISPLAY_NAME_MAPPINGS["CharacterForgeHybridLatentSwitch"] = "Hybrid Latent Switch"
    print("[CharacterForge] Hybrid Latent Switch OK")

except Exception as e:
    print(f"[CharacterForge] ERRORE CONTROLLI BASE: {e}")
    traceback.print_exc()

# ============================================
# STYLE TRANSFER NODI
# ============================================

try:
    from .nodes.style_transfer_node import CharacterForgeStyleTransferNode
    NODE_CLASS_MAPPINGS["CharacterForgeStyleTransferNode"] = CharacterForgeStyleTransferNode
    NODE_DISPLAY_NAME_MAPPINGS["CharacterForgeStyleTransferNode"] = "Style Transfer Node"
    print("[CharacterForge] Style Transfer Node OK")

    from .nodes.lora_style_combinator import CharacterForgeLoRAStyleCombinator
    NODE_CLASS_MAPPINGS["CharacterForgeLoRAStyleCombinator"] = CharacterForgeLoRAStyleCombinator
    NODE_DISPLAY_NAME_MAPPINGS["CharacterForgeLoRAStyleCombinator"] = "LoRA Style Combinator"
    print("[CharacterForge] LoRA Style Combinator OK")

except Exception as e:
    print(f"[CharacterForge] ERRORE STYLE TRANSFER: {e}")
    traceback.print_exc()

# ============================================
# PRESET STYLES DATABASE
# ============================================

try:
    from .preset_styles import STYLE_PRESETS
    PRESET_STYLES_AVAILABLE = len(STYLE_PRESETS)
    print(f"[CharacterForge] Preset Styles caricati: {PRESET_STYLES_AVAILABLE}")
    
    # Log categorie disponibili
    from .preset_styles import get_styles_by_category
    categories = ["retro_80s", "anime", "western", "artistic"]
    for category in categories:
        styles_in_category = get_styles_by_category(category)
        if styles_in_category:
            print(f"[CharacterForge]   {category}: {len(styles_in_category)} stili")

except Exception as e:
    print(f"[CharacterForge] Warning: Preset Styles non disponibili: {e}")
    PRESET_STYLES_AVAILABLE = 0

# ============================================
# INIZIALIZZAZIONE FINALE
# ============================================

print(f"[CharacterForge] v{__version__} caricato: {len(NODE_CLASS_MAPPINGS)} nodi")

if PRESET_STYLES_AVAILABLE > 0:
    print(f"[CharacterForge] Database stili: {PRESET_STYLES_AVAILABLE} preset disponibili")

# ============================================
# ESPOSTAZIONI PUBBLICHE
# ============================================

__all__ = [
    'NODE_CLASS_MAPPINGS',
    'NODE_DISPLAY_NAME_MAPPINGS',
    '__version__',
    '__author__',
    '__license__',
    'STYLE_PRESETS',
    'PRESET_STYLES_AVAILABLE'
]