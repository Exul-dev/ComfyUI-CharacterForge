"""
ComfyUI-CharacterForge Nodes Package
====================================

Gestione importazioni e registrazioni nodi custom per il
controllo granulare dei character sheet e style transfer.

Controlli Base:
- GenderController: Controllo genere
- EthnicityController: Controllo etnia
- BodyController: Controllo corporatura

Controlli Avanzati:
- WeightedConditioning: Conditioning pesato
- HybridLatentSwitch: Switch modalità ibrida

Style Transfer (MODULO 3):
- StyleTransferNode v3.0.0: 11 preset storici + 128 stili anime
  (database preset_styles/anime) nel menu a tendina unico,
  negative_conditioning automatico, denoise_mode
  (safe / balanced / radical), tag anti-fotorealismo
- LoRAStyleCombinator: Combinatore LoRA per stili personalizzati

Scene Interrogator (MODULO 4):
- SceneInterrogatorNode: immagine di scena -> prompt video
  (backend JoyCaption o Florence-2, query configurabile)
- SavePromptNode: salva il prompt su .txt per il modulo video

NOTE v2.3.0:
- I nodi AnimeStyleSelector/AnimeStyleMixer sono SUPERATI:
  i 128 stili sono integrati nello StyleTransferNode v3.0.0.
- Import style transfer da style_transfer_node.py (primario,
  è quello che importa anche il __init__.py radice); fallback
  su StyleTransferNode.py per compatibilità.
- Diagnostica automatica: stampa a ogni avvio se la versione
  caricata contiene i 128 stili (PRESET_CHOICES > 11).

Versione: 2.3.0
"""

# ============================================
# CONTROLLI BASE
# ============================================

from .gender_controller import CharacterForgeGenderController
from .ethnicity_controller import CharacterForgeEthnicityController
from .body_controller import CharacterForgeBodyController

# ============================================
# CONTROLLI AVANZATI
# ============================================

from .weighted_conditioning import CharacterForgeWeightedConditioning
from .hybrid_switch import CharacterForgeHybridLatentSwitch

# ============================================
# STYLE TRANSFER — MODULO 3
# ============================================
# Primario: style_transfer_node.py (v3.0.0, lo stesso file che
# importa il __init__.py radice — così i due import coincidono).
# Fallback: StyleTransferNode.py (copia storica).

try:
    from .style_transfer_node import CharacterForgeStyleTransferNode
    from .lora_style_combinator import CharacterForgeLoRAStyleCombinator
    _STYLE_SOURCE = "style_transfer_node.py"
except ImportError:
    from .StyleTransferNode import CharacterForgeStyleTransferNode
    from .LoRAStyleCombinator import CharacterForgeLoRAStyleCombinator
    _STYLE_SOURCE = "StyleTransferNode.py"

# Diagnostica versione: la v3.0.0 (e la 2.2.0+) espone PRESET_CHOICES
# come attributo di classe con 128 stili anime + 11 preset.
_STYLE_PRESETS = len(getattr(CharacterForgeStyleTransferNode, "PRESET_CHOICES", []))
_STYLES_V3 = _STYLE_PRESETS > 11

if not _STYLES_V3:
    print(f"[CharacterForge-Nodes] ATTENZIONE: {_STYLE_SOURCE} contiene una")
    print(f"[CharacterForge-Nodes]   versione VECCHIA dello StyleTransferNode")
    print(f"[CharacterForge-Nodes]   ({_STYLE_PRESETS} preset, niente 128 stili anime).")
    print(f"[CharacterForge-Nodes]   -> incollare la v3.0.0 in nodes/style_transfer_node.py")

# ============================================
# SCENE INTERROGATOR — MODULO 4
# ============================================

try:
    from .scene_interrogator import CharacterForgeSceneInterrogatorNode
    from .scene_interrogator import CharacterForgeSavePromptNode
    _SCENE_NODES_OK = True
except ImportError as e:
    print(f"[CharacterForge-Nodes] WARNING: Modulo 4 non disponibile: {e}")
    print(f"[CharacterForge-Nodes]   -> creare nodes/scene_interrogator.py")
    _SCENE_NODES_OK = False
except Exception as e:
    print(f"[CharacterForge-Nodes] WARNING: errore caricamento Modulo 4: {e}")
    _SCENE_NODES_OK = False

# ============================================
# CONFIGURAZIONE PACCHETTO
# ============================================

__version__ = "2.3.0"

__all__ = [
    'CharacterForgeGenderController',
    'CharacterForgeEthnicityController',
    'CharacterForgeBodyController',
    'CharacterForgeWeightedConditioning',
    'CharacterForgeHybridLatentSwitch',
    'CharacterForgeStyleTransferNode',
    'CharacterForgeLoRAStyleCombinator',
    'CharacterForgeSceneInterrogatorNode',
    'CharacterForgeSavePromptNode',
]

__package_info__ = {
    "name": "characterforge_nodes",
    "version": __version__,
    "description": "Custom nodes for character sheet control, style transfer and scene interrogation in ComfyUI",
    "nodes_available": len(__all__),
    "styles_v3_loaded": _STYLES_V3,
    "style_presets_count": _STYLE_PRESETS,
    "scene_nodes_loaded": _SCENE_NODES_OK,
    "modules": {
        "controlli (moduli 1-2)": [
            "CharacterForgeGenderController",
            "CharacterForgeEthnicityController",
            "CharacterForgeBodyController",
            "CharacterForgeWeightedConditioning",
            "CharacterForgeHybridLatentSwitch",
        ],
        "style transfer (modulo 3)": [
            "CharacterForgeStyleTransferNode",
            "CharacterForgeLoRAStyleCombinator",
        ],
        "scene interrogator (modulo 4)": [
            "CharacterForgeSceneInterrogatorNode",
            "CharacterForgeSavePromptNode",
        ],
    },
}

# ============================================
# LOG DI CARICAMENTO
# ============================================

print(f"[CharacterForge-Nodes] Pacchetto caricato v{__version__}")
print(f"[CharacterForge-Nodes] Nodi disponibili: {len(__all__)}")
print(f"[CharacterForge-Nodes] Sorgente Style Transfer: {_STYLE_SOURCE}")
if _STYLES_V3:
    print(f"[CharacterForge-Nodes] Style Transfer v3.0.0: OK ({_STYLE_PRESETS} stili nel menu)")
else:
    print(f"[CharacterForge-Nodes] Style Transfer: VERSIONE VECCHIA (vedi warning sopra)")
if _SCENE_NODES_OK:
    print(f"[CharacterForge-Nodes] Modulo 4 Scene Interrogator: OK")
else:
    print(f"[CharacterForge-Nodes] Modulo 4: NON caricato")