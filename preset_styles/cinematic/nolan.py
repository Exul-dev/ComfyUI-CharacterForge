"""
CharacterForge Cinematic - Christopher Nolan
=============================================

Evoluzione della fotografia cinematografica associata alla filmografia di
Christopher Nolan dagli anni 2000 agli anni 2020.

Focus:
- grande formato cinematografico
- composizioni geometriche
- contrasto elevato ma controllato
- fotografia naturale e fisica
- luce motivata
- palette neutre e desaturate
- profondità e separazione dei piani
- texture fotografica realistica
- scala epica e senso della realtà fisica
"""

NOLAN_STYLES = {
    "nolan_2000s": {
        "name": "Nolan - Psychological 2000s",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "early 2000s psychological cinematic photography, precise geometric "
            "composition, restrained neutral color palette, cool desaturated tones, "
            "strong naturalistic contrast, motivated practical lighting, "
            "deep shadows with preserved detail, controlled highlights, "
            "realistic urban environments, subtle film grain, 35mm photographic "
            "texture, realistic skin tones, strong depth separation, "
            "carefully controlled perspective, grounded physical realism, "
            "serious dramatic atmosphere"
        ),
        "negative_prompt": (
            "oversaturated colors, glossy commercial look, excessive bloom, "
            "dreamy fantasy lighting, plastic skin, artificial HDR, "
            "excessive lens flare, crushed unreadable blacks, cartoon, anime, "
            "painterly rendering, synthetic CGI appearance"
        ),
        "denoise": 0.69,
        "structure_weight": 0.86,
        "color_boost": 0.70,
        "keywords": [
            "psychological",
            "geometric",
            "neutral",
            "desaturated",
            "naturalistic",
            "35mm",
            "physical-realism",
            "deep-shadow",
        ],
    },

    "nolan_2010s": {
        "name": "Nolan - Large Format 2010s",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "large-format cinematic photography, monumental composition, "
            "highly controlled perspective, neutral and slightly desaturated "
            "color palette, naturalistic daylight, physically motivated lighting, "
            "deep dimensional shadows, clean highlight rolloff, realistic skin, "
            "fine photographic detail, subtle organic film texture, "
            "large-format film characteristics, expansive environments, "
            "strong foreground and background separation, practical atmosphere, "
            "precise architectural geometry, epic but grounded visual scale, "
            "photographic realism"
        ),
        "negative_prompt": (
            "neon colors, excessive saturation, orange-teal grading, "
            "artificial HDR, plastic textures, excessive sharpening, "
            "fantasy glow, excessive bloom, artificial beauty lighting, "
            "cartoon, anime, painterly rendering, cheap CGI appearance, "
            "flat composition"
        ),
        "denoise": 0.67,
        "structure_weight": 0.91,
        "color_boost": 0.66,
        "keywords": [
            "large-format",
            "epic-scale",
            "natural-light",
            "geometry",
            "physical",
            "film-texture",
            "deep-space",
            "realism",
        ],
    },

    "nolan_2020s": {
        "name": "Nolan - Modern Large Format 2020s",
        "category": "cinematic",
        "era": "2020s",
        "prompt": (
            "contemporary large-format cinematic photography, extremely detailed "
            "photographic image, monumental visual scale, precise geometric framing, "
            "natural and physically motivated illumination, neutral restrained palette, "
            "subtle warm and cool separation without aggressive grading, "
            "deep dimensional blacks, controlled highlights, realistic skin tones, "
            "fine analog film texture, large-format photographic depth, "
            "complex practical environments, atmospheric depth, "
            "strong foreground-background separation, tactile surfaces, "
            "realistic physical materials, expansive compositions, "
            "epic scale grounded in photographic realism"
        ),
        "negative_prompt": (
            "oversaturated colors, exaggerated teal-orange grading, "
            "digital plastic appearance, excessive HDR, excessive sharpening, "
            "artificial glow, excessive bloom, fake volumetric effects, "
            "fantasy lighting, cartoon, anime, painterly rendering, "
            "synthetic CGI appearance, flat lighting"
        ),
        "denoise": 0.64,
        "structure_weight": 0.94,
        "color_boost": 0.62,
        "keywords": [
            "large-format",
            "modern-cinema",
            "epic",
            "geometric",
            "natural-light",
            "analog-texture",
            "physical-realism",
            "high-detail",
        ],
    },

    "nolan_imax": {
        "name": "Nolan - IMAX Epic",
        "category": "cinematic",
        "era": "IMAX",
        "prompt": (
            "IMAX-scale cinematic photography, extremely large-format image, "
            "monumental landscapes and architecture, enormous sense of physical scale, "
            "precise composition, deep perspective, natural atmospheric depth, "
            "high resolving power, realistic fine detail, physically motivated lighting, "
            "controlled contrast, natural daylight, subtle film texture, "
            "realistic skin and materials, carefully separated tonal planes, "
            "powerful environmental composition, tactile physical realism, "
            "immersive theatrical cinematography"
        ),
        "negative_prompt": (
            "small-scale framing, flat perspective, oversaturated colors, "
            "excessive HDR, digital artifacts, artificial sharpening, "
            "plastic surfaces, fantasy glow, excessive bloom, cartoon, anime, "
            "painterly rendering, fake CGI atmosphere, distorted perspective"
        ),
        "denoise": 0.62,
        "structure_weight": 0.96,
        "color_boost": 0.60,
        "keywords": [
            "IMAX",
            "large-format",
            "monumental",
            "epic-scale",
            "deep-perspective",
            "natural-light",
            "high-resolution",
            "physical",
        ],
    },

    "nolan_intimate": {
        "name": "Nolan - Intimate Psychological",
        "category": "cinematic",
        "era": "intimate",
        "prompt": (
            "intimate psychological cinematic photography, controlled close framing, "
            "natural skin texture, restrained neutral palette, low-key motivated lighting, "
            "soft directional illumination, deep but readable shadows, "
            "subtle background separation, realistic practical environments, "
            "precise facial detail, natural imperfections, controlled depth of field, "
            "quiet visual tension, tactile photographic texture, "
            "subtle film grain, realistic contrast, serious grounded atmosphere"
        ),
        "negative_prompt": (
            "beauty retouching, plastic skin, glamour lighting, excessive saturation, "
            "dreamy atmosphere, excessive bokeh, artificial HDR, excessive bloom, "
            "fantasy lighting, cartoon, anime, painterly rendering, "
            "overly soft image, artificial CGI appearance"
        ),
        "denoise": 0.66,
        "structure_weight": 0.89,
        "color_boost": 0.58,
        "keywords": [
            "intimate",
            "psychological",
            "close-up",
            "natural-skin",
            "low-key",
            "neutral",
            "film-grain",
            "tension",
        ],
    },
}


__all__ = ["NOLAN_STYLES"]