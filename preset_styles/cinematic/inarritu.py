"""
CharacterForge Cinematic - Alejandro G. Iñárritu
================================================

Cinematic presets inspired by the visual language of Alejandro G. Iñárritu:
immersive handheld camera work, naturalistic environments, long takes,
raw human intensity, desaturated earth palettes, harsh natural light,
physical textures, environmental scale, and visceral spatial realism.
"""

INARRITU_STYLES = {

    "inarritu_21_grams": {
        "name": "Alejandro G. Iñárritu — Fragmented Intimacy",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "raw intimate dramatic cinematography, handheld 35mm photography, "
            "naturalistic imperfect framing, shallow depth of field used selectively, "
            "available light, muted earth tones, cool gray shadows, subdued skin tones, "
            "grainy photochemical texture, realistic interiors and urban environments, "
            "close physical proximity to characters, slight camera instability, "
            "compressed emotional space, practical lamps and window light, "
            "soft highlight rolloff, visible environmental texture, restrained "
            "production design, spontaneous-looking composition, emotionally tense "
            "human realism"
        ),
        "negative_prompt": (
            "glossy commercial photography, perfect stabilization, artificial beauty "
            "lighting, oversaturated colors, plastic skin, excessive bokeh, clean "
            "digital rendering, superhero composition, polished advertising aesthetic, "
            "flat CGI environments"
        ),
        "denoise": 0.79,
        "structure_weight": 0.82,
        "color_boost": 0.94,
        "keywords": [
            "raw intimacy",
            "handheld 35mm",
            "natural light",
            "muted earth tones",
            "photochemical grain",
            "human realism",
            "emotional proximity"
        ],
    },

    "inarritu_babel": {
        "name": "Alejandro G. Iñárritu — Global Human Drama",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "global dramatic cinematography, documentary-inspired realism, handheld "
            "35mm camera, location photography, natural sunlight and practical lighting, "
            "distinct regional environments, dusty roads, dense cities, rural landscapes, "
            "muted ochre, sand, gray and faded blue palette, realistic atmospheric haze, "
            "moderate depth of field, energetic camera movement, imperfect framing, "
            "foreground obstruction, layered crowds, environmental storytelling, "
            "authentic textures and weathering, fine film grain, restrained contrast, "
            "human figures embedded within vast real locations, visual transitions "
            "between intimate close-ups and environmental wides"
        ),
        "negative_prompt": (
            "studio-perfect environments, tourist postcard aesthetic, glossy travel "
            "photography, oversaturated colors, artificial HDR, plastic textures, "
            "clean digital imagery, generic exoticism, excessive drone spectacle, "
            "perfectly static compositions"
        ),
        "denoise": 0.81,
        "structure_weight": 0.87,
        "color_boost": 0.98,
        "keywords": [
            "global drama",
            "location photography",
            "35mm",
            "documentary realism",
            "dust and haze",
            "muted ochre",
            "layered crowds",
            "environmental wides"
        ],
    },

    "inarritu_biutiful": {
        "name": "Alejandro G. Iñárritu — Urban Desolation",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "urban social drama cinematography, bleak Barcelona cityscape, winter light, "
            "cold gray-blue daylight, dirty concrete, worn apartments, industrial spaces, "
            "realistic street textures, handheld digital-era camera with restrained "
            "sharpness, shallow depth of field for intimate faces, longer lenses for "
            "compressed urban backgrounds, natural practical lighting, subtle haze, "
            "low saturation, subdued skin tones, soft overcast illumination, "
            "environmental imperfections, realistic wardrobe textures, sparse production "
            "design, intimate camera distance, quiet visual desperation without stylization"
        ),
        "negative_prompt": (
            "glamorous urban photography, neon cityscape, polished interiors, "
            "oversaturated cinematic colors, luxury architecture, glossy digital skin, "
            "excessive bokeh, artificial rain, music-video lighting, commercial fashion"
        ),
        "denoise": 0.8,
        "structure_weight": 0.85,
        "color_boost": 0.9,
        "keywords": [
            "urban desolation",
            "Barcelona winter light",
            "gray-blue palette",
            "overcast daylight",
            "handheld digital",
            "industrial textures",
            "social realism"
        ],
    },

    "inarritu_revenant": {
        "name": "Alejandro G. Iñárritu — The Revenant",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "immersive wilderness cinematography, vast natural landscapes, natural light "
            "only, low winter sun, blue-hour shadows, overcast sky, snow, wet bark, mud, "
            "frozen breath, rough wool, leather and weathered skin, large-format "
            "cinematography, wide-angle lenses used extremely close to subjects, "
            "deep environmental perspective, selective shallow focus, long moving takes, "
            "camera physically navigating through terrain, realistic motion blur, "
            "soft cold highlights, subdued blue-gray and brown palette, warm firelight "
            "as rare contrast, atmospheric mist and snow particles, highly tactile "
            "surface detail, restrained digital sharpness, monumental scale combined "
            "with intimate human proximity"
        ),
        "negative_prompt": (
            "fantasy wilderness, artificial studio snow, glossy adventure photography, "
            "oversaturated landscapes, fake fog, excessive HDR, clean costumes, "
            "plastic environments, heroic blockbuster lighting, artificial sunlight, "
            "telephoto wildlife photography"
        ),
        "denoise": 0.83,
        "structure_weight": 0.91,
        "color_boost": 0.92,
        "keywords": [
            "natural light",
            "wilderness",
            "large format",
            "wide-angle close proximity",
            "blue hour",
            "snow",
            "mud",
            "tactile realism"
        ],
    },

    "inarritu_birdman": {
        "name": "Alejandro G. Iñárritu — Continuous Performance",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "continuous-shot theatrical cinematography, backstage theater corridors, "
            "dressing rooms, narrow hallways, exposed brick, practical tungsten bulbs, "
            "cool stage spill, handheld camera flowing continuously between rooms, "
            "wide-angle lenses close to performers, deep spatial focus, long takes, "
            "complex actor blocking, reflections in mirrors, practical backstage clutter, "
            "mixed color temperatures, warm amber tungsten against cyan and neutral "
            "ambient light, subtle digital texture, controlled motion blur, realistic "
            "skin tones, fluid camera choreography, theatrical tension, energetic "
            "urban-night atmosphere, no obvious editorial cutting"
        ),
        "negative_prompt": (
            "static stage photography, isolated portrait shots, conventional coverage, "
            "clean theater interiors, glossy music video, excessive neon, artificial "
            "camera movement, shallow focus everywhere, CGI environments, sterile lighting"
        ),
        "denoise": 0.81,
        "structure_weight": 0.92,
        "color_boost": 1.08,
        "keywords": [
            "continuous shot",
            "theater backstage",
            "wide-angle",
            "long take",
            "actor blocking",
            "mixed color temperature",
            "tungsten and cyan",
            "fluid camera"
        ],
    },

    "inarritu_bardo": {
        "name": "Alejandro G. Iñárritu — Surreal Memory",
        "category": "cinematic",
        "era": "2020s",
        "prompt": (
            "surreal autobiographical cinematic imagery grounded in physical reality, "
            "large-format photography, expansive architectural spaces, dreamlike "
            "perspective shifts, warm golden daylight mixed with cool interior shadows, "
            "soft atmospheric diffusion, carefully controlled wide-angle distortion, "
            "deep focus, elaborate staging, theatrical but tactile environments, "
            "dust particles in light beams, muted terracotta, cream, gray and deep blue, "
            "subtle filmic texture, fluid camera movement, impossible scale handled with "
            "photographic realism, poetic negative space, layered memory imagery, "
            "melancholic grandeur without fantasy gloss"
        ),
        "negative_prompt": (
            "cartoon surrealism, psychedelic neon, synthetic CGI dreamscape, glossy "
            "fantasy art, excessive lens distortion, plastic textures, generic dream "
            "sequence, oversaturated colors, videogame rendering"
        ),
        "denoise": 0.84,
        "structure_weight": 0.89,
        "color_boost": 1.04,
        "keywords": [
            "surreal memory",
            "large format",
            "wide-angle distortion",
            "deep focus",
            "golden daylight",
            "architectural scale",
            "poetic realism",
            "fluid camera"
        ],
    },
}

__all__ = ["INARRITU_STYLES"]
