"""
CharacterForge Cinematic - Spielberg
=====================================

Evoluzione della fotografia cinematografica americana attraverso cinque periodi:
1970s, 1980s, 1990s, 2000s e 2020s.
"""

SPIELBERG_STYLES = {

    "spielberg_1970s": {
        "name": "Steven Spielberg — 1970s New Hollywood",
        "category": "cinematic",
        "era": "1970s",
        "prompt": (
            "1970s American New Hollywood live-action cinema, "
            "classic widescreen 35mm film photography, precise but naturalistic visual storytelling, "
            "carefully composed frames with strong foreground, middle-ground and background separation, "
            "fluid dolly and tracking camera movement, restrained handheld movement when appropriate, "
            "naturalistic blocking, expressive camera placement, "
            "motivated practical lighting, available daylight mixed with tungsten interiors, "
            "strong natural backlight, warm practical sources, soft directional key light, "
            "subtle atmospheric haze, deep but readable shadows, restrained highlights, "
            "warm earth tones, muted greens, amber tungsten contamination, neutral daylight, "
            "vintage spherical 35mm cinema lenses, moderate optical softness, "
            "natural depth of field, organic focus falloff, subtle lens breathing, "
            "fine-to-medium film grain, restrained halation, natural highlight bloom, "
            "realistic motion blur, authentic photochemical exposure, "
            "natural human skin with visible pores, micro-wrinkles, vellus hair, "
            "freckles, scars, uneven pigmentation and natural redness, "
            "physically believable skin response, no beauty retouching, "
            "no plastic skin, no pore removal, no artificial smoothing, "
            "grounded American atmosphere, emotional visual clarity, photographed rather than rendered"
        ),
        "negative_prompt": (
            "digital sterile look, CGI appearance, plastic skin, beauty filter, airbrushed skin, "
            "excessive HDR, excessive sharpness, oversaturated colors, teal and orange grading, "
            "perfect symmetry, artificial bokeh, synthetic lighting, wax skin, pore removal, "
            "skin smoothing, fake film grain, videogame render"
        ),
        "denoise": 0.34,
        "structure_weight": 0.89,
        "color_boost": 0.92,
        "keywords": [
            "1970s",
            "new hollywood",
            "35mm",
            "widescreen",
            "practical lighting",
            "backlight",
        ],
    },

    "spielberg_1980s": {
        "name": "Steven Spielberg — 1980s Classic Adventure 35mm",
        "category": "cinematic",
        "era": "1980s",
        "prompt": (
            "1980s American adventure cinema photographed on 35mm film, "
            "classic widescreen cinematic composition, strong visual geography, "
            "clear foreground and background relationships, expressive camera placement, "
            "fluid dolly, tracking and crane movement, dynamic but controlled camera language, "
            "naturalistic blocking combined with highly readable visual storytelling, "
            "motivated practical lighting, warm tungsten interiors, natural daylight, "
            "golden backlight, controlled rim light, atmospheric shafts of real light, "
            "rich but restrained contrast, deep shadows retaining photographic detail, "
            "warm natural skin tones against cooler environmental backgrounds, "
            "controlled reds, deep blues, muted greens and amber practical highlights, "
            "high-quality spherical 35mm cinema lenses, subtle optical imperfections, "
            "realistic depth of field, organic focus transitions, natural lens flare, "
            "medium fine-grain photochemical texture, restrained halation, "
            "authentic 1980s film response, realistic motion blur and exposure, "
            "human skin with visible pores, micro-wrinkles, vellus hair, freckles, scars, "
            "uneven pigmentation and natural redness, physically accurate light response, "
            "no beauty retouching, no plastic appearance, no artificial smoothing, "
            "cinematic atmosphere, emotional clarity, large-scale photographic realism"
        ),
        "negative_prompt": (
            "digital clean look, CGI, plastic skin, beauty retouching, airbrushed faces, "
            "excessive clarity, excessive saturation, teal-orange blockbuster grade, "
            "fake volumetric light, artificial lens flare, excessive bokeh, HDR halos, "
            "oversharpening, wax skin, pore removal, synthetic lighting, videogame rendering"
        ),
        "denoise": 0.35,
        "structure_weight": 0.88,
        "color_boost": 0.94,
        "keywords": [
            "1980s",
            "adventure cinema",
            "35mm",
            "widescreen",
            "golden backlight",
            "classical composition",
        ],
    },

    "spielberg_1990s": {
        "name": "Steven Spielberg — 1990s Prestige 35mm",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "1990s prestige American cinema photographed on high-quality 35mm film, "
            "refined classical widescreen cinematography, carefully controlled camera movement, "
            "precise dolly, crane and tracking compositions, expressive perspective, "
            "strong spatial continuity, layered staging with foreground and background information, "
            "motivated practical lighting combined with sophisticated studio cinematography, "
            "soft directional key light, controlled daylight, warm tungsten interiors, "
            "strong but believable backlight, subtle atmospheric depth, "
            "rich natural contrast, deep dimensional shadows retaining photographic information, "
            "neutral and warm skin reproduction, restrained environmental saturation, "
            "natural greens, subdued blues, warm amber highlights, "
            "high-quality spherical and anamorphic cinema lenses, "
            "realistic depth of field, organic focus transitions, controlled optical flare, "
            "fine-to-medium 35mm film grain, subtle halation, natural highlight bloom, "
            "wide photochemical exposure latitude, authentic photographic texture, "
            "human skin rendered with pores, micro-wrinkles, vellus hair, freckles, scars, "
            "uneven pigmentation and natural redness, physically believable light interaction, "
            "no digital beautification, no plastic skin, no artificial smoothing, "
            "emotionally expressive but grounded visual realism, photographed on film"
        ),
        "negative_prompt": (
            "digital video appearance, CGI, sterile perfection, plastic skin, beauty filter, "
            "skin smoothing, pore deletion, excessive HDR, crushed blacks, clipped highlights, "
            "excessive teal-orange grading, artificial depth of field, excessive sharpening, "
            "synthetic cinematic effects, fake film grain, commercial beauty photography"
        ),
        "denoise": 0.33,
        "structure_weight": 0.90,
        "color_boost": 0.95,
        "keywords": [
            "1990s",
            "prestige cinema",
            "35mm",
            "widescreen",
            "layered staging",
            "natural contrast",
        ],
    },

    "spielberg_2000s": {
        "name": "Steven Spielberg — 2000s Modern 35mm",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "2000s American cinematic photography retaining the organic character of professional 35mm film, "
            "modern polished cinematography with tactile photochemical texture, "
            "classical widescreen composition combined with dynamic camera movement, "
            "controlled tracking and dolly shots, precise crane movement, "
            "strong spatial continuity, carefully motivated practical lighting, "
            "soft directional key light, realistic daylight, tungsten interiors, "
            "strong controlled backlight and atmospheric separation, "
            "balanced exposure with substantial shadow detail, natural highlight rolloff, "
            "restrained blacks, neutral realistic skin tones, subtle environmental desaturation, "
            "deep blues, muted greens and warm practical amber illumination, "
            "modern spherical and anamorphic cinema lenses, "
            "clean but organic optical rendering, realistic depth of field, "
            "controlled bokeh without artificial blur, subtle optical flare, "
            "fine 35mm film grain, restrained halation, natural film response, "
            "realistic motion blur, professional cinematic exposure, "
            "human skin showing pores, micro-wrinkles, vellus hair, freckles, scars, "
            "small imperfections and natural redness, physically believable subsurface response, "
            "no beauty retouching, no pore removal, no plastic skin, no artificial smoothing, "
            "grounded contemporary realism with large-scale cinematic clarity"
        ),
        "negative_prompt": (
            "digital commercial photography, CGI, plastic skin, beauty filter, airbrushed skin, "
            "excessive sharpness, excessive saturation, modern teal-orange blockbuster grade, "
            "artificial HDR, fake film grain, excessive bokeh, synthetic lighting, "
            "skin smoothing, pore removal, wax skin, videogame render"
        ),
        "denoise": 0.32,
        "structure_weight": 0.91,
        "color_boost": 0.96,
        "keywords": [
            "2000s",
            "modern cinema",
            "35mm",
            "widescreen",
            "dynamic camera",
            "natural skin",
        ],
    },

    "spielberg_2020s": {
        "name": "Steven Spielberg — 2020s Contemporary Cinema",
        "category": "cinematic",
        "era": "2020s",
        "prompt": (
            "2020s contemporary American cinematic photography combining modern digital cinema "
            "with the visual discipline and organic character of traditional film cinematography, "
            "precise widescreen compositions, sophisticated visual storytelling, "
            "controlled dolly, tracking and crane movement, deliberate camera choreography, "
            "strong spatial relationships between characters and environments, "
            "motivated practical lighting supported by modern cinematographic control, "
            "natural daylight, soft directional key light, warm practical interiors, "
            "controlled backlight and edge separation, restrained atmospheric illumination, "
            "high dynamic range while preserving realistic photographic contrast, "
            "soft natural highlight rolloff, readable shadows, restrained blacks, "
            "neutral skin tones with subtle warm highlights, natural environmental colors, "
            "controlled saturation, deep but believable blues and greens, warm amber practical sources, "
            "modern cinema lenses with realistic optical behavior, "
            "natural depth of field, realistic focus transitions, restrained bokeh, "
            "subtle optically motivated lens flare, "
            "fine organic film-like texture, restrained grain, subtle halation, "
            "authentic contemporary cinematic exposure, realistic motion blur, "
            "human skin rendered with pores, micro-wrinkles, vellus hair, freckles, scars, "
            "uneven pigmentation and natural redness, physically believable subsurface scattering, "
            "no beauty retouching, no pore removal, no plastic skin, no artificial smoothing, "
            "emotionally clear contemporary realism, premium theatrical cinematography, "
            "photographed rather than digitally rendered"
        ),
        "negative_prompt": (
            "sterile digital commercial look, CGI, plastic skin, beauty filter, airbrushed skin, "
            "excessive HDR, excessive sharpness, excessive saturation, aggressive teal-orange grading, "
            "synthetic volumetric lighting, artificial bokeh, excessive lens flare, "
            "fake film grain, wax skin, pore removal, skin smoothing, "
            "overprocessed digital image, videogame render, AI-generated appearance"
        ),
        "denoise": 0.31,
        "structure_weight": 0.92,
        "color_boost": 0.97,
        "keywords": [
            "2020s",
            "contemporary cinema",
            "digital cinema",
            "widescreen",
            "practical lighting",
            "photorealistic",
        ],
    },
}


__all__ = ["SPIELBERG_STYLES"]