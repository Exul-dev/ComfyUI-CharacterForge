"""Age response curves (Human Engine, H6-C1 — Age Engine).

THE MATRIX: each aging axis has a RESPONSE CURVE to age —
its own onset, slope and shape, after the gerontological
literature. The curves turn "70 years old" into the RIGHT
VALUES on the RIGHT AXES in the RIGHT PROPORTIONS: folds lead,
bone follows, elasticity inverts, fotoaging can start early.

Curve representation: 4-6 ANCHOR POINTS (age, value) per axis,
smoothstep-interpolated in between. Compact vocabulary,
continuous curves — meticulous underneath, simple on top.

Monotonicity: curves only ascend (or descend, for inverted
axes like elasticity). Aging does not regress ON A CURVE;
regression is a trajectory concern (H6-D), not a curve
property.
"""

from __future__ import annotations

from enum import Enum
from typing import Any


class AgeAxis(Enum):
    """The aging axes the curves drive.

    Grouped by the component that owns them (H6-A layers).
    """

    # --- SkinAging (surface) ---
    WRINKLE_DEPTH = "wrinkle_depth"
    ELASTICITY = "elasticity"           # inverted: 1 -> 0
    SAGGING = "sagging"
    AGE_SPOTS = "age_spots"

    # --- HairAging (color) ---
    SCALP_GRAY = "scalp_gray_extent"
    FACIAL_GRAY = "facial_gray_extent"
    BODY_GRAY = "body_gray_extent"
    GRAY_TEXTURE = "gray_hair_texture"

    # --- FaceAging (soft tissue) ---
    MIDFACE_DESCENT = "midface_descent"
    JOWL_FORMATION = "jowl_formation"
    NASOLABIAL_FOLD = "nasolabial_fold_depth"
    MARIONETTE_FOLD = "marionette_fold_depth"
    CHEEK_HOLLOWING = "cheek_hollowing"
    LIP_VOLUME_LOSS = "lip_volume_loss"
    EARLOBE_ELONGATION = "earlobe_elongation"
    TEMPORAL_HOLLOWING = "temporal_hollowing"
    BROW_DESCENT = "brow_descent"
    UPPER_LID_PTOSIS = "upper_lid_ptosis"
    ORBITAL_HOLLOWING = "orbital_hollowing"
    MANDIBULAR_LOSS = "mandibular_definition_loss"

    # --- BodyAging (the body below the face) ---
    MUSCLE_MASS_LOSS = "muscle_mass_loss"
    STRENGTH_LOSS = "strength_loss"
    FAT_REDISTRIBUTION = "fat_redistribution"
    POSTURAL_STOOPING = "postural_stooping"
    STATURE_LOSS = "stature_loss"
    BODY_SKIN_THINNING = "body_skin_thinning"


def _smoothstep(t: float) -> float:
    """Smooth 0..1 interpolation (no corners, time flows)."""

    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)


