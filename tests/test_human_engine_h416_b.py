from __future__ import annotations

import pytest

import human.anatomy as anatomy_module
from human.anatomy import (
    Abdomen,
    BodySide,
    HumanAnatomy,
    Torso,
    Waist,
)
from human.anatomy.anatomy_component import AnatomyComponent
from human.anatomy.body_type import BodyType, Height


class TestHumanEngineH416B:

    # --- Waist (5) ---

    def test_waist_defaults(self):
        waist = Waist()

        assert waist.is_valid()
        assert waist.component_type == "waist"
        assert waist.circumference == 80.0
        assert waist.width == 27.0
        assert waist.depth == 18.5
        assert waist.shape == "straight"

    def test_waist_rejects_non_positive(self):
        with pytest.raises(ValueError, match="Waist circumference"):
            Waist(circumference=0.0)

        with pytest.raises(ValueError, match="Waist width"):
            Waist(width=-1.0)

        with pytest.raises(ValueError, match="Waist depth"):
            Waist(depth=0.0)

    def test_waist_rejects_invalid_shape(self):
        with pytest.raises(ValueError, match="Invalid waist shape"):
            Waist(shape="hourglass")

    def test_waist_serialization(self):
        data = Waist(shape="tapered").to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "waist"
        assert data["shape"] == "tapered"
        assert data["circumference"] == 80.0

    def test_waist_mutation_invalidates(self):
        waist = Waist()

        assert waist.is_valid()

        waist.width = 0.0
        assert not waist.is_valid()

    # --- Abdomen (5) ---

    def test_abdomen_defaults(self):
        abdomen = Abdomen()

        assert abdomen.is_valid()
        assert abdomen.component_type == "abdomen"
        assert abdomen.length == 25.0
        assert abdomen.width == 28.0
        assert abdomen.depth == 19.0
        assert abdomen.muscularity == 0.5
        assert abdomen.fat_distribution == 0.5
        assert abdomen.shape == "average"

    def test_abdomen_rejects_non_positive(self):
        with pytest.raises(ValueError, match="Abdomen length"):
            Abdomen(length=0.0)

        with pytest.raises(ValueError, match="Abdomen width"):
            Abdomen(width=-1.0)

        with pytest.raises(ValueError, match="Abdomen depth"):
            Abdomen(depth=0.0)

    def test_abdomen_rejects_invalid_ranges(self):
        with pytest.raises(ValueError, match="muscularity"):
            Abdomen(muscularity=-0.1)

        with pytest.raises(ValueError, match="muscularity"):
            Abdomen(muscularity=1.1)

        with pytest.raises(ValueError, match="fat distribution"):
            Abdomen(fat_distribution=-0.1)

        with pytest.raises(ValueError, match="fat distribution"):
            Abdomen(fat_distribution=1.1)

    def test_abdomen_rejects_invalid_shape(self):
        with pytest.raises(ValueError, match="Invalid abdomen shape"):
            Abdomen(shape="wavy")

    def test_abdomen_serialization_and_mutation(self):
        abdomen = Abdomen(shape="sculpted", muscularity=0.9)

        data = abdomen.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["shape"] == "sculpted"
        assert data["muscularity"] == 0.9

        abdomen.fat_distribution = 5.0
        assert not abdomen.is_valid()

    # --- Torso fix (2) ---

    def test_torso_defaults_are_real_centimeters(self):
        torso = Torso()

        assert torso.is_valid()
        assert torso.length == 52.0
        assert torso.width == 36.0
        assert torso.depth == 24.0

    def test_torso_explicit_values_still_accepted(self):
        # The pre-H4.16 test style (relative values) keeps working.
        torso = Torso(length=1.1, width=1.2, depth=1.05, shape="v_shape")

        assert torso.is_valid()
        assert torso.length == 1.1

    # --- HumanAnatomy integration (4) ---

    def test_human_anatomy_defaults_include_waist_and_abdomen(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()
        assert isinstance(anatomy.waist, Waist)
        assert isinstance(anatomy.abdomen, Abdomen)

    def test_human_anatomy_custom_trunk(self):
        anatomy = HumanAnatomy(
            torso=Torso(length=55.0),
            waist=Waist(circumference=72.0, shape="tapered"),
            abdomen=Abdomen(shape="sculpted", muscularity=0.85),
        )

        assert anatomy.torso.length == 55.0
        assert anatomy.waist.circumference == 72.0
        assert anatomy.abdomen.shape == "sculpted"
        assert anatomy.is_valid()

    def test_human_anatomy_serialization_includes_trunk(self):
        data = HumanAnatomy().to_dict()

        assert "waist" in data
        assert "abdomen" in data
        assert data["waist"]["component_type"] == "waist"
        assert data["abdomen"]["component_type"] == "abdomen"
        assert data["torso"]["length"] == 52.0

    def test_human_anatomy_mutation_waist_invalidates(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()

        anatomy.waist.circumference = 0.0
        assert not anatomy.is_valid()

    # --- export / contract (2) ---

    def test_package_exports_h416b(self):
        for name in ("Waist", "Abdomen"):
            assert hasattr(anatomy_module, name)
            assert name in anatomy_module.__all__

        for component in (Waist(), Abdomen()):
            assert isinstance(component, AnatomyComponent)
            assert component.is_valid()

    def test_backward_compatible_constructor(self):
        anatomy = HumanAnatomy(
            body_type=BodyType("slender"),
            height=Height(175),
        )

        assert anatomy.is_valid()
        assert anatomy.waist is not None
        assert anatomy.abdomen is not None
        assert anatomy.pelvis is not None
        assert anatomy.legs is not None