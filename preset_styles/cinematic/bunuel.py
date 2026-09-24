"""
CharacterForge Cinematic - Luis Buñuel
=======================================

Preset cinematografici ispirati alla grammatica visiva di Luis Buñuel:
realismo quotidiano contaminato dal surrealismo, composizioni sobrie,
simbolismo, straniamento, atmosfera onirica e perturbazione della
normalità attraverso dettagli visivi inattesi.
"""

BUNUEL_STYLES = {

    "bunuel_surrealist": {
        "name": "Buñuel - Surrealist Realism",
        "category": "cinematic",
        "era": "1960s-1970s",
        "prompt": (
            "European surrealist cinema, ordinary realistic environment "
            "with subtly impossible details, restrained classical composition, "
            "static or gently observational camera, naturalistic lighting, "
            "muted earth tones, understated production design, "
            "precise architectural framing, dry atmosphere, "
            "fine 35mm film grain, realistic textures, "
            "quiet visual absurdity, dream logic invading everyday reality"
        ),
        "negative_prompt": (
            "colorful fantasy world, cartoon surrealism, psychedelic overload, "
            "excessive visual effects, glossy digital cinema, neon colors, "
            "HDR, chaotic composition, superhero aesthetics, CGI appearance"
        ),
        "denoise": 0.76,
        "structure_weight": 0.91,
        "color_boost": 0.78,
        "keywords": [
            "surrealism",
            "realism",
            "dream_logic",
            "absurdity",
            "35mm",
            "european_cinema"
        ],
    },

    "bunuel_discreet_charm": {
        "name": "Buñuel - Discreet Absurdity",
        "category": "cinematic",
        "era": "1970s",
        "prompt": (
            "elegant European interiors, bourgeois dinner setting, "
            "formal symmetrical architecture, impeccably dressed characters, "
            "calm naturalistic illumination, muted beige gray and brown palette, "
            "precise classical framing, restrained facial expressions, "
            "subtle visual repetition, polite social atmosphere hiding absurdity, "
            "fine-grain 35mm photography, understated surreal tension, "
            "dry observational cinematic style"
        ),
        "negative_prompt": (
            "obvious horror, exaggerated acting, fantasy costumes, "
            "bright theatrical colors, horror lighting, digital sharpness, "
            "excessive camera movement, grotesque CGI, neon palette"
        ),
        "denoise": 0.72,
        "structure_weight": 0.94,
        "color_boost": 0.76,
        "keywords": [
            "bourgeois",
            "dinner",
            "symmetry",
            "social_satire",
            "absurdity",
            "subtle_surrealism"
        ],
    },

    "bunuel_belle_de_jour": {
        "name": "Buñuel - Belle de Jour",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "1960s European psychological cinema, elegant Parisian interiors, "
            "soft daylight through curtains, refined bourgeois spaces, "
            "controlled pastel and neutral palette, restrained color saturation, "
            "formal compositions interrupted by dreamlike details, "
            "medium framing, subtle depth of field, "
            "fine 35mm grain, soft optical rendering, "
            "quiet erotic tension without glamour, psychological ambiguity"
        ),
        "negative_prompt": (
            "modern fashion photography, explicit sexuality, glossy commercial look, "
            "neon lighting, oversaturated colors, HDR, extreme bokeh, "
            "digital sharpness, fantasy environment"
        ),
        "denoise": 0.71,
        "structure_weight": 0.89,
        "color_boost": 0.86,
        "keywords": [
            "1960s",
            "paris",
            "psychological",
            "bourgeois",
            "dreamlike",
            "35mm"
        ],
    },

    "bunuel_dark_symbolism": {
        "name": "Buñuel - Dark Symbolism",
        "category": "cinematic",
        "era": "1960s-1970s",
        "prompt": (
            "dark European art cinema, realistic interiors and decaying architecture, "
            "subdued natural light, deep but controlled shadows, "
            "symbolic objects placed within ordinary environments, "
            "muted ochre gray brown and black palette, "
            "static observational framing, unsettling empty spaces, "
            "fine analog film grain, restrained contrast, "
            "quiet psychological unease, surreal symbolism emerging from realism"
        ),
        "negative_prompt": (
            "gothic fantasy, supernatural horror effects, neon colors, "
            "excessive darkness, horror jump-scare aesthetic, "
            "digital CGI, glossy surfaces, oversaturated cinematic grading"
        ),
        "denoise": 0.77,
        "structure_weight": 0.93,
        "color_boost": 0.70,
        "keywords": [
            "symbolism",
            "dark",
            "surrealism",
            "decay",
            "psychological",
            "analog"
        ],
    },

    "bunuel_dream_reality": {
        "name": "Buñuel - Dream and Reality",
        "category": "cinematic",
        "era": "1970s",
        "prompt": (
            "European dream-reality cinema, realistic location transformed subtly "
            "by impossible continuity, repeated spaces, unexplained objects, "
            "ordinary daylight, restrained naturalistic color, "
            "static compositions, formal blocking, "
            "clean architectural geometry, ambiguous temporal atmosphere, "
            "soft 35mm film grain, realistic skin and material textures, "
            "deadpan surrealism, dream logic presented as everyday reality"
        ),
        "negative_prompt": (
            "psychedelic fantasy, glowing objects, magical effects, "
            "cartoon surrealism, excessive lens distortion, "
            "neon colors, glossy digital rendering, chaotic camera movement, "
            "obvious CGI"
        ),
        "denoise": 0.79,
        "structure_weight": 0.90,
        "color_boost": 0.74,
        "keywords": [
            "dream_reality",
            "deadpan",
            "surrealism",
            "continuity",
            "symbolic",
            "35mm"
        ],
    },
}


__all__ = ["BUNUEL_STYLES"]
