"""
CharacterForge Cinematic - Clint Eastwood
=========================================

Visual language inspired by Eastwood's restrained American cinema:
naturalistic photography, controlled compositions, muted palettes,
practical lighting, western landscapes, economical camera movement,
and understated film texture.
"""

EASTWOOD_STYLES = {

    "eastwood_western": {
        "name": "Eastwood Western",
        "category": "cinematic",
        "era": "1970s-2000s",
        "prompt": (
            "classic American western cinematography, restrained camera language, "
            "wide 35mm landscape compositions, medium-long lenses for compressed "
            "desert distances, expansive skies, solitary figures against vast terrain, "
            "natural sunlight, hard midday shadows, warm late-afternoon backlight, "
            "dust suspended in the air, dry earth and weathered wood textures, "
            "muted ochre, sand, tobacco brown and faded blue palette, "
            "subtle 35mm film grain, organic analog texture, realistic skin tones, "
            "minimal camera movement, deliberate framing, strong horizon lines, "
            "quiet tension, authentic practical locations, understated production design"
        ),
        "negative_prompt": (
            "glossy digital cinema, excessive saturation, neon colors, "
            "anamorphic lens flares, excessive bokeh, hyper-stylized camera movement, "
            "fantasy western aesthetics, plastic skin, HDR look, CGI appearance"
        ),
        "denoise": 0.48,
        "structure_weight": 0.82,
        "color_boost": 0.88,
        "keywords": [
            "western",
            "american landscape",
            "natural light",
            "35mm",
            "muted palette",
            "film grain",
            "wide composition",
            "restrained camera"
        ],
    },

    "eastwood_american_landscape": {
        "name": "Eastwood American Landscape",
        "category": "cinematic",
        "era": "1980s-2000s",
        "prompt": (
            "cinematic American landscape photography, 35mm and 50mm lenses, "
            "large environmental compositions, human figures visually subordinate "
            "to the surrounding landscape, distant mountains, plains, forests and "
            "open roads, natural atmospheric perspective, realistic daylight, "
            "soft overcast illumination or low golden-hour sunlight, "
            "subtle haze, restrained contrast, desaturated earth tones, "
            "faded greens, dusty browns and pale blue sky, natural film response, "
            "fine visible 35mm grain, slightly dry photographic texture, "
            "static or extremely slow camera movement, carefully balanced horizons, "
            "quiet observational mood, authentic American locations"
        ),
        "negative_prompt": (
            "epic fantasy landscape, oversaturated colors, extreme HDR, "
            "digital sharpness, excessive atmospheric effects, artificial fog, "
            "hyperreal CGI, exaggerated lens distortion, glossy commercial photography"
        ),
        "denoise": 0.45,
        "structure_weight": 0.86,
        "color_boost": 0.82,
        "keywords": [
            "landscape",
            "environmental portrait",
            "35mm",
            "50mm",
            "natural light",
            "atmospheric depth",
            "American cinema",
            "film texture"
        ],
    },

    "eastwood_noir": {
        "name": "Eastwood Noir",
        "category": "cinematic",
        "era": "1970s-1990s",
        "prompt": (
            "American crime noir cinematography, restrained 50mm and 85mm lenses, "
            "controlled perspective, deep practical shadows, low-key tungsten interiors, "
            "streetlights and motivated sources, venetian-blind shadows, dim bars, "
            "dark offices and rain-slick streets, strong separation between light "
            "and shadow without excessive stylization, charcoal black, tobacco brown, "
            "dirty amber and steel blue palette, subtle underexposure, "
            "natural skin tones, visible fine-grain 35mm film texture, "
            "modest depth of field, carefully placed negative space, "
            "static compositions and deliberate tracking shots, quiet masculine tension, "
            "weathered production design, realistic urban atmosphere"
        ),
        "negative_prompt": (
            "modern glossy noir, neon cyberpunk, excessive blue lighting, "
            "extreme chiaroscuro, anamorphic flares, crushed digital blacks, "
            "oversharpening, excessive shallow depth of field, comic-book lighting"
        ),
        "denoise": 0.47,
        "structure_weight": 0.83,
        "color_boost": 0.76,
        "keywords": [
            "noir",
            "crime drama",
            "50mm",
            "85mm",
            "low key lighting",
            "tungsten",
            "negative space",
            "35mm grain"
        ],
    },

    "eastwood_muted_drama": {
        "name": "Eastwood Muted Drama",
        "category": "cinematic",
        "era": "1990s-2010s",
        "prompt": (
            "understated American dramatic cinematography, 35mm and 50mm lenses, "
            "naturalistic perspective, restrained depth of field, practical interior lighting, "
            "soft window light, overcast daylight, subdued tungsten illumination, "
            "faces rendered with honest skin texture and gentle contrast, "
            "muted gray, beige, faded green and brown palette, "
            "subtle desaturation, soft film grain, organic 35mm photographic response, "
            "minimal camera movement, static observation and slow controlled dolly shots, "
            "balanced compositions, modest headroom, realistic domestic environments, "
            "weathered materials, quiet emotional tension, no visual ornamentation"
        ),
        "negative_prompt": (
            "melodramatic lighting, glossy commercial look, saturated colors, "
            "excessive bokeh, artificial rim light, beauty lighting, "
            "digital clinical sharpness, music-video camera movement, fantasy aesthetics"
        ),
        "denoise": 0.46,
        "structure_weight": 0.84,
        "color_boost": 0.78,
        "keywords": [
            "dramatic realism",
            "naturalistic lighting",
            "35mm",
            "50mm",
            "muted colors",
            "practical interiors",
            "subtle grain",
            "quiet emotion"
        ],
    },

    "eastwood_late_career": {
        "name": "Eastwood Late Career",
        "category": "cinematic",
        "era": "2000s-2020s",
        "prompt": (
            "late-career American cinematic realism, restrained digital-to-filmic image, "
            "35mm and 50mm equivalent perspective, occasional 85mm portrait compression, "
            "natural daylight, soft overcast skies, practical tungsten interiors, "
            "subdued highlights and controlled shadow detail, muted blue-gray, beige, "
            "olive and brown palette, realistic aging skin and physical texture, "
            "subtle fine grain and gentle photographic softness, modest depth of field, "
            "stable camera, slow deliberate movement, simple symmetrical or balanced framing, "
            "large amounts of environmental context, authentic locations, "
            "minimal production-design ornament, emotionally restrained atmosphere, "
            "quiet observational realism"
        ),
        "negative_prompt": (
            "hypermodern blockbuster cinematography, excessive teal and orange, "
            "neon lighting, extreme shallow depth of field, aggressive handheld movement, "
            "oversaturated digital color, HDR halos, plastic skin, CGI environments"
        ),
        "denoise": 0.44,
        "structure_weight": 0.85,
        "color_boost": 0.80,
        "keywords": [
            "late career",
            "cinematic realism",
            "35mm",
            "50mm",
            "85mm",
            "naturalistic",
            "muted palette",
            "observational camera"
        ],
    },
}

__all__ = ["EASTWOOD_STYLES"]
