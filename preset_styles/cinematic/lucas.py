"""
CharacterForge Cinematic - George Lucas
=======================================

Preset cinematografici ispirati ai principali linguaggi visivi
associati alla filmografia di George Lucas e alla tradizione
cinematografica sviluppata attorno alle sue produzioni.

Focus:
- 35mm photochemical cinematography
- anamorphic perspective
- strong backlight and silhouettes
- practical lighting
- desert and natural landscapes
- smoke, haze and atmospheric depth
- large-scale adventure composition
- mechanical production design
- blue/orange/red color separation
- matte-painting and miniature-era visual language
- transition from photochemical to digital-era photography
"""

LUCAS_STYLES = {

    "lucas_classic_adventure": {
        "name": "Lucas - Classic Adventure",
        "category": "cinematic",
        "era": "1970s-1980s",
        "prompt": (
            "classic 35mm adventure cinematography, 1970s photochemical film "
            "rendering, anamorphic spherical perspective, warm natural sunlight, "
            "strong backlight, pronounced rim light around characters, atmospheric "
            "dust and haze, practical tungsten interiors, deep environmental staging, "
            "24mm and 35mm wide-angle lenses, moderate depth of field, layered "
            "foreground middle ground and background, dynamic diagonal compositions, "
            "heroic silhouettes, tactile physical production design, weathered metal, "
            "painted surfaces, practical props, organic 35mm grain, restrained "
            "halation, warm highlights and cool shadow separation, slightly soft "
            "photochemical detail, large-scale adventure atmosphere"
        ),
        "negative_prompt": (
            "modern digital blockbuster, excessive HDR, sterile CGI, plastic "
            "surfaces, excessive teal and orange, extreme bokeh, flat lighting, "
            "clean futuristic showroom, hyper-sharp digital image, generic fantasy art"
        ),
        "denoise": 0.58,
        "structure_weight": 0.82,
        "color_boost": 1.10,
        "keywords": [
            "1970s 35mm",
            "adventure",
            "anamorphic",
            "backlight",
            "heroic silhouette",
            "practical production",
            "dust haze",
            "film grain"
        ],
    },

    "lucas_space_opera": {
        "name": "Lucas - Space Opera",
        "category": "cinematic",
        "era": "1970s-1980s",
        "prompt": (
            "1970s space-opera cinematography photographed on 35mm film, "
            "anamorphic wide-screen composition, deep blacks surrounding luminous "
            "practical sources, strong blue, red and amber light separation, "
            "hard directional key lighting, atmospheric haze and smoke catching "
            "light beams, 28mm and 35mm lenses for immersive environmental scale, "
            "moderate depth of field, deep layered compositions, characters embedded "
            "inside enormous mechanical environments, low camera angles for heroic "
            "scale, practical illuminated panels, textured metal, cables, machinery "
            "and worn surfaces, controlled lens flare, organic film grain, subtle "
            "halation, photochemical highlight rolloff, tactile miniature and "
            "practical-effects aesthetic, adventurous cinematic energy"
        ),
        "negative_prompt": (
            "clean modern sci-fi, cyberpunk neon, glossy CGI spaceship, excessive "
            "magenta, excessive bloom, flat digital lighting, plastic materials, "
            "sterile environment, extreme shallow depth of field, game-engine render"
        ),
        "denoise": 0.60,
        "structure_weight": 0.85,
        "color_boost": 1.13,
        "keywords": [
            "space opera",
            "35mm",
            "anamorphic",
            "blue red amber",
            "smoke",
            "mechanical environment",
            "practical lights",
            "miniature aesthetic"
        ],
    },

    "lucas_desert": {
        "name": "Lucas - Desert Myth",
        "category": "cinematic",
        "era": "1970s-1980s",
        "prompt": (
            "epic desert cinematography on warm 35mm film, enormous open landscape, "
            "hard sun from a high angle, golden-hour backlight, long shadows, "
            "atmospheric dust, heat haze and distant terrain, 24mm and 35mm lenses, "
            "deep depth of field, environmental portraiture, tiny human figures "
            "against vast landscapes, strong horizon lines, panoramic compositions, "
            "silhouettes against bright skies, ochre sand, burnt orange earth, "
            "muted blue sky, practical weathered costumes and machinery, organic "
            "film grain, gentle highlight bloom, subtle optical softness, natural "
            "exposure rolloff, strong sense of geographic scale and mythic isolation"
        ),
        "negative_prompt": (
            "green landscape, tropical fantasy, digital HDR, oversaturated orange, "
            "flat studio background, artificial fog, excessive bokeh, modern "
            "commercial photography, plastic textures, cartoon desert"
        ),
        "denoise": 0.56,
        "structure_weight": 0.80,
        "color_boost": 1.12,
        "keywords": [
            "desert",
            "35mm",
            "golden hour",
            "heat haze",
            "wide landscape",
            "silhouette",
            "ochre",
            "mythic scale"
        ],
    },

    "lucas_dark_side": {
        "name": "Lucas - Dark Industrial",
        "category": "cinematic",
        "era": "1970s-1980s",
        "prompt": (
            "dark industrial science-fiction cinematography, photochemical 35mm "
            "image, heavy atmospheric smoke, deep black environments, hard shafts "
            "of white and blue light, isolated red practical lights, strong rim "
            "lighting, 28mm wide-angle lenses, moderate depth of field, imposing "
            "architectural scale, characters framed beneath enormous machinery, "
            "low-angle compositions, strong vertical lines, reflective metal "
            "surfaces, worn industrial textures, controlled highlights, subtle "
            "anamorphic flare, organic film grain, slight halation, restrained "
            "color palette dominated by black, steel blue, white and red, "
            "oppressive spatial geometry and monumental visual design"
        ),
        "negative_prompt": (
            "bright colorful sci-fi, clean spaceship interior, glossy modern CGI, "
            "cyberpunk city, excessive neon, soft beauty lighting, flat composition, "
            "HDR, plastic metal, excessive lens distortion"
        ),
        "denoise": 0.61,
        "structure_weight": 0.87,
        "color_boost": 1.06,
        "keywords": [
            "dark industrial",
            "steel blue",
            "red practical",
            "smoke",
            "rim light",
            "28mm",
            "monumental scale",
            "anamorphic flare"
        ],
    },

    "lucas_prequel_digital": {
        "name": "Lucas - Prequel Digital",
        "category": "cinematic",
        "era": "1990s-2000s",
        "prompt": (
            "late 1990s to early 2000s large-scale digital cinema, highly controlled "
            "studio photography, clean but cinematic digital capture, expansive "
            "virtual environments, wide 24mm to 35mm lenses, deep environmental "
            "focus, strong architectural perspective, precise edge definition, "
            "large sets integrated with digital environments, cool blue shadows "
            "against warm gold and amber highlights, controlled volumetric light, "
            "soft directional key lighting, carefully staged symmetrical compositions, "
            "large-scale ceremonial spaces, reflective polished surfaces mixed with "
            "practical textures, restrained digital sharpening, smooth highlight "
            "rolloff, subtle optical bloom, atmospheric depth and monumental "
            "science-fiction production design"
        ),
        "negative_prompt": (
            "modern hyperreal digital cinema, excessive HDR, photoreal game render, "
            "extreme clarity, oversharpening, excessive teal and orange, shallow "
            "portrait bokeh, flat lighting, generic fantasy environment, plastic "
            "skin, sterile white studio"
        ),
        "denoise": 0.54,
        "structure_weight": 0.84,
        "color_boost": 1.11,
        "keywords": [
            "early digital cinema",
            "24mm",
            "deep focus",
            "virtual environments",
            "blue shadows",
            "gold highlights",
            "volumetric light",
            "monumental architecture"
        ],
    },
}

__all__ = ["LUCAS_STYLES"]
