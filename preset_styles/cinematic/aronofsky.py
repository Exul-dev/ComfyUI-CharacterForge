"""
CharacterForge Cinematic - Darren Aronofsky
==========================================

Visual language inspired by Aronofsky's cinema:
intimate wide-angle photography, subjective camera proximity,
physical and psychological intensity, aggressive montage aesthetics,
macro detail, controlled practical lighting, high contrast,
desaturated palettes and visual transformation expressed through
camera, texture, repetition and spatial distortion.
"""

ARONOFSKY_STYLES = {

    "aronofsky_1990s": {
        "name": "Aronofsky 1990s",
        "category": "cinematic",
        "era": "1990s",
        "prompt": (
            "1990s psychological independent cinema, 24mm and 28mm wide-angle lenses, "
            "camera positioned extremely close to subjects, intimate spatial distortion, "
            "handheld and controlled unstable movement, tight corridors and cramped interiors, "
            "high-contrast practical lighting, hard fluorescent sources, dirty tungsten lamps, "
            "deep shadows, stark highlights, desaturated gray, green, brown and dirty yellow palette, "
            "coarse 35mm film grain, gritty analog texture, visible skin and environmental detail, "
            "moderate depth of field, aggressive perspective, fragmented compositions, "
            "subjective framing, claustrophobic atmosphere, raw urban production design"
        ),
        "negative_prompt": (
            "glossy commercial photography, clean digital cinema, pastel colors, "
            "soft beauty lighting, extreme cinematic bokeh, HDR, sterile interiors, "
            "perfectly smooth skin, polished blockbuster aesthetics"
        ),
        "denoise": 0.51,
        "structure_weight": 0.83,
        "color_boost": 0.72,
        "keywords": [
            "1990s",
            "24mm",
            "28mm",
            "wide angle",
            "psychological",
            "gritty",
            "35mm grain",
            "claustrophobic"
        ],
    },

    "aronofsky_requiem": {
        "name": "Aronofsky Hyperkinetic",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "hyperkinetic psychological cinematography, extreme close proximity to characters, "
            "24mm and 28mm wide-angle perspective, rapid handheld movement, "
            "aggressive push-ins, abrupt reframing, subjective point of view, "
            "macro inserts of eyes, hands, skin, food, objects and physical details, "
            "high-contrast practical lighting, fluorescent interiors, harsh tungsten sources, "
            "deep blacks, dirty green, beige, gray and sickly yellow palette, "
            "coarse visible 35mm grain, gritty photographic texture, "
            "shallow depth of field alternating with distorted wide-angle deep space, "
            "visual repetition, fragmented composition, claustrophobic environments, "
            "physical discomfort expressed through camera proximity and optical distortion"
        ),
        "negative_prompt": (
            "smooth stabilized camera, elegant commercial photography, pastel grading, "
            "clean studio lighting, glossy skin, soft romantic imagery, "
            "excessive cinematic bokeh, sterile digital look"
        ),
        "denoise": 0.53,
        "structure_weight": 0.80,
        "color_boost": 0.70,
        "keywords": [
            "hyperkinetic",
            "24mm",
            "macro",
            "handheld",
            "close proximity",
            "high contrast",
            "gritty",
            "psychological intensity"
        ],
    },

    "aronofsky_black_swan": {
        "name": "Aronofsky Psychological Transformation",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "psychological body-horror cinematography, 35mm and 50mm lenses mixed with "
            "close handheld wide-angle shots, intimate camera proximity, "
            "controlled shallow depth of field, mirror compositions, reflections, "
            "fragmented body framing, practical backstage lighting, fluorescent corridors, "
            "cool gray-blue ambience contrasted with warm skin tones and selective crimson accents, "
            "high contrast, deep shadows, realistic skin texture, "
            "subtle 35mm film grain, soft optical halation, "
            "slow creeping camera movement interrupted by nervous handheld motion, "
            "claustrophobic architecture, mirrors and narrow rooms, "
            "visual transformation expressed through texture, posture, shadow and spatial distortion"
        ),
        "negative_prompt": (
            "glossy fashion photography, clean beauty lighting, excessive pastel colors, "
            "generic horror CGI, extreme gore, artificial plastic skin, "
            "perfect symmetry, sterile digital sharpness"
        ),
        "denoise": 0.50,
        "structure_weight": 0.86,
        "color_boost": 0.78,
        "keywords": [
            "psychological",
            "body horror",
            "35mm",
            "50mm",
            "mirror",
            "reflection",
            "crimson",
            "claustrophobic"
        ],
    },

    "aronofsky_the_fountain": {
        "name": "Aronofsky Mythic Dream",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "mythic psychological fantasy cinematography with tactile practical imagery, "
            "macro photography, 50mm and 85mm intimate perspectives, extreme close-ups, "
            "organic textures, skin, water, plants, bark, dust and translucent materials, "
            "soft directional light, warm gold and amber highlights, deep black backgrounds, "
            "cool blue shadows, restrained crimson accents, shallow depth of field, "
            "ethereal optical softness, subtle halation, fine film grain, "
            "controlled camera movement, slow floating compositions, "
            "organic abstract forms replacing conventional spectacle, "
            "rich tactile surfaces, intimate cosmic atmosphere, photographic rather than synthetic fantasy"
        ),
        "negative_prompt": (
            "generic CGI fantasy, videogame rendering, plastic textures, "
            "oversaturated rainbow colors, excessive lens flares, hard digital edges, "
            "cartoon aesthetics, generic space opera"
        ),
        "denoise": 0.48,
        "structure_weight": 0.82,
        "color_boost": 0.88,
        "keywords": [
            "mythic",
            "macro",
            "50mm",
            "85mm",
            "organic texture",
            "amber",
            "blue shadows",
            "dream"
        ],
    },

    "aronofsky_modern": {
        "name": "Aronofsky Modern Intensity",
        "category": "cinematic",
        "era": "2010s-2020s",
        "prompt": (
            "modern psychological drama cinematography, intimate 28mm, 35mm and 50mm lenses, "
            "camera physically close to actors, restrained handheld movement, "
            "subjective framing, compressed interiors, long corridors and confined apartments, "
            "practical daylight mixed with fluorescent and tungsten sources, "
            "hard side light, deep natural shadows, subdued gray, beige, brown and green palette, "
            "selective warm skin tones, controlled desaturation, realistic texture, "
            "fine digital image with subtle filmic grain, soft highlight rolloff, "
            "moderate depth of field, occasional extreme close-ups, "
            "slow push-ins and nervous reframing, tactile production design, "
            "psychological tension expressed through physical space and camera proximity"
        ),
        "negative_prompt": (
            "blockbuster spectacle, glossy digital cinema, excessive teal and orange, "
            "beauty lighting, extreme bokeh, perfect stabilized movement, "
            "plastic skin, oversaturated colors, artificial CGI environments"
        ),
        "denoise": 0.47,
        "structure_weight": 0.85,
        "color_boost": 0.76,
        "keywords": [
            "modern",
            "psychological drama",
            "28mm",
            "35mm",
            "50mm",
            "handheld",
            "desaturated",
            "intimate"
        ],
    },
}

__all__ = ["ARONOFSKY_STYLES"]
