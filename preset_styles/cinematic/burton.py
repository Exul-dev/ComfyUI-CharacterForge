"""
CharacterForge Cinematic - Tim Burton
=====================================

Preset cinematografici ispirati ai principali linguaggi visivi
associati alla filmografia di Tim Burton.

Focus:
- espressionismo gotico
- grandangoli e prospettive deformate
- silhouette e controluce
- bianco e nero / palette desaturate
- nebbia e atmospheric haze
- scenografie teatrali
- architettura verticale e contorta
- contrasto tra pallore dei personaggi e ambienti scuri
- texture analogica e fotografia fiabesca oscura
"""

BURTON_STYLES = {

    "burton_gothic": {
        "name": "Burton - Gothic Expressionism",
        "category": "cinematic",
        "era": "1980s-1990s",
        "prompt": (
            "gothic expressionist cinematography on 35mm film, 24mm and 28mm "
            "wide-angle lenses, exaggerated perspective, slightly tilted vertical "
            "lines, towering architecture, crooked buildings, deep theatrical "
            "staging, strong backlight, hard rim light, dense atmospheric fog, "
            "deep blacks, pale faces emerging from darkness, desaturated blue-gray "
            "and charcoal palette, isolated burgundy accents, moonlit exteriors, "
            "cold tungsten interiors, moderate depth of field, dramatic silhouettes, "
            "organic 35mm grain, subtle halation, restrained optical softness, "
            "painted production design, twisted trees, pointed architecture, "
            "fairy-tale darkness and highly controlled graphic composition"
        ),
        "negative_prompt": (
            "clean modern digital cinema, realistic contemporary architecture, "
            "flat lighting, HDR, glossy CGI, excessive teal and orange, naturalistic "
            "documentary photography, generic horror, excessive bokeh"
        ),
        "denoise": 0.61,
        "structure_weight": 0.86,
        "color_boost": 1.03,
        "keywords": [
            "gothic",
            "expressionism",
            "24mm wide angle",
            "crooked architecture",
            "fog",
            "silhouette",
            "pale skin",
            "35mm grain"
        ],
    },

    "burton_biopunk": {
        "name": "Burton - Dark Fairytale",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "dark fairy-tale cinematography photographed on 35mm film, highly "
            "stylized production design, 28mm and 35mm lenses, exaggerated "
            "perspective, theatrical sets, deep layered staging, pale moonlight, "
            "cold blue-gray ambient light, warm isolated candle and tungsten "
            "sources, soft atmospheric haze, strong backlight, long silhouettes, "
            "desaturated black, gray, blue and brown palette, selective crimson "
            "details, shallow-to-moderate depth of field, textured costumes, "
            "weathered wood, stone and fabric, organic film grain, gentle bloom "
            "around practical lights, slightly imperfect photochemical softness, "
            "storybook atmosphere with macabre visual geometry"
        ),
        "negative_prompt": (
            "bright children's fantasy, glossy CGI, modern digital sharpness, "
            "pastel fantasy, realistic contemporary production design, HDR, "
            "clean studio lighting, excessive saturation, generic horror"
        ),
        "denoise": 0.59,
        "structure_weight": 0.83,
        "color_boost": 1.07,
        "keywords": [
            "dark fairytale",
            "35mm",
            "moonlight",
            "candlelight",
            "desaturated",
            "storybook",
            "macabre",
            "organic grain"
        ],
    },

    "burton_black_white": {
        "name": "Burton - Monochrome",
        "category": "cinematic",
        "era": "1980s-2000s",
        "prompt": (
            "high-contrast black and white 35mm cinematography, expressionist "
            "lighting, deep blacks and luminous pale highlights, 24mm and 35mm "
            "wide-angle lenses, dramatic low angles, exaggerated vertical "
            "perspective, hard key lighting, strong backlight, theatrical shadows, "
            "dense fog and atmospheric diffusion, silhouettes against bright skies, "
            "moderate depth of field, layered production design, crooked trees and "
            "architectural forms, visible organic film grain, silver-rich tonal "
            "response, subtle halation, tactile photochemical texture, graphic "
            "composition, stark separation between character and environment"
        ),
        "negative_prompt": (
            "flat grayscale, low contrast, clean digital monochrome, HDR, "
            "soft beauty lighting, modern minimalist architecture, excessive "
            "bokeh, colorful image, glossy CGI"
        ),
        "denoise": 0.58,
        "structure_weight": 0.88,
        "color_boost": 0.90,
        "keywords": [
            "black and white",
            "high contrast",
            "expressionist",
            "24mm",
            "hard light",
            "fog",
            "silhouette",
            "silver grain"
        ],
    },

    "burton_suburban": {
        "name": "Burton - Suburban Gothic",
        "category": "cinematic",
        "era": "1980s-1990s",
        "prompt": (
            "stylized suburban gothic cinematography on 35mm film, symmetrical "
            "American suburb architecture transformed into uncanny visual geometry, "
            "28mm wide-angle lens, slightly exaggerated perspective, pastel houses "
            "and manicured lawns contrasted with dark clothing and pale characters, "
            "bright overcast daylight, controlled soft shadows, isolated hard "
            "backlight, muted pastel palette with black, white and red accents, "
            "moderate depth of field, centered compositions, theatrical blocking, "
            "organic film grain, subtle photochemical softness, carefully designed "
            "production details, visual repetition, strange stillness and surreal "
            "domestic atmosphere"
        ),
        "negative_prompt": (
            "realistic suburban documentary, generic horror, modern digital image, "
            "HDR, excessive darkness, random messy composition, extreme lens "
            "distortion, glossy commercial photography"
        ),
        "denoise": 0.55,
        "structure_weight": 0.85,
        "color_boost": 1.08,
        "keywords": [
            "suburban gothic",
            "28mm",
            "pastel houses",
            "symmetry",
            "pale characters",
            "overcast",
            "35mm grain",
            "uncanny suburbia"
        ],
    },

    "burton_carnival": {
        "name": "Burton - Macabre Carnival",
        "category": "cinematic",
        "era": "1990s-2000s",
        "prompt": (
            "macabre carnival cinematography on 35mm film, exaggerated wide-angle "
            "perspective, 24mm and 28mm lenses, swirling theatrical production design, "
            "deep layered compositions, saturated crimson, dirty yellow, faded blue "
            "and black palette, practical bulbs and carnival lights, strong backlight "
            "through smoke and fog, colored gels, hard spotlights, dramatic silhouettes, "
            "selective shallow depth of field, visible atmosphere, reflective wet "
            "surfaces, painted scenery, distressed textures, organic film grain, "
            "subtle halation around practical bulbs, controlled lens flare, "
            "expressionist camera angles, whimsical darkness and deliberately "
            "artificial theatrical realism"
        ),
        "negative_prompt": (
            "clean amusement park photography, modern LED carnival, generic circus, "
            "photoreal commercial image, HDR, excessive neon, cyberpunk, flat "
            "composition, sterile production design, plastic CGI"
        ),
        "denoise": 0.63,
        "structure_weight": 0.82,
        "color_boost": 1.17,
        "keywords": [
            "macabre carnival",
            "24mm",
            "colored gels",
            "practical bulbs",
            "fog",
            "crimson",
            "expressionist",
            "film grain"
        ],
    },
}

__all__ = ["BURTON_STYLES"]
