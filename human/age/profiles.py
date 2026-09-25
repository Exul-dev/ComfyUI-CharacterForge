"""Age profiles (Human Engine, H6-C2b — Age Engine).

PROFILES are the ways of aging: named multipliers over the
AgeCurves matrix. A profile scales each axis by its own
factor — the gerontological SHAPE (who leads, who trails)
comes from the curves; the profile tilts the whole picture.

Sex-specific variants: where gerontology documents REAL
differences (graying onset/pace, sarcopenia timing, stature
loss, stooping), each profile carries MALE and FEMALE
variants. The sex is NEVER inferred: the caller passes it
explicitly (or gets the neutral TYPICAL baseline), the same
explicit-composition principle as ReproductiveSystem (H4.20).

Coverage: every age is covered BY CONSTRUCTION — the curves
interpolate continuously 0..100, profiles scale them: the
( age x profile x sex ) space is the full coverage, not a
list of discrete presets.

Scope: ADULT aging. Pediatric development (an 8-year-old is
not a wrinkled-less adult — different body proportions) is
a SEPARATE chapter (developmental body scaling), not a
profile.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from .curves import AgeAxis


class AgeProfile(Enum):
    """The named ways of aging."""

    TYPICAL = "typical"
    GRACEFUL = "graceful"
    WEATHERED = "weathered"
    SEDENTARY = "sedentary"
    ATHLETIC = "athletic"
    SMOKER = "smoker"
    PREMATURE = "premature"


class ProfileSex(Enum):
    """Sex variant for the profile multipliers."""

    NEUTRAL = "neutral"
    MALE = "male"
    FEMALE = "female"


# Multiplier tables: axis -> factor. A factor of 1.0 leaves
# the curve untouched. The tables only list the axes each
# profile actually tilts: every other axis stays 1.0.

_BASE_MULTIPLIERS: dict[AgeProfile, dict[AgeAxis, float]] = {
    AgeProfile.TYPICAL: {},
    AgeProfile.GRACEFUL: {
        AgeAxis.WRINKLE_DEPTH: 0.7,
        AgeAxis.SAGGING: 0.75,
        AgeAxis.ELASTICITY: 1.2,  # inverted axis: HIGHER = better
        AgeAxis.AGE_SPOTS: 0.6,
        AgeAxis.NASOLABIAL_FOLD: 0.7,
        AgeAxis.MARIONETTE_FOLD: 0.7,
        AgeAxis.SCALP_GRAY: 0.8,
        AgeAxis.FACIAL_GRAY: 0.8,
    },
    AgeProfile.WEATHERED: {
        AgeAxis.WRINKLE_DEPTH: 1.4,
        AgeAxis.SAGGING: 1.3,
        AgeAxis.ELASTICITY: 0.8,
        AgeAxis.AGE_SPOTS: 1.6,
        AgeAxis.SCALP_GRAY: 1.1,
        AgeAxis.GRAY_TEXTURE: 1.2,
        AgeAxis.MANDIBULAR_LOSS: 1.1,
    },
    AgeProfile.SEDENTARY: {
        AgeAxis.MUSCLE_MASS_LOSS: 1.3,
        AgeAxis.STRENGTH_LOSS: 1.2,
        AgeAxis.FAT_REDISTRIBUTION: 1.2,
        AgeAxis.POSTURAL_STOOPING: 1.25,
    },
    AgeProfile.ATHLETIC: {
        AgeAxis.MUSCLE_MASS_LOSS: 0.7,
        AgeAxis.STRENGTH_LOSS: 0.75,
        AgeAxis.FAT_REDISTRIBUTION: 0.7,
        AgeAxis.POSTURAL_STOOPING: 1.15,  # joint wear
        AgeAxis.ELASTICITY: 1.1,
    },
    AgeProfile.SMOKER: {
        AgeAxis.WRINKLE_DEPTH: 1.2,
        AgeAxis.ELASTICITY: 0.8,
        AgeAxis.SAGGING: 1.15,
        AgeAxis.SCALP_GRAY: 1.2,
        AgeAxis.FACIAL_GRAY: 1.2,
        AgeAxis.GRAY_TEXTURE: 1.15,
        AgeAxis.AGE_SPOTS: 1.1,
    },
    AgeProfile.PREMATURE: {
        AgeAxis.WRINKLE_DEPTH: 1.5,
        AgeAxis.SAGGING: 1.5,
        AgeAxis.ELASTICITY: 0.6,
        AgeAxis.AGE_SPOTS: 1.4,
        AgeAxis.SCALP_GRAY: 1.5,
        AgeAxis.FACIAL_GRAY: 1.5,
        AgeAxis.BODY_GRAY: 1.4,
        AgeAxis.GRAY_TEXTURE: 1.3,
        AgeAxis.MUSCLE_MASS_LOSS: 1.4,
        AgeAxis.STRENGTH_LOSS: 1.4,
        AgeAxis.POSTURAL_STOOPING: 1.5,
        AgeAxis.STATURE_LOSS: 1.3,
    },
}

# Sex-specific OVERRIDES: layered on top of the base table.
# Only where gerontology documents real differences.
_SEX_OVERRIDES: dict[ProfileSex, dict[AgeAxis, float]] = {
    ProfileSex.FEMALE: {
        AgeAxis.SCALP_GRAY: 0.9,      # later onset, then faster
        AgeAxis.FACIAL_GRAY: 0.9,
        AgeAxis.MUSCLE_MASS_LOSS: 0.85,  # later sarcopenia
        AgeAxis.STRENGTH_LOSS: 0.85,
        AgeAxis.STATURE_LOSS: 1.4,    # bone density loss
        AgeAxis.POSTURAL_STOOPING: 1.2,
    },
    ProfileSex.MALE: {
        AgeAxis.SCALP_GRAY: 1.1,      # earlier graying
        AgeAxis.FACIAL_GRAY: 1.1,
        AgeAxis.MUSCLE_MASS_LOSS: 1.1,  # earlier sarcopenia
        AgeAxis.STRENGTH_LOSS: 1.1,
        AgeAxis.STATURE_LOSS: 0.9,
    },
    ProfileSex.NEUTRAL: {},
}


def profile_multiplier(
    profile: AgeProfile,
    axis: AgeAxis,
    sex: ProfileSex = ProfileSex.NEUTRAL,
) -> float:
    """The multiplier for one axis under one profile and sex.

    Composition: base table x sex override. Both default to
    1.0 (untouched curve).
    """

    if not isinstance(profile, AgeProfile):
        raise ValueError(
            "profile must be an AgeProfile value."
        )

    if not isinstance(axis, AgeAxis):
        raise ValueError(
            "axis must be an AgeAxis value."
        )

    if not isinstance(sex, ProfileSex):
        raise ValueError(
            "sex must be a ProfileSex value."
        )

    base = _BASE_MULTIPLIERS[profile].get(axis, 1.0)
    override = _SEX_OVERRIDES[sex].get(axis, 1.0)

    return base * override


def profile_snapshot(
    age: float,
    profile: AgeProfile,
    sex: ProfileSex = ProfileSex.NEUTRAL,
) -> dict[AgeAxis, float]:
    """The scaled curves for one age, profile and sex.

    Every axis value = curve(age) x multiplier(profile, axis,
    sex), clamped to [0, 1] (multipliers can push beyond the
    curve: never beyond the representable range).
    """

    from .curves import AgeCurves

    result: dict[AgeAxis, float] = {}

    for axis in AgeCurves.axes():
        raw = AgeCurves.value(axis, age)
        scaled = raw * profile_multiplier(profile, axis, sex)
        result[axis] = max(0.0, min(1.0, scaled))

    return result


def _describe(profile: AgeProfile) -> str:
    """Human-readable summary for logging and UI."""

    return {
        AgeProfile.TYPICAL: "the average aging line",
        AgeProfile.GRACEFUL: "ages well: fewer lines, better elasticity",
        AgeProfile.WEATHERED: "hard living and sun: lines and spots amplified",
        AgeProfile.SEDENTARY: "inactive: sarcopenia and redistribution amplified",
        AgeProfile.ATHLETIC: "trained: muscle preserved, joints pay",
        AgeProfile.SMOKER: "smoking skin: elasticity and color age faster",
        AgeProfile.PREMATURE: "accelerated aging across all axes",
    }[profile]