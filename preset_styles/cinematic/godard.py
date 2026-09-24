"""
CharacterForge Cinematic - Jean-Luc Godard
===========================================

Preset cinematografici ispirati al linguaggio visivo della Nouvelle Vague:
jump cuts, composizioni spontanee, colori primari, camera mobile,
strada, appartamenti, fotografia urbana e sperimentazione narrativa.
"""

GODARD_STYLES = {

    "godard_nouvelle_vague": {
        "name": "Godard - Nouvelle Vague",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "French New Wave cinema, spontaneous street photography, "
            "handheld 35mm camera, unconventional framing, natural performances, "
            "urban Paris streets, intimate medium shots, available light, "
            "highly expressive composition, subtle film grain, "
            "black and white photographic texture, imperfect exposure, "
            "documentary immediacy, youthful European atmosphere"
        ),
        "negative_prompt": (
            "polished Hollywood cinematography, perfect studio lighting, "
            "digital sharpness, glossy skin, excessive bokeh, HDR, "
            "fantasy atmosphere, modern commercial photography, "
            "overly symmetrical composition"
        ),
        "denoise": 0.74,
        "structure_weight": 0.82,
        "color_boost": 0.78,
        "keywords": [
            "nouvelle_vague",
            "french_cinema",
            "handheld",
            "street",
            "35mm",
            "naturalistic"
        ],
    },

    "godard_breathless": {
        "name": "Godard - Breathless",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "1960s Paris, black and white French New Wave photography, "
            "restless handheld camera, jump-cut energy, spontaneous street composition, "
            "close observational framing, natural daylight, cigarette smoke, "
            "Parisian boulevards, compact cars, intimate interiors, "
            "high contrast monochrome film, visible grain, imperfect focus, "
            "raw youthful atmosphere, unconventional cinematic framing"
        ),
        "negative_prompt": (
            "modern Paris, smartphones, contemporary vehicles, "
            "digital cinema, clean commercial photography, "
            "perfect focus, glossy fashion editorial, color grading, "
            "Hollywood action lighting"
        ),
        "denoise": 0.77,
        "structure_weight": 0.80,
        "color_boost": 0.70,
        "keywords": [
            "breathless",
            "paris",
            "black_and_white",
            "jump_cut",
            "street",
            "raw"
        ],
    },

    "godard_primary_color": {
        "name": "Godard - Primary Color",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "French New Wave visual experimentation, flat architectural compositions, "
            "bold blocks of primary red blue and yellow, minimalist interiors, "
            "graphic typography-like geometry, theatrical color placement, "
            "naturalistic actors inside highly designed environments, "
            "35mm film texture, restrained shadows, direct frontal compositions, "
            "playful intellectual visual language, European modernist cinema"
        ),
        "negative_prompt": (
            "photorealistic commercial advertising, pastel palette, "
            "neon cyberpunk, excessive gradients, glossy surfaces, "
            "3D render appearance, extreme depth of field, HDR"
        ),
        "denoise": 0.72,
        "structure_weight": 0.91,
        "color_boost": 1.05,
        "keywords": [
            "primary_colors",
            "graphic",
            "modernist",
            "french_new_wave",
            "experimental",
            "geometry"
        ],
    },

    "godard_urban_poetry": {
        "name": "Godard - Urban Poetry",
        "category": "cinematic",
        "era": "1960s-1970s",
        "prompt": (
            "poetic urban cinema, Parisian streets, fragmented human interactions, "
            "observational camera, off-center framing, spontaneous movement, "
            "natural daylight, reflective windows, handwritten signs, "
            "casual clothing, muted European colors, subtle grain, "
            "intellectual melancholy mixed with playful energy, "
            "experimental composition, authentic street atmosphere"
        ),
        "negative_prompt": (
            "epic cinematography, heroic poses, luxury commercial look, "
            "overly dramatic lighting, fantasy environment, "
            "hyper-saturated colors, digital perfection, staged studio scene"
        ),
        "denoise": 0.75,
        "structure_weight": 0.85,
        "color_boost": 0.84,
        "keywords": [
            "urban_poetry",
            "paris",
            "street",
            "experimental",
            "observational",
            "european"
        ],
    },

    "godard_experimental": {
        "name": "Godard - Experimental Cinema",
        "category": "cinematic",
        "era": "1970s",
        "prompt": (
            "experimental European cinema, deliberately fragmented composition, "
            "unconventional camera angles, visual discontinuity, "
            "mixed photographic textures, abrupt changes in scale, "
            "graphic color blocks, natural light colliding with artificial light, "
            "raw 16mm and 35mm film texture, visible grain and imperfect exposure, "
            "conceptual visual language, anti-commercial aesthetic, "
            "intellectual cinematic experimentation"
        ),
        "negative_prompt": (
            "conventional Hollywood composition, polished commercial lighting, "
            "perfect symmetry, glossy digital image, excessive realism, "
            "clean CGI appearance, generic cinematic framing"
        ),
        "denoise": 0.79,
        "structure_weight": 0.87,
        "color_boost": 0.92,
        "keywords": [
            "experimental",
            "fragmentation",
            "16mm",
            "35mm",
            "conceptual",
            "avant_garde"
        ],
    },
}


__all__ = ["GODARD_STYLES"]
