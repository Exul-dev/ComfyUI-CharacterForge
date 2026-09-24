"""
Makoto Shinkai Style
=====================

Il maestro della luce - Your Name, Weathering With You, Suzume.
Cieli iper-dettagliati, lens flares, illuminazione cinematografica.
"""

MAKOTO_SHINKAI_STYLE = {
    "name": "Makoto Shinkai",
    "description": "Stile Shinkai: Your Name, illuminazione cinematografica iper-dettagliata",
    "category": "anime",
    "artist": "Makoto Shinkai",
    "era": "2010s-2020s",
    "prompt": "Makoto Shinkai art style, Your Name aesthetic, hyper-detailed skies, cinematic lens flares, god rays through clouds, Shinkai signature lighting, Weathering With You style, Suzume aesthetic, photorealistic backgrounds with anime characters, Shinkai's detailed environmental art, dramatic cloud formations, golden hour lighting, detailed urban Japan, emotional atmosphere visualized, Shinkai's color grading, weather effects",
    "denoise": 0.20,
    "structure_weight": 0.93,
    "color_boost": 1.25,
    "keywords": [
        "Shinkai",
        "Your Name",
        "Weathering With You",
        "Suzume",
        "hyper-detailed skies",
        "lens flares",
        "god rays",
        "cinematic lighting",
        "golden hour"
    ],
    "negative_keywords": [
        "simple backgrounds",
        "flat lighting",
        "minimal detail",
        "retro aesthetic"
    ],
    "recommended_loras": [
        "shinkai_lora.safetensors"
    ],
    "compatible_combinations": [
        "anime_cinematic",
        "anime_modern",
        "slice_of_life"
    ],
    "inspiration": [
        "Your Name (2016)",
        "Weathering With You (2019)",
        "Suzume (2022)",
        "5 Centimeters per Second (2007)"
    ]
}