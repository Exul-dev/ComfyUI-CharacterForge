import sys
from pathlib import Path

ROOT = Path(r"D:\AVVIO PULITO di ComfyUI\ComfyUI\custom_nodes\ComfyUI-CharacterForge")
sys.path.insert(0, str(ROOT))

from preset_styles.cinematic import CINEMATIC_STYLES


REQUIRED_FIELDS = {
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

EXPECTED_TYPES = {
    "name": str,
    "description": str,
    "category": str,
    "director": str,
    "era": str,
    "decade": int,
    "medium": str,
    "prompt": str,
    "negative_prompt": str,
    "skin_profile": str,
    "lighting_profile": str,
    "lens_profile": str,
    "film_stock": str,
    "grain_profile": str,
    "color_profile": str,
    "atmosphere_profile": str,
    "camera_profile": str,
    "aspect_ratio": str,
    "camera_movement": str,
    "depth_of_field": str,
    "contrast": str,
    "saturation": str,
    "highlight_rolloff": str,
    "black_level": str,
    "denoise": (int, float),
    "structure_weight": (int, float),
    "color_boost": (int, float),
    "keywords": list,
    "negative_keywords": list,
    "recommended_loras": list,
    "compatible_combinations": list,
    "inspiration": list,
}


def fail(message):
    print(f"[FAIL] {message}")


print("=" * 72)
print("CHARACTERFORGE CINEMATIC VALIDATOR")
print("=" * 72)

print(f"Preset caricati: {len(CINEMATIC_STYLES)}")

errors = []
warnings = []

if len(CINEMATIC_STYLES) != 202:
    errors.append(
        f"Numero preset inatteso: {len(CINEMATIC_STYLES)} (attesi 202)"
    )

keys = list(CINEMATIC_STYLES.keys())

if len(keys) != len(set(keys)):
    errors.append("Sono presenti chiavi duplicate.")

directors = {}
decades = {}
categories = {}

for preset_id, preset in CINEMATIC_STYLES.items():

    if not isinstance(preset, dict):
        errors.append(
            f"{preset_id}: il preset non è un dict ({type(preset).__name__})"
        )
        continue

    missing = REQUIRED_FIELDS - set(preset.keys())

    if missing:
        errors.append(
            f"{preset_id}: campi mancanti: {sorted(missing)}"
        )

    extra = set(preset.keys()) - REQUIRED_FIELDS

    if extra:
        warnings.append(
            f"{preset_id}: campi extra: {sorted(extra)}"
        )

    for field, expected in EXPECTED_TYPES.items():

        if field not in preset:
            continue

        value = preset[field]

        if not isinstance(value, expected):
            errors.append(
                f"{preset_id}.{field}: tipo {type(value).__name__}, "
                f"atteso {expected}"
            )

    for field in REQUIRED_FIELDS:

        if field not in preset:
            continue

        value = preset[field]

        if isinstance(value, str) and not value.strip():
            errors.append(
                f"{preset_id}.{field}: stringa vuota"
            )

    for field in (
        "keywords",
        "negative_keywords",
        "recommended_loras",
        "compatible_combinations",
        "inspiration",
    ):

        if field not in preset:
            continue

        value = preset[field]

        if isinstance(value, list):

            for index, item in enumerate(value):

                if not isinstance(item, str):
                    errors.append(
                        f"{preset_id}.{field}[{index}]: "
                        f"tipo {type(item).__name__}, atteso str"
                    )

            if len(value) != len(set(value)):
                warnings.append(
                    f"{preset_id}.{field}: contiene duplicati"
                )

    for field in (
        "denoise",
        "structure_weight",
        "color_boost",
    ):

        if field not in preset:
            continue

        value = preset[field]

        if isinstance(value, (int, float)) and not isinstance(value, bool):

            if field == "denoise" and not 0 <= value <= 1:
                errors.append(
                    f"{preset_id}.{field}: valore fuori range [0,1]: {value}"
                )

            if field == "structure_weight" and not 0 <= value <= 1:
                errors.append(
                    f"{preset_id}.{field}: valore fuori range [0,1]: {value}"
                )

            if field == "color_boost" and not 0 <= value <= 2:
                warnings.append(
                    f"{preset_id}.{field}: valore insolito: {value}"
                )

    director = preset.get("director")
    decade = preset.get("decade")
    category = preset.get("category")

    if director:
        directors.setdefault(director, []).append(preset_id)

    if decade:
        decades.setdefault(decade, []).append(preset_id)

    if category:
        categories.setdefault(category, []).append(preset_id)

    if category != "cinematic":
        errors.append(
            f"{preset_id}: category={category!r}, atteso 'cinematic'"
        )


print()
print("-" * 72)
print("RIEPILOGO")
print("-" * 72)

print(f"Preset:              {len(CINEMATIC_STYLES)}")
print(f"Famiglie/registi:    {len(directors)}")
print(f"Decadi:              {len(decades)}")
print(f"Categorie:           {len(categories)}")
print(f"Errori:              {len(errors)}")
print(f"Avvisi:              {len(warnings)}")

print()
print("-" * 72)
print("DISTRIBUZIONE PER REGISTA")
print("-" * 72)

for director, preset_ids in sorted(
    directors.items(),
    key=lambda item: (-len(item[1]), item[0])
):
    print(f"{director}: {len(preset_ids)}")

if errors:

    print()
    print("=" * 72)
    print("ERRORI")
    print("=" * 72)

    for error in errors:
        fail(error)

if warnings:

    print()
    print("=" * 72)
    print("AVVISI")
    print("=" * 72)

    for warning in warnings:
        print(f"[WARN] {warning}")

print()
print("=" * 72)

if errors:

    print("RISULTATO: FALLITO")
    print("La libreria richiede correzioni.")
    sys.exit(1)

else:

    print("RISULTATO: STRUTTURALMENTE VALIDA")
    print("Tutti i preset hanno superato la verifica strutturale.")
    sys.exit(0)
