"""
CharacterForge Cinematic - Michelangelo Antonioni
==================================================

Preset cinematografici ispirati alle principali caratteristiche
visive del cinema di Michelangelo Antonioni:
alienazione, composizione architettonica, spazio negativo,
silenzio visivo, colori modernisti e paesaggi psicologici.
"""

ANTONIONI_STYLES = {

    "antonioni_1960s": {
        "name": "Antonioni - 1960s Modernist",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "European modernist cinema, psychologically distant composition, "
            "wide architectural framing, characters isolated inside large environments, "
            "precise geometric lines, deep spatial layering, controlled camera placement, "
            "subtle naturalistic lighting, restrained facial expression, "
            "quiet urban atmosphere, elegant Italian modernism, "
            "muted desaturated colors, soft film grain, fine 35mm texture, "
            "deliberate negative space, contemplative cinematic still"
        ),
        "negative_prompt": (
            "extreme saturation, glossy commercial lighting, excessive contrast, "
            "action movie composition, dramatic poses, exaggerated expressions, "
            "shallow depth of field, fisheye distortion, neon cyberpunk, "
            "plastic skin, digital sharpness, excessive bokeh"
        ),
        "denoise": 0.72,
        "structure_weight": 0.88,
        "color_boost": 0.82,
        "keywords": [
            "modernist",
            "architectural",
            "alienation",
            "negative_space",
            "35mm",
            "italian_cinema"
        ],
    },

    "antonioni_red_desert": {
        "name": "Antonioni - Red Desert",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "industrial landscape transformed into psychological space, "
            "minimalist human figure surrounded by factories and polluted terrain, "
            "misty industrial atmosphere, strange muted reds and ochres, "
            "desaturated green and gray surfaces, carefully controlled color accents, "
            "long horizontal compositions, architectural geometry, "
            "soft overcast light, atmospheric haze, restrained 1960s Italian modernism, "
            "subtle analog film grain, poetic visual isolation"
        ),
        "negative_prompt": (
            "clean futuristic city, vibrant tropical colors, fantasy architecture, "
            "high contrast HDR, action composition, glossy surfaces, "
            "oversharpening, excessive cinematic flares, cartoon appearance"
        ),
        "denoise": 0.74,
        "structure_weight": 0.91,
        "color_boost": 0.95,
        "keywords": [
            "industrial",
            "red_desert",
            "pollution",
            "modernism",
            "atmosphere",
            "color_psychology"
        ],
    },

    "antonioni_blowup": {
        "name": "Antonioni - Blow-Up",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "1960s London photography culture, detached observational cinematography, "
            "fashionable urban environment, elegant modern architecture, "
            "medium and wide compositions, photographic framing, "
            "natural daylight mixed with soft artificial illumination, "
            "cool muted palette with selective saturated accents, "
            "subtle mystery without overt drama, realistic street atmosphere, "
            "fine-grain 35mm photography, sophisticated European art cinema"
        ),
        "negative_prompt": (
            "modern smartphones, contemporary vehicles, modern skyscrapers, "
            "neon lighting, cyberpunk, exaggerated mystery effects, "
            "hard Hollywood lighting, excessive saturation, digital photography look"
        ),
        "denoise": 0.70,
        "structure_weight": 0.86,
        "color_boost": 0.88,
        "keywords": [
            "1960s_london",
            "photography",
            "fashion",
            "urban",
            "mystery",
            "35mm"
        ],
    },

    "antonioni_late_modernism": {
        "name": "Antonioni - Late Modernism",
        "category": "cinematic",
        "era": "1970s",
        "prompt": (
            "international modernist cinema, monumental architecture, "
            "isolated protagonist inside vast contemporary environments, "
            "long-lens observational framing, distant camera perspective, "
            "minimal human interaction, dry natural light, "
            "bleached earth tones, pale concrete, dusty atmosphere, "
            "subtle analog grain, understated contrast, "
            "philosophical visual emptiness, precise geometric composition"
        ),
        "negative_prompt": (
            "crowded composition, exaggerated emotion, romantic glamour, "
            "high saturation, fantasy lighting, heroic framing, "
            "extreme shallow depth of field, glossy digital cinema, "
            "action movie aesthetics"
        ),
        "denoise": 0.73,
        "structure_weight": 0.93,
        "color_boost": 0.76,
        "keywords": [
            "late_modernism",
            "architecture",
            "isolation",
            "minimalism",
            "long_lens",
            "philosophical"
        ],
    },

    "antonioni_landscape": {
        "name": "Antonioni - Psychological Landscape",
        "category": "cinematic",
        "era": "timeless",
        "prompt": (
            "psychological landscape cinema, human figure visually subordinate to environment, "
            "vast empty spaces, unusual architectural framing, "
            "carefully balanced negative space, distant perspective, "
            "natural atmospheric light, subdued earth tones, "
            "soft gray skies, muted greens and ochres, "
            "quiet tension, contemplative stillness, "
            "fine 35mm grain, restrained cinematic contrast, "
            "European art-house composition, landscape expressing inner emotion"
        ),
        "negative_prompt": (
            "epic fantasy landscape, heroic character framing, vibrant colors, "
            "dramatic sunset, excessive lens flare, oversaturated skies, "
            "busy scenery, glossy commercial photography, artificial HDR, "
            "hyper-detailed digital sharpness"
        ),
        "denoise": 0.76,
        "structure_weight": 0.95,
        "color_boost": 0.80,
        "keywords": [
            "psychological_landscape",
            "negative_space",
            "isolation",
            "architecture",
            "art_house",
            "contemplative"
        ],
    },
}


__all__ = ["ANTONIONI_STYLES"]
