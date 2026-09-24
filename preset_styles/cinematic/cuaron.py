"""
CharacterForge Cinematic - Alfonso Cuarón
=========================================

Cinematic presets inspired by the visual language of Alfonso Cuarón:
long takes, immersive camera movement, naturalistic lighting, wide-angle
spatial compositions, controlled depth of field, restrained palettes,
environmental realism, and precise visual choreography.
"""

CUARON_STYLES = {

    "cuaron_1990s": {
        "name": "Alfonso Cuarón — 1990s Naturalism",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "naturalistic 1990s cinematic photography, intimate human environments, "
            "soft available light, practical lamps, overcast daylight, restrained "
            "earth-tone palette, subtle warm skin tones, 35mm spherical lenses, "
            "moderate depth of field, handheld and gently floating camera movement, "
            "observational framing, carefully composed everyday spaces, realistic "
            "textures, modest production design, slightly soft photochemical image, "
            "fine 35mm film grain, natural exposure, understated contrast, "
            "characters integrated naturally into their surroundings, quiet realism"
        ),
        "negative_prompt": (
            "glossy digital cinema, excessive contrast, artificial HDR, neon colors, "
            "plastic skin, extreme shallow depth of field, sterile studio lighting, "
            "fashion photography, videogame rendering, excessive sharpening, "
            "overproduced spectacle"
        ),
        "denoise": 0.77,
        "structure_weight": 0.84,
        "color_boost": 1.04,
        "keywords": [
            "1990s naturalism",
            "35mm film",
            "available light",
            "observational camera",
            "earth tones",
            "human realism",
            "soft photochemical texture"
        ],
    },

    "cuaron_children_of_men": {
        "name": "Alfonso Cuarón — Immersive Dystopia",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "immersive dystopian cinematography, documentary-like realism, desaturated "
            "gray-green and brown palette, dirty urban environments, weathered concrete, "
            "fog, smoke, rain and dust, natural overcast daylight mixed with practical "
            "vehicle and street lighting, wide-angle 35mm spherical lenses, deep spatial "
            "focus, long-take visual grammar, camera physically moving through crowds and "
            "environments, foreground obstacles passing close to lens, complex layered "
            "blocking, handheld precision, realistic motion blur, restrained film grain, "
            "low saturation, muted highlights, environmental storytelling, visceral "
            "presence without glossy spectacle"
        ),
        "negative_prompt": (
            "clean science fiction, glossy dystopia, neon cyberpunk, superhero framing, "
            "synthetic CGI environments, excessive lens flare, oversaturated colors, "
            "perfectly clean streets, shallow portrait photography, static studio shots, "
            "video game graphics"
        ),
        "denoise": 0.82,
        "structure_weight": 0.9,
        "color_boost": 0.94,
        "keywords": [
            "immersive dystopia",
            "long take",
            "wide angle",
            "deep focus",
            "gray-green palette",
            "documentary realism",
            "crowd choreography",
            "environmental storytelling"
        ],
    },

    "cuaron_gravity": {
        "name": "Alfonso Cuarón — Orbital Immersion",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "immersive orbital cinematography, vast black space surrounding delicate "
            "human figures, physically coherent spacecraft interiors, luminous Earth "
            "curvature, controlled practical illumination, cool blue-white highlights, "
            "deep blacks, subtle cyan atmosphere, large-format cinematic photography, "
            "wide-angle lens perspective transitioning into intimate close proximity, "
            "extreme spatial continuity, long fluid camera movement, floating camera "
            "trajectories, precise reflections in visors and glass, controlled depth of "
            "field, restrained optical distortion, delicate atmospheric glow, realistic "
            "micro-scratches and material textures, subtle digital-era filmic grain, "
            "elegant minimalism and physical immersion"
        ),
        "negative_prompt": (
            "cartoon space, fantasy planets, excessive lens flare, colorful space opera, "
            "unrealistic spacecraft geometry, plastic surfaces, oversaturated nebulae, "
            "flat lighting, videogame HUD, exaggerated depth of field, artificial stars"
        ),
        "denoise": 0.8,
        "structure_weight": 0.92,
        "color_boost": 1.03,
        "keywords": [
            "orbital immersion",
            "large format",
            "fluid camera",
            "deep black",
            "Earth curvature",
            "cool blue-white",
            "spatial continuity",
            "physical realism"
        ],
    },

    "cuaron_roma": {
        "name": "Alfonso Cuarón — Roma",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "black-and-white large-format cinematography, highly detailed domestic "
            "environment, soft natural daylight, subtle tonal gradations, luminous "
            "white skies, rich but restrained blacks, wide-angle compositions, deep "
            "focus across architectural spaces, static frames alternating with slow "
            "lateral camera movement, carefully choreographed foreground and background "
            "action, tiled floors, concrete, glass, weathered walls and everyday objects "
            "rendered with extraordinary texture, soft atmospheric diffusion, precise "
            "geometric composition, realistic human scale, elegant negative space, "
            "fine monochromatic grain, high dynamic range without artificial HDR, "
            "quiet observational realism"
        ),
        "negative_prompt": (
            "harsh black crush, artificial HDR, glossy monochrome, excessive contrast, "
            "studio lighting, shallow focus, surreal environments, empty production "
            "design, digital plastic texture, excessive sharpening, fashion editorial"
        ),
        "denoise": 0.79,
        "structure_weight": 0.9,
        "color_boost": 0.88,
        "keywords": [
            "black and white",
            "large format",
            "deep focus",
            "domestic realism",
            "geometric composition",
            "soft daylight",
            "observational cinema",
            "monochrome texture"
        ],
    },

    "cuaron_immersive_camera": {
        "name": "Alfonso Cuarón — Continuous Camera",
        "category": "cinematic",
        "era": "2000s–2010s",
        "prompt": (
            "continuous-take cinematography, immersive camera physically moving through "
            "the environment, long uninterrupted shot feeling, wide spherical lens, "
            "deep focus, carefully choreographed actors crossing multiple depth planes, "
            "foreground objects passing close to camera, natural occlusion, realistic "
            "motion blur, fluid handheld stabilization, precise spatial geography, "
            "camera motivated by human movement, natural practical lighting, subtle "
            "environmental haze, realistic skin and materials, restrained cinematic "
            "palette, fine filmic texture, complex blocking visible in a single frame, "
            "strong sense of physical presence and temporal continuity"
        ),
        "negative_prompt": (
            "static portrait, conventional shot-reverse-shot, artificial camera paths, "
            "impossible spatial geometry, excessive steadicam smoothness, shallow focus "
            "everywhere, glossy commercial photography, videogame camera, CGI motion, "
            "television lighting, excessive visual effects"
        ),
        "denoise": 0.81,
        "structure_weight": 0.93,
        "color_boost": 1.02,
        "keywords": [
            "continuous take",
            "long take",
            "wide lens",
            "deep focus",
            "complex blocking",
            "immersive camera",
            "spatial continuity",
            "natural lighting"
        ],
    },
}

__all__ = ["CUARON_STYLES"]
