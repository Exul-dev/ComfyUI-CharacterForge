"""
CharacterForge Cinematic - Akira Kurosawa
==========================================

Preset cinematografici ispirati all'evoluzione della fotografia,
della composizione e della messa in scena del cinema di Akira Kurosawa.

Focus:
- composizioni dinamiche
- profondità spaziale
- luce naturale e atmosferica
- contrasto deciso
- movimento e direzione visiva
- paesaggi monumentali
- texture fotografica organica
- rapporto tra personaggi e ambiente
"""

KUROSAWA_STYLES = {
    "kurosawa_1950s": {
        "name": "Kurosawa - Classic 1950s",
        "category": "cinematic",
        "era": "1950s",
        "prompt": (
            "classic 1950s Japanese cinema photography, high-contrast black and white "
            "visual language, dynamic composition, deep spatial perspective, "
            "strong atmospheric depth, dramatic natural light, expressive faces, "
            "textured environments, precise framing, powerful silhouettes, "
            "visible 35mm film grain, rich blacks, luminous highlights, "
            "realistic skin texture, rain-soaked surfaces, wind and weather, "
            "strong visual storytelling, photographic realism"
        ),
        "negative_prompt": (
            "modern digital look, glossy photography, oversaturated colors, "
            "plastic skin, excessive HDR, artificial beauty lighting, "
            "soft commercial lighting, excessive bloom, cartoon, anime, "
            "painterly rendering, synthetic CGI appearance"
        ),
        "denoise": 0.70,
        "structure_weight": 0.88,
        "color_boost": 0.54,
        "keywords": [
            "black-and-white",
            "1950s",
            "high-contrast",
            "deep-focus",
            "35mm",
            "dramatic",
            "weather",
            "realism",
        ],
    },

    "kurosawa_1960s": {
        "name": "Kurosawa - Dynamic 1960s",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "1960s Japanese cinematic photography, dynamic widescreen composition, "
            "strong horizontal and diagonal movement, deep environmental perspective, "
            "dramatic natural daylight, bold shadows, textured landscapes, "
            "precise blocking, expressive character silhouettes, powerful weather "
            "conditions, dust, rain and wind, restrained color palette, "
            "organic 35mm film grain, realistic skin tones, tactile environments, "
            "strong visual rhythm, cinematic photographic realism"
        ),
        "negative_prompt": (
            "flat composition, static framing, glossy commercial aesthetic, "
            "oversaturated colors, artificial HDR, plastic surfaces, "
            "beauty retouching, excessive bloom, fantasy glow, cartoon, anime, "
            "painterly rendering, synthetic CGI appearance"
        ),
        "denoise": 0.68,
        "structure_weight": 0.91,
        "color_boost": 0.60,
        "keywords": [
            "1960s",
            "widescreen",
            "dynamic",
            "diagonal",
            "weather",
            "natural-light",
            "35mm",
            "environment",
        ],
    },

    "kurosawa_1970s": {
        "name": "Kurosawa - Color 1970s",
        "category": "cinematic",
        "era": "1970s",
        "prompt": (
            "1970s Japanese color cinema, restrained earthy color palette, "
            "rich reds and muted natural tones, dramatic environmental composition, "
            "strong directional sunlight, atmospheric landscapes, deep shadows, "
            "textured architecture, expressive human figures within large spaces, "
            "organic 35mm film texture, natural skin tones, controlled saturation, "
            "weathered surfaces, powerful silhouettes, cinematic depth, "
            "authentic period photographic realism"
        ),
        "negative_prompt": (
            "modern digital color science, neon colors, excessive saturation, "
            "orange-teal grading, glossy commercial photography, plastic skin, "
            "artificial HDR, excessive sharpening, excessive bloom, cartoon, anime, "
            "painterly rendering, synthetic CGI appearance"
        ),
        "denoise": 0.69,
        "structure_weight": 0.90,
        "color_boost": 0.68,
        "keywords": [
            "1970s",
            "color-film",
            "earth-tones",
            "red",
            "natural-light",
            "35mm",
            "weathered",
            "dramatic",
        ],
    },

    "kurosawa_samurai": {
        "name": "Kurosawa - Samurai Epic",
        "category": "cinematic",
        "era": "samurai",
        "prompt": (
            "epic historical Japanese cinema, samurai-era environment, "
            "monumental natural landscapes, dramatic cloudy sky, rain, mist and wind, "
            "dynamic group composition, powerful silhouettes, layered depth, "
            "precise character blocking, textured traditional architecture, "
            "muddy ground, weathered fabrics and armor, natural directional light, "
            "restrained earthy colors, authentic physical materials, "
            "organic film texture, strong atmospheric perspective, "
            "grounded historical photographic realism"
        ),
        "negative_prompt": (
            "fantasy armor, glossy costumes, video-game appearance, neon colors, "
            "plastic materials, excessive CGI, magical effects, excessive bloom, "
            "anime, cartoon, painterly rendering, artificial HDR, "
            "modern architecture, modern clothing"
        ),
        "denoise": 0.67,
        "structure_weight": 0.94,
        "color_boost": 0.62,
        "keywords": [
            "samurai",
            "historical",
            "epic",
            "rain",
            "wind",
            "mist",
            "earth-tones",
            "deep-space",
        ],
    },

    "kurosawa_humanist": {
        "name": "Kurosawa - Humanist Drama",
        "category": "cinematic",
        "era": "humanist",
        "prompt": (
            "humanist Japanese dramatic cinema, intimate but spatially aware framing, "
            "natural human expressions, realistic skin texture, restrained tonal palette, "
            "soft natural daylight, practical interior lighting, "
            "deep environmental context, carefully arranged characters, "
            "authentic everyday environments, subtle film grain, "
            "weathered physical surfaces, realistic imperfections, "
            "quiet emotional tension, observational photographic realism"
        ),
        "negative_prompt": (
            "glamour photography, beauty retouching, plastic skin, "
            "excessive bokeh, dreamy fantasy lighting, oversaturated colors, "
            "glossy commercial aesthetic, artificial HDR, cartoon, anime, "
            "painterly rendering, synthetic CGI appearance"
        ),
        "denoise": 0.66,
        "structure_weight": 0.86,
        "color_boost": 0.56,
        "keywords": [
            "humanist",
            "drama",
            "natural",
            "intimate",
            "observational",
            "realism",
            "film-grain",
            "Japanese-cinema",
        ],
    },
}


__all__ = ["KUROSAWA_STYLES"]
