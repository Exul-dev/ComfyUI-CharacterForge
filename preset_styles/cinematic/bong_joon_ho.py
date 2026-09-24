"""
CharacterForge Cinematic - Bong Joon-ho
=======================================

Visual language inspired by Bong Joon-ho's cinema:
architectural compositions, layered staging, precise tracking shots,
wide-angle environmental photography, vertical spatial relationships,
natural and practical lighting, controlled color palettes and
genre transitions expressed through camera language and production design.
"""

BONG_JOON_HO_STYLES = {

    "bong_joon_ho_memories": {
        "name": "Bong Korean Crime",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "2000s Korean crime-drama cinematography, 35mm spherical lenses, "
            "28mm and 35mm environmental perspectives, precise tracking shots, "
            "controlled handheld movement, layered compositions with multiple characters, "
            "dense rural and suburban environments, natural overcast daylight, "
            "practical fluorescent interiors, sodium-vapor streetlights, "
            "muted green, gray, brown and faded yellow palette, "
            "subtle warm skin tones against cool surroundings, "
            "fine 35mm film grain, realistic optical texture, moderate depth of field, "
            "long lateral camera movements, carefully composed foreground objects, "
            "wet roads, concrete, vegetation and weathered architecture, "
            "quiet tension with sudden visual intensity"
        ),
        "negative_prompt": (
            "glossy Hollywood crime thriller, excessive teal and orange, "
            "neon cyberpunk, generic shallow depth of field, HDR, "
            "plastic skin, excessive handheld chaos, sterile environments"
        ),
        "denoise": 0.48,
        "structure_weight": 0.88,
        "color_boost": 0.82,
        "keywords": [
            "Korean crime",
            "35mm",
            "28mm",
            "tracking",
            "overcast",
            "fluorescent",
            "layered composition",
            "film grain"
        ],
    },

    "bong_joon_ho_vertical_space": {
        "name": "Bong Vertical Space",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "architectural social drama cinematography, 24mm and 28mm wide-angle lenses, "
            "strong vertical compositions, stairs, corridors, basements, elevated rooms "
            "and multi-level architecture, characters arranged at different heights, "
            "deep spatial staging, precise lateral tracking shots, controlled dolly movement, "
            "symmetrical and geometric framing, practical interior lighting, "
            "cool fluorescent sources contrasted with warm household lamps, "
            "muted gray, beige, green and brown palette, selective warm highlights, "
            "fine cinematic grain, realistic skin texture, moderate depth of field, "
            "strong environmental context, production design used as narrative structure, "
            "visual separation between social spaces through architecture and elevation"
        ),
        "negative_prompt": (
            "flat staging, empty backgrounds, excessive bokeh, glossy luxury photography, "
            "neon lighting, artificial CGI architecture, extreme fisheye distortion, "
            "HDR, plastic surfaces"
        ),
        "denoise": 0.49,
        "structure_weight": 0.93,
        "color_boost": 0.80,
        "keywords": [
            "architecture",
            "vertical space",
            "24mm",
            "28mm",
            "stairs",
            "basement",
            "tracking shot",
            "social space"
        ],
    },

    "bong_joon_ho_parasite": {
        "name": "Bong Controlled Thriller",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "precisely controlled contemporary Korean thriller cinematography, "
            "24mm, 35mm and 50mm lenses, symmetrical architectural compositions, "
            "deep focus environmental staging, smooth dolly and tracking shots, "
            "carefully choreographed blocking, modern interiors contrasted with cramped spaces, "
            "soft daylight through large windows, practical tungsten and fluorescent illumination, "
            "cool gray, muted green, cream and warm amber palette, "
            "controlled contrast, realistic skin tones, subtle filmic grain, "
            "clean but organic optical rendering, reflections through glass, "
            "stairs and corridors used as compositional lines, restrained camera movement, "
            "dark humor and suspense conveyed through spatial precision"
        ),
        "negative_prompt": (
            "generic thriller aesthetics, handheld action camera, excessive shallow focus, "
            "neon cyberpunk, oversaturated color grading, glossy commercial interiors, "
            "digital HDR, extreme lens distortion"
        ),
        "denoise": 0.46,
        "structure_weight": 0.94,
        "color_boost": 0.86,
        "keywords": [
            "controlled thriller",
            "24mm",
            "35mm",
            "50mm",
            "symmetry",
            "deep focus",
            "glass",
            "architecture"
        ],
    },

    "bong_joon_ho_snow": {
        "name": "Bong Snowy Dystopia",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "stylized dystopian cinematography grounded in photographic realism, "
            "wide 24mm and 28mm lenses, long corridors and enclosed industrial spaces, "
            "strong leading lines, controlled symmetrical compositions, "
            "cold blue-gray ambient light, fluorescent practicals, harsh white sources, "
            "selective warm amber and red accents, snow and condensation, "
            "metal, glass, concrete and worn industrial textures, "
            "moderate depth of field, precise tracking camera, smooth lateral movement, "
            "subtle atmospheric haze, controlled contrast, realistic skin tones, "
            "fine cinematic grain, restrained highlight bloom, "
            "large-scale production design with dense environmental detail"
        ),
        "negative_prompt": (
            "fantasy CGI, generic cyberpunk, neon overload, clean futuristic surfaces, "
            "plastic environments, excessive bloom, oversaturated colors, "
            "game-engine rendering, chaotic camera movement"
        ),
        "denoise": 0.50,
        "structure_weight": 0.90,
        "color_boost": 0.84,
        "keywords": [
            "dystopian",
            "snow",
            "24mm",
            "28mm",
            "industrial",
            "blue gray",
            "tracking",
            "production design"
        ],
    },

    "bong_joon_ho_dark_comedy": {
        "name": "Bong Dark Comedy",
        "category": "cinematic",
        "era": "2000s-2020s",
        "prompt": (
            "darkly comic Korean cinematic realism, 35mm and 40mm lenses, "
            "wide environmental framing, carefully timed camera movement, "
            "characters placed within detailed ordinary environments, "
            "slightly exaggerated but believable architectural geometry, "
            "soft overcast daylight, practical fluorescent interiors, "
            "warm household lamps, restrained muted palette with selective saturated accents, "
            "natural skin tones, subtle 35mm film grain, moderate depth of field, "
            "precise blocking, lateral tracking shots, static observational frames, "
            "foreground objects creating visual irony, cluttered domestic and urban textures, "
            "comic situations filmed with serious photographic discipline"
        ),
        "negative_prompt": (
            "sitcom lighting, cartoon composition, broad slapstick photography, "
            "glossy commercial look, excessive saturation, fake film scratches, "
            "generic shallow bokeh, sterile environments"
        ),
        "denoise": 0.45,
        "structure_weight": 0.87,
        "color_boost": 0.84,
        "keywords": [
            "dark comedy",
            "35mm",
            "40mm",
            "Korean cinema",
            "observational",
            "blocking",
            "tracking",
            "domestic realism"
        ],
    },
}

__all__ = ["BONG_JOON_HO_STYLES"]
