"""
Historical Style
================

Vagabond, Vinland Saga, Rurouni Kenshin - accuratezza storica,
design d'epoca, atmosfera autentica.
"""

HISTORICAL = {
    "name": "Storico",
    "description": "Storico: Vagabond, Vinland Saga, accuratezza d'epoca",
    "category": "anime",
    "genre": "historical",
    "era": "various",
    "prompt": "historical anime style, Vagabond aesthetic, Vinland Saga style, historical accuracy in design, period-appropriate costumes, historical anime genre, authentic atmosphere, samurai era design, medieval European aesthetic, historical weapon detail, period character designs, authentic historical settings",
    "denoise": 0.22,
    "structure_weight": 0.92,
    "color_boost": 1.1,
    "keywords": [
        "historical",
        "Vagabond",
        "Vinland Saga",
        "period accuracy",
        "authentic",
        "samurai era",
        "medieval"
    ],
    "negative_keywords": [
        "anachronistic elements",
        "modern clothing",
        "contemporary setting",
        "fantasy elements"
    ],
    "recommended_loras": [
        "historical_anime_lora.safetensors"
    ],
    "compatible_combinations": [
        "inoue_style",
        "takahashi_rumiko_inuyasha",
        "seinen_90s_style"
    ],
    "inspiration": [
        "Vagabond (1998)",
        "Vinland Saga (2005)",
        "Rurouni Kenshin (1994)"
    ]
}