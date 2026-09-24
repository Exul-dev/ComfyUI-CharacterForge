"""
CharacterForge Cinematic - Orson Welles
========================================

Preset cinematografici ispirati al cinema di Orson Welles:
deep focus, chiaroscuro, grandangoli, prospettive espressioniste,
architettura monumentale e composizioni fortemente teatrali.
"""

WELLES_STYLES = {

    "welles_citizen_kane": {
        "name": "Welles - Citizen Kane",
        "category": "cinematic",
        "era": "1940s",
        "prompt": (
            "classic American cinema, deep focus cinematography, "
            "extreme wide angle lens, monumental interiors, "
            "low camera position, dramatic foreground objects, "
            "towering ceilings, deep spatial layering, "
            "high contrast chiaroscuro, theatrical shadows, "
            "rich black levels, controlled highlights, "
            "35mm film texture, atmospheric smoke, "
            "expressionist composition, imposing visual architecture"
        ),
        "negative_prompt": (
            "flat lighting, shallow depth of field, modern digital cinema, "
            "soft commercial photography, pastel colors, "
            "excessive bokeh, glossy skin, HDR, fisheye distortion, "
            "contemporary architecture"
        ),
        "denoise": 0.74,
        "structure_weight": 0.96,
        "color_boost": 0.72,
        "keywords": [
            "deep_focus",
            "chiaroscuro",
            "wide_angle",
            "low_angle",
            "expressionism",
            "1940s"
        ],
    },

    "welles_noir": {
        "name": "Welles - Film Noir",
        "category": "cinematic",
        "era": "1940s-1950s",
        "prompt": (
            "dark film noir cinematography, extreme chiaroscuro, "
            "hard directional light, Venetian blind shadows, "
            "wet streets, deep black shadows, isolated pools of light, "
            "dramatic low angle framing, wide lens distortion, "
            "dense atmospheric smoke, noir urban architecture, "
            "high contrast black and white 35mm film, "
            "ominous theatrical composition"
        ),
        "negative_prompt": (
            "bright cheerful lighting, pastel palette, soft beauty lighting, "
            "modern LED lighting, clean digital image, "
            "low contrast, excessive color saturation, romantic glamour"
        ),
        "denoise": 0.76,
        "structure_weight": 0.92,
        "color_boost": 0.68,
        "keywords": [
            "film_noir",
            "chiaroscuro",
            "black_and_white",
            "hard_light",
            "wide_angle",
            "smoke"
        ],
    },

    "welles_ambersons": {
        "name": "Welles - The Magnificent Ambersons",
        "category": "cinematic",
        "era": "1940s",
        "prompt": (
            "period American drama, grand Victorian interiors, "
            "deep focus photography, elegant tracking composition, "
            "large rooms with layered foreground middle ground and background, "
            "soft but directional period lighting, warm wood textures, "
            "dramatic architectural perspective, restrained monochrome palette, "
            "fine 35mm grain, theatrical staging, "
            "nostalgic atmosphere and visual grandeur"
        ),
        "negative_prompt": (
            "modern furniture, contemporary clothing, flat composition, "
            "digital sharpness, neon colors, glossy photography, "
            "shallow focus, modern cinematic lighting"
        ),
        "denoise": 0.72,
        "structure_weight": 0.95,
        "color_boost": 0.70,
        "keywords": [
            "period_drama",
            "victorian",
            "deep_focus",
            "architecture",
            "nostalgia",
            "1940s"
        ],
    },

    "welles_macbeth": {
        "name": "Welles - Macbeth",
        "category": "cinematic",
        "era": "1940s",
        "prompt": (
            "expressionist medieval drama, monumental stone environments, "
            "heavy fog, stark chiaroscuro, towering angular architecture, "
            "low camera perspective, dramatic silhouettes, "
            "rough stone textures, atmospheric smoke, "
            "deep blacks and silver highlights, theatrical staging, "
            "highly sculptural faces, austere black and white 35mm photography, "
            "dark mythological atmosphere"
        ),
        "negative_prompt": (
            "bright fantasy colors, glossy medieval fantasy, "
            "modern costume design, clean digital rendering, "
            "photographic beauty lighting, cheerful atmosphere, "
            "soft pastel colors"
        ),
        "denoise": 0.78,
        "structure_weight": 0.94,
        "color_boost": 0.66,
        "keywords": [
            "expressionist",
            "macbeth",
            "fog",
            "medieval",
            "chiaroscuro",
            "black_and_white"
        ],
    },

    "welles_touch_of_evil": {
        "name": "Welles - Touch of Evil",
        "category": "cinematic",
        "era": "1950s",
        "prompt": (
            "1950s border-town noir, elaborate long take composition, "
            "extreme wide angle lens, distorted perspective, "
            "night streets, harsh street lamps, neon signs, "
            "deep shadows, wet pavement, smoky interiors, "
            "characters entering and leaving frame, "
            "complex spatial choreography, high contrast monochrome, "
            "gritty 35mm film grain, tense expressionist atmosphere"
        ),
        "negative_prompt": (
            "clean modern city, contemporary vehicles, smartphone screens, "
            "soft romantic lighting, polished digital cinema, "
            "flat perspective, shallow commercial photography, "
            "oversaturated neon"
        ),
        "denoise": 0.77,
        "structure_weight": 0.93,
        "color_boost": 0.74,
        "keywords": [
            "touch_of_evil",
            "noir",
            "long_take",
            "wide_angle",
            "night",
            "border_town"
        ],
    },
}


__all__ = ["WELLES_STYLES"]
