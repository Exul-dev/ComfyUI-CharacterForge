
"""
CharacterForge Preset Styles Package
====================================

Gestione preset di stile organizzati per categoria.
Ogni sottocartella contiene stili specifici.

Categorie:
- retro_80s: Stili anni '80 (anime, fotografia, VHS, synthwave)
- anime: Stili anime/manga (moderno, Ghibli)
- western: Stili occidentali (cartoon, comic)
- artistic: Stili artistici (watercolor, pixel art)
- cinematic: Stili cinematografici realistici

Versione: 2.2.0
"""

from .retro_80s import RETRO_80S_STYLES
from .anime import ANIME_STYLES
from .western import WESTERN_STYLES
from .artistic import ARTISTIC_STYLES
from .cinematic import CINEMATIC_STYLES


# ============================================
# DATABASE COMBINATO
# ============================================

STYLE_PRESETS = {}
STYLE_PRESETS.update(RETRO_80S_STYLES)
STYLE_PRESETS.update(ANIME_STYLES)
STYLE_PRESETS.update(WESTERN_STYLES)
STYLE_PRESETS.update(ARTISTIC_STYLES)
STYLE_PRESETS.update(CINEMATIC_STYLES)


# ============================================
# FUNZIONI UTILITY
# ============================================

def get_style_by_name(style_name):
    """
    Ottiene un preset stile per nome.

    Args:
        style_name (str): Nome dello stile

    Returns:
        dict: Configurazione stile o None se non trovato
    """
    return STYLE_PRESETS.get(style_name, None)


def list_available_styles():
    """
    Lista tutti gli stili disponibili.

    Returns:
        list: Lista nomi stili
    """
    return list(STYLE_PRESETS.keys())


def get_styles_by_category(category):
    """
    Ottiene stili per categoria.

    Args:
        category (str): Categoria dello stile

    Returns:
        dict: Stili della categoria
    """
    categories = {
        "retro_80s": RETRO_80S_STYLES,
        "anime": ANIME_STYLES,
        "western": WESTERN_STYLES,
        "artistic": ARTISTIC_STYLES,
        "cinematic": CINEMATIC_STYLES,
    }

    return categories.get(category, {})


def get_compatible_styles(style_name):
    """
    Ottiene stili compatibili per combinazioni.

    Returns:
        list: Stili compatibili
    """
    style = STYLE_PRESETS.get(style_name, {})
    return style.get("compatible_combinations", [])


def search_styles_by_keyword(keyword):
    """
    Cerca stili per keyword.

    Args:
        keyword (str): Keyword da cercare

    Returns:
        list: Stili che contengono la keyword
    """
    matching_styles = []

    for style_name, style_config in STYLE_PRESETS.items():

        # Cerca nel nome
        if keyword.lower() in style_name.lower():
            matching_styles.append(style_name)
            continue

        # Cerca nella descrizione
        if keyword.lower() in style_config.get("description", "").lower():
            matching_styles.append(style_name)
            continue

        # Cerca nelle keywords
        keywords = style_config.get("keywords", [])

        for kw in keywords:
            if keyword.lower() in kw.lower():
                matching_styles.append(style_name)
                break

    return list(set(matching_styles))


def get_style_prompt(style_name):
    """
    Ottiene solo il prompt di uno stile.

    Args:
        style_name (str): Nome stile

    Returns:
        str: Prompt stile o stringa vuota
    """
    style = STYLE_PRESETS.get(style_name, {})
    return style.get("prompt", "")


def get_style_denoise(style_name):
    """
    Ottiene il denoise consigliato di uno stile.

    Args:
        style_name (str): Nome stile

    Returns:
        float: Denoise consigliato o 0.25 default
    """
    style = STYLE_PRESETS.get(style_name, {})
    return style.get("denoise", 0.25)


def get_recommended_loras(style_name):
    """
    Ottiene LoRA consigliati per uno stile.

    Args:
        style_name (str): Nome stile

    Returns:
        list: LoRA consigliati
    """
    style = STYLE_PRESETS.get(style_name, {})
    return style.get("recommended_loras", [])


# ============================================
# ESPOSTAZIONI PUBBLICHE
# ============================================

__all__ = [
    "STYLE_PRESETS",
    "RETRO_80S_STYLES",
    "ANIME_STYLES",
    "WESTERN_STYLES",
    "ARTISTIC_STYLES",
    "CINEMATIC_STYLES",
    "get_style_by_name",
    "list_available_styles",
    "get_styles_by_category",
    "get_compatible_styles",
    "search_styles_by_keyword",
    "get_style_prompt",
    "get_style_denoise",
    "get_recommended_loras",
]


# ============================================
# INIZIALIZZAZIONE
# ============================================

print(
    f"[CharacterForge-Styles] Preset caricati: {len(STYLE_PRESETS)}"
)

print(
    "[CharacterForge-Styles] "
    "Categorie: retro_80s, anime, western, artistic, cinematic"
)


# Log dettagliato per categoria
for category_name, category_styles in [
    ("retro_80s", RETRO_80S_STYLES),
    ("anime", ANIME_STYLES),
    ("western", WESTERN_STYLES),
    ("artistic", ARTISTIC_STYLES),
    ("cinematic", CINEMATIC_STYLES),
]:
    if category_styles:
        print(
            f"[CharacterForge-Styles]   "
            f"{category_name}: {len(category_styles)} stili"
        )
