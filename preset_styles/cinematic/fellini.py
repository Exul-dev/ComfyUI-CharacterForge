"""
CharacterForge Cinematic - Federico Fellini
============================================

Preset cinematografici basati sull'evoluzione della fotografia,
della messa in scena e dell'immaginario visivo del cinema di Federico Fellini.

Focus:
- composizioni teatrali
- surrealismo cinematografico
- grandangoli espressivi
- luce morbida e diffusa
- atmosfera da sogno
- scenografie elaborate
- personaggi eccentrici
- movimento di gruppo
- fotografia italiana del dopoguerra
"""

FELLINI_STYLES = {
    "fellini_1950s": {
        "name": "Fellini - Neorealist 1950s",
        "category": "cinematic",
        "era": "1950s",
        "prompt": (
            "1950s Italian cinematic photography, postwar Italian atmosphere, "
            "neorealist visual texture, black and white 35mm film, natural daylight, "
            "authentic streets and interiors, expressive faces, imperfect environments, "
            "documentary-inspired composition, deep spatial staging, "
            "soft atmospheric contrast, organic film grain, realistic skin texture, "
            "humanistic observation, tactile architecture, "
            "authentic Italian photographic realism"
        ),
        "negative_prompt": (
            "glossy commercial photography, modern digital cinema, oversaturated colors, "
            "plastic skin, artificial HDR, fantasy glow, excessive bloom, "
            "beauty retouching, cartoon, anime, painterly rendering, "
            "synthetic CGI appearance"
        ),
        "denoise": 0.70,
        "structure_weight": 0.84,
        "color_boost": 0.46,
        "keywords": [
            "1950s",
            "Italian",
            "neorealist",
            "black-and-white",
            "35mm",
            "street",
            "humanist",
            "film-grain",
        ],
    },

    "fellini_1960s": {
        "name": "Fellini - Dreamlike 1960s",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "1960s Italian dreamlike cinema, expressive widescreen composition, "
            "black and white photographic texture, theatrical staging, "
            "surreal atmosphere grounded in physical reality, soft diffused light, "
            "dramatic shadows, elaborate characters, eccentric faces, "
            "deep spatial composition, expressive camera perspective, "
            "organic 35mm grain, rich tonal range, theatrical environments, "
            "dreamlike but tactile photographic realism"
        ),
        "negative_prompt": (
            "modern digital sharpness, glossy advertising, saturated neon colors, "
            "plastic skin, artificial HDR, excessive CGI, excessive bloom, "
            "generic fantasy art, cartoon, anime, painterly rendering, "
            "synthetic 3D appearance"
        ),
        "denoise": 0.69,
        "structure_weight": 0.88,
        "color_boost": 0.52,
        "keywords": [
            "1960s",
            "dreamlike",
            "surreal",
            "theatrical",
            "widescreen",
            "black-and-white",
            "eccentric",
            "35mm",
        ],
    },

    "fellini_1970s": {
        "name": "Fellini - Baroque Color 1970s",
        "category": "cinematic",
        "era": "1970s",
        "prompt": (
            "1970s Italian baroque cinematic photography, expressive color film, "
            "warm muted reds, ochres, creams and dusty browns, theatrical lighting, "
            "large elaborate sets, surreal architecture, eccentric costumes, "
            "wide-angle compositions, deep layered staging, soft diffused illumination, "
            "rich atmospheric haze, visible film grain, tactile production design, "
            "dramatic character groups, playful visual excess, "
            "authentic analog photographic texture"
        ),
        "negative_prompt": (
            "modern digital color grading, neon cyberpunk colors, excessive saturation, "
            "glossy commercial photography, artificial HDR, plastic materials, "
            "excessive sharpening, clean minimalist interiors, cartoon, anime, "
            "painterly rendering, synthetic CGI appearance"
        ),
        "denoise": 0.68,
        "structure_weight": 0.90,
        "color_boost": 0.78,
        "keywords": [
            "1970s",
            "baroque",
            "Italian",
            "warm",
            "ochre",
            "wide-angle",
            "theatrical",
            "analog",
        ],
    },

    "fellini_surreal": {
        "name": "Fellini - Cinematic Surrealism",
        "category": "cinematic",
        "era": "surreal",
        "prompt": (
            "Italian cinematic surrealism, dream logic rendered as physical reality, "
            "theatrical environments, oversized props and architecture, "
            "eccentric human figures, expressive wide-angle perspective, "
            "soft studio illumination mixed with practical sources, "
            "warm muted color palette, atmospheric haze, elaborate staging, "
            "layered foreground middle-ground and background, "
            "organic analog film grain, tactile surfaces, "
            "strange but believable photographic realism"
        ),
        "negative_prompt": (
            "generic fantasy illustration, video game graphics, digital concept art, "
            "neon colors, excessive CGI, plastic characters, glossy surfaces, "
            "hyperreal HDR, sterile composition, cartoon, anime, "
            "flat 2D illustration, synthetic 3D rendering"
        ),
        "denoise": 0.65,
        "structure_weight": 0.92,
        "color_boost": 0.74,
        "keywords": [
            "surrealism",
            "dream",
            "theatrical",
            "wide-angle",
            "baroque",
            "eccentric",
            "staging",
            "analog-film",
        ],
    },

    "fellini_ensemble": {
        "name": "Fellini - Grand Ensemble",
        "category": "cinematic",
        "era": "ensemble",
        "prompt": (
            "large ensemble Italian cinematic composition, dozens of expressive "
            "characters arranged across multiple depth planes, theatrical blocking, "
            "dynamic group movement, elaborate period costumes, "
            "wide-angle lens perspective, warm diffused studio light, "
            "soft atmospheric haze, layered production design, "
            "rich but restrained analog color, visible film grain, "
            "tactile surfaces, expressive faces, controlled visual chaos, "
            "complex cinematic staging with photographic realism"
        ),
        "negative_prompt": (
            "random crowd composition, flat staging, modern fashion photography, "
            "neon colors, excessive saturation, plastic faces, artificial HDR, "
            "digital sterile appearance, cartoon, anime, painterly rendering, "
            "synthetic CGI crowd, duplicated faces"
        ),
        "denoise": 0.67,
        "structure_weight": 0.94,
        "color_boost": 0.70,
        "keywords": [
            "ensemble",
            "crowd",
            "group",
            "wide-angle",
            "theatrical",
            "Italian",
            "staging",
            "depth",
        ],
    },
}


__all__ = ["FELLINI_STYLES"]
