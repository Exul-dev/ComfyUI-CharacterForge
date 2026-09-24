"""
CharacterForge Cinematic - John Ford
=====================================

Preset cinematografici ispirati al cinema di John Ford:
composizioni epiche, paesaggi monumentali, controluce,
western classico, profondità scenica e fotografia in 35mm.
"""

FORD_STYLES = {

    "ford_western": {
        "name": "Ford - Classic Western",
        "category": "cinematic",
        "era": "1940s-1950s",
        "prompt": (
            "classic American western cinematography, monumental desert landscape, "
            "vast open sky, lone rider or small group framed against enormous terrain, "
            "strong horizontal composition, deep staging, natural sunlight, "
            "dramatic cloud formations, warm earth tones, dusty atmosphere, "
            "35mm film grain, restrained contrast, authentic period western costume, "
            "poetic frontier atmosphere, iconic cinematic silhouette"
        ),
        "negative_prompt": (
            "modern western, contemporary vehicles, neon lighting, "
            "fantasy landscape, glossy digital photography, "
            "excessive saturation, superhero posing, HDR, "
            "extreme shallow depth of field"
        ),
        "denoise": 0.73,
        "structure_weight": 0.94,
        "color_boost": 0.88,
        "keywords": [
            "classic_western",
            "frontier",
            "desert",
            "monumental_landscape",
            "35mm",
            "american_cinema"
        ],
    },

    "ford_monument_valley": {
        "name": "Ford - Monument Valley",
        "category": "cinematic",
        "era": "1940s-1950s",
        "prompt": (
            "Monument Valley inspired western landscape, towering red sandstone formations, "
            "vast blue sky, tiny human figures against immense geological structures, "
            "low horizon, carefully balanced negative space, "
            "golden sunlight, long shadows, dusty wind, "
            "warm sandstone palette, deep atmospheric perspective, "
            "classic 35mm film texture, monumental American frontier imagery"
        ),
        "negative_prompt": (
            "city skyline, lush tropical vegetation, fantasy castles, "
            "modern clothing, oversaturated orange, HDR, "
            "digital matte painting appearance, excessive lens flare"
        ),
        "denoise": 0.74,
        "structure_weight": 0.97,
        "color_boost": 0.96,
        "keywords": [
            "monument_valley",
            "sandstone",
            "western",
            "frontier",
            "wide_landscape",
            "golden_light"
        ],
    },

    "ford_cavalry": {
        "name": "Ford - Cavalry",
        "category": "cinematic",
        "era": "1940s-1960s",
        "prompt": (
            "classic cavalry western, disciplined horse formation moving across frontier terrain, "
            "wide panoramic composition, layered riders and horses, "
            "dust rising behind the formation, strong afternoon sunlight, "
            "natural shadows, authentic 19th century uniforms, "
            "deep focus, monumental landscape, restrained color palette, "
            "subtle 35mm grain, dignified military procession, "
            "epic but grounded American cinema"
        ),
        "negative_prompt": (
            "modern military uniforms, assault weapons, fantasy armor, "
            "video game aesthetics, excessive action blur, "
            "Hollywood blockbuster VFX, neon colors, glossy digital image"
        ),
        "denoise": 0.76,
        "structure_weight": 0.95,
        "color_boost": 0.84,
        "keywords": [
            "cavalry",
            "horsemen",
            "frontier",
            "formation",
            "western",
            "deep_focus"
        ],
    },

    "ford_family": {
        "name": "Ford - Family and Community",
        "category": "cinematic",
        "era": "1940s-1950s",
        "prompt": (
            "warm American family drama, rural community gathering, "
            "large group composition with natural interpersonal relationships, "
            "porch or farmhouse setting, soft afternoon sunlight, "
            "wooden architecture, dusty roads, authentic period clothing, "
            "balanced ensemble framing, gentle shadows, "
            "warm restrained earth tones, subtle 35mm grain, "
            "humanistic classical Hollywood cinematography"
        ),
        "negative_prompt": (
            "modern suburban architecture, fashion photography, "
            "glossy commercial lighting, artificial posing, "
            "extreme bokeh, oversaturated colors, digital sharpness"
        ),
        "denoise": 0.71,
        "structure_weight": 0.90,
        "color_boost": 0.86,
        "keywords": [
            "family",
            "community",
            "rural",
            "ensemble",
            "humanistic",
            "classical_hollywood"
        ],
    },

    "ford_black_and_white": {
        "name": "Ford - Black and White Frontier",
        "category": "cinematic",
        "era": "1930s-1950s",
        "prompt": (
            "black and white American western, dramatic clouds over open frontier, "
            "high contrast sunlight, deep shadows, dusty terrain, "
            "wide landscape composition, strong silhouettes, "
            "weathered faces, horses and wooden structures, "
            "deep focus, authentic 35mm monochrome film grain, "
            "classic photographic contrast, monumental visual simplicity"
        ),
        "negative_prompt": (
            "color photography, modern objects, digital rendering, "
            "soft pastel lighting, excessive HDR, glossy surfaces, "
            "fantasy western, extreme shallow depth of field"
        ),
        "denoise": 0.75,
        "structure_weight": 0.95,
        "color_boost": 0.60,
        "keywords": [
            "black_and_white",
            "western",
            "monochrome",
            "frontier",
            "silhouette",
            "35mm"
        ],
    },
}


__all__ = ["FORD_STYLES"]
