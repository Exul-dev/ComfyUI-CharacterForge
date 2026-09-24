"""
CharacterForge Cinematic - Ingmar Bergman
==========================================

Preset cinematografici basati sull'evoluzione della fotografia,
della composizione e della messa in scena del cinema di Ingmar Bergman.

Focus:
- primi piani psicologici
- bianco e nero espressivo
- luce naturale e teatrale
- composizioni minimaliste
- contrasto tonale
- volti e micro-espressioni
- silenzio visivo
- atmosfera introspettiva
"""

BERGMAN_STYLES = {
    "bergman_1950s": {
        "name": "Bergman - Nordic 1950s",
        "category": "cinematic",
        "era": "1950s",
        "prompt": (
            "1950s Scandinavian cinematic photography, expressive black and white, "
            "high tonal contrast, soft Nordic daylight, intimate compositions, "
            "natural human faces, realistic skin texture, restrained staging, "
            "quiet interiors, sparse environments, subtle film grain, "
            "deep but soft shadows, luminous windows, atmospheric darkness, "
            "precise facial expressions, contemplative mood, "
            "authentic 35mm photographic realism"
        ),
        "negative_prompt": (
            "glossy commercial photography, oversaturated colors, beauty retouching, "
            "plastic skin, excessive HDR, artificial neon, fantasy glow, "
            "excessive bloom, cartoon, anime, painterly rendering, "
            "synthetic CGI appearance"
        ),
        "denoise": 0.70,
        "structure_weight": 0.86,
        "color_boost": 0.48,
        "keywords": [
            "1950s",
            "Nordic",
            "black-and-white",
            "intimate",
            "natural-light",
            "psychological",
            "35mm",
            "film-grain",
        ],
    },

    "bergman_1960s": {
        "name": "Bergman - Psychological 1960s",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "1960s Scandinavian psychological cinema, stark black and white "
            "photography, extremely expressive close-ups, sculpted facial lighting, "
            "deep shadows, luminous highlights, minimalist interiors, "
            "precise framing, emotionally charged faces, natural skin texture, "
            "subtle film grain, controlled exposure, soft window light, "
            "dramatic negative space, sparse visual environment, "
            "introspective cinematic realism"
        ),
        "negative_prompt": (
            "glamour lighting, commercial beauty photography, saturated colors, "
            "plastic skin, excessive smoothing, artificial HDR, excessive sharpness, "
            "fantasy glow, neon lighting, cartoon, anime, painterly rendering, "
            "synthetic CGI appearance"
        ),
        "denoise": 0.68,
        "structure_weight": 0.90,
        "color_boost": 0.44,
        "keywords": [
            "1960s",
            "psychological",
            "close-up",
            "black-and-white",
            "negative-space",
            "window-light",
            "faces",
            "introspection",
        ],
    },

    "bergman_1970s": {
        "name": "Bergman - Color 1970s",
        "category": "cinematic",
        "era": "1970s",
        "prompt": (
            "1970s Scandinavian color cinema, restrained deep reds, muted creams "
            "and subdued natural tones, intimate interior photography, "
            "soft directional window light, carefully controlled shadows, "
            "expressive faces, precise close framing, tactile fabrics and walls, "
            "natural skin tones, subtle film grain, low saturation, "
            "quiet psychological tension, minimalist composition, "
            "rich but controlled cinematic color"
        ),
        "negative_prompt": (
            "neon colors, excessive saturation, glossy commercial look, "
            "orange-teal grading, beauty retouching, plastic skin, "
            "artificial HDR, excessive bloom, fantasy lighting, cartoon, anime, "
            "painterly rendering, synthetic CGI appearance"
        ),
        "denoise": 0.69,
        "structure_weight": 0.89,
        "color_boost": 0.62,
        "keywords": [
            "1970s",
            "color-film",
            "deep-red",
            "muted",
            "interior",
            "faces",
            "psychological",
            "film-grain",
        ],
    },

    "bergman_portrait": {
        "name": "Bergman - Psychological Portrait",
        "category": "cinematic",
        "era": "portrait",
        "prompt": (
            "intense psychological cinematic portrait, extremely close facial framing, "
            "natural human skin texture, visible subtle imperfections, "
            "soft directional window light, sculpted facial planes, "
            "deep controlled shadows, luminous eyes, restrained neutral palette, "
            "minimal background, dramatic negative space, subtle organic film grain, "
            "quiet emotional tension, realistic expression, "
            "observational photographic realism"
        ),
        "negative_prompt": (
            "beauty photography, glamour retouching, perfect skin, plastic texture, "
            "excessive makeup, excessive bokeh, glossy commercial lighting, "
            "oversaturated colors, fantasy glow, artificial HDR, cartoon, anime, "
            "painterly rendering, CGI appearance"
        ),
        "denoise": 0.64,
        "structure_weight": 0.91,
        "color_boost": 0.46,
        "keywords": [
            "portrait",
            "psychological",
            "close-up",
            "face",
            "window-light",
            "negative-space",
            "natural-skin",
            "intimate",
        ],
    },

    "bergman_nordic_landscape": {
        "name": "Bergman - Nordic Landscape",
        "category": "cinematic",
        "era": "landscape",
        "prompt": (
            "Nordic cinematic landscape photography, austere Scandinavian environment, "
            "soft overcast daylight, pale skies, muted earth tones, "
            "coastal rocks, sparse vegetation, quiet rural architecture, "
            "deep atmospheric perspective, restrained composition, "
            "natural weather conditions, subtle mist, realistic physical textures, "
            "organic film grain, subdued contrast, contemplative silence, "
            "minimalist photographic realism"
        ),
        "negative_prompt": (
            "tropical landscape, vivid saturated colors, fantasy environment, "
            "dramatic artificial sky, excessive HDR, excessive sharpening, "
            "glossy travel photography, neon colors, cartoon, anime, "
            "painterly rendering, synthetic CGI appearance"
        ),
        "denoise": 0.67,
        "structure_weight": 0.88,
        "color_boost": 0.50,
        "keywords": [
            "Nordic",
            "landscape",
            "overcast",
            "minimalist",
            "mist",
            "muted",
            "rural",
            "atmospheric",
        ],
    },
}


__all__ = ["BERGMAN_STYLES"]
