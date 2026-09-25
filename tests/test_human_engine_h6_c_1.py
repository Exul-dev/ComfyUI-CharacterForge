from __future__ import annotations

import pytest

from human.age import AgeAxis, AgeCurves


class TestHumanEngineH6C1:

    # --- vocabolario (2) ---

    def test_axes_cardinality_measured(self):
        # Cardinality MEASURED from the module (not declared):
        # the lesson of the 21-vs-20 assert.
        enum_count = len(list(AgeAxis))
        curve_count = len(AgeCurves.axes())

        assert enum_count == curve_count  # enum == dict
        assert enum_count >= 15  # sanity: all layers present
        # 4 skin + 4 hair + 12 face + 6 body = 26
        # (H6-B extended the matrix 20 -> 26: contract evolution,
        # same precedent as Hair VALID_LENGTHS 6 -> 7. This test
        # failing after the extension was the cardinality guard
        # doing its job.)
        assert enum_count == 26

    def test_every_axis_has_a_curve(self):
        assert set(AgeCurves.axes()) == set(AgeAxis)

    # --- le proporzioni (il cuore della richiesta) (4) ---

    def test_folds_lead_bone_at_all_ages(self):
        # THE gerontological hierarchy: soft tissue shows first,
        # bone contour last — at every age where both exist.
        for age in (40, 50, 60, 70, 80, 90):
            nasolabial = AgeCurves.value(
                AgeAxis.NASOLABIAL_FOLD, age
            )
            orbital = AgeCurves.value(
                AgeAxis.ORBITAL_HOLLOWING, age
            )
            mandibular = AgeCurves.value(
                AgeAxis.MANDIBULAR_LOSS, age
            )

            assert nasolabial >= orbital, (
                f"folds must lead orbital at {age}"
            )
            assert nasolabial >= mandibular, (
                f"folds must lead mandibular at {age}"
            )

    def test_beard_grays_before_scalp_before_body(self):
        # The real sequence: facial > scalp > body gray.
        for age in (40, 50, 60, 70, 80):
            facial = AgeCurves.value(
                AgeAxis.FACIAL_GRAY, age
            )
            scalp = AgeCurves.value(
                AgeAxis.SCALP_GRAY, age
            )
            body = AgeCurves.value(
                AgeAxis.BODY_GRAY, age
            )

            assert facial >= scalp, (
                f"beard must lead scalp at {age}"
            )
            assert scalp >= body, (
                f"scalp must lead body at {age}"
            )

    def test_elasticity_is_inverted(self):
        # Starts at 1.0 (youth), DECREASES with age.
        young = AgeCurves.value(AgeAxis.ELASTICITY, 20)
        old = AgeCurves.value(AgeAxis.ELASTICITY, 80)

        assert young > 0.9  # near-full resilience
        assert old < young  # inverted: descends
        assert old < 0.4   # well below half

        # Monotone DESCENT
        prev = AgeCurves.value(AgeAxis.ELASTICITY, 0)
        for age in range(1, 101):
            curr = AgeCurves.value(AgeAxis.ELASTICITY, age)
            assert curr <= prev + 1e-9, (
                f"elasticity must not increase at {age}"
            )
            prev = curr

    def test_ptosis_accelerates_after_55(self):
        # The real acceleration: 55->65 grows more than 45->55.
        p45 = AgeCurves.value(AgeAxis.UPPER_LID_PTOSIS, 45)
        p55 = AgeCurves.value(AgeAxis.UPPER_LID_PTOSIS, 55)
        p65 = AgeCurves.value(AgeAxis.UPPER_LID_PTOSIS, 65)

        assert (p65 - p55) > (p55 - p45)

    # --- monotonicità generale (1) ---

    def test_damage_axes_are_monotone_ascending(self):
        # Aging signs do not regress ON A CURVE (regression is
        # a trajectory concern, H6-D).
        damage_axes = [
            axis for axis in AgeAxis
            if axis is not AgeAxis.ELASTICITY
        ]

        for axis in damage_axes:
            prev = AgeCurves.value(axis, 0)
            for age in range(1, 101):
                curr = AgeCurves.value(axis, age)
                assert curr >= prev - 1e-9, (
                    f"{axis.value} regredisse at {age}"
                )
                prev = curr

    # --- continuità smoothstep (2) ---

    def test_no_abrupt_jumps(self):
        # Smoothstep means smooth: on 1-year steps the delta
        # must be tiny for every axis.
        for axis in AgeAxis:
            prev = AgeCurves.value(axis, 0)
            for age in range(1, 101):
                curr = AgeCurves.value(axis, age)
                assert abs(curr - prev) < 0.08, (
                    f"{axis.value}: jump {curr - prev} at {age}"
                )
                prev = curr

    def test_value_between_anchors_is_bounded(self):
        # Interpolation stays within the anchor values.
        for axis in AgeAxis:
            values = [
                AgeCurves.value(axis, age)
                for age in range(0, 101, 5)
            ]
            assert all(0.0 <= v <= 1.0 for v in values), (
                f"{axis.value}: out of range"
            )

    # --- clamp e validazione (3) ---

    def test_clamp_below_and_above_range(self):
        assert AgeCurves.value(AgeAxis.SAGGING, 0) == 0.0
        assert AgeCurves.value(
            AgeAxis.SAGGING, 150
        ) == AgeCurves.value(AgeAxis.SAGGING, 100)
        assert AgeCurves.value(
            AgeAxis.ELASTICITY, 150
        ) == AgeCurves.value(AgeAxis.ELASTICITY, 100)

    def test_rejects_negative_age(self):
        with pytest.raises(ValueError, match="negative"):
            AgeCurves.value(AgeAxis.SAGGING, -1)

    def test_rejects_invalid_axis(self):
        with pytest.raises(ValueError, match="AgeAxis"):
            AgeCurves.value("sagging", 50)

        with pytest.raises(ValueError, match="AgeAxis"):
            AgeCurves.value(None, 50)

    # --- snapshot (2) ---

    def test_snapshot_matches_value(self):
        snap = AgeCurves.snapshot(70)

        for axis in AgeAxis:
            assert snap[axis] == AgeCurves.value(axis, 70)

    def test_snapshot_covers_all_axes(self):
        snap = AgeCurves.snapshot(45)

        assert set(snap.keys()) == set(AgeAxis)

    # --- le età chiave (3) ---

    def test_young_20_is_mostly_neutral(self):
        snap = AgeCurves.snapshot(20)

        # The first nasolabial hint exists (the first fold ~25)
        assert snap[AgeAxis.NASOLABIAL_FOLD] > 0.0
        # But almost everything else is minimal
        assert snap[AgeAxis.SAGGING] < 0.05
        assert snap[AgeAxis.SCALP_GRAY] == 0.0
        assert snap[AgeAxis.MANDIBULAR_LOSS] == 0.0
        # Elasticity still high
        assert snap[AgeAxis.ELASTICITY] > 0.9

    def test_seventy_is_proportionally_aged(self):
        snap = AgeCurves.snapshot(70)

        # The proportions, certified as numbers:
        assert snap[AgeAxis.WRINKLE_DEPTH] > 0.7  # deep lines
        assert snap[AgeAxis.FACIAL_GRAY] > 0.75  # well gray
        assert snap[AgeAxis.NASOLABIAL_FOLD] > 0.6
        assert snap[AgeAxis.MANDIBULAR_LOSS] < 0.3  # bone just starting
        assert snap[AgeAxis.ELASTICITY] < 0.4  # well lost
        # folds > bone (the hierarchy)
        assert snap[AgeAxis.NASOLABIAL_FOLD] > snap[AgeAxis.MANDIBULAR_LOSS]

    def test_ninety_is_near_maximum(self):
        snap = AgeCurves.snapshot(90)

        assert snap[AgeAxis.WRINKLE_DEPTH] > 0.85
        assert snap[AgeAxis.FACIAL_GRAY] > 0.85
        assert snap[AgeAxis.ELASTICITY] < 0.2

    # --- onset reali (1) ---

    def test_onsets_follow_gerontology(self):
        # Gray starts ~30-35 (not at 15)
        assert AgeCurves.value(AgeAxis.SCALP_GRAY, 25) == 0.0
        assert AgeCurves.value(AgeAxis.SCALP_GRAY, 40) > 0.0

        # Bone contour starts late (~45-60)
        # Mandibular onset anchor is (45, 0.0): BELOW 45 the
        # curve is exactly zero; at 50 it is already rising
        # inside the 45->60 segment (smoothstep). The boundary
        # for "still zero" is the anchor age itself.
        assert AgeCurves.value(AgeAxis.MANDIBULAR_LOSS, 45) == 0.0
        assert AgeCurves.value(AgeAxis.MANDIBULAR_LOSS, 50) > 0.0
        assert AgeCurves.value(AgeAxis.MANDIBULAR_LOSS, 65) > 0.0

        # The nasolabial fold is the FIRST (~25)
        assert AgeCurves.value(AgeAxis.NASOLABIAL_FOLD, 22) > 0.0
