"""The apparent_age operator (Human Engine, H6-C2 — Age Engine).

ONE DIAL, TWENTY PROPORTIONS. This is the operator the future
ComfyUI node exposes: a single age number that configures every
aging component proportionally, after the AgeCurves matrix.

What it does:

1. reads the AgeCurves snapshot for the target age;
2. UPDATES the existing SkinAging, HairAging, FaceAging on the
   Human entity IN PLACE (or creates them if absent) — the
   old -> new comparison is always against the CURRENT state,
   making the report truthful and the operator idempotent;
3. returns an AgeResult: a field-by-field changed/preserved
   report.

Idempotency: calling apparent_age(h, 60) twice reports every
field as PRESERVED on the second call — the operator compares
against the current state, not against factory defaults. This
is the fix over the first draft, which always rebuilt from
scratch and reported false changes.

What it does NOT do (by design):

- it never touches ChronologicalAge or DevelopmentalStage;
- it never touches identity or anatomy structure;
- it does not "partially age": it SETS the target state
  (trajectories are H6-D's concern).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..anatomy.face_aging import FaceAging
from ..hair.hair_aging import GrayingPattern, HairAging
from ..skin.skin_aging import SkinAging, WrinkleZone
from .curves import AgeAxis, AgeCurves

# Zone salience for wrinkle distribution.
_ZONE_SALIENCE: dict[WrinkleZone, float] = {
    WrinkleZone.FOREHEAD: 1.0,
    WrinkleZone.CROW_FEET: 0.95,
    WrinkleZone.NASOLABIAL: 1.0,
    WrinkleZone.GLABELLA: 0.85,
    WrinkleZone.UNDER_EYE: 0.8,
    WrinkleZone.PERIORAL: 0.75,
    WrinkleZone.MARIONETTE: 0.8,
    WrinkleZone.NECK: 0.7,
    WrinkleZone.DECOLLETE: 0.5,
    WrinkleZone.HANDS: 0.6,
}


def _graying_pattern_for(extent: float) -> GrayingPattern:
    if extent <= 0.0:
        return GrayingPattern.NONE
    if extent < 0.35:
        return GrayingPattern.TEMPLES_FIRST
    if extent < 0.7:
        return GrayingPattern.SALT_PEPPER
    return GrayingPattern.DIFFUSE


@dataclass
class FieldChange:
    """One property transition."""

    component: str
    field: str
    before: Any
    after: Any


@dataclass
class AgeResult:
    """The changed/preserved report of an apparent_age call."""

    target_age: float
    changes: list[FieldChange] = field(default_factory=list)
    preserved: list[str] = field(default_factory=list)

    def changed_fields(self, component: str) -> list[str]:
        return [
            c.field for c in self.changes
            if c.component == component
        ]

    def preserved_fields(self, component: str) -> list[str]:
        return [
            p.split(".")[1]
            for p in self.preserved
            if p.startswith(component + ".")
        ]

    def to_dict(self) -> dict[str, Any]:
        return {
            "target_age": self.target_age,
            "changes": [
                {
                    "component": c.component,
                    "field": c.field,
                    "before": c.before,
                    "after": c.after,
                }
                for c in self.changes
            ],
            "preserved": list(self.preserved),
        }


def _set_and_record(
    result: AgeResult,
    component_name: str,
    obj: Any,
    attr: str,
    new_value: Any,
) -> None:
    """Set a field IN PLACE and record the true transition.

    The comparison is against the CURRENT value of the field
    on the (possibly pre-existing) component: truthful reports
    and idempotency by construction.
    """

    old = getattr(obj, attr, None)

    if old != new_value:
        setattr(obj, attr, new_value)
        result.changes.append(
            FieldChange(
                component=component_name,
                field=attr,
                before=old,
                after=new_value,
            )
        )
    else:
        result.preserved.append(
            component_name + "." + attr
        )


def _update_skin_aging(
    result: AgeResult,
    skin: SkinAging,
    age: float,
) -> None:
    """Update an EXISTING SkinAging in place from the curves."""

    snap = AgeCurves.snapshot(age)

    _set_and_record(result, "skin_aging", skin, "wrinkle_depth",
                     snap[AgeAxis.WRINKLE_DEPTH])
    _set_and_record(result, "skin_aging", skin, "elasticity",
                     snap[AgeAxis.ELASTICITY])
    _set_and_record(result, "skin_aging", skin, "sagging",
                     snap[AgeAxis.SAGGING])
    _set_and_record(result, "skin_aging", skin, "age_spots",
                     snap[AgeAxis.AGE_SPOTS])

    base = snap[AgeAxis.WRINKLE_DEPTH]
    for zone in WrinkleZone:
        salience = _ZONE_SALIENCE.get(zone, 0.7)
        zone_value = round(base * salience, 4)
        old = skin.wrinkle_map.get(zone, 0.0)
        skin.wrinkle_map[zone] = zone_value

        if old != zone_value:
            result.changes.append(
                FieldChange(
                    component="skin_aging",
                    field=f"wrinkle_map.{zone.value}",
                    before=old,
                    after=zone_value,
                )
            )
        else:
            result.preserved.append(
                f"skin_aging.wrinkle_map.{zone.value}"
            )

    skin.validate()


def _update_hair_aging(
    result: AgeResult,
    hair: HairAging,
    age: float,
) -> None:
    """Update an EXISTING HairAging in place from the curves."""

    snap = AgeCurves.snapshot(age)

    _set_and_record(result, "hair_aging", hair, "scalp_gray_extent",
                     snap[AgeAxis.SCALP_GRAY])
    _set_and_record(result, "hair_aging", hair, "facial_gray_extent",
                     snap[AgeAxis.FACIAL_GRAY])
    _set_and_record(result, "hair_aging", hair, "body_gray_extent",
                     snap[AgeAxis.BODY_GRAY])
    _set_and_record(result, "hair_aging", hair, "gray_hair_texture",
                     snap[AgeAxis.GRAY_TEXTURE])

    pattern = _graying_pattern_for(snap[AgeAxis.SCALP_GRAY])
    _set_and_record(result, "hair_aging", hair, "graying_pattern",
                     pattern)

    hair.validate()


_FACE_AXIS_MAP = {
    "midface_descent": AgeAxis.MIDFACE_DESCENT,
    "jowl_formation": AgeAxis.JOWL_FORMATION,
    "nasolabial_fold_depth": AgeAxis.NASOLABIAL_FOLD,
    "marionette_fold_depth": AgeAxis.MARIONETTE_FOLD,
    "cheek_hollowing": AgeAxis.CHEEK_HOLLOWING,
    "lip_volume_loss": AgeAxis.LIP_VOLUME_LOSS,
    "earlobe_elongation": AgeAxis.EARLOBE_ELONGATION,
    "temporal_hollowing": AgeAxis.TEMPORAL_HOLLOWING,
    "brow_descent": AgeAxis.BROW_DESCENT,
    "upper_lid_ptosis": AgeAxis.UPPER_LID_PTOSIS,
    "orbital_hollowing": AgeAxis.ORBITAL_HOLLOWING,
    "mandibular_definition_loss": AgeAxis.MANDIBULAR_LOSS,
}


def _update_face_aging(
    result: AgeResult,
    face: FaceAging,
    age: float,
) -> None:
    """Update an EXISTING FaceAging in place from the curves."""

    snap = AgeCurves.snapshot(age)

    for field_name, axis in _FACE_AXIS_MAP.items():
        _set_and_record(
            result, "face_aging", face, field_name,
            snap[axis],
        )

    face.validate()


def _get_or_register(human: Any, name: str, factory: Any) -> Any:
    """Get the existing component or register a fresh one.

    The component is always MUTATED IN PLACE afterwards: the
    operator never discards the current state.
    """

    if human.has_component(name):
        return human.get_component(name)

    fresh = factory()
    human.register_component(name, fresh)
    return fresh


def apparent_age(human: Any, age: float) -> AgeResult:
    """Set a Human's apparent age with one call.

    Updates SkinAging, HairAging and FaceAging IN PLACE on the
    given Human entity, proportionally to the AgeCurves matrix.
    Returns an AgeResult with the field-by-field changed/
    preserved report — truthful against the CURRENT state.

    Idempotent: same age twice -> second report is all
    preserved. Rejuvenating: younger age -> changes reflect
    the actual regression.
    """

    if age < 0:
        raise ValueError(
            "apparent_age age cannot be negative."
        )

    result = AgeResult(target_age=age)

    skin = _get_or_register(human, "skin_aging", SkinAging)
    hair = _get_or_register(human, "hair_aging", HairAging)
    face = _get_or_register(human, "face_aging", FaceAging)

    _update_skin_aging(result, skin, age)
    _update_hair_aging(result, hair, age)
    _update_face_aging(result, face, age)

    return result