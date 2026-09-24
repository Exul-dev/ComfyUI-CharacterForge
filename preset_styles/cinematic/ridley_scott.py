"""
CharacterForge Cinematic - Ridley Scott
=======================================

Visual language inspired by Ridley Scott's cinematic photography:
industrial production design, atmospheric environments, controlled
wide-angle compositions, strong practical lighting, backlight,
haze, monumental architecture, desaturated palettes and highly
designed visual worlds grounded in photographic realism.
"""

RIDLEY_SCOTT_STYLES = {

    "ridley_scott_1970s_1980s": {
        "name": "Ridley Scott Early",
        "category": "cinematic",
        "era": "1970s-1980s",
        "prompt": (
            "late 1970s and 1980s cinematic photography, spherical and anamorphic "
            "wide-angle lenses, strong environmental composition, deep spatial layering, "
            "industrial architecture, monumental practical sets, dense foreground details, "
            "hard motivated light mixed with atmospheric haze, shafts of light through smoke, "
            "cool fluorescent interiors contrasted with warm practical lamps, "
            "deep blacks, metallic gray, dirty amber and muted blue palette, "
            "subtle 35mm film grain, soft halation around practical lights, "
            "controlled highlight rolloff, realistic skin texture, "
            "slow deliberate camera movement, low angles and carefully designed silhouettes, "
            "dense production design, tactile metal, concrete, pipes, machinery and weathered surfaces"
        ),
        "negative_prompt": (
            "clean futuristic minimalism, glossy digital cinema, neon cyberpunk overload, "
            "plastic surfaces, excessive saturation, extreme HDR, sterile lighting, "
            "cartoon rendering, excessive shallow depth of field"
        ),
        "denoise": 0.49,
        "structure_weight": 0.88,
        "color_boost": 0.84,
        "keywords": [
            "industrial",
            "1980s",
            "35mm",
            "wide angle",
            "practical lighting",
            "haze",
            "deep space",
            "film grain"
        ],
    },

    "ridley_scott_industrial_scifi": {
        "name": "Ridley Scott Industrial Sci-Fi",
        "category": "cinematic",
        "era": "1970s-1980s",
        "prompt": (
            "dark industrial science-fiction cinematography, 24mm and 28mm wide-angle lenses, "
            "strong perspective distortion used deliberately, enormous practical interiors, "
            "claustrophobic corridors opening into monumental spaces, layered foreground "
            "and background machinery, wet metal, condensation, pipes, cables and worn surfaces, "
            "low-key lighting, fluorescent practicals, sodium vapor, tungsten pools of light, "
            "dense volumetric smoke, backlit particles, localized highlights, "
            "desaturated olive, gray, brown and dirty amber palette, "
            "deep black shadows, restrained color separation, subtle 35mm grain, "
            "soft optical halation, realistic atmospheric depth, "
            "slow tracking shots and creeping camera movement, oppressive physical scale"
        ),
        "negative_prompt": (
            "clean spaceship interiors, glossy white sci-fi, neon cyberpunk, "
            "minimalist futuristic design, excessive blue lighting, perfect surfaces, "
            "CGI plasticity, extreme bloom, oversharpening, weightless environments"
        ),
        "denoise": 0.51,
        "structure_weight": 0.90,
        "color_boost": 0.78,
        "keywords": [
            "industrial science fiction",
            "24mm",
            "28mm",
            "claustrophobic",
            "practical set",
            "smoke",
            "metal",
            "low key"
        ],
    },

    "ridley_scott_historical_epic": {
        "name": "Ridley Scott Historical Epic",
        "category": "cinematic",
        "era": "2000s-2010s",
        "prompt": (
            "large-scale historical epic cinematography, anamorphic wide lenses combined "
            "with long telephoto compression, monumental landscapes, enormous practical sets, "
            "dense crowds arranged in layered compositions, golden-hour backlight, "
            "dust and atmospheric haze, strong sunlight filtered through smoke, "
            "deep warm highlights with cooler shadow regions, bronze, sand, stone, "
            "weathered red and muted blue palette, natural skin tones, "
            "controlled contrast, subtle filmic grain, soft highlight halation, "
            "large crane movements and sweeping tracking shots balanced with intimate close-ups, "
            "heroic low angles, carefully designed silhouettes, tactile costumes, "
            "architecture and physically believable production design"
        ),
        "negative_prompt": (
            "fantasy video-game rendering, excessive orange and teal, "
            "plastic armor, artificial landscapes, oversaturated colors, "
            "weightless crowds, excessive digital sharpening, cartoon aesthetics"
        ),
        "denoise": 0.50,
        "structure_weight": 0.89,
        "color_boost": 0.90,
        "keywords": [
            "historical epic",
            "anamorphic",
            "wide landscape",
            "golden hour",
            "dust",
            "crowds",
            "monumental",
            "cinematic grain"
        ],
    },

    "ridley_scott_noir": {
        "name": "Ridley Scott Urban Noir",
        "category": "cinematic",
        "era": "1980s-2000s",
        "prompt": (
            "urban noir cinematography, 35mm and 50mm lenses, occasional 24mm wide-angle "
            "environmental framing, rain-soaked streets, dense architectural backgrounds, "
            "night exteriors illuminated by practical street lamps, storefronts and vehicle lights, "
            "wet asphalt reflections, controlled haze, hard backlight, motivated side light, "
            "deep shadow pockets, muted charcoal, steel blue, dirty amber and brown palette, "
            "subtle desaturation, realistic skin tones, fine 35mm film grain, "
            "soft halation around practical lights, restrained depth of field, "
            "precise compositions with strong verticals and layers, slow tracking camera, "
            "architectural framing, oppressive urban density"
        ),
        "negative_prompt": (
            "neon cyberpunk, excessive magenta and cyan, glossy commercial photography, "
            "extreme shallow depth of field, artificial fog, HDR halos, "
            "plastic skin, oversaturated reflections, video-game city"
        ),
        "denoise": 0.48,
        "structure_weight": 0.86,
        "color_boost": 0.80,
        "keywords": [
            "urban noir",
            "35mm",
            "50mm",
            "rain",
            "wet asphalt",
            "practical lights",
            "architecture",
            "night"
        ],
    },

    "ridley_scott_digital": {
        "name": "Ridley Scott Digital",
        "category": "cinematic",
        "era": "2010s-2020s",
        "prompt": (
            "modern Ridley Scott cinematic photography, large-format digital appearance "
            "with restrained filmic texture, wide-angle environmental compositions, "
            "24mm, 32mm and 50mm perspectives, enormous production design, "
            "naturalistic daylight mixed with strong practical sources, "
            "controlled atmospheric haze, volumetric sunlight, dust and smoke, "
            "muted earth tones with selective warm highlights, steel blue shadows, "
            "realistic skin tones, moderate depth of field, crisp but not clinical detail, "
            "soft highlight rolloff, subtle grain texture, carefully controlled camera movement, "
            "sweeping crane shots, slow tracking, occasional handheld immediacy, "
            "monumental architecture and highly tactile environments"
        ),
        "negative_prompt": (
            "sterile digital look, excessive 8K sharpness, oversaturated blockbuster grading, "
            "generic CGI, excessive lens flares, plastic materials, artificial bokeh, "
            "clean minimalist sets, cartoon rendering"
        ),
        "denoise": 0.46,
        "structure_weight": 0.87,
        "color_boost": 0.84,
        "keywords": [
            "modern digital",
            "large format",
            "24mm",
            "32mm",
            "50mm",
            "atmospheric haze",
            "monumental",
            "tactile"
        ],
    },
}

__all__ = ["RIDLEY_SCOTT_STYLES"]
