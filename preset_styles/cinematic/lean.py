"""
CharacterForge Cinematic - David Lean
======================================

Preset cinematografici ispirati alla fotografia di David Lean:
grande formato, paesaggi monumentali, profondità atmosferica,
controluce, composizione epica, luce naturale e attenzione
alla scala del personaggio rispetto all'ambiente.
"""

LEAN_STYLES = {

    "lean_epic_landscape": {
        "name": "Lean - Epic Landscape",
        "category": "cinematic",
        "era": "1950s-1960s",
        "prompt": (
            "epic large-format cinematography, enormous landscape scale, "
            "tiny human figures against monumental terrain, "
            "deep atmospheric perspective, carefully layered foreground "
            "middle ground and distant background, natural sunlight, "
            "dramatic cloud formations, subtle haze, long visual horizons, "
            "rich but restrained color palette, fine large-format film grain, "
            "precise classical composition, sweeping cinematic grandeur"
        ),
        "negative_prompt": (
            "small cramped environment, modern digital photography, "
            "extreme shallow depth of field, oversaturated fantasy colors, "
            "HDR, excessive lens flare, artificial fog, "
            "video game environment, plastic surfaces"
        ),
        "denoise": 0.74,
        "structure_weight": 0.96,
        "color_boost": 0.92,
        "keywords": [
            "epic_landscape",
            "large_format",
            "deep_focus",
            "atmospheric_perspective",
            "monumental",
            "natural_light"
        ],
    },

    "lean_lawrence_arabia": {
        "name": "Lean - Desert Monumentality",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "vast desert cinematography, monumental dunes and rocky formations, "
            "extreme scale contrast between human figures and landscape, "
            "long-lens compression across shimmering heat haze, "
            "golden and amber sunlight, deep blue sky, "
            "fine sand particles illuminated by backlight, "
            "precise panoramic composition, enormous negative space, "
            "rich large-format color photography, subtle film grain, "
            "majestic natural atmosphere"
        ),
        "negative_prompt": (
            "fantasy desert, oversaturated orange, artificial CGI sand, "
            "modern clothing, contemporary vehicles, excessive HDR, "
            "neon colors, cartoon appearance, extreme digital sharpness"
        ),
        "denoise": 0.76,
        "structure_weight": 0.97,
        "color_boost": 1.00,
        "keywords": [
            "desert",
            "large_format",
            "heat_haze",
            "backlight",
            "panoramic",
            "scale"
        ],
    },

    "lean_doctor_zhivago": {
        "name": "Lean - Winter Landscape",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "epic winter cinematography, vast snow-covered landscape, "
            "soft diffused overcast daylight, pale blue and ivory palette, "
            "delicate atmospheric haze, distant architecture, "
            "human figures isolated within immense frozen environments, "
            "carefully controlled exposure, soft highlights, "
            "large-format film texture, fine grain, "
            "quiet monumental composition, romantic but restrained visual atmosphere"
        ),
        "negative_prompt": (
            "neon winter colors, fantasy ice palace, excessive contrast, "
            "HDR, artificial snow, glossy digital rendering, "
            "extreme bokeh, oversharpening, cartoon style"
        ),
        "denoise": 0.73,
        "structure_weight": 0.95,
        "color_boost": 0.88,
        "keywords": [
            "winter",
            "snow",
            "diffused_light",
            "large_format",
            "pale_palette",
            "isolation"
        ],
    },

    "lean_bridge_on_the_river": {
        "name": "Lean - Tropical Naturalism",
        "category": "cinematic",
        "era": "1950s",
        "prompt": (
            "lush tropical landscape photographed with classical large-format cinema, "
            "dense vegetation, humid atmospheric depth, soft natural daylight, "
            "filtered sunlight through leaves, warm earth tones, "
            "layered river environment, subtle mist and humidity, "
            "balanced ensemble composition, restrained color saturation, "
            "organic film grain, realistic textures, "
            "poetic contrast between human figures and expansive natural surroundings"
        ),
        "negative_prompt": (
            "tropical postcard aesthetic, excessive saturation, fantasy jungle, "
            "artificial studio lighting, HDR, digital oversharpening, "
            "extreme shallow depth of field, neon greens"
        ),
        "denoise": 0.72,
        "structure_weight": 0.92,
        "color_boost": 0.94,
        "keywords": [
            "tropical",
            "river",
            "humidity",
            "natural_light",
            "large_format",
            "vegetation"
        ],
    },

    "lean_intimate_drama": {
        "name": "Lean - Intimate Drama",
        "category": "cinematic",
        "era": "1940s-1950s",
        "prompt": (
            "classical British dramatic cinematography, intimate interior scene, "
            "carefully controlled key light, soft window illumination, "
            "subtle chiaroscuro, restrained shadows, elegant blocking, "
            "medium and medium-close compositions, layered interior depth, "
            "natural skin tones, muted warm palette, "
            "fine-grain 35mm film texture, delicate halation, "
            "quiet emotional atmosphere, precise classical framing"
        ),
        "negative_prompt": (
            "modern digital cinema, beauty-commercial lighting, "
            "excessive bokeh, neon colors, HDR, extreme contrast, "
            "plastic skin, handheld chaos, oversharpening"
        ),
        "denoise": 0.70,
        "structure_weight": 0.90,
        "color_boost": 0.82,
        "keywords": [
            "intimate",
            "british_cinema",
            "interior",
            "window_light",
            "35mm",
            "classical"
        ],
    },
}


__all__ = ["LEAN_STYLES"]
