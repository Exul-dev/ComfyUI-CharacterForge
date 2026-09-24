"""
CharacterForge Cinematic - Wong Kar-wai
=======================================

Visual language inspired by Wong Kar-wai's cinema:
intimate urban spaces, saturated practical light, expressive
color separation, optical motion trails, step-printing aesthetics,
shallow and medium depth of field, reflective surfaces, fragmented
compositions and emotionally charged nocturnal photography.
"""

WONG_KAR_WAI_STYLES = {

    "wong_kar_wai_1990s": {
        "name": "Wong Kar-wai 1990s",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "1990s Hong Kong arthouse cinematography, 35mm and 50mm lenses, "
            "intimate handheld camera, compressed urban interiors, narrow corridors, "
            "small apartments and crowded streets, saturated practical lighting, "
            "green fluorescent light mixed with warm tungsten, deep red and amber accents, "
            "wet pavement reflections, mirrors and glass surfaces, "
            "shallow to moderate depth of field, soft optical focus, "
            "slow shutter motion trails, expressive subject movement, "
            "step-printing inspired temporal blur, visible 35mm film grain, "
            "subtle halation, imperfect framing, off-center compositions, "
            "characters partially obscured by foreground objects, "
            "melancholic nocturnal atmosphere, dense urban texture"
        ),
        "negative_prompt": (
            "clean digital cinema, sterile composition, perfect symmetry, "
            "generic bokeh, excessive HDR, hyper-sharp skin, daylight commercial photography, "
            "modern LED lighting, plastic surfaces, empty environments"
        ),
        "denoise": 0.49,
        "structure_weight": 0.83,
        "color_boost": 1.04,
        "keywords": [
            "Hong Kong",
            "1990s",
            "35mm",
            "50mm",
            "step printing",
            "motion trails",
            "neon",
            "film grain"
        ],
    },

    "wong_kar_wai_chungking": {
        "name": "Wong Kar-wai Urban Neon",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "dense Hong Kong night cinematography, 28mm and 35mm wide-angle lenses, "
            "close proximity to subjects, handheld camera, narrow urban streets, "
            "food stalls, storefronts and cramped interiors, saturated green fluorescent "
            "light contrasted with deep red, orange and amber practical lights, "
            "wet asphalt reflections, colored glass, mirrors and reflective metal, "
            "slow shutter motion streaks, step-printing aesthetic, "
            "strong temporal blur around moving figures, shallow and medium depth of field, "
            "soft 35mm optical rendering, visible film grain, halation around practical lights, "
            "fragmented framing, characters cropped by the edge of frame, "
            "layered foreground obstructions, intimate restless urban atmosphere"
        ),
        "negative_prompt": (
            "clean futuristic city, cyberpunk worldbuilding, sterile neon, "
            "perfectly sharp motion, CGI streets, excessive depth of field, "
            "symmetrical commercial composition, modern digital sensor look"
        ),
        "denoise": 0.51,
        "structure_weight": 0.81,
        "color_boost": 1.10,
        "keywords": [
            "Hong Kong",
            "urban neon",
            "28mm",
            "35mm",
            "green fluorescent",
            "red light",
            "motion streaks",
            "step printing"
        ],
    },

    "wong_kar_wai_in_the_mood": {
        "name": "Wong Kar-wai Romantic Restraint",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "intimate romantic cinematography, 50mm and 75mm lenses, "
            "compressed perspective, restrained camera movement, elegant shallow depth of field, "
            "characters framed through doorways, curtains, mirrors and narrow architectural gaps, "
            "warm tungsten practicals, soft window light, muted red, amber, brown and dark green palette, "
            "rich textile textures, patterned wallpaper, wood and aged interiors, "
            "subtle underexposure, soft highlight rolloff, fine 35mm film grain, "
            "gentle halation, delicate motion blur, slow controlled movement, "
            "long-lens observation, negative space between characters, "
            "melancholic romantic atmosphere, restrained physical intimacy"
        ),
        "negative_prompt": (
            "bright commercial romance, pastel wedding photography, "
            "extreme bokeh, glossy skin, modern minimalist interiors, "
            "high-key lighting, excessive saturation, digital sharpness"
        ),
        "denoise": 0.46,
        "structure_weight": 0.87,
        "color_boost": 0.92,
        "keywords": [
            "romantic",
            "50mm",
            "75mm",
            "shallow depth",
            "tungsten",
            "textile",
            "35mm grain",
            "melancholy"
        ],
    },

    "wong_kar_wai_2046": {
        "name": "Wong Kar-wai Futuristic Memory",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "stylized futuristic romantic cinematography grounded in analog film photography, "
            "35mm and 50mm lenses, selective wide-angle perspectives, reflective surfaces, "
            "train interiors, corridors and enclosed architectural spaces, "
            "deep crimson, amber, emerald and electric blue practical lighting, "
            "soft atmospheric haze, controlled backlight, reflective glass and polished metal, "
            "moderate shallow depth of field, elegant camera movement, "
            "slow-motion fragments, subtle temporal distortion, "
            "visible 35mm grain, optical halation, gentle chromatic color separation, "
            "rich production design with period-futurist textures, "
            "dreamlike melancholy, visual memory rather than literal realism"
        ),
        "negative_prompt": (
            "generic cyberpunk, videogame science fiction, sterile CGI, "
            "excessive neon, hard digital edges, HDR, plastic materials, "
            "military sci-fi, generic futuristic city"
        ),
        "denoise": 0.50,
        "structure_weight": 0.85,
        "color_boost": 1.05,
        "keywords": [
            "futuristic memory",
            "35mm",
            "50mm",
            "crimson",
            "emerald",
            "amber",
            "reflective surfaces",
            "analog sci-fi"
        ],
    },

    "wong_kar_wai_motion": {
        "name": "Wong Kar-wai Motion Blur",
        "category": "cinematic",
        "era": "1990s-2000s",
        "prompt": (
            "expressive motion-blur cinematography, 35mm film camera, "
            "slow shutter photography combined with controlled camera movement, "
            "subject partially sharp against streaking urban lights, "
            "step-printing inspired temporal fragmentation, "
            "28mm and 35mm lenses for intimate proximity, "
            "saturated red, green, yellow and blue practical lights, "
            "wet reflective streets, glass, mirrors and chrome surfaces, "
            "soft focus transitions, visible analog grain, halation, "
            "off-center compositions, diagonal framing, foreground obstructions, "
            "characters isolated inside dense urban environments, "
            "dreamlike nocturnal atmosphere, emotional subjectivity expressed through optics"
        ),
        "negative_prompt": (
            "accidental motion blur, completely unreadable image, "
            "digital smear, excessive sharpening, sterile studio photography, "
            "flat lighting, empty backgrounds, generic action photography"
        ),
        "denoise": 0.52,
        "structure_weight": 0.79,
        "color_boost": 1.08,
        "keywords": [
            "motion blur",
            "slow shutter",
            "step printing",
            "35mm",
            "urban night",
            "reflections",
            "fragmentation",
            "dreamlike"
        ],
    },
}

__all__ = ["WONG_KAR_WAI_STYLES"]
