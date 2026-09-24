"""
CharacterForge Cinematic - David Lynch
======================================

Preset cinematografici ispirati ai principali linguaggi visivi
associati alla filmografia di David Lynch.

Focus:
- fotografia low-key e contrastata
- tungsteno e practical lighting
- neri profondi e colori primari saturi
- blu/ciano notturni
- profondità di campo selettiva
- grandangoli e prospettive leggermente deformate
- atmosfera onirica, inquietante e sospesa
- texture analogica, haze, fumo e bloom controllato
- composizioni geometriche e spazi apparentemente ordinari
  trasformati in ambienti stranianti
"""

LYNCH_STYLES = {

    "lynch_blue_velvet": {
        "name": "Lynch - Blue Velvet",
        "category": "cinematic",
        "era": "1980s",
        "prompt": (
            "cinematic 35mm film photography, Lynch-inspired suburban noir, "
            "ordinary American suburbia rendered uncanny, deep saturated blues, "
            "rich cobalt night tones, isolated red practical lights, warm tungsten "
            "interiors against cool exterior darkness, low-key lighting, strong "
            "contrast, deep blacks with controlled shadow detail, selective shallow "
            "depth of field, 35mm and 50mm spherical lenses, slightly compressed "
            "perspective, carefully framed static compositions, symmetrical suburban "
            "geometry, foreground objects used as visual anchors, subtle atmospheric "
            "haze, restrained halation around practical lights, organic 1980s 35mm "
            "film grain, tactile production design, polished surfaces contrasted "
            "with decaying textures, unsettling stillness, beautiful but disturbing "
            "photographic atmosphere"
        ),
        "negative_prompt": (
            "clean digital photography, modern LED lighting, flat exposure, "
            "washed colors, excessive HDR, plastic skin, sterile environment, "
            "generic horror lighting, excessive gore, excessive dutch angles, "
            "over-sharpening, excessive bokeh, futuristic production design"
        ),
        "denoise": 0.58,
        "structure_weight": 0.78,
        "color_boost": 1.12,
        "keywords": [
            "suburban noir",
            "deep blue",
            "tungsten practicals",
            "35mm film",
            "low key",
            "uncanny suburbia",
            "analog grain",
            "static composition"
        ],
    },

    "lynch_lost_highway": {
        "name": "Lynch - Lost Highway",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "dark 35mm neo-noir cinematography, Lynch-inspired psychological "
            "nightmare, almost-black interiors, dense shadows swallowing parts of "
            "the frame, violent pools of tungsten light, cold blue-black exterior "
            "night, practical lamps and isolated headlights, high contrast exposure, "
            "deep blacks, selective highlights, wide 28mm and 35mm lenses creating "
            "subtle spatial unease, occasional longer lens compression, shallow to "
            "moderate depth of field, characters isolated inside large negative "
            "spaces, corridors and rooms extending into darkness, asymmetrical "
            "framing, reflections and mirrors, smoke and atmospheric diffusion, "
            "controlled halation, coarse organic 1990s film grain, slightly muted "
            "skin tones against saturated red and blue accents, tactile analog "
            "texture, nocturnal psychological tension"
        ),
        "negative_prompt": (
            "bright modern digital image, evenly lit room, cheerful palette, "
            "clean commercial photography, excessive neon, cyberpunk aesthetic, "
            "perfectly sharp digital detail, HDR, glossy CGI, oversaturated skin, "
            "soft romantic lighting, daylight dominant scene"
        ),
        "denoise": 0.61,
        "structure_weight": 0.80,
        "color_boost": 1.08,
        "keywords": [
            "neo noir",
            "black interiors",
            "blue-black night",
            "tungsten pools",
            "28mm lens",
            "negative space",
            "mirrors",
            "1990s grain"
        ],
    },

    "lynch_twin_peaks": {
        "name": "Lynch - Twin Peaks",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "cinematic 35mm television photography with Lynch-inspired surreal "
            "Pacific Northwest atmosphere, misty forests, wet roads and small-town "
            "interiors, cool overcast daylight mixed with warm tungsten practicals, "
            "rich forest greens, muted browns, deep reds and electric blue accents, "
            "soft diffused exterior light, controlled low-key interiors, moderate "
            "depth of field, 35mm and 50mm spherical lenses, carefully layered "
            "foreground middle ground and background, centered compositions mixed "
            "with slightly uncanny framing, curtains, wood paneling, diner interiors "
            "and reflective surfaces, subtle haze, wet-surface reflections, gentle "
            "lens bloom, organic 1990s film grain, naturalistic skin rendering, "
            "quiet small-town realism disrupted by surreal color and atmosphere"
        ),
        "negative_prompt": (
            "modern digital television look, sterile interiors, excessive teal and "
            "orange, blockbuster contrast, futuristic city, hard studio lighting, "
            "flat backgrounds, excessive shallow depth of field, hyperreal CGI, "
            "clean clinical surfaces, excessive saturation"
        ),
        "denoise": 0.56,
        "structure_weight": 0.76,
        "color_boost": 1.10,
        "keywords": [
            "Pacific Northwest",
            "mist",
            "forest green",
            "warm practicals",
            "red accents",
            "wood interiors",
            "wet roads",
            "1990s television film"
        ],
    },

    "lynch_surreal_noir": {
        "name": "Lynch - Surreal Noir",
        "category": "cinematic",
        "era": "1990s-2000s",
        "prompt": (
            "surreal noir cinematography on photochemical film, oppressive low-key "
            "lighting, deep black negative space, isolated pools of light, saturated "
            "red curtains and blue practicals, hard backlight cutting through smoke, "
            "fog and atmospheric haze, 24mm to 35mm wide-angle lenses close to the "
            "subject, subtle barrel distortion and exaggerated foreground scale, "
            "shallow-to-moderate depth of field, unusual camera height, characters "
            "placed against architectural voids, reflections, mirrors and glossy "
            "surfaces, geometric corridors, long empty rooms, controlled perspective "
            "distortion, strong separation between warm and cool light sources, "
            "organic film grain, restrained halation, slight gate-weave feeling, "
            "uncomfortable stillness, dream logic translated into concrete "
            "photographic language"
        ),
        "negative_prompt": (
            "generic horror movie, extreme dutch angle, action photography, "
            "clean digital sharpness, excessive lens distortion, fisheye extreme, "
            "flat lighting, bright commercial colors, generic cyberpunk, CGI look, "
            "excessive fog hiding all details"
        ),
        "denoise": 0.63,
        "structure_weight": 0.82,
        "color_boost": 1.16,
        "keywords": [
            "surreal noir",
            "red curtains",
            "blue practicals",
            "wide angle",
            "negative space",
            "hard backlight",
            "smoke haze",
            "photochemical grain"
        ],
    },

    "lynch_dream_reality": {
        "name": "Lynch - Dream Reality",
        "category": "cinematic",
        "era": "2000s-2010s",
        "prompt": (
            "cinematic dream-reality photography, ordinary locations photographed "
            "with subtly impossible atmosphere, naturalistic compositions disrupted "
            "by uncanny lighting, soft daylight mixed with isolated artificial "
            "practicals, cool cyan shadows and warm amber highlights, deep tonal "
            "separation, controlled black levels, 35mm and 50mm lenses with selective "
            "focus, occasional 85mm compression for psychological isolation, moderate "
            "depth of field, faces emerging from darkness, large areas of negative "
            "space, reflections and layered glass, curtains, doorways and thresholds "
            "used as compositional frames, restrained camera movement, atmospheric "
            "diffusion, subtle bloom, organic film grain, slightly imperfect analog "
            "texture, realistic skin with dreamlike tonal rendering, visual ambiguity "
            "between mundane reality and subconscious space"
        ),
        "negative_prompt": (
            "generic fantasy, obvious dream effects, glowing fantasy aura, clean "
            "digital commercial image, excessive bloom, excessive bokeh, pastel "
            "dreamcore, glossy CGI, surreal objects everywhere, cartoon appearance, "
            "flat cinematic lighting"
        ),
        "denoise": 0.60,
        "structure_weight": 0.79,
        "color_boost": 1.09,
        "keywords": [
            "dream reality",
            "cyan shadows",
            "amber highlights",
            "threshold framing",
            "reflections",
            "35mm film",
            "selective focus",
            "analog atmosphere"
        ],
    },
}

__all__ = ["LYNCH_STYLES"]
