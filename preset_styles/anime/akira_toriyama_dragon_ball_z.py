"""
Dragon Ball Z Style Specific
=============================

Stile specifico DBZ - energia chi, trasformazioni, auras.
"""

DRAGON_BALL_Z = {
    "name": "Dragon Ball Z",
    "description": "Stile specifico Dragon Ball Z con auras, chi energy, trasformazioni",
    "category": "anime",
    "series": "Dragon Ball Z",
    "prompt": "Dragon Ball Z art style, DBZ energy aura effects, Super Saiyan transformation aesthetic, Toriyama DBZ style, chi energy visualization, Super Saiyan hair design, DBZ character proportions, golden aura effects, energy blast visualization, Dragon Ball Z battle damage, Toriyama's DBZ era linework, Super Saiyan aesthetic, DBZ power up effects, ki energy effects",
    "denoise": 0.25,
    "structure_weight": 0.87,
    "color_boost": 1.45,
    "keywords": [
        "Dragon Ball Z",
        "Super Saiyan",
        "chi energy",
        "aura effects",
        "power up",
        "energy blasts",
        "ki energy",
        "transformation",
        "battle damage"
    ],
    "negative_keywords": [
        "Dragon Ball original style",
        "minimal energy effects",
        "realistic proportions",
        "subtle aesthetic"
    ],
    "recommended_loras": [
        "dragon_ball_z_lora.safetensors"
    ],
    "compatible_combinations": [
        "toriyama_style",
        "shonen_battle",
        "shonen_90s_style"
    ],
    "inspiration": [
        "Dragon Ball Z (1989)",
        "DBZ movies (1989-1996)"
    ]
}