"""
CharacterForge Cinematic - Martin Scorsese
==========================================

Evoluzione fotografica attraverso quattro periodi:
1970s, 1980s, 1990s e 2000s.
"""

SCORSESE_STYLES = {

    "scorsese_1970s": {
        "name": "Martin Scorsese — 1970s New Hollywood",
        "category": "cinematic",
        "era": "1970s",
        "prompt": (
            "1970s American New Hollywood live-action cinema, "
            "gritty 35mm film photography, intimate observational framing, "
            "handheld documentary-influenced camera language, naturalistic blocking, "
            "imperfect practical lighting, available light mixed with tungsten interiors, "
            "slightly underexposed shadows, restrained highlights, textured blacks, "
            "muted urban colors, warm dirty tungsten tones, subtle green and amber contamination, "
            "vintage spherical 35mm lenses, moderate optical softness, natural lens breathing, "
            "organic focus falloff, fine-to-medium film grain, subtle halation, realistic motion blur, "
            "authentic photographic exposure, natural human skin with visible pores, micro-wrinkles, "
            "vellus hair, freckles, scars and irregular redness, physically believable skin response, "
            "no beauty retouching, no plastic skin, no pore removal, no artificial smoothing, "
            "lived-in urban atmosphere, raw human realism, photographed rather than digitally rendered"
        ),
        "negative_prompt": (
            "digital clean look, CGI appearance, plastic skin, beauty filter, airbrushed skin, "
            "excessive HDR, excessive sharpness, oversaturated colors, teal and orange grading, "
            "perfect symmetry, artificial bokeh, synthetic lighting, wax skin, pore removal, "
            "skin smoothing"
        ),
        "denoise": 0.34,
        "structure_weight": 0.88,
        "color_boost": 0.92,
        "keywords": [
            "new hollywood",
            "1970s",
            "35mm",
            "gritty",
            "urban",
            "naturalistic",
        ],
    },

    "scorsese_1980s": {
        "name": "Martin Scorsese — 1980s Urban 35mm",
        "category": "cinematic",
        "era": "1980s",
        "prompt": (
            "1980s American urban cinema photographed on 35mm film, "
            "sophisticated but tactile live-action cinematography, controlled handheld movement, "
            "expressive dolly and tracking compositions, strong practical sources, "
            "motivated tungsten interiors, sodium-vapor street lighting, selective hard backlight, "
            "rich but restrained contrast, dense shadows retaining photographic detail, "
            "warm skin tones against cooler urban backgrounds, controlled reds and amber highlights, "
            "vintage spherical prime lenses with natural falloff, subtle optical imperfections, "
            "realistic depth of field, organic focus transitions, medium 35mm film grain, "
            "restrained halation, realistic highlight rolloff, authentic photographic exposure, "
            "naturally imperfect human skin with pores, micro-wrinkles, facial texture, vellus hair, "
            "freckles, scars and natural redness, physically accurate skin response, "
            "no beauty retouching, no plastic appearance, nocturnal city atmosphere, smoky interiors, "
            "rain-slick streets when appropriate, intense but believable cinematic realism"
        ),
        "negative_prompt": (
            "digital sterile image, CGI, plastic skin, beauty retouching, excessive clarity, "
            "excessive saturation, teal-orange blockbuster grade, fake volumetric light, "
            "perfect skin, artificial smoothing, HDR halos, oversharpening"
        ),
        "denoise": 0.35,
        "structure_weight": 0.87,
        "color_boost": 0.94,
        "keywords": [
            "1980s",
            "urban cinema",
            "35mm",
            "tungsten",
            "night",
            "practical lighting",
        ],
    },

    "scorsese_1990s": {
        "name": "Martin Scorsese — 1990s Refined 35mm",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "1990s prestige American cinema photographed on high-quality 35mm film, "
            "refined but organic cinematography, deliberate camera movement, fluid tracking shots, "
            "carefully staged compositions, expressive perspective without artificial perfection, "
            "practical and motivated lighting, soft tungsten interiors, controlled daylight, "
            "deep dimensional shadows, rich natural contrast, subtle warm highlights with neutral skin reproduction, "
            "sophisticated restrained color palette, spherical cinema primes, realistic depth of field, "
            "precise but organic focus transitions, fine-to-medium 35mm grain, gentle film halation, "
            "natural highlight bloom, realistic exposure latitude, authentic photographic texture, "
            "human skin rendered with pores, micro-wrinkles, vellus hair, freckles, scars, "
            "uneven pigmentation and natural redness, realistic subsurface light response, "
            "no digital beautification, no plastic skin, no artificial smoothing, "
            "emotionally charged urban atmosphere, tactile period realism, photographed on film"
        ),
        "negative_prompt": (
            "digital video look, CGI, sterile perfection, plastic skin, beauty filter, "
            "skin smoothing, pore deletion, excessive HDR, excessive teal-orange, crushed blacks, "
            "clipped highlights, artificial depth of field, excessive sharpening, synthetic cinematic effects"
        ),
        "denoise": 0.33,
        "structure_weight": 0.90,
        "color_boost": 0.95,
        "keywords": [
            "1990s",
            "prestige cinema",
            "35mm",
            "tracking",
            "refined",
            "organic",
        ],
    },

    "scorsese_2000s": {
        "name": "Martin Scorsese — 2000s Modern Film",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "early-2000s modern American cinematic photography with the organic character of 35mm film, "
            "polished professional cinematography while retaining tactile photographic imperfections, "
            "controlled camera movement, dynamic tracking and dolly compositions, carefully motivated practical lighting, "
            "soft directional key light, realistic urban night illumination, balanced exposure with rich shadow detail, "
            "restrained blacks, natural highlight rolloff, nuanced neutral and warm skin tones, "
            "subtle desaturation in environments, spherical and modern cinema prime lenses, "
            "clean but organic optical rendering, realistic depth of field, controlled bokeh, "
            "fine film grain, subtle halation, restrained film texture, authentic 35mm photographic response, "
            "realistic human skin showing pores, micro-wrinkles, vellus hair, freckles, scars, "
            "small imperfections and natural redness, physically believable light interaction, "
            "no beauty retouching, no pore removal, no plastic skin, no artificial smoothing, "
            "mature urban atmosphere, grounded contemporary realism, cinematic rather than commercial photography"
        ),
        "negative_prompt": (
            "digital commercial photography, CGI, plastic skin, beauty filter, airbrushed skin, "
            "excessive sharpness, excessive saturation, modern teal-orange blockbuster grade, "
            "artificial HDR, fake film grain, excessive bokeh, synthetic lighting, "
            "skin smoothing, pore removal"
        ),
        "denoise": 0.32,
        "structure_weight": 0.91,
        "color_boost": 0.96,
        "keywords": [
            "2000s",
            "modern cinema",
            "35mm",
            "polished",
            "urban",
            "natural skin",
        ],
    },
}


__all__ = ["SCORSESE_STYLES"]