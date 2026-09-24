"""
CharacterForge Preset Styles - Categoria retro_80s
Versione: 1.0.1
- FIX: esporta RETRO_80S_STYLES (nome mancante nel file precedente,
  che bloccava il caricamento dell'intero pacchetto preset_styles).
"""

RETRO_80S_STYLES = {
    "retro_80s_anime": {
        "name": "1980s Retro Anime",
        "description": "1980s Retro Anime, VHS grain, cel animation",
        "era": "1980s", "genre": "anime",
        "prompt": "1980s retro anime style, vintage cel animation aesthetic, hand-drawn animation quality, VHS grain texture, analog film photography look, retro color grading with warm oranges and cool blues, 80s anime character design with sharp angular features, dramatic 80s lighting with strong contrast, retro anime film grain, 16mm film aesthetic, vintage Japanese animation from the 1980s, reminiscent of Akira and Fist of the North Star era",
        "recommended_lora": ["retro_80s_anime_lora.safetensors"],
        "lora_strength": 0.8, "denoise_base": 0.28,
        "structure_weight": 0.88, "color_boost": 1.15,
        "tags": ["retro", "80s", "anime", "cel animation", "VHS grain"],
    },
    "retro_80s_photography": {
        "name": "1980s Film Photography",
        "description": "1980s Film Photography, analog warmth",
        "era": "1980s", "genre": "photography",
        "prompt": "1980s film photography aesthetic, analog 35mm film grain, vintage Kodachrome colors, warm golden hour lighting, retro color grading with muted highlights and deep shadows, 80s photographic style, VHS home video quality, soft focus background, nostalgic vintage look, old school photography with natural imperfections, film burn effects",
        "recommended_lora": ["retro_80s_film_lora.safetensors"],
        "lora_strength": 0.6, "denoise_base": 0.22,
        "structure_weight": 0.92, "color_boost": 1.1,
        "tags": ["retro", "80s", "film photography", "analog", "Kodachrome"],
    },
    "vhs_retro": {
        "name": "VHS Retro",
        "description": "VHS Retro, analog video aesthetic",
        "era": "1980s", "genre": "video",
        "prompt": "VHS retro aesthetic, analog video tape quality, scan lines, tracking errors, chromatic aberration, 1980s home video look, degraded video quality with authentic imperfections, VHS tape noise, analog distortion, retro CRT television display, vintage video artifacts",
        "recommended_lora": ["vhs_retro_lora.safetensors"],
        "lora_strength": 0.75, "denoise_base": 0.25,
        "structure_weight": 0.90, "color_boost": 1.2,
        "tags": ["VHS", "retro", "analog video", "scan lines", "CRT"],
    },
    "synthwave_80s": {
        "name": "Synthwave 80s",
        "description": "Synthwave 80s, neon retro-futurism",
        "era": "1980s", "genre": "retro-futurism",
        "prompt": "synthwave 80s aesthetic, neon pink and cyan color palette, retro-futuristic design, 1980s sci-fi anime style, chrome and neon elements, sunset gradient backgrounds, grid floors, retro futuristic character design, cyberpunk 80s aesthetic, Miami Vice color grading",
        "recommended_lora": ["synthwave_lora.safetensors"],
        "lora_strength": 0.7, "denoise_base": 0.30,
        "structure_weight": 0.85, "color_boost": 1.6,
        "tags": ["synthwave", "80s", "neon", "retro-futurism", "cyberpunk"],
    },
}