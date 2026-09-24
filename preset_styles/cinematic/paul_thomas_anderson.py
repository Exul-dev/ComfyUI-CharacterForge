"""
CharacterForge Cinematic - Paul Thomas Anderson
===============================================

Visual language inspired by Paul Thomas Anderson's cinema:
expressive long takes, precise dolly movement, deep spatial staging,
35mm and large-format photography, naturalistic and practical light,
strong environmental compositions, tactile production design and
organic analog film texture.
"""

PAUL_THOMAS_ANDERSON_STYLES = {

    "pta_1990s": {
        "name": "PTA 1990s",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "1990s American independent cinema cinematography, 35mm spherical lenses, "
            "24mm, 35mm and 50mm perspectives, deep spatial staging, long tracking shots, "
            "precise dolly movement, complex blocking, characters moving through layered environments, "
            "naturalistic practical lighting, warm tungsten interiors, soft daylight through windows, "
            "controlled contrast, muted earth tones, tobacco brown, beige, faded green and blue, "
            "natural skin tones, fine 35mm film grain, subtle halation, organic optical softness, "
            "moderate depth of field, carefully composed negative space, detailed suburban and industrial "
            "production design, emotionally tense atmosphere, observational camera language"
        ),
        "negative_prompt": (
            "glossy blockbuster photography, excessive shallow depth of field, "
            "digital clinical sharpness, neon lighting, extreme saturation, "
            "music-video camera movement, generic commercial composition"
        ),
        "denoise": 0.47,
        "structure_weight": 0.86,
        "color_boost": 0.86,
        "keywords": [
            "1990s",
            "35mm",
            "dolly",
            "long take",
            "deep staging",
            "naturalistic",
            "film grain",
            "American cinema"
        ],
    },

    "pta_magnolia": {
        "name": "PTA Ensemble Drama",
        "category": "cinematic",
        "era": "1990s-2000s",
        "prompt": (
            "large ensemble drama cinematography, 35mm film, 28mm and 35mm wide lenses, "
            "long uninterrupted tracking shots through interconnected spaces, "
            "multiple characters arranged at different depths, deep focus, "
            "fluid lateral camera movement, precise blocking, expressive foreground-background relationships, "
            "practical fluorescent and tungsten lighting, overcast daylight, "
            "warm beige interiors contrasted with cool exterior ambience, "
            "restrained saturation, realistic skin tones, visible fine 35mm grain, "
            "soft highlight rolloff, subtle halation, dense production design, "
            "ordinary American architecture, emotionally charged but visually controlled atmosphere"
        ),
        "negative_prompt": (
            "static single-subject portrait, extreme bokeh, glossy studio lighting, "
            "digital sharpness, oversaturated colors, chaotic handheld camera, "
            "empty backgrounds, artificial CGI environments"
        ),
        "denoise": 0.49,
        "structure_weight": 0.90,
        "color_boost": 0.84,
        "keywords": [
            "ensemble",
            "long take",
            "35mm",
            "deep focus",
            "tracking shot",
            "blocking",
            "practical light",
            "American suburbia"
        ],
    },

    "pta_there_will_be_blood": {
        "name": "PTA Oil Landscape",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "large-format inspired American historical cinematography, 65mm photographic scale, "
            "wide 32mm and 40mm environmental perspectives, immense western landscapes, "
            "figures isolated against terrain, strong horizontal compositions, "
            "deep atmospheric perspective, harsh natural sunlight, dusty air, "
            "smoke and fire illuminated by practical sources, dramatic backlight, "
            "dark interiors with warm oil-lamp and tungsten illumination, "
            "earth brown, black, ochre, faded blue and dusty gray palette, "
            "rich shadow detail, subtle film grain, gentle halation, "
            "precise dolly movement, slow controlled camera, monumental environmental framing, "
            "weathered wood, oil machinery, dirt and tactile production design"
        ),
        "negative_prompt": (
            "fantasy western, excessive orange grading, HDR landscape, "
            "plastic CGI environments, modern clothing, neon colors, "
            "extreme digital sharpness, generic blockbuster spectacle"
        ),
        "denoise": 0.50,
        "structure_weight": 0.91,
        "color_boost": 0.83,
        "keywords": [
            "65mm",
            "oil landscape",
            "western",
            "dust",
            "firelight",
            "large format",
            "deep space",
            "historical drama"
        ],
    },

    "pta_phantom_thread": {
        "name": "PTA Elegant 35mm",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "elegant 35mm period-drama cinematography, 50mm and 75mm lenses, "
            "precise symmetrical and centered compositions, controlled shallow depth of field, "
            "soft window daylight, practical tungsten lamps, diffused studio illumination, "
            "warm cream, ivory, muted green, burgundy and brown palette, "
            "rich textile and wood textures, subtle film grain, delicate halation, "
            "smooth dolly movement, slow deliberate reframing, restrained camera language, "
            "carefully designed interiors, geometric furniture placement, "
            "faces isolated against sophisticated production design, tactile costume detail, "
            "quiet psychological tension, luxurious but photographic realism"
        ),
        "negative_prompt": (
            "modern fashion photography, glossy commercial beauty lighting, "
            "excessive bokeh, plastic skin, digital perfection, neon colors, "
            "overly stylized symmetry, HDR"
        ),
        "denoise": 0.45,
        "structure_weight": 0.88,
        "color_boost": 0.91,
        "keywords": [
            "35mm",
            "50mm",
            "75mm",
            "period drama",
            "textiles",
            "symmetry",
            "tungsten",
            "psychological"
        ],
    },

    "pta_licorice_pizza": {
        "name": "PTA 1970s California",
        "category": "cinematic",
        "era": "1970s recreation / 2020s production",
        "prompt": (
            "1970s Southern California photographic atmosphere, 35mm film cinematography, "
            "40mm and 50mm lenses, relaxed handheld movement mixed with smooth tracking shots, "
            "sunny suburban streets, low-rise architecture, school corridors, diners and shops, "
            "natural daylight, warm late-afternoon sunlight, practical fluorescent interiors, "
            "soft golden highlights, muted orange, cream, faded green, denim blue and brown palette, "
            "natural skin tones, fine analog film grain, gentle halation, slight optical softness, "
            "moderate depth of field, casual off-center framing, lived-in production design, "
            "period cars, signage and textures, youthful energy with nostalgic realism"
        ),
        "negative_prompt": (
            "digital clean-room look, modern architecture, hyper-saturated retro filters, "
            "Instagram aesthetic, excessive bokeh, artificial film scratches, "
            "plastic skin, exaggerated vintage effects"
        ),
        "denoise": 0.46,
        "structure_weight": 0.84,
        "color_boost": 0.93,
        "keywords": [
            "1970s California",
            "35mm",
            "40mm",
            "50mm",
            "natural light",
            "analog grain",
            "nostalgia",
            "suburban"
        ],
    },
}

__all__ = ["PAUL_THOMAS_ANDERSON_STYLES"]
