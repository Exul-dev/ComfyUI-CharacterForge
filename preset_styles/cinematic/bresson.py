"""
CharacterForge Cinematic - Robert Bresson
==========================================

Preset cinematografici ispirati alla grammatica visiva di Robert Bresson:
minimalismo, austerità, composizione rigorosa, luce naturale,
spazi vuoti, gesti essenziali, dettagli fisici e fotografia non ornamentale.
"""

BRESSON_STYLES = {

    "bresson_minimalist": {
        "name": "Bresson - Minimalist Cinema",
        "category": "cinematic",
        "era": "1950s-1960s",
        "prompt": (
            "austere European art cinema, minimalist composition, "
            "static restrained framing, natural available light, "
            "simple architectural environments, muted neutral palette, "
            "large areas of negative space, understated contrast, "
            "unembellished textures, realistic surfaces, "
            "fine-grain 35mm film photography, quiet atmosphere, "
            "precise visual economy, contemplative stillness"
        ),
        "negative_prompt": (
            "glamorous cinematography, dramatic lighting effects, "
            "oversaturated colors, excessive camera movement, "
            "fantasy atmosphere, glossy digital rendering, HDR, "
            "extreme bokeh, decorative composition, visual clutter"
        ),
        "denoise": 0.69,
        "structure_weight": 0.95,
        "color_boost": 0.66,
        "keywords": [
            "minimalism",
            "austerity",
            "negative_space",
            "natural_light",
            "35mm",
            "art_cinema"
        ],
    },

    "bresson_human_gesture": {
        "name": "Bresson - Human Gesture",
        "category": "cinematic",
        "era": "1950s-1960s",
        "prompt": (
            "close observational cinema focused on human gesture and movement, "
            "hands opening a door, footsteps, objects being handled, "
            "partial body framing, restrained facial visibility, "
            "natural window light, soft directional shadows, "
            "plain interiors, muted gray brown and beige palette, "
            "fine 35mm grain, shallow but controlled depth of field, "
            "quiet physical realism, precise minimalist composition"
        ),
        "negative_prompt": (
            "fashion posing, glamorous portraiture, exaggerated emotion, "
            "dramatic action photography, beauty lighting, "
            "neon colors, glossy surfaces, excessive bokeh, HDR"
        ),
        "denoise": 0.71,
        "structure_weight": 0.91,
        "color_boost": 0.64,
        "keywords": [
            "gesture",
            "hands",
            "movement",
            "minimalist",
            "natural_light",
            "physical_detail"
        ],
    },

    "bresson_prison": {
        "name": "Bresson - Confinement",
        "category": "cinematic",
        "era": "1950s",
        "prompt": (
            "austere prison interior, narrow corridors and sparse rooms, "
            "rigorous geometric composition, vertical bars and architectural lines, "
            "soft daylight entering through small windows, "
            "low saturation grayscale and muted earth tones, "
            "deep controlled shadows, realistic worn concrete and wood textures, "
            "static camera perspective, fine analog film grain, "
            "psychological restraint, quiet tension without melodrama"
        ),
        "negative_prompt": (
            "action prison movie, dramatic spotlight, excessive darkness, "
            "violent spectacle, glossy surfaces, neon colors, "
            "Hollywood cinematography, excessive camera shake, HDR"
        ),
        "denoise": 0.74,
        "structure_weight": 0.97,
        "color_boost": 0.61,
        "keywords": [
            "confinement",
            "prison",
            "geometry",
            "bars",
            "austerity",
            "monochrome"
        ],
    },

    "bresson_rural": {
        "name": "Bresson - Rural Stillness",
        "category": "cinematic",
        "era": "1960s-1970s",
        "prompt": (
            "quiet rural European landscape, sparse countryside, "
            "simple roads, fields and modest buildings, "
            "overcast natural daylight, soft gray sky, "
            "restrained earth-tone palette, low visual saturation, "
            "human figure integrated subtly into environment, "
            "static observational framing, delicate atmospheric depth, "
            "fine 35mm film grain, realistic vegetation and soil textures, "
            "minimalist contemplative atmosphere"
        ),
        "negative_prompt": (
            "epic landscape photography, vivid green fields, fantasy countryside, "
            "dramatic sunset, HDR, excessive lens flare, "
            "glossy digital photography, oversaturated colors, "
            "heroic character framing"
        ),
        "denoise": 0.70,
        "structure_weight": 0.94,
        "color_boost": 0.69,
        "keywords": [
            "rural",
            "stillness",
            "countryside",
            "overcast",
            "minimalism",
            "35mm"
        ],
    },

    "bresson_black_and_white": {
        "name": "Bresson - Monochrome Austerity",
        "category": "cinematic",
        "era": "1950s",
        "prompt": (
            "austere black and white European cinema, "
            "highly controlled grayscale, natural window illumination, "
            "soft highlights with dense but detailed shadows, "
            "simple architectural framing, precise geometry, "
            "human figures isolated in restrained environments, "
            "subtle atmospheric depth, authentic 35mm monochrome grain, "
            "realistic skin texture, quiet visual tension, "
            "photographic simplicity and emotional restraint"
        ),
        "negative_prompt": (
            "color photography, glossy noir, dramatic spotlight, "
            "extreme contrast clipping, crushed blacks, HDR, "
            "digital sharpness, excessive film scratches, "
            "stylized fantasy composition"
        ),
        "denoise": 0.72,
        "structure_weight": 0.96,
        "color_boost": 0.58,
        "keywords": [
            "black_and_white",
            "monochrome",
            "austerity",
            "geometry",
            "natural_light",
            "35mm"
        ],
    },
}


__all__ = ["BRESSON_STYLES"]
