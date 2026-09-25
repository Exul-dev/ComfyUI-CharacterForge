"""
CharacterForge Cinematic - Stanley Kubrick
==========================================

Evoluzione cinematografica per periodo:
- 1960s
- 1970s
- 1980s
- 1990s
"""

KUBRICK_STYLES = {

    "kubrick_1960s": {
        "name": "Stanley Kubrick — 1960s",
        "description": "Cinematic realism inspired by Kubrick's 1960s visual language: controlled compositions, crisp monochrome or restrained color, wide-angle spatial clarity and precise photographic lighting.",
        "category": "cinematic",
        "artist": "Stanley Kubrick",
        "era": "1960s",
        "period": "1960-1969",
        "prompt": (
            "35mm motion picture film, 1960s cinematic photography, "
            "precise symmetrical composition, carefully controlled framing, "
            "wide-angle spherical cinema lens, deep spatial clarity, "
            "moderate depth of field, geometric architecture, strong visual order, "
            "clean horizon lines, deliberate negative space, restrained camera perspective, "
            "natural but highly controlled lighting, hard directional key light, "
            "precise practical illumination, crisp shadow boundaries, "
            "subtle bounce light, realistic exposure, strong but readable contrast, "
            "natural skin with visible pores, subtle micro-wrinkles, natural redness, "
            "realistic under-eye texture, individual facial hairs and small imperfections, "
            "no beauty smoothing, authentic photographic skin response, "
            "restrained 1960s color reproduction, muted reds, controlled blues, "
            "warm neutral highlights, slightly cool shadows, natural film density, "
            "fine 35mm grain, subtle film halation, gentle optical softness, "
            "slight gate weave, realistic highlight rolloff, mild chromatic aberration, "
            "period-authentic production design, realistic materials, "
            "quiet intellectual atmosphere, precise theatrical cinematography, "
            "photochemical image texture, authentic 1960s film appearance, "
            "no modern digital sharpness, no HDR, no plastic skin, "
            "no excessive saturation, no artificial smoothing"
        ),
        "denoise": 0.28,
        "structure_weight": 0.91,
        "color_boost": 1.05,
        "keywords": [
            "Kubrick",
            "1960s",
            "symmetry",
            "wide angle",
            "geometric composition",
            "35mm",
            "controlled lighting",
            "photochemical film"
        ],
        "negative_keywords": [
            "modern digital cinema",
            "HDR",
            "plastic skin",
            "beauty filter",
            "oversaturation",
            "handheld chaos"
        ],
        "recommended_loras": [],
        "compatible_combinations": [
            "cinematic_1960s",
            "classic_35mm",
            "architectural_cinema"
        ],
        "inspiration": [
            "1960s studio cinematography",
            "European art cinema",
            "precision photographic composition"
        ]
    },

    "kubrick_1970s": {
        "name": "Stanley Kubrick — 1970s",
        "description": "1970s cinematic realism with controlled symmetry, naturalistic interiors, available-light atmosphere, wide-angle compositions and tactile photochemical texture.",
        "category": "cinematic",
        "artist": "Stanley Kubrick",
        "era": "1970s",
        "period": "1970-1979",
        "prompt": (
            "35mm motion picture film, 1970s cinematic photography, "
            "highly controlled symmetrical composition, precise centered framing, "
            "wide-angle spherical cinema lenses, immersive architectural perspective, "
            "deep environmental staging, deliberate camera placement, "
            "naturalistic available-light cinematography, practical interior lighting, "
            "soft window illumination, candlelight where appropriate, "
            "subtle tungsten warmth, deep natural shadows, restrained fill light, "
            "realistic low-light exposure, visible shadow detail, "
            "natural imperfect skin with visible pores, micro-wrinkles, freckles, "
            "subtle redness, realistic facial texture, individual hairs, "
            "natural under-eye detail, slight perspiration and environmental skin response, "
            "no cosmetic smoothing, no plastic appearance, "
            "earthy 1970s film palette, muted browns, faded reds, olive greens, "
            "warm amber practical lights, subdued blue-gray shadows, "
            "rich but restrained color density, organic 35mm grain, "
            "fine-to-medium film grain structure, gentle halation, "
            "subtle lens softness, realistic highlight bloom, "
            "slight exposure variation, restrained chromatic aberration, "
            "period-authentic production design, worn materials, aged interiors, "
            "realistic wood, stone, metal, fabric and glass, "
            "psychological atmosphere, quiet tension, observational realism, "
            "photochemical theatrical film texture, authentic 1970s cinema, "
            "no digital clarity, no modern HDR, no beauty retouching, "
            "no excessive saturation, no artificial sharpness"
        ),
        "denoise": 0.30,
        "structure_weight": 0.90,
        "color_boost": 1.10,
        "keywords": [
            "Kubrick",
            "1970s",
            "symmetry",
            "available light",
            "wide angle",
            "earthy palette",
            "35mm grain",
            "psychological atmosphere"
        ],
        "negative_keywords": [
            "digital cinema",
            "plastic skin",
            "beauty retouching",
            "HDR",
            "neon colors",
            "modern commercial photography"
        ],
        "recommended_loras": [],
        "compatible_combinations": [
            "cinematic_1970s",
            "naturalistic_film",
            "psychological_cinema"
        ],
        "inspiration": [
            "1970s photochemical cinema",
            "available-light interiors",
            "architectural psychological drama"
        ]
    },

    "kubrick_1980s": {
        "name": "Stanley Kubrick — 1980s",
        "description": "1980s Kubrick-inspired cinematic realism emphasizing cold interiors, geometric symmetry, controlled wide-angle perspective and atmospheric practical lighting.",
        "category": "cinematic",
        "artist": "Stanley Kubrick",
        "era": "1980s",
        "period": "1980-1989",
        "prompt": (
            "35mm motion picture film, 1980s cinematic photography, "
            "extreme geometric composition, precise bilateral symmetry, "
            "centered vanishing point, wide-angle spherical lens, "
            "deep perspective, long architectural corridors, "
            "strong spatial geometry, deliberate camera height, "
            "slow controlled visual rhythm, cold practical interior lighting, "
            "fluorescent illumination, tungsten practicals, soft window spill, "
            "high contrast but preserved shadow information, "
            "cool ambient shadows with restrained warm practical highlights, "
            "realistic skin texture under hard interior lighting, "
            "visible pores, micro-wrinkles, subtle blemishes, natural redness, "
            "realistic facial planes, individual hair detail, "
            "slight dryness and environmental texture, "
            "no beauty filter, no pore removal, no plastic skin, "
            "desaturated 1980s color palette, cold whites, muted blues, "
            "faded reds, restrained amber practical lights, "
            "slightly cool neutral balance, organic photochemical color response, "
            "medium 35mm film grain, subtle halation around practical lights, "
            "controlled highlight bloom, slight optical softness, "
            "gentle gate weave, subtle exposure instability, "
            "restrained chromatic aberration, realistic lens characteristics, "
            "cold institutional atmosphere, psychological tension, "
            "precise production design, realistic worn surfaces, "
            "photochemical theatrical texture, authentic 1980s film appearance, "
            "no digital rendering, no modern HDR, no excessive clarity, "
            "no glossy skin, no artificial smoothing, no oversaturation"
        ),
        "denoise": 0.31,
        "structure_weight": 0.90,
        "color_boost": 1.08,
        "keywords": [
            "Kubrick",
            "1980s",
            "symmetry",
            "cold interiors",
            "fluorescent light",
            "wide angle",
            "geometric perspective",
            "psychological tension"
        ],
        "negative_keywords": [
            "modern digital",
            "warm commercial lighting",
            "plastic skin",
            "beauty filter",
            "HDR",
            "oversaturation"
        ],
        "recommended_loras": [],
        "compatible_combinations": [
            "cinematic_1980s",
            "cold_interior",
            "psychological_horror"
        ],
        "inspiration": [
            "1980s photochemical cinema",
            "institutional interiors",
            "geometric psychological cinematography"
        ]
    },

    "kubrick_1990s": {
        "name": "Stanley Kubrick — 1990s",
        "description": "Late-period 1990s cinematic realism with controlled movement, naturalistic low-light interiors, precise framing and dense photochemical texture.",
        "category": "cinematic",
        "artist": "Stanley Kubrick",
        "era": "1990s",
        "period": "1990-1999",
        "prompt": (
            "35mm motion picture film, 1990s cinematic photography, "
            "precise controlled composition, deliberate framing, "
            "wide-angle spherical cinema lens, immersive spatial perspective, "
            "carefully controlled camera movement, restrained tracking, "
            "naturalistic interior lighting, practical lamps, window light, "
            "soft tungsten sources, subtle mixed-color illumination, "
            "deep but readable shadows, realistic low-light exposure, "
            "natural skin with highly visible pores, micro-wrinkles, freckles, "
            "subtle scars, natural redness, realistic under-eye texture, "
            "vellus hair, irregular facial hair, environmental skin response, "
            "no beauty smoothing, no artificial pore removal, "
            "authentic imperfect human skin, "
            "restrained 1990s color palette, neutral skin tones, "
            "muted greens, brown-gray environments, subdued reds, "
            "cool shadow separation, realistic film color density, "
            "medium-fine 35mm grain, organic grain variation, "
            "subtle halation, natural highlight rolloff, "
            "gentle optical softness, slight lens breathing, "
            "minor gate weave, restrained chromatic aberration, "
            "realistic exposure variation, tactile photochemical texture, "
            "dense production design, believable worn materials, "
            "quiet psychological atmosphere, observational realism, "
            "serious theatrical film aesthetic, authentic 1990s film appearance, "
            "no digital cinema look, no excessive sharpening, "
            "no HDR, no plastic skin, no beauty filter, "
            "no excessive saturation, no sterile modern rendering"
        ),
        "denoise": 0.32,
        "structure_weight": 0.89,
        "color_boost": 1.10,
        "keywords": [
            "Kubrick",
            "1990s",
            "35mm",
            "controlled tracking",
            "low light",
            "naturalistic lighting",
            "psychological realism",
            "photochemical texture"
        ],
        "negative_keywords": [
            "digital cinema",
            "plastic skin",
            "beauty smoothing",
            "HDR",
            "oversharpening",
            "commercial gloss"
        ],
        "recommended_loras": [],
        "compatible_combinations": [
            "cinematic_1990s",
            "naturalistic_35mm",
            "psychological_drama"
        ],
        "inspiration": [
            "1990s photochemical cinema",
            "naturalistic interiors",
            "late-period psychological cinematography"
        ]
    }
}


__all__ = ["KUBRICK_STYLES"]
