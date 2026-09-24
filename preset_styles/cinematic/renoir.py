"""
CharacterForge Cinematic - Jean Renoir
=======================================

Preset cinematografici ispirati alla grammatica visiva di Jean Renoir:
profondità di campo, piani multipli, macchina mobile, luce naturale,
ambienti organici, composizione fluida e rapporto dinamico tra personaggi
e spazio.
"""

RENOIR_STYLES = {

    "renoir_deep_focus": {
        "name": "Renoir - Deep Focus",
        "category": "cinematic",
        "era": "1930s-1940s",
        "prompt": (
            "classic French cinema, deep focus cinematography, "
            "multiple planes of action simultaneously readable, "
            "foreground middle ground and background characters, "
            "naturalistic lighting, soft daylight, fluid spatial composition, "
            "deep architectural perspective, realistic textures, "
            "subtle 35mm film grain, moderate contrast, "
            "organic staging, spontaneous human interaction, "
            "rich visual depth without artificial emphasis"
        ),
        "negative_prompt": (
            "extreme shallow depth of field, isolated subject only, "
            "modern commercial photography, HDR, glossy digital rendering, "
            "excessive bokeh, artificial studio lighting, "
            "static flat composition, oversaturated colors"
        ),
        "denoise": 0.72,
        "structure_weight": 0.96,
        "color_boost": 0.84,
        "keywords": [
            "deep_focus",
            "multiple_planes",
            "35mm",
            "french_cinema",
            "spatial_depth",
            "naturalistic"
        ],
    },

    "renoir_rules_of_game": {
        "name": "Renoir - The Rules of the Game",
        "category": "cinematic",
        "era": "1930s",
        "prompt": (
            "1930s French estate, elegant ensemble staging, "
            "large interconnected interior and garden spaces, "
            "characters distributed across multiple depths, "
            "deep focus, fluid camera movement, natural daylight, "
            "soft window illumination, subtle atmospheric haze, "
            "warm restrained monochrome or muted tones, "
            "fine 35mm film texture, sophisticated social choreography, "
            "spontaneous movement within carefully layered composition"
        ),
        "negative_prompt": (
            "modern mansion, television sitcom staging, "
            "isolated close-up composition, extreme bokeh, "
            "glossy fashion photography, digital sharpness, "
            "artificial spotlighting, oversaturated colors"
        ),
        "denoise": 0.74,
        "structure_weight": 0.97,
        "color_boost": 0.79,
        "keywords": [
            "ensemble",
            "estate",
            "deep_focus",
            "social_choreography",
            "1930s",
            "fluid_camera"
        ],
    },

    "renoir_riverbank": {
        "name": "Renoir - Riverbank Naturalism",
        "category": "cinematic",
        "era": "1930s",
        "prompt": (
            "French countryside by a river, natural outdoor cinematography, "
            "soft summer daylight, reflections on water, lush vegetation, "
            "organic framing through leaves and branches, "
            "characters naturally integrated into landscape, "
            "gentle camera movement, medium and wide compositions, "
            "warm but restrained tonal palette, delicate film grain, "
            "slightly soft optical rendering, humid atmospheric depth, "
            "poetic realism and spontaneous human presence"
        ),
        "negative_prompt": (
            "tourist postcard photography, oversaturated greens, "
            "dramatic fantasy landscape, HDR, excessive lens flare, "
            "digital sharpness, artificial fog, extreme bokeh"
        ),
        "denoise": 0.71,
        "structure_weight": 0.91,
        "color_boost": 0.92,
        "keywords": [
            "riverbank",
            "nature",
            "summer",
            "natural_light",
            "soft_focus",
            "french_countryside"
        ],
    },

    "renoir_human_ensemble": {
        "name": "Renoir - Human Ensemble",
        "category": "cinematic",
        "era": "1930s-1950s",
        "prompt": (
            "humanistic ensemble cinema, several characters interacting naturally "
            "within a shared environment, layered staging, "
            "foreground conversation with secondary action in background, "
            "deep focus, gentle camera movement, natural available light, "
            "soft shadows, realistic skin tones, warm neutral palette, "
            "fine 35mm grain, organic imperfections, "
            "unforced expressions and spontaneous body language, "
            "rich spatial relationships between people"
        ),
        "negative_prompt": (
            "single-subject portrait, rigid posing, fashion editorial, "
            "shallow depth of field, glossy studio lighting, "
            "digital commercial aesthetic, excessive saturation, HDR"
        ),
        "denoise": 0.70,
        "structure_weight": 0.94,
        "color_boost": 0.85,
        "keywords": [
            "ensemble",
            "humanistic",
            "deep_focus",
            "interaction",
            "natural_light",
            "staging"
        ],
    },

    "renoir_color_naturalism": {
        "name": "Renoir - Color Naturalism",
        "category": "cinematic",
        "era": "1950s-1960s",
        "prompt": (
            "French color cinematography, natural outdoor light, "
            "soft warm daylight, restrained saturated colors, "
            "rich greens, muted reds, natural skin tones, "
            "deep spatial composition, gentle optical softness, "
            "realistic fabrics and vegetation, subtle atmospheric perspective, "
            "organic camera placement, fine color film grain, "
            "human figures naturally embedded within environment, "
            "poetic realism without artificial color grading"
        ),
        "negative_prompt": (
            "modern digital color grading, teal and orange, neon colors, "
            "HDR, excessive saturation, glossy commercial photography, "
            "extreme bokeh, artificial rim lighting, plastic textures"
        ),
        "denoise": 0.73,
        "structure_weight": 0.92,
        "color_boost": 0.98,
        "keywords": [
            "color_naturalism",
            "french_cinema",
            "natural_light",
            "deep_focus",
            "color_film",
            "poetic_realism"
        ],
    },
}


__all__ = ["RENOIR_STYLES"]
