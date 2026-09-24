"""
Chibi Style
============

Super-deformed - proporzioni esagerate cute,
teste enormi, corpicini piccoli.
"""

CHIBI_STYLE = {
    "name": "Chibi",
    "description": "Chibi super-deformed: teste grandi, corpi piccoli, cute estremo",
    "category": "anime",
    "genre": "chibi",
    "era": "universal",
    "prompt": "chibi anime style, super-deformed proportions, extremely large heads, tiny bodies, maximum cuteness aesthetic, chibi character designs, oversized expressive eyes, stubby limbs, chibi proportions, adorable simplified features, super cute aesthetic, chibi manga style, kawaii maximum, simplified but expressive, chibi transformation aesthetic",
    "denoise": 0.28,
    "structure_weight": 0.82,
    "color_boost": 1.4,
    "keywords": [
        "chibi",
        "super-deformed",
        "large heads",
        "tiny bodies",
        "cute",
        "kawaii",
        "stubby limbs",
        "expressive eyes"
    ],
    "negative_keywords": [
        "realistic proportions",
        "detailed anatomy",
        "serious aesthetic",
        "adult proportions"
    ],
    "recommended_loras": [
        "chibi_style_lora.safetensors"
    ],
    "compatible_combinations": [
        "moe_2000s_style",
        "shojo_modern",
        "musical_idol"
    ],
    "inspiration": [
        "Chibi Maruko-chan",
        "SD Gundam",
        "Lucky Star",
        "Aggretsuko chibi scenes"
    ]
}