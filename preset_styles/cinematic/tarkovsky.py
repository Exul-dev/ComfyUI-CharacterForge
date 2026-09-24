"""
CharacterForge Cinematic - Andrei Tarkovsky
============================================

Preset cinematografici basati sull'evoluzione della fotografia,
della composizione e della messa in scena del cinema di Andrei Tarkovsky.

Focus:
- contemplazione visiva
- piani sequenza atmosferici
- luce naturale
- paesaggi umidi e decadenti
- acqua, nebbia e pioggia
- profondità spaziale
- palette desaturate
- texture analogica
- rapporto poetico tra natura, architettura e personaggio
"""

TARKOVSKY_STYLES = {
    "tarkovsky_1960s": {
        "name": "Tarkovsky - Early 1960s",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "1960s Soviet cinematic photography, restrained black and white tones, "
            "long contemplative compositions, natural daylight, realistic interiors, "
            "deep spatial perspective, austere architecture, expressive faces, "
            "subtle atmospheric haze, organic 35mm film grain, "
            "soft shadows, luminous highlights, realistic textures, "
            "quiet observational atmosphere, poetic photographic realism"
        ),
        "negative_prompt": (
            "glossy commercial photography, oversaturated colors, artificial HDR, "
            "plastic skin, excessive beauty retouching, neon lighting, "
            "fantasy glow, excessive bloom, cartoon, anime, painterly rendering, "
            "synthetic CGI appearance"
        ),
        "denoise": 0.70,
        "structure_weight": 0.86,
        "color_boost": 0.44,
        "keywords": [
            "1960s",
            "Soviet",
            "black-and-white",
            "natural-light",
            "contemplative",
            "35mm",
            "austere",
            "poetic",
        ],
    },

    "tarkovsky_1970s": {
        "name": "Tarkovsky - Poetic Color 1970s",
        "category": "cinematic",
        "era": "1970s",
        "prompt": (
            "1970s Soviet poetic cinema, muted earth-tone color palette, "
            "desaturated greens and browns, natural overcast daylight, "
            "wet vegetation, abandoned architecture, shallow pools of water, "
            "mist and rain, long contemplative framing, deep environmental space, "
            "slow visual rhythm, subtle analog film grain, tactile weathered surfaces, "
            "soft natural shadows, restrained highlights, "
            "dreamlike atmosphere grounded in physical photographic realism"
        ),
        "negative_prompt": (
            "vivid saturated colors, glossy commercial photography, "
            "clean modern architecture, artificial neon, excessive HDR, "
            "fantasy glow, excessive bloom, plastic surfaces, cartoon, anime, "
            "painterly rendering, synthetic CGI appearance"
        ),
        "denoise": 0.68,
        "structure_weight": 0.91,
        "color_boost": 0.58,
        "keywords": [
            "1970s",
            "poetic",
            "earth-tones",
            "rain",
            "water",
            "mist",
            "decay",
            "analog",
        ],
    },

    "tarkovsky_stalker": {
        "name": "Tarkovsky - Decayed Zone",
        "category": "cinematic",
        "era": "zone",
        "prompt": (
            "post-industrial abandoned landscape, overgrown ruins, wet concrete, "
            "rusted metal, stagnant water, dense vegetation, atmospheric mist, "
            "muted green and brown palette, desaturated colors, "
            "soft overcast natural light, deep spatial perspective, "
            "weathered textures, damp surfaces, subtle reflections, "
            "long contemplative cinematic composition, organic film grain, "
            "quiet mysterious atmosphere, physically realistic environment"
        ),
        "negative_prompt": (
            "clean futuristic environment, neon cyberpunk, glossy surfaces, "
            "bright saturated colors, fantasy magic effects, excessive fog, "
            "artificial HDR, excessive sharpening, cartoon, anime, "
            "painterly rendering, synthetic CGI appearance"
        ),
        "denoise": 0.66,
        "structure_weight": 0.95,
        "color_boost": 0.52,
        "keywords": [
            "abandoned",
            "industrial",
            "ruins",
            "rust",
            "water",
            "vegetation",
            "mist",
            "decay",
        ],
    },

    "tarkovsky_solaris": {
        "name": "Tarkovsky - Cosmic Intimacy",
        "category": "cinematic",
        "era": "cosmic",
        "prompt": (
            "philosophical science-fiction cinematography, intimate human spaces "
            "contrasted with immense cosmic environments, restrained neutral palette, "
            "naturalistic interior lighting, deep shadows, soft reflections, "
            "glass and water surfaces, atmospheric depth, realistic materials, "
            "minimal futuristic design, tactile analog film texture, "
            "subtle visual tension, contemplative framing, "
            "quiet psychological atmosphere, grounded photographic realism"
        ),
        "negative_prompt": (
            "colorful space opera, neon cyberpunk, futuristic fantasy, "
            "glossy spaceship interiors, excessive CGI, excessive lens flare, "
            "bright saturated colors, artificial HDR, cartoon, anime, "
            "painterly rendering, plastic materials"
        ),
        "denoise": 0.67,
        "structure_weight": 0.92,
        "color_boost": 0.50,
        "keywords": [
            "science-fiction",
            "cosmic",
            "intimate",
            "water",
            "reflection",
            "minimalist",
            "analog",
            "psychological",
        ],
    },

    "tarkovsky_nature": {
        "name": "Tarkovsky - Elemental Nature",
        "category": "cinematic",
        "era": "nature",
        "prompt": (
            "poetic natural landscape cinematography, untouched woodland, "
            "wet grass, trees moving in wind, rain-soaked earth, shallow streams, "
            "fog drifting through vegetation, muted green and brown tones, "
            "soft overcast daylight, natural atmospheric perspective, "
            "subtle sunlight breaking through clouds, tactile organic surfaces, "
            "long contemplative composition, restrained contrast, "
            "fine analog film grain, profound sense of silence and space, "
            "realistic environmental photography"
        ),
        "negative_prompt": (
            "bright fantasy forest, oversaturated greens, tropical vegetation, "
            "artificial magical light, excessive HDR, excessive sharpening, "
            "glossy nature photography, cartoon, anime, painterly rendering, "
            "synthetic CGI environment"
        ),
        "denoise": 0.65,
        "structure_weight": 0.90,
        "color_boost": 0.48,
        "keywords": [
            "nature",
            "forest",
            "rain",
            "wind",
            "fog",
            "water",
            "earth",
            "contemplative",
        ],
    },
}


__all__ = ["TARKOVSKY_STYLES"]
