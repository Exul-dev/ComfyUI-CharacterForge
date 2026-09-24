"""
Anime Cinematic Style
======================

Stile anime cinematografico con qualità film.
Illuminazione complessa, composizione artistica.
Ispirato a: Your Name, Weathering With You, Suzume.
"""

ANIME_CINEMATIC = {
    "name": "Anime Cinematic",
    "description": "Stile anime cinematografico con qualità film e illuminazione complessa",
    "category": "anime",
    "era": "modern",
    "prompt": "cinematic anime style, film quality Japanese animation, Your Name aesthetic, Weathering With You style, Shinkai Makoto visual style, detailed atmospheric lighting, lens flares, god rays, cinematic composition, movie quality backgrounds, sophisticated color grading, detailed environmental art, emotional atmosphere, cinematic anime film aesthetic, Suzume quality animation",
    "denoise": 0.20,
    "structure_weight": 0.95,
    "color_boost": 1.2,
    "keywords": [
        "cinematic",
        "anime film",
        "Your Name",
        "Weathering With You",
        "Shinkai Makoto",
        "atmospheric",
        "lens flares",
        "god rays",
        "movie quality"
    ],
    "negative_keywords": [
        "TV anime quality",
        "simple backgrounds",
        "flat lighting",
        "low budget",
        "basic composition"
    ],
    "recommended_loras": [
        "anime_cinematic_lora.safetensors"
    ],
    "compatible_combinations": [
        "anime_modern",
        "ghibli",
        "slice_of_life"
    ],
    "inspiration": [
        "Your Name (2016)",
        "Weathering With You (2019)",
        "Suzume (2022)",
        "A Silent Voice (2016)"
    ]
}