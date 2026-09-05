"""
ComfyUI-CharacterForge
=====================

Set professionale di nodi custom per il controllo granulare dei character sheet
con supporto ibrido Text-to-Sheet e Image-to-Sheet.

Ottimizzato per Krea2/Flux e compatibile con l'ultima versione di ComfyUI.

Versione: 2.0.0
Autore: [Il Tuo Nome]
Licenza: MIT
Repository: https://github.com/tuousername/ComfyUI-CharacterForge

Caratteristiche Principali:
- Controllo granulare genere, etnia, corporatura
- Sistema weighted conditioning con pesi configurabili
- Workflow ibrido Text-to-Sheet / Image-to-Sheet
- Preservazione automatica struttura character sheet
- Supporto LoRA per stili personalizzati
- Compatibilità IPAdapter per identità da riferimento

Categorie Nodi:
- CharacterForge/Basic: Controlli base (genere, corporatura)
- CharacterForge/Advanced: Controlli avanzati (etnia, conditioning)
- CharacterForge/Hybrid: Sistema switch modalità ibrida
"""

import os
import sys
import json
import traceback
from pathlib import Path

# ============================================
# CONFIGURAZIONE GLOBALE
# ============================================

__version__ = "2.0.0"
__author__ = "[Il Tuo Nome]"
__license__ = "MIT"
__repository__ = "https://github.com/tuousername/ComfyUI-CharacterForge"

# Percorso base del pacchetto
PACKAGE_DIR = Path(__file__).parent
CONFIG_DIR = PACKAGE_DIR / "config"
NODES_DIR = PACKAGE_DIR / "nodes"

# ============================================
# CARICAMENTO CONFIGURAZIONE
# ============================================

def load_config():
    """
    Carica la configurazione di default del pacchetto.
    
    Returns:
        dict: Configurazione caricata o configurazione di default
    """
    default_config = {
        "version": __version__,
        "debug_mode": False,
        "hybrid_mode": True,
        "default_mode": "text_to_sheet",
        "preserve_structure": True,
        "weight_range": {
            "min": 0.0,
            "max": 1.5,
            "step": 0.01
        },
        "max_conditioning_inputs": 4,
        "model_compatibility": {
            "primary": ["flux1-dev", "flux1-schnell", "krea2"],
            "secondary": ["sdxl-base", "sd3-large"],
            "lora_support": True,
            "ipadapter_support": True
        }
    }
    
    try:
        config_path = CONFIG_DIR / "default_config.json"
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                loaded_config = json.load(f)
                # Merge con default (loaded ha priorità)
                default_config.update(loaded_config)
    except Exception as e:
        print(f"[CharacterForge] Warning: Impossibile caricare config, uso default: {e}")
    
    return default_config

# ============================================
# IMPORTAZIONE NODI
# ============================================

# Lista nodi disponibili per importazione
AVAILABLE_NODES = [
    "gender_controller",
    "ethnicity_controller", 
    "body_controller",
    "weighted_conditioning",
    "hybrid_switch"
]

def import_nodes():
    """
    Importa dinamicamente tutti i nodi disponibili.
    
    Returns:
        tuple: (NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS, NODE_LOADED_SUCCESSFULLY, NODE_FAILED_IMPORTS)
    """
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}
    NODE_LOADED_SUCCESSFULLY = []
    NODE_FAILED_IMPORTS = {}
    
    # Importazione moduli
    imported_modules = {}
    for node_module_name in AVAILABLE_NODES:
        try:
            # Importazione dinamica del modulo
            module_path = f".nodes.{node_module_name}"
            module = __import__(module_path, fromlist=[''])
            imported_modules[node_module_name] = module
            
            # Verifica che il modulo abbia NODE_CLASS_MAPPINGS
            if hasattr(module, 'NODE_CLASS_MAPPINGS'):
                # Merge dei mappings del modulo
                module_mappings = module.NODE_CLASS_MAPPINGS
                for key, value in module_mappings.items():
                    if key not in NODE_CLASS_MAPPINGS:  # Evita sovrascritture
                        NODE_CLASS_MAPPINGS[key] = value
                
                # Merge display names
                if hasattr(module, 'NODE_DISPLAY_NAME_MAPPINGS'):
                    module_display_names = module.NODE_DISPLAY_NAME_MAPPINGS
                    for key, value in module_display_names.items():
                        if key not in NODE_DISPLAY_NAME_MAPPINGS:
                            NODE_DISPLAY_NAME_MAPPINGS[key] = value
                
                NODE_LOADED_SUCCESSFULLY.append(node_module_name)
            else:
                # Se non ha NODE_CLASS_MAPPINGS, cerca classi esportate
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if (isinstance(attr, type) and 
                        attr_name.startswith('CharacterForge') and
                        attr_name not in ('CharacterForge',)):
                        
                        NODE_CLASS_MAPPINGS[attr_name] = attr
                        display_name = attr_name.replace('CharacterForge', '').replace('Controller', ' Controller')
                        NODE_DISPLAY_NAME_MAPPINGS[attr_name] = display_name.strip()
                
                NODE_LOADED_SUCCESSFULLY.append(node_module_name)
                
        except ImportError as e:
            NODE_FAILED_IMPORTS[node_module_name] = f"ImportError: {e}"
            print(f"[CharacterForge] Warning: Impossibile importare '{node_module_name}': {e}")
        except Exception as e:
            NODE_FAILED_IMPORTS[node_module_name] = f"GenericError: {e}"
            print(f"[CharacterForge] Warning: Errore caricamento '{node_module_name}': {e}")
            if DEBUG_MODE:
                traceback.print_exc()
    
    return NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS, NODE_LOADED_SUCCESSFULLY, NODE_FAILED_IMPORTS

