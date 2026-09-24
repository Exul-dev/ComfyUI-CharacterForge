"""
CharacterForge Cinematic - David Fincher
=========================================

Evoluzione della fotografia cinematografica associata alla filmografia di
David Fincher dagli anni '80 agli anni 2020.

Focus:
- composizioni estremamente controllate
- fotografia low-key
- palette fredde e desaturate
- ombre profonde ma leggibili
- contaminazioni verdi/ciano
- luce artificiale controllata
- texture cinematografica precisa
- atmosfera urbana, psicologica e realistica
"""

FINCHER_STYLES = {
    "fincher_1980s": {
        "name": "Fincher - Industrial 1980s",
        "category": "cinematic",
        "era": "1980s",
        "prompt": (
            "dark industrial cinematic photography, late 1980s visual language, "
            "highly controlled composition, dramatic artificial lighting, "
            "deep shadows, hard directional sources, cool metallic environments, "
            "subtle green and cyan contamination, urban night atmosphere, "
            "precise framing, graphic silhouettes, restrained color palette, "
            "35mm film texture, visible but fine grain, realistic skin texture, "
            "slightly underexposed image, strong tonal separation, "
            "cinematic contrast, photographic realism"
        ),
        "negative_prompt": (
            "bright cheerful colors, excessive saturation, glossy commercial look, "
            "soft beauty lighting, fantasy glow, excessive bloom, plastic skin, "
            "overexposed highlights, crushed unreadable shadows, cartoon, anime, "
            "painterly rendering, artificial HDR"
        ),
        "denoise": 0.68,
        "structure_weight": 0.82,
        "color_boost": 0.78,
        "keywords": [
            "industrial",
            "dark",
            "cold",
            "urban",
            "35mm",
            "low-key",
            "green-cyan",
            "hard-light",
        ],
    },

    "fincher_1990s": {
        "name": "Fincher - Psychological 1990s",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "1990s psychological crime cinema, meticulously controlled framing, "
            "cold desaturated color palette, deep blacks with preserved shadow detail, "
            "muted skin tones, subtle green and cyan color contamination, "
            "low-key tungsten and fluorescent lighting, dense urban interiors, "
            "moody night photography, precise perspective, restrained camera movement, "
            "35mm cinematic texture, fine organic film grain, realistic faces and skin, "
            "controlled highlights, slightly dirty atmospheric texture, "
            "ominous visual tension, photographic realism"
        ),
        "negative_prompt": (
            "warm romantic lighting, vivid colors, oversaturated reds, "
            "clean fashion photography, glossy commercial advertising, "
            "soft dreamy atmosphere, excessive lens flare, excessive bloom, "
            "plastic skin, HDR halos, fantasy lighting, cartoon, anime, "
            "painterly texture"
        ),
        "denoise": 0.70,
        "structure_weight": 0.86,
        "color_boost": 0.72,
        "keywords": [
            "psychological",
            "crime",
            "desaturated",
            "cold",
            "fluorescent",
            "tungsten",
            "35mm",
            "deep-shadows",
        ],
    },

    "fincher_2000s": {
        "name": "Fincher - Digital Transition 2000s",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "early 2000s precision digital-cinema aesthetic, highly controlled "
            "cinematography, cool neutral palette, restrained saturation, "
            "deep blacks, clean but textured midtones, controlled highlights, "
            "subtle green-cyan contamination, artificial interior lighting, "
            "fluorescent practicals, dark urban environments, precise symmetrical "
            "composition, extremely deliberate framing, realistic skin texture, "
            "fine film-to-digital transitional texture, subtle grain, "
            "cinematic contrast, understated visual tension, photographic realism"
        ),
        "negative_prompt": (
            "oversaturated colors, warm orange-teal grading, glossy blockbuster look, "
            "excessive sharpening, excessive HDR, crushed blacks without detail, "
            "plastic skin, beauty retouching, fantasy glow, excessive bloom, "
            "cartoon, anime, painterly rendering, artificial CGI appearance"
        ),
        "denoise": 0.68,
        "structure_weight": 0.88,
        "color_boost": 0.68,
        "keywords": [
            "digital-transition",
            "cool-neutral",
            "precise",
            "fluorescent",
            "urban",
            "desaturated",
            "deep-blacks",
            "realism",
        ],
    },

    "fincher_2010s": {
        "name": "Fincher - Digital Precision 2010s",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "modern digital cinema, extremely precise composition, controlled "
            "camera perspective, cool neutral and desaturated palette, "
            "subtle green-cyan tonal bias, deep but readable shadows, "
            "soft controlled highlights, carefully motivated practical lighting, "
            "fluorescent interiors, overcast daylight, nocturnal urban environments, "
            "clean digital image with subtle cinematic texture, realistic skin tones, "
            "high micro-detail, restrained contrast, precise exposure, "
            "minimal visual clutter, psychological atmosphere, "
            "premium photographic realism"
        ),
        "negative_prompt": (
            "vivid saturated colors, orange-teal blockbuster grading, "
            "excessive sharpening, excessive clarity, artificial HDR, "
            "plastic skin, beauty filter, dreamy glow, excessive lens flare, "
            "soft fantasy lighting, cartoon, anime, painterly rendering, "
            "CGI-looking surfaces"
        ),
        "denoise": 0.66,
        "structure_weight": 0.90,
        "color_boost": 0.64,
        "keywords": [
            "digital-cinema",
            "precision",
            "cool-neutral",
            "desaturated",
            "fluorescent",
            "micro-detail",
            "psychological",
            "realistic",
        ],
    },

    "fincher_2020s": {
        "name": "Fincher - Modern Digital 2020s",
        "category": "cinematic",
        "era": "2020s",
        "prompt": (
            "contemporary prestige digital cinema, large-format photographic feel, "
            "exceptionally controlled composition, restrained monochromatic palette, "
            "cool neutral tones, subtle cyan-green shadows, natural skin reproduction, "
            "deep dimensional blacks, controlled highlight rolloff, precise practical "
            "lighting, soft directional sources, realistic low-light exposure, "
            "clean high-resolution digital texture, extremely fine detail, "
            "subtle cinematic grain, carefully separated planes, "
            "minimalist visual design, psychological tension, "
            "serious photographic realism"
        ),
        "negative_prompt": (
            "oversaturated colors, exaggerated teal and orange, glossy advertising, "
            "plastic skin, excessive HDR, artificial sharpening, excessive bloom, "
            "dreamy fantasy lighting, neon overload, crushed shadows, "
            "cartoon, anime, painterly rendering, synthetic CGI appearance"
        ),
        "denoise": 0.64,
        "structure_weight": 0.92,
        "color_boost": 0.60,
        "keywords": [
            "modern-digital",
            "large-format",
            "monochromatic",
            "cool-neutral",
            "precision",
            "low-light",
            "micro-detail",
            "prestige-cinema",
        ],
    },
}


__all__ = ["FINCHER_STYLES"]