"""
CharacterForge Cinematic - Denis Villeneuve
============================================

Evoluzione della fotografia cinematografica associata alla filmografia di
Denis Villeneuve dagli anni 2000 agli anni 2020.

Focus:
- composizioni monumentali
- minimalismo visivo
- atmosfere contemplative
- palette desaturate
- luce naturale e volumetrica
- grandi spazi architettonici
- profondità atmosferica
- contrasto controllato
- fotografia epica ma realistica
"""

VILLENEUVE_STYLES = {
    "villeneuve_2000s": {
        "name": "Villeneuve - Atmospheric 2000s",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "early 2000s atmospheric cinematic photography, restrained composition, "
            "muted natural colors, desaturated earth tones, soft overcast daylight, "
            "controlled contrast, realistic skin texture, natural imperfections, "
            "quiet psychological atmosphere, subtle film grain, "
            "deep environmental perspective, sparse compositions, "
            "naturalistic interiors, subdued highlights, "
            "documentary-like photographic realism"
        ),
        "negative_prompt": (
            "oversaturated colors, glossy commercial photography, excessive bloom, "
            "fantasy glow, plastic skin, beauty retouching, artificial HDR, "
            "excessive sharpening, cartoon, anime, painterly rendering, "
            "synthetic CGI appearance"
        ),
        "denoise": 0.70,
        "structure_weight": 0.84,
        "color_boost": 0.68,
        "keywords": [
            "atmospheric",
            "muted",
            "natural",
            "psychological",
            "overcast",
            "documentary",
            "film-grain",
            "realism",
        ],
    },

    "villeneuve_2010s": {
        "name": "Villeneuve - Monumental 2010s",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "2010s monumental cinematic photography, vast architectural compositions, "
            "minimalist visual design, muted neutral palette, desaturated colors, "
            "soft atmospheric light, volumetric haze, precise geometric framing, "
            "deep environmental perspective, controlled contrast, "
            "large-scale environments, realistic materials and textures, "
            "subtle filmic grain, natural skin tones, carefully controlled highlights, "
            "quiet tension, contemplative atmosphere, "
            "epic photographic realism"
        ),
        "negative_prompt": (
            "bright saturated colors, excessive neon, glossy blockbuster aesthetic, "
            "orange-teal grading, excessive lens flare, artificial HDR, "
            "plastic surfaces, fantasy glow, excessive bloom, cartoon, anime, "
            "painterly rendering, synthetic CGI appearance, cluttered composition"
        ),
        "denoise": 0.67,
        "structure_weight": 0.92,
        "color_boost": 0.62,
        "keywords": [
            "monumental",
            "minimalist",
            "architectural",
            "desaturated",
            "atmospheric",
            "volumetric",
            "geometric",
            "epic",
        ],
    },

    "villeneuve_2020s": {
        "name": "Villeneuve - Modern Epic 2020s",
        "category": "cinematic",
        "era": "2020s",
        "prompt": (
            "modern large-format cinematic photography, immense environmental scale, "
            "minimalist composition, sophisticated neutral and desaturated palette, "
            "natural atmospheric perspective, soft directional sunlight, "
            "controlled volumetric haze, monumental architecture and landscapes, "
            "precise geometric framing, deep spatial layering, "
            "realistic physical materials, subtle analog film texture, "
            "natural skin reproduction, controlled highlight rolloff, "
            "deep dimensional shadows, tactile surfaces, "
            "immersive theatrical photographic realism"
        ),
        "negative_prompt": (
            "oversaturated fantasy colors, excessive orange-teal grading, "
            "artificial HDR, excessive sharpening, plastic skin, fake materials, "
            "excessive bloom, neon overload, fantasy glow, cartoon, anime, "
            "painterly rendering, synthetic CGI appearance, flat lighting"
        ),
        "denoise": 0.64,
        "structure_weight": 0.95,
        "color_boost": 0.60,
        "keywords": [
            "modern-epic",
            "large-format",
            "monumental",
            "minimalist",
            "atmospheric",
            "desaturated",
            "spatial-depth",
            "theatrical",
        ],
    },

    "villeneuve_sci_fi": {
        "name": "Villeneuve - Atmospheric Science Fiction",
        "category": "cinematic",
        "era": "science-fiction",
        "prompt": (
            "serious atmospheric science-fiction cinematography, monumental scale, "
            "minimalist futuristic architecture, restrained desaturated palette, "
            "cool neutrals, muted earth tones, carefully controlled accent colors, "
            "volumetric atmosphere, naturalistic light behavior, "
            "soft directional illumination, deep spatial perspective, "
            "massive environmental structures, realistic physical materials, "
            "subtle analog texture, controlled contrast, atmospheric depth, "
            "human figures dwarfed by architecture, contemplative cinematic realism"
        ),
        "negative_prompt": (
            "colorful space opera, neon overload, cyberpunk saturation, "
            "glossy futuristic surfaces, excessive lens flare, artificial HDR, "
            "fantasy glow, cartoon, anime, painterly rendering, "
            "plastic materials, toy-like architecture, synthetic CGI appearance"
        ),
        "denoise": 0.65,
        "structure_weight": 0.96,
        "color_boost": 0.58,
        "keywords": [
            "science-fiction",
            "monumental",
            "futuristic",
            "minimalist",
            "volumetric",
            "desaturated",
            "architecture",
            "atmosphere",
        ],
    },

    "villeneuve_human": {
        "name": "Villeneuve - Human Intimacy",
        "category": "cinematic",
        "era": "human",
        "prompt": (
            "intimate dramatic cinematography, restrained close framing, "
            "natural human skin texture, muted neutral colors, soft directional light, "
            "overcast daylight, subtle shadow gradients, realistic interiors, "
            "controlled depth of field, quiet atmospheric background, "
            "natural imperfections, realistic facial detail, "
            "subtle film grain, subdued highlights, contemplative emotional atmosphere, "
            "minimal visual distraction, grounded photographic realism"
        ),
        "negative_prompt": (
            "beauty photography, glamour lighting, plastic skin, excessive smoothing, "
            "oversaturated colors, dreamy fantasy glow, excessive bokeh, "
            "artificial HDR, excessive sharpening, cartoon, anime, "
            "painterly rendering, artificial CGI appearance"
        ),
        "denoise": 0.67,
        "structure_weight": 0.88,
        "color_boost": 0.56,
        "keywords": [
            "intimate",
            "human",
            "dramatic",
            "natural-skin",
            "muted",
            "soft-light",
            "film-grain",
            "contemplative",
        ],
    },
}


__all__ = ["VILLENEUVE_STYLES"]