"""
CharacterForge Cinematic - James Cameron
========================================

Cinematic presets focused on photographic language:
- large-scale composition
- practical and motivated lighting
- wide-angle perspective
- industrial and technological environments
- atmospheric depth
- physical materials and textures
- analog film rendering and period-specific photography
"""

CAMERON_STYLES = {

    "cameron_1980s": {
        "name": "Cameron - 1980s Action",
        "category": "cinematic",
        "era": "1980s",
        "prompt": (
            "1980s 35mm action cinematography, hard practical lighting, "
            "high-contrast photochemical image, deep blacks with preserved shadow "
            "detail, tungsten interiors, cold blue night exteriors, strong backlight, "
            "industrial environments, wet concrete and brushed metal, smoke and "
            "atmospheric haze, 24mm and 28mm wide-angle spherical lenses, moderate "
            "depth of field, strong foreground perspective, low camera positions, "
            "dynamic but controlled compositions, practical light sources visible "
            "inside the frame, physically motivated highlights, sweat and water "
            "texture on skin, coarse organic 1980s 35mm grain, restrained halation, "
            "subtle film softness, tactile production design, muscular visual "
            "geometry, grounded practical-effects aesthetic"
        ),
        "negative_prompt": (
            "modern digital cinema, clean HDR, excessive teal and orange, "
            "plastic CGI surfaces, weightless environments, soft fashion lighting, "
            "excessive shallow depth of field, futuristic glossy production design, "
            "overly clean blacks, video-game rendering"
        ),
        "denoise": 0.59,
        "structure_weight": 0.81,
        "color_boost": 1.08,
        "keywords": [
            "1980s 35mm",
            "hard practical light",
            "industrial",
            "blue night",
            "tungsten",
            "24mm wide angle",
            "smoke",
            "practical effects"
        ],
    },

    "cameron_tech_noir": {
        "name": "Cameron - Tech Noir",
        "category": "cinematic",
        "era": "1980s",
        "prompt": (
            "dark 35mm tech-noir cinematography, urban night photography, wet "
            "streets reflecting sodium vapor and blue practical lights, hard side "
            "lighting, strong backlights, deep blacks, controlled highlights, "
            "high local contrast, 24mm and 35mm lenses, moderate depth of field "
            "with environmental context retained, low-angle compositions, "
            "architectural perspective, characters framed against machinery and "
            "urban infrastructure, rain, smoke and steam creating volumetric layers, "
            "visible practical sources, physically motivated exposure, coarse "
            "photochemical grain, subtle halation around street lamps, slightly "
            "cool cyan shadows against dirty amber highlights, gritty urban texture, "
            "mechanical details rendered with tactile realism, relentless nocturnal "
            "atmosphere"
        ),
        "negative_prompt": (
            "clean cyberpunk neon, modern LED colors, glossy futuristic city, "
            "soft beauty lighting, excessive magenta, excessive bloom, digital "
            "noise, HDR, weightless CGI, perfectly clean streets, shallow portrait "
            "photography"
        ),
        "denoise": 0.62,
        "structure_weight": 0.83,
        "color_boost": 1.11,
        "keywords": [
            "tech noir",
            "wet streets",
            "sodium vapor",
            "blue practicals",
            "rain",
            "steam",
            "35mm grain",
            "urban machinery"
        ],
    },

    "cameron_military_scifi": {
        "name": "Cameron - Military Sci-Fi",
        "category": "cinematic",
        "era": "1980s",
        "prompt": (
            "1980s military science-fiction cinematography, practical industrial "
            "production design, claustrophobic corridors and machinery, fluorescent "
            "overhead lighting mixed with hard directional sources, cold green-blue "
            "ambient shadows, warm tungsten work lights, dense atmospheric haze, "
            "24mm and 32mm wide-angle lenses, deep focus where environmental "
            "geography matters, moderate depth of field for human subjects, strong "
            "leading lines, layered compositions, low and eye-level camera positions, "
            "controlled handheld energy, practical smoke, metallic surfaces, worn "
            "equipment, condensation and grime, high micro-contrast without digital "
            "sharpness, organic 35mm grain, slight halation around bright practicals, "
            "physically believable exposure, utilitarian visual design"
        ),
        "negative_prompt": (
            "clean futuristic showroom, glossy spaceship, modern LED lighting, "
            "weightless CGI, excessive neon, fantasy armor, excessive depth blur, "
            "plastic materials, sterile surfaces, modern digital sharpness, "
            "overly stylized color grading"
        ),
        "denoise": 0.58,
        "structure_weight": 0.86,
        "color_boost": 1.07,
        "keywords": [
            "military sci-fi",
            "industrial corridors",
            "fluorescent",
            "wide angle",
            "deep focus",
            "practical smoke",
            "worn metal",
            "35mm"
        ],
    },

    "cameron_epic": {
        "name": "Cameron - Epic Romance",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "epic 1990s 35mm romantic historical cinematography, large-scale "
            "production design, elegant period interiors, warm tungsten and candle "
            "light, cool moonlit exterior tones, soft but directional key lighting, "
            "controlled backlight separating subjects from ornate environments, "
            "35mm and 50mm spherical lenses, occasional 75mm to 100mm compression "
            "for intimate emotional moments, moderate depth of field preserving "
            "environmental context, carefully balanced symmetrical compositions, "
            "layered foreground and background staging, luminous skin tones, "
            "controlled highlight rolloff, subtle diffusion, restrained halation, "
            "fine organic 35mm film grain, rich navy, burgundy and gold palette, "
            "water reflections, atmospheric depth, practical candle and lamp sources, "
            "grand visual scale combined with intimate human framing"
        ),
        "negative_prompt": (
            "modern digital blockbuster look, excessive teal and orange, plastic "
            "skin, extreme bokeh, flat lighting, sterile period interiors, "
            "over-sharpening, HDR, excessive saturation, fantasy lighting, CGI sheen"
        ),
        "denoise": 0.55,
        "structure_weight": 0.79,
        "color_boost": 1.12,
        "keywords": [
            "1990s 35mm",
            "period epic",
            "candlelight",
            "warm tungsten",
            "moonlight",
            "gold and burgundy",
            "layered staging",
            "fine grain"
        ],
    },

    "cameron_immersive": {
        "name": "Cameron - Immersive World",
        "category": "cinematic",
        "era": "2000s-2010s",
        "prompt": (
            "immersive large-scale digital cinema, environmental world building, "
            "physically motivated volumetric lighting, enormous foreground-to-"
            "background depth, wide 18mm to 24mm cinematic lenses, deep environmental "
            "focus, strong spatial continuity, characters integrated naturally into "
            "vast landscapes, atmospheric perspective, dense foliage and environmental "
            "texture, shafts of light through mist, water and airborne particles "
            "catching illumination, cool cyan shadows balanced with warm organic "
            "highlights, controlled saturation, realistic skin rendering, subtle "
            "lens flare, smooth highlight rolloff, clean but cinematic digital "
            "capture, precise edge detail combined with cinematic softness, dynamic "
            "camera perspective, strong vertical and diagonal composition, immersive "
            "scale, tactile environmental realism"
        ),
        "negative_prompt": (
            "flat digital illustration, generic fantasy art, excessive neon, "
            "plastic CGI, oversaturated colors, cartoon rendering, fake depth of "
            "field, miniature appearance, excessive sharpening, chromatic artifacts, "
            "uniform lighting, flat backgrounds"
        ),
        "denoise": 0.57,
        "structure_weight": 0.84,
        "color_boost": 1.15,
        "keywords": [
            "immersive world",
            "18mm wide angle",
            "volumetric light",
            "atmospheric perspective",
            "environmental depth",
            "cyan shadows",
            "organic highlights",
            "digital cinema"
        ],
    },
}

__all__ = ["CAMERON_STYLES"]
