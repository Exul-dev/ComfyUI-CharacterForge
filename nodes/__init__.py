"""
ComfyUI-CharacterForge Nodes Package
====================================

Gestione importazioni e registrazioni nodi custom per il
controllo granulare dei character sheet.

Questo pacchetto contiene tutti i nodi che compongono
CharacterForge:
- GenderController: Controllo genere
- EthnicityController: Controllo etnia
- BodyController: Controllo corporatura
- WeightedConditioning: Conditioning pesato
- HybridLatentSwitch: Switch modalità ibrida

Versione: 2.0.0
"""

# Importazioni dei nodi principali
from .gender_controller import CharacterForgeGenderController
from .ethnicity_controller import CharacterForgeEthnicityController
from .body_controller import CharacterForgeBodyController
from .weighted_conditioning import CharacterForgeWeightedConditioning
from .hybrid_switch import CharacterForgeHybridLatentSwitch

# Versione del pacchetto nodes
__version__ = "2.0.0"

# Esportazioni pubbliche
__all__ = [
    'CharacterForgeGenderController',
    'CharacterForgeEthnicityController',
    'CharacterForgeBodyController',
    'CharacterForgeWeightedConditioning',
    'CharacterForgeHybridLatentSwitch'
]

# Informazioni pacchetto
__package_info__ = {
    "name": "characterforge_nodes",
    "version": __version__,
    "description": "Custom nodes for character sheet control in ComfyUI",
    "nodes_available": len(__all__),
    "categories": {
        "CharacterForge/Basic": [
            "CharacterForgeGenderController",
            "CharacterForgeBodyController"
        ],
        "CharacterForge/Advanced": [
            "CharacterForgeEthnicityController",
            "CharacterForgeWeightedConditioning"
        ],
        "CharacterForge/Hybrid": [
            "CharacterForgeHybridLatentSwitch"
        ]
    }
}

# Log di caricamento
print(f"[CharacterForge-Nodes] Pacchetto caricato v{__version__}")
print(f"[CharacterForge-Nodes] Nodi disponibili: {len(__all__)}")