"""
ComfyUI-CharacterForge
=====================

Set professionale di nodi custom per il controllo granulare dei character sheet
con supporto ibrido Text-to-Sheet e Image-to-Sheet.

Ottimizzato per Krea2 e compatibile con l'ultima versione di ComfyUI.

Versione: 2.1.0
Autore: Massimo Bivona
Licenza: MIT
"""

__version__ = "2.1.0"
__author__ = "Massimo Bivona"
__license__ = "MIT"

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# Valori disponibili anche quando pytest carica questo file come
# modulo standalone senza package parent.
PRESET_STYLES_AVAILABLE = 0
STYLE_PRESETS = {}

# ============================================================
# BOOTSTRAP COMFYUI
# ============================================================
#
# In ComfyUI __package__ è valorizzato e il custom node viene
# caricato come package.
#
# Durante pytest, invece, questa directory può essere eseguita
# come package-less __init__.py. Gli import relativi (.nodes...)
# in quel contesto non sono validi.
#
# I test importano direttamente i moduli che devono testare,
# quindi il bootstrap ComfyUI non deve essere eseguito durante
# la raccolta pytest.

if __package__:

    # ============================================
    # CONTROLLI BASE
    # ============================================

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

    # ============================================
    # STYLE TRANSFER
    # ============================================

    from .nodes.style_transfer_node import CharacterForgeStyleTransferNode
    NODE_CLASS_MAPPINGS["CharacterForgeStyleTransferNode"] = CharacterForgeStyleTransferNode
    NODE_DISPLAY_NAME_MAPPINGS["CharacterForgeStyleTransferNode"] = "Style Transfer Node"
    print("[CharacterForge] Style Transfer Node OK")

    from .nodes.lora_style_combinator import CharacterForgeLoRAStyleCombinator
    NODE_CLASS_MAPPINGS["CharacterForgeLoRAStyleCombinator"] = CharacterForgeLoRAStyleCombinator
    NODE_DISPLAY_NAME_MAPPINGS["CharacterForgeLoRAStyleCombinator"] = "LoRA Style Combinator"
    print("[CharacterForge] LoRA Style Combinator OK")

    # ============================================
    # PRESET STYLES DATABASE
    # ============================================

    from .preset_styles import STYLE_PRESETS
    PRESET_STYLES_AVAILABLE = len(STYLE_PRESETS)
    print(f"[CharacterForge] Preset Styles caricati: {PRESET_STYLES_AVAILABLE}")

    from .preset_styles import get_styles_by_category

    categories = ["retro_80s", "anime", "western", "artistic", "cinematic"]

    for category in categories:
        styles_in_category = get_styles_by_category(category)
        if styles_in_category:
            print(
                f"[CharacterForge]   {category}: "
                f"{len(styles_in_category)} stili"
            )

    # ============================================
    # INIZIALIZZAZIONE FINALE
    # ============================================

    print(
        f"[CharacterForge] v{__version__} caricato: "
        f"{len(NODE_CLASS_MAPPINGS)} nodi"
    )

    if PRESET_STYLES_AVAILABLE > 0:
        print(
            f"[CharacterForge] Database stili: "
            f"{PRESET_STYLES_AVAILABLE} preset disponibili"
        )

# ============================================================
# ESPOSIZIONI PUBBLICHE
# ============================================================

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "__version__",
    "__author__",
    "__license__",
    "STYLE_PRESETS",
    "PRESET_STYLES_AVAILABLE",
]
