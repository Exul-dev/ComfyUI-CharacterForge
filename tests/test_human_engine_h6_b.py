from __future__ import annotations

import pytest

from human.age import (
    AgeAxis,
    AgeCurves,
    BodyAging,
    apparent_age,
)
from human.human import Human


class TestHumanEngineH6B:

    # --- vocabolario (2) ---

    def test_axes_cardinality_measured(self):
        # Cardinality MEASURED from the module (not declared).
        assert len(list(AgeAxis)) == 26
        assert len(AgeCurves.axes()) == 26

    def test_body_aging_axes_vocabulary(self):
        expected = [
            "body_skin_thinning",
            "fat_redistribution",
            "muscle_mass_loss",
            "postural_stooping",
            "stature_loss",
            "strength_loss",
        ]
        assert sorted(BodyAging.VALID_AXES) == expected
        assert len(BodyAging.VALID_AXES) == 6

    def test_default_is_age_neutral(self):
        body = BodyAging()

        assert body.is_valid()
        assert body.component_type == "body_aging"
        for axis in BodyAging.VALID_AXES:
            assert getattr(body, axis) == 0.0, axis

    def test_validation_ranges(self):
        for axis in BodyAging.VALID_AXES:
            with pytest.raises(ValueError, match=axis):
                BodyAging(**{axis: 1.5})

            with pytest.raises(ValueError, match=axis):
                BodyAging(**{axis: -0.1})

        assert BodyAging(
            **{axis: 1.0 for axis in BodyAging.VALID_AXES}
        ).is_valid()

    # --- le proporzioni del corpo (3) ---

    def test_strength_drops_before_and_faster_than_mass(self):
        # THE gerontological dissociation: strength declines
        # EARLIER and FASTER than mass. Two separate axes,
        # never conflated.
        for age in (35, 45, 55, 65, 75, 85):
            strength = AgeCurves.value(AgeAxis.STRENGTH_LOSS, age)
            mass = AgeCurves.value(AgeAxis.MUSCLE_MASS_LOSS, age)

            assert strength >= mass, (
                f"strength must lead mass at {age}"
            )

    def test_stooping_is_last_to_arrive(self):
        for age in (50, 60, 70, 80):
            stoop = AgeCurves.value(
                AgeAxis.POSTURAL_STOOPING, age
            )
            mass = AgeCurves.value(
                AgeAxis.MUSCLE_MASS_LOSS, age
            )
            strength = AgeCurves.value(
                AgeAxis.STRENGTH_LOSS, age
            )

            assert stoop <= mass, (
                f"stooping must trail mass at {age}"
            )
            assert stoop <= strength, (
                f"stooping must trail strength at {age}"
            )

    def test_stature_loss_is_modest(self):
        # Late onset and modest ceiling: even at 100 it stays
        # below 0.5 (the real decline is a few centimeters).
        # Onset anchor is (40, 0.0): the zero boundary is the
        # anchor age itself (the smoothstep lesson — inside
        # the 40->55 segment the curve is already alive, e.g.
        # 0.037 at 50).
        assert AgeCurves.value(AgeAxis.STATURE_LOSS, 40) == 0.0
        assert AgeCurves.value(AgeAxis.STATURE_LOSS, 50) > 0.0
        assert AgeCurves.value(AgeAxis.STATURE_LOSS, 100) < 0.5

    def test_mass_onset_after_35(self):
        assert AgeCurves.value(AgeAxis.MUSCLE_MASS_LOSS, 35) == 0.0
        assert AgeCurves.value(AgeAxis.MUSCLE_MASS_LOSS, 50) > 0.0

    # --- l operatore esteso (4) ---

    def test_apparent_age_configures_body(self):
        human = Human(name="Body Op")
        apparent_age(human, 70)

        assert human.has_component("body_aging")
        assert human.validate() is None

        body = human.get_component("body_aging")
        snap = AgeCurves.snapshot(70)

        assert body.strength_loss == snap[AgeAxis.STRENGTH_LOSS]
        assert body.muscle_mass_loss == snap[AgeAxis.MUSCLE_MASS_LOSS]
        assert body.fat_redistribution == snap[AgeAxis.FAT_REDISTRIBUTION]
        assert body.postural_stooping == snap[AgeAxis.POSTURAL_STOOPING]
        assert body.stature_loss == snap[AgeAxis.STATURE_LOSS]
        assert body.body_skin_thinning == snap[AgeAxis.BODY_SKIN_THINNING]

    def test_body_report_included(self):
        human = Human(name="Body Report")
        result = apparent_age(human, 70)

        body_changed = result.changed_fields("body_aging")

        assert "strength_loss" in body_changed
        assert "muscle_mass_loss" in body_changed
        assert "postural_stooping" in body_changed

    def test_face_not_broken_by_body(self):
        # The face and skin still configured after the body
        # extension: nothing broke.
        human = Human(name="Not Broken")
        apparent_age(human, 70)

        snap = AgeCurves.snapshot(70)

        skin = human.get_component("skin_aging")
        assert skin.wrinkle_depth == snap[AgeAxis.WRINKLE_DEPTH]

        face = human.get_component("face_aging")
        assert face.nasolabial_fold_depth == snap[AgeAxis.NASOLABIAL_FOLD]

    def test_body_idempotent_and_reversible(self):
        human = Human(name="Body Reversal")
        apparent_age(human, 80)

        # Idempotent
        r2 = apparent_age(human, 80)
        assert len(r2.changes) == 0

        # Reversible
        apparent_age(human, 25)
        body = human.get_component("body_aging")

        assert body.strength_loss < 0.2
        assert body.postural_stooping == 0.0
        assert body.stature_loss == 0.0
        assert body.muscle_mass_loss == 0.0

    # --- serializzazione (1) ---

    def test_body_serialization(self):
        human = Human(name="Body Serialization")
        apparent_age(human, 75)

        data = human.to_dict()
        components = data["human_engine"]["components"]

        assert "body_aging" in components
        assert (
            components["body_aging"]["strength_loss"] > 0.6
        )
        assert (
            components["body_aging"]["stature_loss"] > 0.1
        )

    # --- export (1) ---

    def test_package_exports_h6b(self):
        from human import age as age_pkg

        assert hasattr(age_pkg, "BodyAging")
        assert "BodyAging" in age_pkg.__all__