class AgeCurves:
    """The age -> value matrix, anchor-interpolated.

    Each axis maps to a list of (age, value) anchors. The
    value at any age derives by smoothstep interpolation
    between the surrounding anchors: the vocabulary is small,
    the curve is continuous.
    """

    # Anchor points per axis: (age, value).
    # Sources: simplified gerontological norms, documented
    # per axis. These are the TYPICAL aging trajectories —
    # H6-C2 profiles scale them per character.
    _CURVES: dict[AgeAxis, tuple[tuple[float, float], ...]] = {
        # --- surface ---
        AgeAxis.WRINKLE_DEPTH: (
            (0, 0.0), (25, 0.05), (35, 0.2), (50, 0.45),
            (65, 0.7), (80, 0.9), (100, 1.0),
        ),
        AgeAxis.ELASTICITY: (  # inverted: starts full
            (0, 1.0), (25, 0.95), (40, 0.75), (60, 0.5),
            (75, 0.3), (90, 0.15), (100, 0.1),
        ),
        AgeAxis.SAGGING: (
            (0, 0.0), (30, 0.05), (45, 0.2), (60, 0.5),
            (75, 0.75), (90, 0.9), (100, 1.0),
        ),
        AgeAxis.AGE_SPOTS: (
            (0, 0.0), (35, 0.05), (50, 0.2), (65, 0.45),
            (80, 0.7), (100, 0.9),
        ),
        # --- hair color ---
        AgeAxis.SCALP_GRAY: (
            (0, 0.0), (30, 0.0), (40, 0.1), (50, 0.3),
            (60, 0.55), (70, 0.75), (85, 0.9), (100, 1.0),
        ),
        AgeAxis.FACIAL_GRAY: (  # beard grays FIRST
            (0, 0.0), (28, 0.05), (38, 0.2), (48, 0.45),
            (60, 0.7), (75, 0.85), (100, 1.0),
        ),
        AgeAxis.BODY_GRAY: (  # body stays dark longer
            (0, 0.0), (35, 0.0), (50, 0.1), (65, 0.3),
            (80, 0.5), (100, 0.7),
        ),
        AgeAxis.GRAY_TEXTURE: (
            (0, 0.0), (35, 0.0), (50, 0.15), (65, 0.4),
            (80, 0.6), (100, 0.75),
        ),
        # --- soft tissue descent ---
        AgeAxis.MIDFACE_DESCENT: (
            (0, 0.0), (30, 0.0), (45, 0.15), (60, 0.45),
            (75, 0.7), (90, 0.85), (100, 0.95),
        ),
        AgeAxis.JOWL_FORMATION: (
            (0, 0.0), (35, 0.0), (50, 0.15), (65, 0.45),
            (80, 0.7), (100, 0.85),
        ),
        AgeAxis.NASOLABIAL_FOLD: (  # the FIRST fold, ~25
            (0, 0.0), (25, 0.05), (35, 0.2), (50, 0.4),
            (65, 0.6), (80, 0.8), (100, 0.9),
        ),
        AgeAxis.MARIONETTE_FOLD: (
            (0, 0.0), (35, 0.0), (50, 0.15), (65, 0.4),
            (80, 0.65), (100, 0.8),
        ),
        AgeAxis.CHEEK_HOLLOWING: (
            (0, 0.0), (30, 0.0), (45, 0.15), (60, 0.4),
            (75, 0.65), (90, 0.8), (100, 0.9),
        ),
        # --- volume loss ---
        AgeAxis.LIP_VOLUME_LOSS: (
            (0, 0.0), (30, 0.05), (45, 0.25), (60, 0.45),
            (75, 0.6), (90, 0.7), (100, 0.75),
        ),
        AgeAxis.EARLOBE_ELONGATION: (
            (0, 0.0), (40, 0.05), (55, 0.2), (70, 0.45),
            (85, 0.65), (100, 0.8),
        ),
        AgeAxis.TEMPORAL_HOLLOWING: (
            (0, 0.0), (40, 0.0), (55, 0.15), (70, 0.4),
            (85, 0.6), (100, 0.75),
        ),
        # --- ptosis ---
        AgeAxis.BROW_DESCENT: (
            (0, 0.0), (40, 0.05), (55, 0.2), (70, 0.45),
            (85, 0.65), (100, 0.8),
        ),
        AgeAxis.UPPER_LID_PTOSIS: (  # accelerates after 55
            (0, 0.0), (40, 0.05), (55, 0.15), (65, 0.35),
            (75, 0.6), (85, 0.75), (100, 0.85),
        ),
        # --- bony contour (the last to show) ---
        AgeAxis.ORBITAL_HOLLOWING: (
            (0, 0.0), (45, 0.0), (60, 0.15), (75, 0.4),
            (90, 0.6), (100, 0.7),
        ),
        AgeAxis.MANDIBULAR_LOSS: (
            (0, 0.0), (45, 0.0), (60, 0.1), (75, 0.3),
            (90, 0.5), (100, 0.6),
        ),
        # --- body: the real mass/strength dissociation ---
        AgeAxis.MUSCLE_MASS_LOSS: (
            (0, 0.0), (35, 0.0), (50, 0.1), (65, 0.3),
            (80, 0.5), (95, 0.7), (100, 0.75),
        ),
        AgeAxis.STRENGTH_LOSS: (
            (0, 0.0), (28, 0.05), (40, 0.15), (55, 0.35),
            (70, 0.6), (85, 0.8), (100, 0.9),
        ),
        AgeAxis.FAT_REDISTRIBUTION: (
            (0, 0.0), (30, 0.05), (45, 0.2), (60, 0.4),
            (75, 0.6), (90, 0.75), (100, 0.8),
        ),
        AgeAxis.POSTURAL_STOOPING: (
            (0, 0.0), (50, 0.0), (65, 0.1), (80, 0.3),
            (95, 0.5), (100, 0.55),
        ),
        AgeAxis.STATURE_LOSS: (
            (0, 0.0), (40, 0.0), (55, 0.05), (70, 0.15),
            (85, 0.3), (100, 0.4),
        ),
        AgeAxis.BODY_SKIN_THINNING: (
            (0, 0.0), (35, 0.0), (50, 0.1), (65, 0.3),
            (80, 0.5), (100, 0.65),
        ),
    }

    @classmethod
    def axes(cls) -> list[AgeAxis]:
        """All the axes the curves drive."""

        return list(cls._CURVES.keys())

    @classmethod
    def value(cls, axis: AgeAxis, age: float) -> float:
        """The axis value at the given age.

        Smoothstep-interpolated between anchors: continuous,
        corner-free. Below the first anchor returns the first
        value; above the last, the last.
        """

        if not isinstance(axis, AgeAxis):
            raise ValueError(
                "AgeCurves axis must be an AgeAxis value."
            )

        if age < 0:
            raise ValueError(
                "AgeCurves age cannot be negative."
            )

        anchors = cls._CURVES[axis]

        if age <= anchors[0][0]:
            return anchors[0][1]

        if age >= anchors[-1][0]:
            return anchors[-1][1]

        for index in range(len(anchors) - 1):
            age_a, value_a = anchors[index]
            age_b, value_b = anchors[index + 1]

            if age_a <= age <= age_b:
                span = age_b - age_a

                if span <= 0:
                    return value_b

                t = (age - age_a) / span
                t = _smoothstep(t)

                return value_a + (value_b - value_a) * t

        return anchors[-1][1]

    @classmethod
    def snapshot(cls, age: float) -> dict[AgeAxis, float]:
        """Every axis value at the given age: the full matrix
        column. The base for H6-C2 profiles."""

        return {
            axis: cls.value(axis, age)
            for axis in cls._CURVES
        }
