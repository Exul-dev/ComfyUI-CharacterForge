"""
Trigger Style
==============

Stile Studio Trigger con energia esplosiva.
Colori neon, pose esagerate, action dinamica.
Ispirato a: Kill la Kill, Gurren Lagann, Promare.
"""

TRIGGER_STYLE = {
    "name": "Studio Trigger",
    "description": "Stile Studio Trigger con energia esplosiva e colori neon",
    "category": "anime",
    "era": "modern",
    "studio": "Studio Trigger",
    "prompt": "Studio Trigger anime style, explosive energy aesthetic, Kill la Kill style, Gurren Lagann aesthetic, Promare look, exaggerated dynamic poses, vibrant neon colors, high contrast lighting, sakuga animation quality, Trigger studio signature style, over-the-top action scenes, bold graphic designs, dynamic perspective angles, energetic character designs, explosive visual effects",
    "denoise": 0.28,
    "structure_weight": 0.85,
    "color_boost": 1.5,
    "keywords": [
        "Trigger",
        "Kill la Kill",
        "Gurren Lagann",
        "Promare",
        "explosive",
        "neon colors",
        "dynamic poses",
        "sakuga",
        "high energy"
    ],
    "negative_keywords": [
        "calm atmosphere",
        "muted colors",
        "static poses",
        "realistic proportions",
        "slice of life",
        "subtle animation"
    ],
    "recommended_loras": [
        "trigger_lora.safetensors"
    ],
    "compatible_combinations": [
        "anime_modern",
        "shonen_battle",
        "synthwave_80s"
    ],
    "inspiration": [
        "Kill la Kill (2013)",
        "Gurren Lagann (2007)",
        "Promare (2019)",
        "Cyberpunk Edgerunners (2022)"
    ]
}