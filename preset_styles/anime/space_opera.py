"""
Space Opera Style
==================

Legend of Galactic Heroes, Macross - spazio epico,
battaglie galattiche, estetica futuristica classica.
"""

SPACE_OPERA = {
    "name": "Space Opera",
    "description": "Space Opera: LoGH, Macross, battaglie galattiche epiche",
    "category": "anime",
    "genre": "space_opera",
    "era": "1980s-2020s",
    "prompt": "space opera anime style, Legend of Galactic Heroes aesthetic, Macross style, epic galactic battles, space fleet warfare, space opera aesthetic, detailed spaceship design, galactic empire aesthetic, space opera character design, epic scale space battles, futuristic but classic aesthetic",
    "denoise": 0.24,
    "structure_weight": 0.90,
    "color_boost": 1.2,
    "keywords": [
        "space opera",
        "Galactic Heroes",
        "Macross",
        "galactic battles",
        "space fleet",
        "epic scale",
        "futuristic classic"
    ],
    "negative_keywords": [
        "grounded military",
        "minimal space",
        "contemporary only",
        "small scale"
    ],
    "recommended_loras": [
        "space_opera_lora.safetensors"
    ],
    "compatible_combinations": [
        "leiji_matsumoto_style",
        "yoshiyuki_tomino_style",
        "sunrise_style"
    ],
    "inspiration": [
        "Legend of Galactic Heroes (1988)",
        "Macross (1982)",
        "Crest of the Stars (1999)"
    ]
}