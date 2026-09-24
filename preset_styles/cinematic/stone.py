"""
CharacterForge Cinematic - Oliver Stone
=======================================

Preset cinematografici ispirati ai principali linguaggi visivi
associati alla filmografia di Oliver Stone.

Focus:
- fotografia documentaristica e nervosa
- 16mm / 35mm photochemical texture
- handheld camera language
- grandangoli ravvicinati
- shutter duro e motion texture
- available light e practical lighting
- grana evidente
- desaturazione e contaminazione cromatica
- composizioni instabili
- forte contrasto tra reportage e fotografia psicologica
"""

STONE_STYLES = {

    "stone_1980s": {
        "name": "Stone - 1980s Grit",
        "category": "cinematic",
        "era": "1980s",
        "prompt": (
            "gritty 35mm photochemical cinematography, raw 1980s documentary "
            "aesthetic, handheld camera language, 24mm and 28mm wide-angle lenses "
            "used close to subjects, strong perspective exaggeration, available "
            "light mixed with harsh practical sources, tungsten interiors, sodium "
            "street lighting, deep shadows, hard highlights, visible film grain, "
            "slightly rough exposure, imperfect framing, off-center compositions, "
            "foreground obstruction, realistic skin texture, muted earth tones with "
            "occasional saturated red and yellow accents, smoke, dust and atmospheric "
            "imperfections, physical 35mm texture, restrained optical softness, "
            "urgent observational atmosphere"
        ),
        "negative_prompt": (
            "clean commercial photography, polished digital cinema, perfect "
            "symmetry, soft beauty lighting, excessive bokeh, HDR, glossy surfaces, "
            "plastic skin, sterile environment, artificial cinematic perfection"
        ),
        "denoise": 0.63,
        "structure_weight": 0.77,
        "color_boost": 1.04,
        "keywords": [
            "1980s grit",
            "35mm",
            "handheld",
            "24mm",
            "available light",
            "film grain",
            "documentary",
            "imperfect framing"
        ],
    },

    "stone_war_documentary": {
        "name": "Stone - War Documentary",
        "category": "cinematic",
        "era": "1980s-1990s",
        "prompt": (
            "war-documentary cinematography on 16mm and 35mm film, aggressive "
            "handheld camera, 24mm wide-angle lens extremely close to subjects, "
            "shallow and deep focus alternating according to chaotic geography, "
            "available daylight, harsh overhead sun, dirty fluorescent interiors, "
            "smoke, dust, mud and atmospheric debris, high contrast exposure, "
            "desaturated greens and browns, dirty yellow highlights, occasional "
            "blood-red accents, pronounced coarse film grain, rough emulsion texture, "
            "fast shutter motion rendering, slight frame instability, imperfect "
            "focus transitions, off-axis framing, foreground obstruction, documentary "
            "proximity, no glamour, tactile physical environment"
        ),
        "negative_prompt": (
            "clean war movie, glossy blockbuster photography, perfectly stabilized "
            "camera, heroic beauty lighting, excessive slow motion, HDR, digital "
            "clarity, clean uniforms, saturated fantasy colors, studio look"
        ),
        "denoise": 0.66,
        "structure_weight": 0.74,
        "color_boost": 0.98,
        "keywords": [
            "16mm",
            "war documentary",
            "handheld",
            "dirty greens",
            "mud",
            "dust",
            "coarse grain",
            "fast shutter"
        ],
    },

    "stone_natural_born": {
        "name": "Stone - Hyperreal Satire",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "1990s 35mm hyperreal satirical cinematography, aggressive visual "
            "contrast, handheld and low-angle camera positions, wide 24mm and 28mm "
            "lenses, saturated reds, sickly greens, dirty yellows and electric "
            "street colors, mixed color temperatures, practical neon and tungsten "
            "sources, hard backlight, strong flare, occasional overexposure, "
            "selective focus, unstable framing, rapid visual shifts, layered "
            "foreground elements, exaggerated perspective, coarse photochemical "
            "grain, visible optical imperfections, atmospheric smoke, nightclub "
            "haze and urban grime, heightened reality without becoming digital, "
            "visual excess grounded in physical film texture"
        ),
        "negative_prompt": (
            "tasteful restrained palette, clean modern digital photography, "
            "perfectly balanced exposure, minimalist composition, pastel colors, "
            "soft romantic lighting, pristine environment, CGI smoothness, HDR"
        ),
        "denoise": 0.64,
        "structure_weight": 0.76,
        "color_boost": 1.18,
        "keywords": [
            "hyperreal satire",
            "1990s 35mm",
            "wide angle",
            "mixed color temperature",
            "neon",
            "flare",
            "coarse grain",
            "visual excess"
        ],
    },

    "stone_political_drama": {
        "name": "Stone - Political Drama",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "1990s political drama cinematography, 35mm film with documentary "
            "influence, controlled handheld movement, 28mm and 35mm lenses, "
            "moderate depth of field preserving institutional environments, "
            "fluorescent office lighting mixed with warm tungsten practicals, "
            "greenish institutional shadows, muted beige and gray palette, "
            "hard side lighting on faces, occasional dramatic backlight, "
            "off-center framing, layered compositions through doorways and glass, "
            "reflections and foreground obstructions, visible analog grain, "
            "subtle halation, realistic imperfect exposure, restrained saturation, "
            "institutional architecture emphasized through perspective, observational "
            "camera language with moments of heightened psychological intensity"
        ),
        "negative_prompt": (
            "luxury corporate photography, pristine office, modern LED lighting, "
            "soft beauty portrait, excessive shallow depth of field, glossy digital "
            "cinema, symmetrical commercial composition, HDR, oversaturation"
        ),
        "denoise": 0.60,
        "structure_weight": 0.82,
        "color_boost": 1.01,
        "keywords": [
            "political drama",
            "35mm",
            "fluorescent",
            "institutional",
            "handheld",
            "glass reflections",
            "muted palette",
            "analog grain"
        ],
    },

    "stone_psychological": {
        "name": "Stone - Psychological Intensity",
        "category": "cinematic",
        "era": "1990s-2000s",
        "prompt": (
            "psychological cinematic photography with documentary realism, "
            "35mm and occasional 16mm texture, close handheld camera, 24mm wide "
            "angle used within intimate personal space, distorted perspective, "
            "shallow depth of field alternating with sudden deep-focus environmental "
            "shots, hard directional practical lighting, strong side light, "
            "backlight through smoke, mixed color temperatures, desaturated skin "
            "tones against isolated saturated colors, deep blacks, aggressive "
            "highlight contrast, coarse film grain, subtle gate instability, "
            "motion texture, reflections, mirrors and foreground obstructions, "
            "claustrophobic framing, physical imperfections in the image, "
            "intense observational atmosphere and subjective psychological pressure"
        ),
        "negative_prompt": (
            "clean portrait photography, stable tripod aesthetic, soft beauty light, "
            "perfect skin, smooth digital image, excessive bokeh, dreamy pastel "
            "palette, polished blockbuster look, CGI, HDR, sterile composition"
        ),
        "denoise": 0.65,
        "structure_weight": 0.79,
        "color_boost": 1.06,
        "keywords": [
            "psychological intensity",
            "16mm texture",
            "24mm close",
            "handheld",
            "mixed lighting",
            "deep blacks",
            "coarse grain",
            "subjective camera"
        ],
    },
}

__all__ = ["STONE_STYLES"]