# ============================================
# INIZIALIZZAZIONE
# ============================================

# Carica configurazione globale
CONFIG = load_config()
DEBUG_MODE = CONFIG.get("debug_mode", False)

# Importa tutti i nodi
try:
    NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS, NODE_LOADED_SUCCESSFULLY, NODE_FAILED_IMPORTS = import_nodes()
except Exception as e:
    print(f"[CharacterForge] ERRORE CRITICO durante l'importazione dei nodi: {e}")
    if DEBUG_MODE:
        traceback.print_exc()
    # Fallback: mappings vuoti
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}
    NODE_LOADED_SUCCESSFULLY = []
    NODE_FAILED_IMPORTS = {}

# ============================================
# CONFIGURAZIONE COMPATIBILITÀ MODELLI
# ============================================

MODEL_COMPATIBILITY = {
    "primary_models": [
        "flux1-dev",
        "flux1-schnell", 
        "krea2",
        "flux1-dev-fp8"
    ],
    "secondary_models": [
        "sdxl-base-1.0",
        "sd3-large",
        "juggernaut-xl"
    ],
    "lora_support": True,
    "ipadapter_support": True,
    "controlnet_support": True,
    "min_vram_gb": 16,
    "recommended_vram_gb": 24,
    "recommended_ram_gb": 32
}

# ============================================
# UTILITIES E HELPER FUNCTIONS
# ============================================

def get_node_info(node_name):
    """
    Ottiene informazioni dettagliate su un nodo specifico.
    
    Args:
        node_name (str): Nome del nodo
        
    Returns:
        dict: Informazioni sul nodo o None se non trovato
    """
    if node_name in NODE_CLASS_MAPPINGS:
        node_class = NODE_CLASS_MAPPINGS[node_name]
        
        # Estrae informazioni dal nodo
        info = {
            "name": node_name,
            "display_name": NODE_DISPLAY_NAME_MAPPINGS.get(node_name, node_name),
            "class": node_class.__name__,
            "module": node_class.__module__,
            "category": getattr(node_class, 'CATEGORY', 'Unknown'),
            "function": getattr(node_class, 'FUNCTION', None),
            "description": node_class.__doc__.split('\n')[0] if node_class.__doc__ else "No description"
        }
        
        # Estrae input types se disponibili
        if hasattr(node_class, 'INPUT_TYPES'):
            try:
                input_types = node_class.INPUT_TYPES()
                info["inputs"] = {
                    "required": list(input_types.get("required", {}).keys()),
                    "optional": list(input_types.get("optional", {}).keys())
                }
            except Exception:
                info["inputs"] = "Unable to retrieve"
        
        return info
    return None

def list_all_nodes():
    """
    Lista tutti i nodi disponibili con le loro informazioni.
    
    Returns:
        list: Lista di dizionari con informazioni sui nodi
    """
    nodes_info = []
    for node_name in NODE_CLASS_MAPPINGS:
        info = get_node_info(node_name)
        if info:
            nodes_info.append(info)
    return nodes_info

