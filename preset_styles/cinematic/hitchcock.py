"""
CharacterForge Cinematic — Alfred Hitchcock
===========================================

Preset cinematografici ispirati alla fotografia e alla grammatica visiva
associata alle diverse fasi della carriera di Alfred Hitchcock.

IMPORTANTE:
Questi preset NON applicano automaticamente LoRA.
Definiscono una direzione fotografica, luministica, compositiva
e materica per il motore CharacterForge.
"""

HITCHCOCK_STYLES = {

# ================================================================
# HITCHCOCK — ANNI 1950
# ================================================================

"hitchcock_1950s": {
    "name": "Alfred Hitchcock — 1950s",
    "description": (
        "Cinema thriller classico degli anni '50: fotografia controllata, "
        "composizioni geometriche, tensione psicologica, illuminazione "
        "espressiva e resa fotografica analogica raffinata."
    ),

    "category": "cinematic",
    "director": "Alfred Hitchcock",
    "era": "1950s",
    "decade": 1950,
    "medium": "35mm color film",

    "prompt": (
        "1950s Alfred Hitchcock inspired cinematic photography, "
        "classic Hollywood thriller visual language, "
        "precise geometric composition, carefully controlled framing, "
        "psychological visual tension, elegant 35mm color film, "
        "classical three point lighting, controlled studio key light, "
        "subtle fill light, deep but readable shadows, "
        "moderate cinematic contrast, restrained highlights, "
        "natural human skin texture, visible pores, subtle facial lines, "
        "realistic under-eye texture, natural vellus hair, "
        "slightly imperfect skin tone, authentic period makeup, "
        "carefully shaped faces, expressive eyes, "
        "vintage spherical prime lenses, moderate depth of field, "
        "optical softness at the edges, natural film halation, "
        "fine organic 35mm grain, restrained warm color response, "
        "slightly muted reds and greens, elegant neutral skin tones, "
        "period-accurate wardrobe and production design, "
        "controlled camera placement, deliberate perspective, "
        "suspenseful atmosphere, visual storytelling, "
        "classic Hollywood production photography"
    ),

    "negative_prompt": (
        "plastic skin, beauty filter, skin smoothing, airbrushed skin, "
        "pore removal, artificial facial symmetry, CGI skin, "
        "modern digital sharpness, excessive HDR, oversaturated colors, "
        "teal and orange grading, modern blockbuster lighting, "
        "neon lighting, excessive bloom, excessive lens flare, "
        "heavy chromatic aberration, excessive depth of field blur, "
        "hyperreal digital photography, waxy skin, porcelain skin, "
        "perfect skin, excessive sharpening, modern fashion, "
        "modern cinematic color grading"
    ),

    "skin_profile": "studio_1950",
    "lighting_profile": "studio_classic",
    "lens_profile": "spherical_classic",
    "film_stock": "kodachrome",
    "grain_profile": "fine",
    "color_profile": "warm_classic",
    "atmosphere_profile": "smoky_city",
    "camera_profile": "new_hollywood",

    "aspect_ratio": "1.66:1",
    "camera_movement": "deliberate controlled movement",
    "depth_of_field": "moderate",
    "contrast": "medium-high",
    "saturation": "moderate",
    "highlight_rolloff": "soft",
    "black_level": "deep but detailed",

    "denoise": 0.28,
    "structure_weight": 0.88,
    "color_boost": 1.05,

    "keywords": [
        "Hitchcock",
        "1950s",
        "classic Hollywood",
        "psychological thriller",
        "35mm",
        "studio photography",
        "suspense",
        "geometric composition",
        "controlled lighting",
        "analog film",
        "classic color"
    ],

    "negative_keywords": [
        "digital look",
        "plastic skin",
        "beauty retouching",
        "modern grading",
        "HDR",
        "neon",
        "teal orange"
    ],

    "recommended_loras": [],

    "compatible_combinations": [
        "cinematic_noir",
        "classic_thriller",
        "1950s_hollywood",
        "vintage_35mm"
    ],

    "inspiration": [
        "Rear Window (1954)",
        "Vertigo (1958)",
        "North by Northwest (1959)"
    ]
},


# ================================================================
# HITCHCOCK — ANNI 1960
# ================================================================

"hitchcock_1960s": {
    "name": "Alfred Hitchcock — 1960s",
    "description": (
        "Thriller psicologico degli anni '60 con fotografia più "
        "contrastata, composizione grafica, atmosfera inquietante, "
        "ombre più profonde e una resa cromatica più drammatica."
    ),

    "category": "cinematic",
    "director": "Alfred Hitchcock",
    "era": "1960s",
    "decade": 1960,
    "medium": "35mm film",

    "prompt": (
        "1960s Alfred Hitchcock inspired cinematic photography, "
        "psychological thriller atmosphere, mature suspense cinema, "
        "graphic visual composition, precise framing, "
        "strong architectural geometry, unsettling negative space, "
        "dramatic 35mm photographic texture, "
        "controlled directional lighting, harder key light, "
        "deeper shadows, restrained fill, "
        "high but controlled contrast, "
        "natural human skin with visible pores and micro texture, "
        "subtle wrinkles, realistic under-eye shadows, "
        "natural facial asymmetry, small skin imperfections, "
        "realistic facial hair, authentic period makeup, "
        "vintage spherical cinema lenses, "
        "moderate optical softness, subtle halation, "
        "organic film grain, slightly desaturated cinematic color, "
        "cooler shadow separation, restrained warm highlights, "
        "natural skin response to hard directional light, "
        "ominous atmosphere, psychological tension, "
        "deliberate camera placement, "
        "strong foreground and background relationships, "
        "controlled perspective, cinematic suspense, "
        "1960s production design and wardrobe"
    ),

    "negative_prompt": (
        "plastic skin, wax skin, porcelain skin, beauty filter, "
        "airbrushing, skin smoothing, pore removal, "
        "perfect facial symmetry, CGI appearance, "
        "modern digital sharpness, excessive HDR, "
        "teal and orange blockbuster grading, "
        "oversaturated colors, neon cyberpunk lighting, "
        "excessive bloom, excessive lens flare, "
        "modern commercial beauty photography, "
        "excessive bokeh, artificial depth of field, "
        "digital noise, excessive sharpening, "
        "modern fashion, modern production design"
    ),

    "skin_profile": "natural_1960",
    "lighting_profile": "low_key",
    "lens_profile": "vintage_prime",
    "film_stock": "eastmancolor",
    "grain_profile": "medium",
    "color_profile": "desaturated",
    "atmosphere_profile": "smoky_city",
    "camera_profile": "kubrick_symmetry",

    "aspect_ratio": "1.85:1",
    "camera_movement": "precise restrained movement",
    "depth_of_field": "moderate-shallow",
    "contrast": "high",
    "saturation": "moderate-low",
    "highlight_rolloff": "controlled",
    "black_level": "deep",

    "denoise": 0.30,
    "structure_weight": 0.87,
    "color_boost": 1.00,

    "keywords": [
        "Hitchcock",
        "1960s",
        "psychological thriller",
        "35mm",
        "graphic composition",
        "negative space",
        "low key lighting",
        "deep shadows",
        "film grain",
        "psychological tension",
        "vintage cinema"
    ],

    "negative_keywords": [
        "plastic skin",
        "digital photography",
        "beauty retouching",
        "HDR",
        "modern blockbuster",
        "neon",
        "oversaturation"
    ],

    "recommended_loras": [],

    "compatible_combinations": [
        "cinematic_noir",
        "psychological_thriller",
        "1960s_film",
        "vintage_35mm"
    ],

    "inspiration": [
        "Psycho (1960)",
        "The Birds (1963)",
        "Marnie (1964)"
    ]
}

}
__all__ = [
"HITCHCOCK_STYLES",
]

