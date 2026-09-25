from __future__ import annotations

import pytest

from human.anatomy import FaceAging
from human.anatomy.anatomy_component import AnatomyComponent
from human.human import Human


class TestHumanEngineH6A3:

    # --- vocabolario e default (3) ---

    def test_axes_vocabulary(self):
        expected = [
            "brow_descent",
            "cheek_hollowing",
            "earlobe_elongation",
            "jowl_formation",
            "lip_volume_loss",
            "mandibular_definition_loss",
            "marionette_fold_depth",
            "midface_descent",
            "nasolabial_fold_depth",
            "orbital_hollowing",
            "temporal_hollowing",
            "upper_lid_ptosis",
        ]
        assert sorted(FaceAging.VALID_AXES) == expected
        assert len(FaceAging.VALID_AXES) == 12

    def test_default_is_age_neutral(self):
        aging = FaceAging()

        assert aging.is_valid()
        assert aging.component_type == "face_aging"
        for axis in FaceAging.VALID_AXES:
            assert getattr(aging, axis) == 0.0, axis

    def test_is_anatomy_component(self):
        aging = FaceAging()

        assert isinstance(aging, AnatomyComponent)

    # --- assi indipendenti (3) ---

    def test_all_axes_independently_settable(self):
        kwargs = {axis: 0.5 for axis in FaceAging.VALID_AXES}
        aging = FaceAging(**kwargs)

        assert aging.is_valid()
        for axis in FaceAging.VALID_AXES:
            assert getattr(aging, axis) == 0.5

    def test_ptosis_only_clinical_case(self):
        ptosis = FaceAging(upper_lid_ptosis=0.9)

        assert ptosis.is_valid()
        assert ptosis.upper_lid_ptosis == 0.9
        assert ptosis.midface_descent == 0.0
        assert ptosis.nasolabial_fold_depth == 0.0

    def test_validation_ranges(self):
        with pytest.raises(ValueError, match="midface_descent"):
            FaceAging(midface_descent=1.5)

        with pytest.raises(ValueError, match="lip_volume_loss"):
            FaceAging(lip_volume_loss=-0.1)

        for axis in FaceAging.VALID_AXES:
            with pytest.raises(ValueError, match=axis):
                FaceAging(**{axis: 1.1})

        assert FaceAging(
            **{axis: 1.0 for axis in FaceAging.VALID_AXES}
        ).is_valid()

    # --- il volto anziano tipico (2) ---

    def test_typical_aged_face_is_representable(self):
        aged = FaceAging(
            midface_descent=0.7,
            jowl_formation=0.6,
            nasolabial_fold_depth=0.8,
            marionette_fold_depth=0.5,
            cheek_hollowing=0.6,
            lip_volume_loss=0.7,
            earlobe_elongation=0.4,
            temporal_hollowing=0.5,
            brow_descent=0.5,
            upper_lid_ptosis=0.6,
            orbital_hollowing=0.4,
            mandibular_definition_loss=0.5,
        )

        assert aged.is_valid()
        assert (
            aged.nasolabial_fold_depth
            > aged.orbital_hollowing
        )

    def test_jowl_formation_with_marionettes(self):
        jowls = FaceAging(
            jowl_formation=0.7,
            marionette_fold_depth=0.6,
        )

        assert jowls.is_valid()

    # --- serializzazione (2) ---

    def test_serialization(self):
        aged = FaceAging(
            midface_descent=0.3,
            upper_lid_ptosis=0.4,
        )

        data = aged.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "face_aging"
        assert data["midface_descent"] == 0.3
        assert data["upper_lid_ptosis"] == 0.4
        assert data["lip_volume_loss"] == 0.0

    def test_mutation_invalidates(self):
        aging = FaceAging()

        assert aging.is_valid()

        aging.jowl_formation = 2.0
        assert not aging.is_valid()

    # --- Human integration (3) ---

    def test_human_registration(self):
        human = Human(name="FaceAging Test")
        human.register_component(
            "face_aging",
            FaceAging(midface_descent=0.5),
        )

        assert human.has_component("face_aging")
        assert human.validate() is None

    def test_full_age_stack_three_layers(self):
        from human.hair import HairAging
        from human.skin import SkinAging

        human = Human(name="Full Age Stack")
        human.register_component("skin_aging", SkinAging())
        human.register_component("hair_aging", HairAging())
        human.register_component("face_aging", FaceAging())

        assert human.validate() is None
        assert set(human.component_names()) == {
            "human_identity",
            "demographics",
            "skin_aging",
            "hair_aging",
            "face_aging",
        }

    def test_layer_separation_documented(self):
        from human.skin import SkinAging, WrinkleZone

        skin = SkinAging(
            wrinkle_map={
                zone: 0.0 for zone in WrinkleZone
            }
        )
        skin.wrinkle_map[WrinkleZone.NASOLABIAL] = 0.7
        face = FaceAging(nasolabial_fold_depth=0.6)

        assert skin.is_valid()
        assert face.is_valid()