def get_supported_features():
    """
    Ottiene le funzionalità supportate da questa versione.
    
    Returns:
        list: Lista delle funzionalità supportate
    """
    features = []
    
    if "CharacterForgeGenderController" in NODE_CLASS_MAPPINGS:
        features.append("gender_control")
    
    if "CharacterForgeEthnicityController" in NODE_CLASS_MAPPINGS:
        features.append("ethnicity_control")
    
    if "CharacterForgeBodyController" in NODE_CLASS_MAPPINGS:
        features.append("body_type_control")
    
    if "CharacterForgeWeightedConditioning" in NODE_CLASS_MAPPINGS:
        features.append("weighted_conditioning")
    
    if "CharacterForgeHybridLatentSwitch" in NODE_CLASS_MAPPINGS:
        features.append("hybrid_mode")
    
    return features

def check_model_compatibility(model_name):
    """
    Verifica la compatibilità di un modello.
    
    Args:
        model_name (str): Nome del modello da verificare
        
    Returns:
        tuple: (is_compatible, compatibility_level)
    """
    model_name_lower = model_name.lower()
    
    for model in MODEL_COMPATIBILITY["primary_models"]:
        if model in model_name_lower:
            return True, "primary"
    
    for model in MODEL_COMPATIBILITY["secondary_models"]:
        if model in model_name_lower:
            return True, "secondary"
    
    return False, "unknown"

# ============================================
# VALIDAZIONE INSTALLAZIONE
# ============================================

def validate_installation():
    """
    Valida che l'installazione sia corretta e completa.
    
    Returns:
        tuple: (is_valid, issues_list)
    """
    issues = []
    
    # Verifica che almeno un nodo sia caricato
    if len(NODE_CLASS_MAPPINGS) == 0:
        issues.append("Nessun nodo caricato correttamente")
    
    # Verifica nodi critici
    critical_nodes = [
        "CharacterForgeGenderController",
        "CharacterForgeWeightedConditioning"
    ]
    
    for critical_node in critical_nodes:
        if critical_node not in NODE_CLASS_MAPPINGS:
            issues.append(f"Nodo critico mancante: {critical_node}")
    
    # Verifica configurazione
    if not CONFIG:
        issues.append("Configurazione non caricata")
    
    # Verifica directory
    if not NODES_DIR.exists():
        issues.append(f"Directory nodes non trovata: {NODES_DIR}")
    
    return len(issues) == 0, issues

