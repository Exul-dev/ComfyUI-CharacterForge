"""
CharacterForge Cinematic - Robert Zemeckis
==========================================

Visual language inspired by Zemeckis' cinematic evolution:
classic Hollywood adventure photography, dynamic compositions,
controlled spectacle, practical environments, expressive lighting,
precise camera movement and increasingly sophisticated integration
between live-action photography and visual effects.
"""

ZEMECKIS_STYLES = {

    "zemeckis_1980s": {
        "name": "Zemeckis 1980s Adventure",
        "category": "cinematic",
        "era": "1980s",
        "prompt": (
            "1980s Hollywood adventure cinematography, energetic but controlled camera language, "
            "35mm spherical lenses, moderate wide-angle perspective, dynamic compositions, "
            "clean deep-focus environments, practical locations, expressive backlight, "
            "warm tungsten interiors, bright natural daylight, strong motivated sources, "
            "rich but believable primary colors, warm skin tones, subtle cyan shadows, "
            "fine 35mm film grain, organic photochemical texture, crisp optical detail, "
            "carefully staged foreground and background action, practical props and vehicles, "
            "precise dolly and tracking movement, low-angle hero framing, adventurous atmosphere"
        ),
        "negative_prompt": (
            "modern digital cinema, teal and orange grading, excessive HDR, "
            "extreme shallow depth of field, sterile CGI appearance, excessive lens flares, "
            "hyperreal sharpening, desaturated modern palette, handheld chaos"
        ),
        "denoise": 0.48,
        "structure_weight": 0.83,
        "color_boost": 0.94,
        "keywords": [
            "1980s",
            "35mm",
            "adventure",
            "Hollywood",
            "practical effects",
            "deep focus",
            "dynamic camera",
            "film grain"
        ],
    },

    "zemeckis_back_to_the_future": {
        "name": "Zemeckis Time Adventure",
        "category": "cinematic",
        "era": "1980s",
        "prompt": (
            "classic 1980s time-travel adventure cinematography, anamorphic-inspired spectacle "
            "without excessive distortion, wide establishing shots, medium close-ups with "
            "strong environmental context, 35mm film response, precise dolly shots, "
            "rapid but readable camera movement, practical night exteriors, wet pavement, "
            "warm sodium-vapor street lighting, cool blue night ambience, glowing practical lights, "
            "strong rim and backlight used with motivation, saturated but controlled reds, blues "
            "and yellows, natural skin tones, visible fine film grain, subtle halation, "
            "clean optical contrast, carefully composed production design, mechanical details, "
            "period-specific props and vehicles, energetic sense of discovery"
        ),
        "negative_prompt": (
            "modern cyberpunk, neon overload, digital video texture, excessive bloom, "
            "extreme anamorphic distortion, crushed blacks, plastic skin, excessive bokeh, "
            "generic science-fiction design"
        ),
        "denoise": 0.47,
        "structure_weight": 0.85,
        "color_boost": 0.98,
        "keywords": [
            "time travel",
            "1980s adventure",
            "night exterior",
            "35mm",
            "practical lighting",
            "wet pavement",
            "film halation",
            "period production design"
        ],
    },

    "zemeckis_epic": {
        "name": "Zemeckis Epic Spectacle",
        "category": "cinematic",
        "era": "1990s-2000s",
        "prompt": (
            "large-scale Hollywood spectacle cinematography, 35mm film photography, "
            "wide spherical lenses combined with longer telephoto compression, "
            "monumental establishing compositions, strong foreground-background layering, "
            "precise crane and dolly movement, sweeping camera choreography, "
            "dramatic natural landscapes, volumetric sunlight used sparingly, "
            "golden-hour backlight, practical atmospheric haze, controlled highlights, "
            "rich earth tones and restrained saturated colors, realistic skin tones, "
            "fine-grain photochemical texture, subtle film halation, "
            "detailed production design, large crowds and environmental depth, "
            "spectacle grounded in believable physical space"
        ),
        "negative_prompt": (
            "video-game graphics, synthetic CGI surfaces, excessive HDR, "
            "plastic environments, extreme saturation, chaotic camera movement, "
            "generic fantasy lighting, excessive fog, digital sharpening"
        ),
        "denoise": 0.50,
        "structure_weight": 0.86,
        "color_boost": 0.92,
        "keywords": [
            "epic",
            "spectacle",
            "35mm",
            "crane shot",
            "deep space",
            "golden hour",
            "film texture",
            "large scale"
        ],
    },

    "zemeckis_human_drama": {
        "name": "Zemeckis Human Drama",
        "category": "cinematic",
        "era": "1990s-2000s",
        "prompt": (
            "classic American dramatic cinematography, 35mm and 50mm lenses, "
            "natural perspective, moderate depth of field, carefully motivated practical lighting, "
            "soft window daylight, warm household tungsten, gentle backlight, "
            "subtle contrast between warm interiors and cool exteriors, "
            "natural skin texture, restrained color grading, beige, brown, faded blue and green palette, "
            "fine 35mm grain, subtle halation, realistic optical softness, "
            "stable dolly movement, measured close-ups, balanced compositions, "
            "environmental storytelling, detailed practical locations, "
            "emotion expressed through framing and performance rather than visual excess"
        ),
        "negative_prompt": (
            "music-video aesthetics, excessive shallow focus, glossy commercial lighting, "
            "neon colors, extreme contrast, digital clinical sharpness, "
            "artificial rim lighting, exaggerated camera movement"
        ),
        "denoise": 0.45,
        "structure_weight": 0.84,
        "color_boost": 0.84,
        "keywords": [
            "human drama",
            "35mm",
            "50mm",
            "natural light",
            "practical interiors",
            "subtle grain",
            "balanced composition",
            "American cinema"
        ],
    },

    "zemeckis_digital_spectacle": {
        "name": "Zemeckis Digital Spectacle",
        "category": "cinematic",
        "era": "2000s-2010s",
        "prompt": (
            "early digital-era Hollywood spectacle with cinematic photographic discipline, "
            "35mm-derived visual language blended with controlled digital effects, "
            "precise virtual camera movement, wide environmental compositions, "
            "dynamic tracking and crane perspectives, physically motivated lighting, "
            "strong separation between foreground characters and digital environments, "
            "cool blue shadows with warm practical highlights, controlled saturation, "
            "realistic skin tones, moderate depth of field, subtle photographic grain overlay, "
            "soft highlight rolloff, detailed atmospheric perspective, "
            "complex production design, believable interaction between actors, props and environments, "
            "polished but still photographic cinematic texture"
        ),
        "negative_prompt": (
            "cheap CGI, video-game rendering, weightless characters, excessive motion blur, "
            "plastic skin, oversaturated digital colors, fake depth of field, "
            "hyper-sharp 8K appearance, synthetic lighting, cartoon rendering"
        ),
        "denoise": 0.46,
        "structure_weight": 0.88,
        "color_boost": 0.87,
        "keywords": [
            "digital spectacle",
            "visual effects",
            "virtual camera",
            "tracking shot",
            "cinematic realism",
            "controlled saturation",
            "depth",
            "photographic texture"
        ],
    },
}

__all__ = ["ZEMECKIS_STYLES"]
