"""
CharacterForge Cinematic - Billy Wilder
========================================

Preset cinematografici ispirati alla fotografia e alla grammatica
visiva di Billy Wilder: noir, commedia sofisticata, illuminazione
classica hollywoodiana, composizione narrativa, interni eleganti,
contrasto fotografico e atmosfera urbana.
"""

WILDER_STYLES = {

    "wilder_noir": {
        "name": "Wilder - Classic Noir",
        "category": "cinematic",
        "era": "1940s",
        "prompt": (
            "classic American film noir cinematography, black and white 35mm film, "
            "hard directional key light, deep chiaroscuro, venetian blind shadows, "
            "smoky interiors, wet nighttime streets, isolated pools of illumination, "
            "precise classical composition, medium and wide framing, "
            "deep blacks with controlled highlights, restrained grayscale, "
            "visible fine film grain, atmospheric haze, "
            "elegant but morally tense urban environment"
        ),
        "negative_prompt": (
            "modern digital cinema, soft beauty lighting, pastel colors, "
            "HDR, excessive bloom, neon cyberpunk, extreme shallow depth of field, "
            "glossy commercial photography, oversharpening, fantasy atmosphere"
        ),
        "denoise": 0.74,
        "structure_weight": 0.92,
        "color_boost": 0.64,
        "keywords": [
            "film_noir",
            "black_and_white",
            "chiaroscuro",
            "35mm",
            "hard_light",
            "urban"
        ],
    },

    "wilder_sunset_boulevard": {
        "name": "Wilder - Sunset Boulevard",
        "category": "cinematic",
        "era": "1950s",
        "prompt": (
            "1950s Hollywood noir melodrama, decaying grand mansion interiors, "
            "dramatic staircase compositions, deep shadows, dusty sunlight through windows, "
            "aged velvet and dark wood textures, expressive practical lamps, "
            "controlled black and white exposure, strong tonal separation, "
            "medium wide theatrical framing, deep spatial composition, "
            "fine 35mm grain, slightly softened optical rendering, "
            "decadent atmosphere, visual contrast between glamour and decay"
        ),
        "negative_prompt": (
            "modern mansion, contemporary furniture, clean luxury interiors, "
            "bright cheerful lighting, saturated colors, digital sharpness, "
            "minimalist architecture, excessive bokeh, glossy fashion photography"
        ),
        "denoise": 0.75,
        "structure_weight": 0.94,
        "color_boost": 0.66,
        "keywords": [
            "hollywood_noir",
            "mansion",
            "decay",
            "black_and_white",
            "dramatic_interior",
            "35mm"
        ],
    },

    "wilder_apartment": {
        "name": "Wilder - Apartment Comedy",
        "category": "cinematic",
        "era": "1950s-1960s",
        "prompt": (
            "classic Hollywood studio cinematography, sophisticated apartment interior, "
            "balanced ensemble composition, medium shots and carefully staged two-shots, "
            "soft key lighting with gentle fill, practical lamps, "
            "warm neutral interior palette, elegant production design, "
            "clean but organic 35mm film texture, subtle grain, "
            "precise eyelines, layered blocking, restrained depth of field, "
            "polished theatrical composition with natural human expressions"
        ),
        "negative_prompt": (
            "modern sitcom aesthetic, television lighting, excessive wide angle, "
            "digital sharpness, plastic skin, extreme bokeh, "
            "neon colors, handheld documentary style, HDR"
        ),
        "denoise": 0.69,
        "structure_weight": 0.89,
        "color_boost": 0.86,
        "keywords": [
            "classic_hollywood",
            "apartment",
            "ensemble",
            "comedy",
            "studio_lighting",
            "35mm"
        ],
    },

    "wilder_the_seven_year_itch": {
        "name": "Wilder - Summer Manhattan",
        "category": "cinematic",
        "era": "1950s",
        "prompt": (
            "1950s Manhattan summer atmosphere, classic Hollywood color photography, "
            "soft warm daylight, elegant urban interiors, apartment windows, "
            "subtle pastel wardrobe and architectural colors, "
            "controlled studio fill combined with natural-looking illumination, "
            "medium and medium-wide compositions, sophisticated blocking, "
            "fine-grain color 35mm film, gentle halation, restrained contrast, "
            "light comedic atmosphere, polished but photographic cinematic texture"
        ),
        "negative_prompt": (
            "modern Manhattan, contemporary cars, smartphone screens, "
            "digital advertising look, oversaturated colors, "
            "hard modern LED lighting, excessive bokeh, HDR, "
            "hyperreal digital sharpness"
        ),
        "denoise": 0.71,
        "structure_weight": 0.87,
        "color_boost": 0.96,
        "keywords": [
            "1950s_manhattan",
            "summer",
            "color_35mm",
            "classic_hollywood",
            "warm_light",
            "comedy"
        ],
    },

    "wilder_elegant_cynicism": {
        "name": "Wilder - Elegant Cynicism",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "sophisticated American cinema, elegant urban interiors and hotel rooms, "
            "precise classical framing, subtle visual irony, "
            "controlled studio lighting mixed with practical sources, "
            "moderate contrast, carefully separated foreground middle ground background, "
            "muted sophisticated color palette, natural skin tones, "
            "fine 35mm grain, restrained halation, realistic fabric and wood texture, "
            "polished composition with an understated darker undertone"
        ),
        "negative_prompt": (
            "modern digital advertising, excessive saturation, fantasy lighting, "
            "extreme camera angles, handheld chaos, plastic surfaces, "
            "HDR, excessive bloom, razor-sharp digital rendering"
        ),
        "denoise": 0.70,
        "structure_weight": 0.91,
        "color_boost": 0.82,
        "keywords": [
            "sophisticated",
            "urban",
            "classical_framing",
            "35mm",
            "studio_lighting",
            "irony"
        ],
    },
}


__all__ = ["WILDER_STYLES"]
