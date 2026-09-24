"""
CharacterForge Cinematic - Coen Brothers
========================================

Preset cinematografici ispirati ai principali linguaggi visivi
associati ai fratelli Coen.

Focus:
- 35mm photochemical cinematography
- wide-angle compositions
- deep staging
- American noir and western photography
- winter daylight and snow
- tungsten interiors
- muted earth palettes
- strong graphic geometry
- controlled symmetrical framing
- atmospheric landscapes
- practical production design
- restrained optical effects
"""

COEN_STYLES = {

    "coen_noir": {
        "name": "Coen - American Noir",
        "category": "cinematic",
        "era": "1980s-1990s",
        "prompt": (
            "American noir cinematography on 35mm film, 28mm and 35mm wide-angle "
            "lenses, strong geometric composition, deep staging, low-key tungsten "
            "lighting, hard practical sources, venetian-blind shadows, smoky interiors, "
            "deep blacks with controlled shadow detail, muted brown, olive and cream "
            "palette, isolated saturated red accents, moderate depth of field, "
            "foreground objects framing characters, symmetrical and deliberately "
            "static compositions, subtle camera movement, organic film grain, "
            "slight photochemical softness, restrained halation, tactile wood, "
            "metal and fabric textures, dry observational atmosphere"
        ),
        "negative_prompt": (
            "modern digital noir, excessive teal and orange, glossy CGI, extreme "
            "bokeh, HDR, neon cyberpunk, soft beauty lighting, sterile environments, "
            "overly saturated colors, music-video aesthetic"
        ),
        "denoise": 0.57,
        "structure_weight": 0.84,
        "color_boost": 1.05,
        "keywords": [
            "American noir",
            "35mm",
            "28mm",
            "tungsten",
            "deep staging",
            "wood texture",
            "film grain",
            "graphic geometry"
        ],
    },

    "coen_fargo_winter": {
        "name": "Coen - Fargo Winter",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "1990s 35mm winter cinematography, enormous snow-covered landscapes, "
            "cold overcast daylight, pale blue-gray sky, muted white and beige palette, "
            "subtle warm tungsten interiors contrasting with icy exterior light, "
            "35mm and 50mm lenses, moderate depth of field, restrained perspective, "
            "wide static compositions, characters isolated inside vast white negative "
            "space, atmospheric snow and distant haze, soft directional daylight, "
            "controlled exposure preserving snow texture, organic fine film grain, "
            "slight photochemical softness, realistic skin tones, weathered winter "
            "clothing, practical vehicles and rural architecture, understated "
            "visual absurdity created through scale and composition"
        ),
        "negative_prompt": (
            "fantasy snow, blue fantasy lighting, excessive contrast, HDR, "
            "oversaturated winter colors, glossy digital photography, artificial "
            "snow, extreme bokeh, postcard landscape, cinematic teal and orange"
        ),
        "denoise": 0.55,
        "structure_weight": 0.83,
        "color_boost": 1.01,
        "keywords": [
            "winter",
            "snow",
            "overcast",
            "blue gray",
            "negative space",
            "35mm",
            "rural landscape",
            "fine grain"
        ],
    },

    "coen_western": {
        "name": "Coen - Western Landscape",
        "category": "cinematic",
        "era": "2000s-2010s",
        "prompt": (
            "epic American western cinematography on 35mm film, vast natural "
            "landscapes, 24mm and 35mm wide-angle lenses for environmental scale, "
            "50mm and longer lenses for compressed distant figures, harsh natural "
            "daylight, warm golden-hour backlight, deep blue skies, dusty atmospheric "
            "perspective, muted ochre and brown earth tones, restrained green, "
            "strong silhouettes, carefully balanced horizon lines, characters "
            "frequently dwarfed by terrain, moderate to deep depth of field, "
            "static contemplative compositions, organic film grain, subtle "
            "anamorphic-style flare, tactile dust and weathered materials, "
            "naturalistic skin tones, monumental but unsentimental landscape "
            "photography"
        ),
        "negative_prompt": (
            "fantasy western, excessive orange grading, HDR landscape, glossy "
            "digital photography, oversaturated sky, artificial haze, plastic "
            "textures, extreme bokeh, modern commercial travel photography"
        ),
        "denoise": 0.56,
        "structure_weight": 0.81,
        "color_boost": 1.08,
        "keywords": [
            "western",
            "35mm",
            "wide landscape",
            "golden hour",
            "dust",
            "deep blue sky",
            "silhouette",
            "natural light"
        ],
    },

    "coen_suburban_america": {
        "name": "Coen - Suburban Absurdity",
        "category": "cinematic",
        "era": "1990s-2000s",
        "prompt": (
            "suburban American cinematography photographed on 35mm film, ordinary "
            "houses, offices and parking lots transformed through precise composition, "
            "28mm and 35mm lenses, moderate depth of field, centered and symmetrical "
            "framing, static camera, flat winter daylight or soft overcast skies, "
            "warm tungsten interiors, muted beige, brown, olive and faded blue palette, "
            "small isolated saturated color accents, practical fluorescent lighting, "
            "deadpan visual geometry, carefully staged foreground and background "
            "details, realistic skin tones, organic film grain, subtle halation, "
            "tactile domestic textures, understated visual comedy produced by "
            "composition rather than exaggerated effects"
        ),
        "negative_prompt": (
            "sitcom lighting, glossy commercial photography, exaggerated comedy "
            "visuals, excessive color grading, extreme wide-angle distortion, "
            "modern LED lighting, HDR, shallow portrait bokeh, CGI"
        ),
        "denoise": 0.54,
        "structure_weight": 0.85,
        "color_boost": 1.03,
        "keywords": [
            "suburban America",
            "symmetry",
            "28mm",
            "fluorescent",
            "muted palette",
            "static camera",
            "deadpan",
            "35mm grain"
        ],
    },

    "coen_neo_western": {
        "name": "Coen - Neo Western Noir",
        "category": "cinematic",
        "era": "2000s-2010s",
        "prompt": (
            "dark neo-western cinematography on 35mm film, wide 24mm and 35mm lenses, "
            "long empty roads, desert and rural industrial environments, hard natural "
            "sunlight, deep evening shadows, isolated practical lights at night, "
            "strong backlight, dark silhouettes, muted earth colors, faded green, "
            "brown, charcoal and dusty yellow palette, occasional red accent, "
            "moderate depth of field, environmental compositions with large negative "
            "space, static framing contrasted with restrained tracking movement, "
            "organic film grain, subtle halation around headlights, realistic "
            "atmospheric haze, tactile asphalt, metal, dust and worn clothing, "
            "bleak but visually precise American landscape photography"
        ),
        "negative_prompt": (
            "glossy action movie, excessive orange and teal, cyberpunk, HDR, "
            "fantasy landscape, clean digital image, excessive bokeh, heroic "
            "blockbuster framing, plastic materials"
        ),
        "denoise": 0.59,
        "structure_weight": 0.82,
        "color_boost": 1.05,
        "keywords": [
            "neo western",
            "noir",
            "desert",
            "24mm",
            "negative space",
            "headlights",
            "dust",
            "35mm film"
        ],
    },
}

__all__ = ["COEN_STYLES"]
