"""
CharacterForge Cinematic - Quentin Tarantino
============================================

Preset cinematografici ispirati ai principali linguaggi visivi
associati alla filmografia di Quentin Tarantino.

Focus:
- 35mm photochemical cinematography
- anamorphic widescreen
- low-angle and high-angle compositions
- trunk-shot perspective
- lateral tracking language
- crash zoom feeling
- saturated practical colors
- tungsten, neon and sodium-vapor lighting
- strong foreground/background staging
- deep environmental compositions
- pulp, exploitation and crime-film texture
"""

TARANTINO_STYLES = {

    "tarantino_pulp": {
        "name": "Tarantino - Pulp Crime",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "1990s 35mm photochemical pulp crime cinematography, anamorphic widescreen "
            "perspective, 35mm and 40mm lenses, strong geometric compositions, low-angle "
            "camera positions, characters framed with deliberate foreground objects, "
            "deep environmental staging, saturated reds, yellows and dirty blues, "
            "warm tungsten interiors mixed with cool night ambience, hard directional "
            "practical lighting, controlled backlight, moderate depth of field, "
            "organic film grain, subtle halation, slight optical softness, polished "
            "but tactile production design, leather, chrome, wood and worn surfaces, "
            "high visual contrast without HDR, stylized crime-film atmosphere"
        ),
        "negative_prompt": (
            "modern digital cinema, teal and orange blockbuster grading, excessive HDR, "
            "plastic CGI, flat composition, generic action photography, extreme bokeh, "
            "pastel colors, sterile interiors, video-game rendering"
        ),
        "denoise": 0.58,
        "structure_weight": 0.84,
        "color_boost": 1.17,
        "keywords": [
            "pulp crime",
            "35mm",
            "anamorphic",
            "low angle",
            "tungsten",
            "saturated colors",
            "film grain",
            "deep staging"
        ],
    },

    "tarantino_trunk_shot": {
        "name": "Tarantino - Trunk Shot",
        "category": "cinematic",
        "era": "1990s-2000s",
        "prompt": (
            "iconic low-angle trunk-shot visual language, camera positioned extremely "
            "low looking upward at characters, 24mm to 28mm wide-angle lens, strong "
            "perspective distortion, anamorphic 35mm film rendering, faces and bodies "
            "arranged around the upper frame, hard overhead practical lighting, "
            "deep shadows under brows, strong rim light, warm tungsten ambience, "
            "rich blacks, saturated red and amber accents, visible film grain, "
            "subtle halation, tactile physical props dominating foreground, "
            "deliberate geometric staging, theatrical character blocking, "
            "controlled depth of field with environmental context retained"
        ),
        "negative_prompt": (
            "eye-level portrait, telephoto compression, modern digital sharpness, "
            "soft beauty lighting, excessive bokeh, flat perspective, HDR, "
            "generic action shot, fisheye extreme distortion"
        ),
        "denoise": 0.61,
        "structure_weight": 0.88,
        "color_boost": 1.14,
        "keywords": [
            "trunk shot",
            "24mm",
            "low angle",
            "anamorphic",
            "hard overhead light",
            "deep shadows",
            "35mm grain",
            "geometric staging"
        ],
    },

    "tarantino_retro_crime": {
        "name": "Tarantino - Retro Crime",
        "category": "cinematic",
        "era": "1990s-2000s",
        "prompt": (
            "retro crime-film cinematography photographed on 35mm anamorphic film, "
            "visual language inspired by 1960s and 1970s exploitation cinema, "
            "35mm and 50mm lenses, occasional long-lens compression, strong primary "
            "colors, mustard yellow, deep red, turquoise blue and warm brown, "
            "hard tungsten practicals, colored neon signs, sodium street lights, "
            "controlled smoke and haze, moderate depth of field, symmetrical "
            "compositions, strong horizontal lines, deliberate centered framing, "
            "organic film grain, slightly faded photochemical color response, "
            "subtle halation and lens flare, tactile locations, vintage cars, "
            "chrome, leather and wood textures, stylized retro atmosphere"
        ),
        "negative_prompt": (
            "clean modern digital image, contemporary minimalist design, pastel "
            "palette, excessive teal and orange, sterile environments, CGI surfaces, "
            "HDR, hyper-sharp detail, modern LED lighting"
        ),
        "denoise": 0.57,
        "structure_weight": 0.80,
        "color_boost": 1.19,
        "keywords": [
            "retro crime",
            "exploitation",
            "35mm anamorphic",
            "mustard yellow",
            "deep red",
            "turquoise",
            "neon",
            "vintage texture"
        ],
    },

    "tarantino_western": {
        "name": "Tarantino - Spaghetti Western",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "epic 35mm western cinematography with anamorphic widescreen character, "
            "extreme landscape scale, 35mm and 50mm lenses, occasional long-lens "
            "compression for distant figures, harsh desert sunlight, golden-hour "
            "backlight, strong rim light, deep shadows beneath hats, dusty air, "
            "atmospheric perspective, warm ochre earth, faded blue sky, dark brown "
            "costumes, carefully controlled saturated reds, low-angle hero framing, "
            "wide compositions with tiny human figures against enormous landscapes, "
            "close facial portraits with shallow depth of field, organic film grain, "
            "subtle anamorphic flare, photochemical highlight rolloff, tactile dust "
            "and weathered textures, deliberate pacing expressed through static "
            "composition and visual scale"
        ),
        "negative_prompt": (
            "digital western, clean desert photography, fantasy landscape, excessive "
            "orange grading, HDR, plastic skin, modern fashion photography, "
            "excessive bokeh, CGI environment, flat lighting"
        ),
        "denoise": 0.56,
        "structure_weight": 0.82,
        "color_boost": 1.13,
        "keywords": [
            "western",
            "35mm anamorphic",
            "desert",
            "golden hour",
            "rim light",
            "long lens",
            "landscape scale",
            "dust"
        ],
    },

    "tarantino_neon_night": {
        "name": "Tarantino - Neon Night",
        "category": "cinematic",
        "era": "1990s-2000s",
        "prompt": (
            "stylized 35mm night cinematography, anamorphic widescreen, wet urban "
            "streets, neon signs and practical restaurant lighting, deep black "
            "backgrounds, saturated red, blue and amber light sources, hard side "
            "lighting on faces, strong backlight, visible practical fixtures, "
            "35mm and 50mm lenses, moderate shallow depth of field, reflections "
            "on chrome and wet asphalt, deliberate symmetrical compositions, "
            "tracking-shot energy, lateral spatial relationships, occasional "
            "low-angle framing, controlled smoke and atmospheric haze, organic "
            "film grain, subtle halation around neon, slight anamorphic flare, "
            "rich tactile surfaces, nocturnal pulp atmosphere"
        ),
        "negative_prompt": (
            "cyberpunk city, excessive neon everywhere, modern LED aesthetic, "
            "clean digital night photography, excessive bloom, HDR, plastic skin, "
            "generic music-video look, extreme shallow depth of field"
        ),
        "denoise": 0.60,
        "structure_weight": 0.81,
        "color_boost": 1.20,
        "keywords": [
            "neon night",
            "wet asphalt",
            "35mm",
            "anamorphic flare",
            "red blue amber",
            "tungsten",
            "tracking shot",
            "film grain"
        ],
    },
}

__all__ = ["TARANTINO_STYLES"]
