"""
CharacterForge Cinematic - Gareth Edwards
==========================================

Cinematic presets inspired by Gareth Edwards:
documentary-influenced science fiction, naturalistic lighting, practical
environments, enormous technological structures contrasted with ordinary
human spaces, restrained color palettes, atmospheric scale, grounded
visual effects, and intimate human perspective within monumental worlds.
"""

GARETH_EDWARDS_STYLES = {

    "gareth_edwards_monumental": {
        "name": "Gareth Edwards — Monumental Sci-Fi",
        "category": "cinematic",
        "era": "2010s–2020s",
        "prompt": (
            "grounded science-fiction cinematography, enormous technological structures "
            "rising behind ordinary human environments, documentary realism, natural "
            "daylight, overcast skies, atmospheric haze, muted gray, blue and earth-tone "
            "palette, realistic concrete, steel, dust and weathered surfaces, wide "
            "spherical lenses, deep environmental perspective, human figures kept small "
            "against colossal architecture, restrained depth of field, subtle handheld "
            "camera movement, practical foreground objects, realistic atmospheric "
            "perspective, soft highlight rolloff, understated digital film texture, "
            "photographic realism, immense scale achieved through composition rather "
            "than visual excess"
        ),
        "negative_prompt": (
            "glossy space opera, excessive neon, clean futuristic architecture, "
            "superhero spectacle, artificial HDR, oversaturated colors, plastic CGI, "
            "generic concept art, videogame rendering, excessive lens flare, "
            "weightless environments"
        ),
        "denoise": 0.81,
        "structure_weight": 0.91,
        "color_boost": 0.96,
        "keywords": [
            "monumental sci-fi",
            "documentary realism",
            "natural daylight",
            "environmental scale",
            "wide lens",
            "atmospheric haze",
            "weathered technology"
        ],
    },

    "gareth_edwards_rogue_one": {
        "name": "Gareth Edwards — War in Space",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "grounded military science-fiction cinematography, war documentary influence, "
            "dense battlefield environments, tropical vegetation mixed with military "
            "technology, smoke, dust, rain and debris, natural sunlight filtered through "
            "clouds, muted green, gray, brown and desaturated blue palette, practical "
            "lighting, handheld camera, wide-angle lenses close to characters, long-lens "
            "compression for distant battles, deep environmental layers, realistic "
            "motion blur, imperfect framing, enormous spacecraft visible within real "
            "landscapes, practical costume and prop textures, restrained visual effects, "
            "cinematic grain and atmospheric depth, human-scale war photography combined "
            "with monumental science-fiction imagery"
        ),
        "negative_prompt": (
            "clean futuristic battlefield, glossy military advertisement, neon sci-fi, "
            "plastic armor, sterile environments, excessive explosions, oversaturated "
            "colors, videogame graphics, superhero posing, artificial studio lighting"
        ),
        "denoise": 0.82,
        "structure_weight": 0.9,
        "color_boost": 0.97,
        "keywords": [
            "war documentary",
            "military sci-fi",
            "tropical battlefield",
            "handheld",
            "dust and smoke",
            "muted green",
            "large-scale warfare"
        ],
    },

    "gareth_edwards_monsters": {
        "name": "Gareth Edwards — Low-Budget Realism",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "naturalistic low-budget science-fiction cinematography, real locations, "
            "ordinary streets and interiors transformed by subtle speculative elements, "
            "available light, practical lamps, overcast daylight, muted earth colors, "
            "gray-blue shadows, handheld DSLR-like photographic character, lightweight "
            "camera perspective, moderate depth of field, imperfect exposure, realistic "
            "skin texture, environmental haze, weathered buildings, roadside details, "
            "distant colossal creatures integrated naturally into landscapes, restrained "
            "visual effects, observational framing, intimate human scale, subtle digital "
            "noise, documentary immediacy and believable physical space"
        ),
        "negative_prompt": (
            "blockbuster spectacle, polished CGI, fantasy creature close-up, glossy "
            "lighting, studio sets, futuristic architecture, excessive color grading, "
            "perfect stabilization, clean concept-art backgrounds, videogame rendering"
        ),
        "denoise": 0.79,
        "structure_weight": 0.84,
        "color_boost": 0.92,
        "keywords": [
            "low-budget realism",
            "real locations",
            "available light",
            "handheld",
            "observational",
            "subtle VFX",
            "human scale"
        ],
    },

    "gareth_edwards_creator": {
        "name": "Gareth Edwards — Creator",
        "category": "cinematic",
        "era": "2020s",
        "prompt": (
            "near-future science-fiction cinematography grounded in contemporary reality, "
            "dense Asian-inspired megacity environments, practical urban architecture, "
            "rain, humid atmosphere, concrete, glass, metal and weathered technology, "
            "natural overcast daylight mixed with practical signage and interior light, "
            "restrained cyan, gray, amber and muted red palette, wide spherical lenses, "
            "deep focus environmental compositions, handheld documentary movement, "
            "characters integrated into crowded streets, realistic reflections on wet "
            "surfaces, subtle volumetric atmosphere, believable robotics and machinery, "
            "large technological objects contrasted against ordinary human life, "
            "photographic imperfections, understated digital texture, tactile realism"
        ),
        "negative_prompt": (
            "cyberpunk neon overload, glossy futuristic city, pristine robots, "
            "plastic CGI, exaggerated holograms, videogame interface, excessive bloom, "
            "oversaturated colors, sterile architecture, superhero aesthetics"
        ),
        "denoise": 0.82,
        "structure_weight": 0.89,
        "color_boost": 1.04,
        "keywords": [
            "near future",
            "urban sci-fi",
            "rain",
            "wet surfaces",
            "robotics",
            "documentary camera",
            "deep focus",
            "tactile realism"
        ],
    },

    "gareth_edwards_natural_light": {
        "name": "Gareth Edwards — Natural Light Sci-Fi",
        "category": "cinematic",
        "era": "2010s–2020s",
        "prompt": (
            "natural-light science-fiction cinematography, no artificial glamour lighting, "
            "soft overcast daylight, golden-hour backlight, practical interior illumination, "
            "large-scale environments photographed with realistic atmospheric perspective, "
            "dust particles, humidity, smoke and distant haze, muted blue-gray and brown "
            "palette, subtle warm highlights, wide spherical lenses, deep environmental "
            "focus, realistic scale relationships, ordinary human figures surrounded by "
            "advanced technology, restrained camera movement, slight handheld instability, "
            "natural skin tones, realistic material response, understated filmic contrast, "
            "subtle grain, physically believable visual effects and photographic texture"
        ),
        "negative_prompt": (
            "studio glamour lighting, neon palette, artificial HDR, excessive contrast, "
            "glossy CGI, clean futuristic surfaces, fantasy lighting, plastic skin, "
            "overly shallow depth of field, commercial advertising look"
        ),
        "denoise": 0.8,
        "structure_weight": 0.88,
        "color_boost": 0.95,
        "keywords": [
            "natural light",
            "overcast",
            "golden hour",
            "wide spherical lens",
            "atmospheric perspective",
            "realistic VFX",
            "subtle grain"
        ],
    },
}

__all__ = ["GARETH_EDWARDS_STYLES"]
