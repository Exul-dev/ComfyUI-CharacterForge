"""
CharacterForge Cinematic - Brian De Palma
=========================================

Visual language inspired by De Palma's cinema:
voyeuristic framing, split-screen structures, split-diopter depth,
wide-angle perspectives, elaborate camera movement, geometric
compositions, saturated color, practical lighting and suspense
built through spatial relationships.
"""

DEPALMA_STYLES = {

    "depalma_thriller": {
        "name": "De Palma Thriller",
        "category": "cinematic",
        "era": "1970s-1980s",
        "prompt": (
            "1970s and 1980s psychological thriller cinematography, "
            "24mm and 28mm wide-angle lenses, deliberate perspective distortion, "
            "voyeuristic compositions, strong foreground-background relationships, "
            "deep spatial staging, long tracking shots, slow camera reveals, "
            "precise dolly movement, practical tungsten interiors, hard motivated "
            "backlight, saturated red accents, deep blue shadows, cream and amber highlights, "
            "rich but controlled color, fine 35mm film grain, subtle halation, "
            "carefully controlled depth of field, architectural framing, "
            "visual suspense created through negative space and off-screen information"
        ),
        "negative_prompt": (
            "modern digital thriller, handheld chaos, flat compositions, "
            "generic shallow depth of field, excessive teal and orange, "
            "HDR appearance, plastic skin, extreme lens distortion, "
            "music-video editing aesthetics"
        ),
        "denoise": 0.49,
        "structure_weight": 0.88,
        "color_boost": 0.96,
        "keywords": [
            "thriller",
            "24mm",
            "28mm",
            "voyeurism",
            "tracking shot",
            "suspense",
            "35mm",
            "saturated color"
        ],
    },

    "depalma_split_screen": {
        "name": "De Palma Split Screen",
        "category": "cinematic",
        "era": "1970s-1980s",
        "prompt": (
            "1970s experimental thriller cinematography, split-screen visual grammar, "
            "parallel action presented as simultaneous spatial information, "
            "symmetrical compositions, wide-angle 24mm perspective, "
            "deep staging across foreground and background, carefully synchronized camera movement, "
            "long lateral tracking shots, controlled zooms, practical tungsten lighting, "
            "strong red and blue color accents, muted beige architecture, "
            "fine-grain 35mm film texture, optical softness, subtle halation, "
            "precise geometric framing, theatrical blocking, visual tension generated "
            "by contrasting simultaneous actions and spatial distance"
        ),
        "negative_prompt": (
            "random collage, chaotic editing, modern social-media split screen, "
            "digital sharpness, excessive neon, generic cinematic framing, "
            "extreme fisheye distortion, artificial CGI"
        ),
        "denoise": 0.50,
        "structure_weight": 0.90,
        "color_boost": 0.94,
        "keywords": [
            "split screen",
            "parallel action",
            "24mm",
            "deep staging",
            "tracking",
            "geometric composition",
            "35mm film",
            "visual suspense"
        ],
    },

    "depalma_split_diopter": {
        "name": "De Palma Split Diopter",
        "category": "cinematic",
        "era": "1970s-1980s",
        "prompt": (
            "cinematic split-diopter photography, foreground and background subjects "
            "simultaneously sharp, extreme depth staging, 35mm film camera, "
            "wide-angle 28mm lens character, deliberate optical split-diopter effect, "
            "strong compositional diagonals, faces or objects positioned at different "
            "depths within the same frame, voyeuristic point of view, slow controlled dolly, "
            "practical interior lighting, warm tungsten mixed with cool ambient light, "
            "saturated red accents, deep blue shadows, fine 35mm grain, subtle optical halation, "
            "slightly theatrical production design, suspenseful negative space, "
            "visual information carefully distributed throughout the frame"
        ),
        "negative_prompt": (
            "ordinary shallow depth of field, completely uniform focus, "
            "modern digital bokeh, excessive lens blur, fisheye distortion, "
            "HDR, plastic skin, random composition, flat staging"
        ),
        "denoise": 0.48,
        "structure_weight": 0.92,
        "color_boost": 0.91,
        "keywords": [
            "split diopter",
            "deep focus",
            "foreground background",
            "28mm",
            "35mm",
            "voyeuristic",
            "suspense",
            "optical technique"
        ],
    },

    "depalma_voyeurism": {
        "name": "De Palma Voyeurism",
        "category": "cinematic",
        "era": "1970s-1990s",
        "prompt": (
            "voyeuristic psychological cinema, 50mm and 85mm lenses alternating "
            "with wide environmental shots, subjective point of view, surveillance-like "
            "framing, views through windows, doors, mirrors and architectural openings, "
            "compressed telephoto observation, deliberate framing within framing, "
            "low-key practical lighting, isolated pools of warm light, cool exterior ambience, "
            "deep crimson accents, muted cream and gray surroundings, "
            "fine 35mm film grain, soft halation around practical lights, "
            "slow creeping camera movement, controlled zooms, long takes, "
            "negative space surrounding observed characters, tension created through distance"
        ),
        "negative_prompt": (
            "action-camera perspective, handheld documentary style, "
            "extreme digital clarity, excessive bokeh, neon cyberpunk, "
            "random camera movement, oversaturated colors, generic surveillance footage"
        ),
        "denoise": 0.47,
        "structure_weight": 0.87,
        "color_boost": 0.89,
        "keywords": [
            "voyeurism",
            "50mm",
            "85mm",
            "surveillance",
            "mirror",
            "framing within framing",
            "telephoto",
            "psychological"
        ],
    },

    "depalma_neon_suspense": {
        "name": "De Palma Neon Suspense",
        "category": "cinematic",
        "era": "1980s-1990s",
        "prompt": (
            "stylized 1980s and 1990s urban thriller photography, 28mm and 35mm lenses, "
            "dramatic architectural compositions, night streets, reflective glass, "
            "wet pavement, practical neon signage used selectively, saturated red, "
            "magenta and blue light against dark neutral environments, strong backlighting, "
            "controlled haze, motivated practical sources, deep shadows, "
            "fine 35mm film grain, visible analog texture, soft halation around colored lights, "
            "precise dolly and crane movements, long tracking shots, "
            "dramatic silhouettes, voyeuristic distance, geometric city architecture, "
            "stylized but physically believable production design"
        ),
        "negative_prompt": (
            "modern cyberpunk overload, excessive neon everywhere, LED digital look, "
            "HDR, oversharpening, plastic surfaces, excessive bloom, "
            "random handheld movement, video-game aesthetics"
        ),
        "denoise": 0.49,
        "structure_weight": 0.86,
        "color_boost": 1.02,
        "keywords": [
            "neon",
            "urban thriller",
            "28mm",
            "35mm",
            "wet pavement",
            "tracking shot",
            "halation",
            "analog"
        ],
    },
}

__all__ = ["DEPALMA_STYLES"]
