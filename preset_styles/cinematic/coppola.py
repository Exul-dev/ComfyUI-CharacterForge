"""
CharacterForge Cinematic - Francis Ford Coppola
================================================

Cinematic presets inspired by Francis Ford Coppola:
classical American composition, deep-focus staging, expressive practical
lighting, warm and shadow-rich interiors, anamorphic widescreen imagery,
operatic visual scale, period texture, intimate character photography,
and carefully choreographed ensemble scenes.
"""

COPPOLA_STYLES = {

    "coppola_godfather": {
        "name": "Francis Ford Coppola — The Godfather",
        "category": "cinematic",
        "era": "1970s",
        "prompt": (
            "1970s American crime cinema, warm low-key interior lighting, deep "
            "brown and amber palette, extremely controlled shadows, faces partially "
            "falling into darkness, practical table lamps and overhead fixtures, "
            "rich wood interiors, dark suits, aged leather and textured walls, "
            "35mm anamorphic photography, moderate depth of field, carefully "
            "composed medium shots, restrained camera movement, strong negative "
            "space, deep blacks, warm skin tones, subtle film grain, soft "
            "photochemical highlights, elegant period production design, "
            "quiet visual authority, intimate family drama photographed with "
            "operatic seriousness"
        ),
        "negative_prompt": (
            "modern digital cinema, glossy crime thriller, neon lighting, "
            "oversaturated colors, flat illumination, excessive bokeh, "
            "clean contemporary interiors, plastic textures, television look, "
            "action-movie spectacle"
        ),
        "denoise": 0.79,
        "structure_weight": 0.89,
        "color_boost": 1.08,
        "keywords": [
            "1970s crime cinema",
            "low-key lighting",
            "amber",
            "deep shadows",
            "35mm anamorphic",
            "wood interiors",
            "film grain"
        ],
    },

    "coppola_apocalypse": {
        "name": "Francis Ford Coppola — Apocalypse Now",
        "category": "cinematic",
        "era": "1970s",
        "prompt": (
            "1970s war epic cinematography, humid tropical landscape, dense jungle, "
            "river mist, smoke, fire and rain, monumental anamorphic widescreen, "
            "deep green vegetation contrasted with orange firelight and dirty amber "
            "sunset, atmospheric haze, silhouettes disappearing into darkness, "
            "35mm anamorphic lenses, long lateral compositions, deep environmental "
            "perspective, slow tracking movement, helicopter-scale vistas, practical "
            "explosions and smoke, weathered military equipment, mud, sweat and "
            "water-saturated textures, rich film grain, soft highlight rolloff, "
            "dreamlike scale grounded in physical photographic texture"
        ),
        "negative_prompt": (
            "clean military imagery, modern digital war photography, glossy action "
            "movie, sterile jungle, oversaturated tropical colors, videogame "
            "battlefield, artificial CGI smoke, excessive sharpness, superhero framing"
        ),
        "denoise": 0.84,
        "structure_weight": 0.91,
        "color_boost": 1.1,
        "keywords": [
            "war epic",
            "tropical jungle",
            "anamorphic",
            "smoke",
            "firelight",
            "deep green",
            "amber",
            "1970s film grain"
        ],
    },

    "coppola_70s_american": {
        "name": "Francis Ford Coppola — 1970s American Drama",
        "category": "cinematic",
        "era": "1970s",
        "prompt": (
            "1970s American character drama, naturalistic urban locations, "
            "practical tungsten interiors, overcast exterior daylight, muted "
            "brown, beige, gray and faded blue palette, 35mm spherical and "
            "anamorphic photography, moderate depth of field, carefully layered "
            "foreground and background staging, long observational takes, "
            "subtle handheld movement, realistic apartment interiors, worn "
            "architecture, period clothing and analog objects, soft film grain, "
            "slightly imperfect exposure, natural skin tones, restrained contrast, "
            "human-scale compositions, visual realism with formal classical control"
        ),
        "negative_prompt": (
            "modern commercial photography, glossy digital image, neon colors, "
            "perfectly clean interiors, excessive shallow depth of field, "
            "fashion editorial lighting, artificial HDR, videogame rendering"
        ),
        "denoise": 0.78,
        "structure_weight": 0.84,
        "color_boost": 0.97,
        "keywords": [
            "1970s America",
            "character drama",
            "35mm",
            "tungsten",
            "urban realism",
            "muted palette",
            "period texture"
        ],
    },

    "coppola_one_from_the_heart": {
        "name": "Francis Ford Coppola — One from the Heart",
        "category": "cinematic",
        "era": "1980s",
        "prompt": (
            "stylized romantic cinematic spectacle, artificial Las Vegas night, "
            "large practical neon signs, theatrical production design, saturated "
            "magenta, cyan, red and amber lighting, glowing practical architecture, "
            "wide anamorphic compositions, controlled shallow depth of field, "
            "soft diffusion filters, deliberate lens flares, reflective wet streets, "
            "dreamlike studio realism, elaborate sets, choreographed camera movement, "
            "slow crane and dolly perspectives, rich color separation, romantic "
            "melancholy, analog film texture, visual excess controlled through "
            "precise composition"
        ),
        "negative_prompt": (
            "generic neon cyberpunk, modern LED aesthetic, photorealistic street "
            "photography, sterile CGI, random color noise, flat lighting, "
            "videogame city, excessive digital sharpness, generic music video"
        ),
        "denoise": 0.83,
        "structure_weight": 0.86,
        "color_boost": 1.25,
        "keywords": [
            "theatrical neon",
            "Las Vegas",
            "magenta",
            "cyan",
            "anamorphic",
            "studio spectacle",
            "romantic fantasy"
        ],
    },

    "coppola_epic_family": {
        "name": "Francis Ford Coppola — Operatic Family Saga",
        "category": "cinematic",
        "era": "1970s–1990s",
        "prompt": (
            "operatic family saga cinematography, large ensemble staging, layered "
            "characters across multiple depth planes, deep-focus photography, "
            "warm practical interiors contrasted with cool exterior daylight, "
            "rich burgundy, dark green, brown, cream and gold palette, elegant "
            "period architecture, candlelight, fireplaces and tungsten fixtures, "
            "35mm anamorphic widescreen, controlled camera movement, slow dollies, "
            "carefully motivated reframing, expressive doorways and architectural "
            "frames, detailed costumes and props, subtle film grain, rich blacks, "
            "soft highlight rolloff, intimate close-ups embedded within large "
            "compositions, visual sense of family history and generational scale"
        ),
        "negative_prompt": (
            "soap opera lighting, modern glossy drama, shallow focus everywhere, "
            "generic period film, sterile sets, excessive digital grading, "
            "plastic costumes, artificial HDR, flat ensemble staging"
        ),
        "denoise": 0.81,
        "structure_weight": 0.92,
        "color_boost": 1.1,
        "keywords": [
            "family saga",
            "deep focus",
            "ensemble staging",
            "anamorphic",
            "candlelight",
            "burgundy",
            "generational drama"
        ],
    },
}

__all__ = ["COPPOLA_STYLES"]
