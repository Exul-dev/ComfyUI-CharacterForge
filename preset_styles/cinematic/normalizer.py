from copy import deepcopy


V3_FIELDS = {
    "name",
    "description",
    "category",
    "director",
    "era",
    "decade",
    "medium",
    "prompt",
    "negative_prompt",
    "skin_profile",
    "lighting_profile",
    "lens_profile",
    "film_stock",
    "grain_profile",
    "color_profile",
    "atmosphere_profile",
    "camera_profile",
    "aspect_ratio",
    "camera_movement",
    "depth_of_field",
    "contrast",
    "saturation",
    "highlight_rolloff",
    "black_level",
    "denoise",
    "structure_weight",
    "color_boost",
    "keywords",
    "negative_keywords",
    "recommended_loras",
    "compatible_combinations",
    "inspiration",
}


DEFAULT_V3 = {
    "name": "",
    "description": "",
    "category": "cinematic",
    "director": "Unknown",
    "era": "Unknown",
    "decade": 2000,
    "medium": "35mm film",
    "prompt": "",
    "negative_prompt": "",
    "skin_profile": "natural_1960",
    "lighting_profile": "natural_soft",
    "lens_profile": "spherical_classic",
    "film_stock": "kodak_vision3",
    "grain_profile": "fine",
    "color_profile": "warm_classic",
    "atmosphere_profile": "dream_soft",
    "camera_profile": "new_hollywood",
    "aspect_ratio": "2.39:1",
    "camera_movement": "controlled",
    "depth_of_field": "moderate",
    "contrast": "medium",
    "saturation": "moderate",
    "highlight_rolloff": "soft",
    "black_level": "deep",
    "denoise": 0.25,
    "structure_weight": 0.85,
    "color_boost": 1.0,
    "keywords": [],
    "negative_keywords": [],
    "recommended_loras": [],
    "compatible_combinations": [],
    "inspiration": [],
}


KUBRICK_DEFAULTS = {
    "director": "Stanley Kubrick",
    "medium": "35mm film",
    "skin_profile": "natural_1960",
    "lighting_profile": "studio_classic",
    "lens_profile": "vintage_prime",
    "film_stock": "kodak_vision3",
    "grain_profile": "fine",
    "color_profile": "desaturated",
    "atmosphere_profile": "dream_soft",
    "camera_profile": "kubrick_symmetry",
    "aspect_ratio": "1.66:1",
    "camera_movement": "precise",
    "depth_of_field": "deep",
    "contrast": "medium-high",
    "saturation": "restrained",
    "highlight_rolloff": "soft",
    "black_level": "deep",
    "negative_prompt": (
        "plastic skin, beauty filter, oversharpening, excessive HDR, "
        "modern blockbuster grading"
    ),
}


LEONE_DEFAULTS = {
    "director": "Sergio Leone",
    "decade": 1960,
    "medium": "35mm Techniscope",
    "skin_profile": "weathered_western",
    "lighting_profile": "hard_desert_sun",
    "lens_profile": "anamorphic_wide",
    "film_stock": "kodachrome",
    "grain_profile": "medium",
    "color_profile": "warm_classic",
    "atmosphere_profile": "dusty_frontier",
    "camera_profile": "techniscope_western",
    "aspect_ratio": "2.35:1",
    "camera_movement": "slow_deliberate",
    "depth_of_field": "deep",
    "contrast": "high",
    "saturation": "warm",
    "highlight_rolloff": "soft",
    "black_level": "deep",
}


def normalize_cinematic(preset_id: str, preset: dict) -> dict:
    """
    Normalizza un preset cinematico V1/V2/V3
    nello schema canonico V3 da 32 campi.
    """

    if not isinstance(preset, dict):
        raise TypeError("preset deve essere un dict")

    source = deepcopy(preset)

    # ---------------------------------------------------------
    # MIGRAZIONE KUBRICK V2
    # ---------------------------------------------------------

    if preset_id.startswith("kubrick_"):

        if "director" not in source and "artist" in source:
            source["director"] = source["artist"]

        if "era" not in source and "period" in source:
            source["era"] = source["period"]

        source.pop("artist", None)
        source.pop("period", None)

        for key, value in KUBRICK_DEFAULTS.items():
            source.setdefault(key, value)

    # ---------------------------------------------------------
    # MIGRAZIONE LEONE V1
    # ---------------------------------------------------------

    elif preset_id.startswith("leone_"):

        for key, value in LEONE_DEFAULTS.items():
            source.setdefault(key, value)

    # ---------------------------------------------------------
    # DEFAULT GENERALE
    # ---------------------------------------------------------

    result = deepcopy(DEFAULT_V3)
    result.update(source)

    # ---------------------------------------------------------
    # DECADE DA ERA
    # ---------------------------------------------------------

    if result["decade"] == 2000:

        era = str(result.get("era", ""))

        if len(era) >= 4 and era[:4].isdigit():
            result["decade"] = int(era[:4])

    # ---------------------------------------------------------
    # SCHEMA V3 ESATTO
    # ---------------------------------------------------------

    return {
        field: result[field]
        for field in V3_FIELDS
    }