def print_installation_report():
    """
    Stampa un report completo dell'installazione.
    """
    print("\n" + "="*60)
    print("  COMFYUI-CHARACTERFORGE INSTALLATION REPORT")
    print("="*60)
    
    print(f"\n📦 Versione: {__version__}")
    print(f"👤 Autore: {__author__}")
    print(f⚖️  Licenza: {__license__}")
    print(f"🔗 Repository: {__repository__}")
    
    print(f"\n⚙️  Configurazione:")
    print(f"   • Modalità Ibrida: {'✅ Attiva' if CONFIG.get('hybrid_mode') else '❌ Disattiva'}")
    print(f"   • Modalità Default: {CONFIG.get('default_mode', 'text_to_sheet')}")
    print(f"   • Preservazione Struttura: {'✅ Attiva' if CONFIG.get('preserve_structure') else '❌ Disattiva'}")
    print(f"   • Debug Mode: {'✅ Attivo' if DEBUG_MODE else '❌ Disattivo'}")
    
    print(f"\n🧩 Nodi Caricati: {len(NODE_CLASS_MAPPINGS)}")
    print(f"   • Caricati con successo: {len(NODE_LOADED_SUCCESSFULLY)}")
    print(f"   • Errori importazione: {len(NODE_FAILED_IMPORTS)}")
    
    if NODE_LOADED_SUCCESSFULLY:
        print(f"\n✅ Nodi Funzionanti:")
        for node_name in NODE_LOADED_SUCCESSFULLY:
            display_name = NODE_DISPLAY_NAME_MAPPINGS.get(
                f"CharacterForge{node_name.replace('_', '').title()}Controller", 
                node_name
            )
            print(f"   • {node_name}")
    
    if NODE_FAILED_IMPORTS:
        print(f"\n❌ Nodi con Errori:")
        for node_name, error in NODE_FAILED_IMPORTS.items():
            print(f"   • {node_name}: {error}")
    
    print(f"\n🎯 Funzionalità Supportate:")
    for feature in get_supported_features():
        print(f"   • {feature}")
    
    print(f"\n🤖 Modelli Compatibili:")
    print(f"   • Primari: {', '.join(MODEL_COMPATIBILITY['primary_models'])}")
    print(f"   • Secondari: {', '.join(MODEL_COMPATIBILITY['secondary_models'])}")
    
    # Validazione
    is_valid, issues = validate_installation()
    
    print(f"\n{'='*60}")
    if is_valid:
        print("✅ INSTALLAZIONE VALIDA E COMPLETA!")
    else:
        print("⚠️  PROBLEMI RILEVATI:")
        for issue in issues:
            print(f"   • {issue}")
    print("="*60 + "\n")

# ============================================
# ESPOSTAZIONI PUBBLICHE
# ============================================

# Esportazioni principali per ComfyUI
__all__ = [
    # Mappings principali (richiesti da ComfyUI)
    'NODE_CLASS_MAPPINGS',
    'NODE_DISPLAY_NAME_MAPPINGS',
    
    # Informazioni versione
    '__version__',
    '__author__',
    '__license__',
    '__repository__',
    
    # Configurazioni
    'CONFIG',
    'MODEL_COMPATIBILITY',
    'DEBUG_MODE',
    
    # Utilities
    'get_node_info',
    'list_all_nodes',
    'get_supported_features',
    'check_model_compatibility',
    'validate_installation',
    'print_installation_report'
]

# ============================================
# INIZIALIZZAZIONE E REPORT
# ============================================

# Stampa report all'avvio (solo se non in modalità silenziosa)
if os.environ.get('CHARACTERFORGE_SILENT', '0') != '1':
    try:
        print(f"[CharacterForge] Inizializzazione v{__version__}...")
        print(f"[CharacterForge] Nodi registrati: {len(NODE_CLASS_MAPPINGS)}")
        print(f"[CharacterForge] Nodi caricati: {', '.join(NODE_LOADED_SUCCESSFULLY)}")
        
        if NODE_FAILED_IMPORTS:
            print(f"[CharacterForge] Warning: {len(NODE_FAILED_IMPORTS)} nodi con errori")
        
        # Report completo solo in debug mode o se esplicitamente richiesto
        if DEBUG_MODE or os.environ.get('CHARACTERFORGE_VERBOSE', '0') == '1':
            print_installation_report()
        
    except Exception as e:
        print(f"[CharacterForge] Errore durante inizializzazione: {e}")
        if DEBUG_MODE:
            traceback.print_exc()

# ============================================
# COMPATIBILITÀ VERSIONI
# ============================================

# Verifica compatibilità con versione ComfyUI
def check_comfyui_compatibility():
    """
    Verifica compatibilità con la versione di ComfyUI in esecuzione.
    """
    try:
        import comfy
        comfyui_version = getattr(comfy, 'VERSION', 'unknown')
        print(f"[CharacterForge] ComfyUI Version: {comfyui_version}")
        return True
    except ImportError:
        print("[CharacterForge] Warning: ComfyUI core non rilevato (modalità standalone)")
        return False
    except Exception as e:
        print(f"[CharacterForge] Warning: Errore verifica compatibilità: {e}")
        return False

# Esegui verifica compatibilità
check_comfyui_compatibility()

# ============================================
# CLEANUP (eseguito allo shutdown)
# ============================================

def _cleanup():
    """
    Cleanup eseguito allo shutdown di ComfyUI.
    """
    # Eventuali cleanup necessari
    pass

import atexit
atexit.register(_cleanup)

# ============================================
# METADATA PACCHETTO
# ============================================

# Metadata per pip/installazione
__metadata__ = {
    "name": "comfyui-characterforge",
    "version": __version__,
    "description": "Professional character sheet control nodes for ComfyUI with hybrid Text/Image support",
    "author": __author__,
    "license": __license__,
    "url": __repository__,
    "keywords": ["comfyui", "character-sheet", "ai-art", "text-to-image", "image-to-image"],
    "classifiers": [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Topic :: Artistic Software",
        "Topic :: Multimedia :: Graphics",
    ]
}

# ============================================
# FINE FILE
# ============================================
# ComfyUI-CharacterForge v2.0.0
# Repository: https://github.com/tuousername/ComfyUI-CharacterForge
# 
# Questo file è l'entry point principale del pacchetto.
# Gestisce:
# - Importazione dinamica di tutti i nodi
# - Configurazione globale del pacchetto
# - Validazione dell'installazione
# - Report diagnostici
# - Compatibilità con ComfyUI
# 
# Per aggiungere nuovi nodi:
# 1. Crea il file in nodes/nome_nuovo_nodo.py
# 2. Aggiungi "nome_nuovo_nodo" a AVAILABLE_NODES
# 3. Implementa la classe CharacterForgeNomeNuovoNodo
# 4. Riavvia ComfyUI