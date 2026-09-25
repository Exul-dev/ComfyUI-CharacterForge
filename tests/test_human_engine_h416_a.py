from __future__ import annotations

import pytest

import human.anatomy as anatomy_module
from human.anatomy import (
    Ear,
    Ears,
    BodySide,
    Face,
    Head,
    Mouth,
    Nose,
    Philtrum,
)
from human.anatomy.anatomy_component import AnatomyComponent


class TestHumanEngineH416A:

    # --- Ear (7) ---

    def test_ear_defaults(self):
        ear = Ear(side=BodySide.LEFT)

        assert ear.is_valid()
        assert ear.component_type == "ear"
        assert ear.side is BodySide.LEFT
        assert ear.length == 6.0
        assert ear.width == 3.5
        assert ear.protrusion == 0.3
        assert ear.lobe_size == "average"
        assert ear.lobe_attachment == "attached"
        assert ear.shape == "oval"
        assert ear.prominence == 0.5

    def test_ear_requires_side(self):
        with pytest.raises(TypeError):
            Ear()

    def test_ear_rejects_invalid_side(self):
        with pytest.raises(ValueError, match="side"):
            Ear(side="left")

        with pytest.raises(ValueError, match="side"):
            Ear(side=None)

    def test_ear_rejects_non_positive_dimensions(self):
        with pytest.raises(ValueError, match="Ear length"):
            Ear(side=BodySide.LEFT, length=0.0)

        with pytest.raises(ValueError, match="Ear width"):
            Ear(side=BodySide.LEFT, width=-1.0)

    def test_ear_protrusion_range(self):
        assert Ear(side=BodySide.LEFT, protrusion=0.0).is_valid()
        assert Ear(side=BodySide.LEFT, protrusion=1.0).is_valid()

        with pytest.raises(ValueError, match="protrusion"):
            Ear(side=BodySide.LEFT, protrusion=-0.1)

        with pytest.raises(ValueError, match="protrusion"):
            Ear(side=BodySide.LEFT, protrusion=1.1)

    def test_ear_rejects_invalid_enums(self):
        with pytest.raises(ValueError, match="lobe size"):
            Ear(side=BodySide.LEFT, lobe_size="huge")

        with pytest.raises(ValueError, match="lobe attachment"):
            Ear(side=BodySide.LEFT, lobe_attachment="floating")

        with pytest.raises(ValueError, match="Invalid ear shape"):
            Ear(side=BodySide.LEFT, shape="square")

    def test_ear_serialization_and_mutation(self):
        ear = Ear(side=BodySide.RIGHT)

        data = ear.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "ear"
        assert data["side"] == "right"
        assert data["lobe_attachment"] == "attached"

        ear.prominence = 5.0
        assert not ear.is_valid()

    # --- Ears (5) ---

    def test_ears_defaults_bilateral(self):
        ears = Ears()

        assert ears.is_valid()
        assert ears.component_type == "ears"
        assert ears.left.side is BodySide.LEFT
        assert ears.right.side is BodySide.RIGHT

    def test_ears_rejects_wrong_sides(self):
        with pytest.raises(ValueError, match="Ears.left"):
            Ears(left=Ear(side=BodySide.RIGHT))

        with pytest.raises(ValueError, match="Ears.right"):
            Ears(right=Ear(side=BodySide.LEFT))

    def test_ears_asymmetry_is_representable(self):
        ears = Ears(
            left=Ear(side=BodySide.LEFT, protrusion=0.1, shape="round"),
            right=Ear(side=BodySide.RIGHT, protrusion=0.8, shape="oval"),
        )

        assert ears.is_valid()
        assert ears.left.protrusion == 0.1
        assert ears.right.protrusion == 0.8
        assert ears.left.shape != ears.right.shape

    def test_ears_serialization(self):
        data = Ears().to_dict()

        assert data["schema_version"] == "1.0"
        assert data["left"]["side"] == "left"
        assert data["right"]["side"] == "right"

    def test_ears_mutation_invalidates(self):
        ears = Ears()

        assert ears.is_valid()

        ears.left.length = 0.0
        assert not ears.is_valid()

    # --- Nose (7) ---

    def test_nose_defaults(self):
        nose = Nose()

        assert nose.is_valid()
        assert nose.component_type == "nose"
        assert nose.height == 5.0
        assert nose.width == 3.5
        assert nose.projection == 2.5
        assert nose.bridge == "straight"
        assert nose.tip == "straight"
        assert nose.nostril_shape == "oval"
        assert nose.nostril_visibility == 0.3

    def test_nose_rejects_non_positive_dimensions(self):
        with pytest.raises(ValueError, match="Nose height"):
            Nose(height=0.0)

        with pytest.raises(ValueError, match="Nose width"):
            Nose(width=-1.0)

        with pytest.raises(ValueError, match="Nose projection"):
            Nose(projection=0.0)

    def test_nose_rejects_invalid_bridge(self):
        with pytest.raises(ValueError, match="Invalid nose bridge"):
            Nose(bridge="wavy")

    def test_nose_rejects_invalid_tip(self):
        with pytest.raises(ValueError, match="Invalid nose tip"):
            Nose(tip="crooked")

    def test_nose_rejects_invalid_nostril_shape(self):
        with pytest.raises(ValueError, match="Invalid nostril shape"):
            Nose(nostril_shape="triangular")

    def test_nose_nostril_visibility_range(self):
        assert Nose(nostril_visibility=0.0).is_valid()
        assert Nose(nostril_visibility=1.0).is_valid()

        with pytest.raises(ValueError, match="nostril visibility"):
            Nose(nostril_visibility=-0.1)

        with pytest.raises(ValueError, match="nostril visibility"):
            Nose(nostril_visibility=1.1)

    def test_nose_serialization_and_mutation(self):
        nose = Nose(bridge="convex", tip="upturned")

        data = nose.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["bridge"] == "convex"
        assert data["tip"] == "upturned"
        assert data["projection"] == 2.5

        nose.height = -1.0
        assert not nose.is_valid()

    # --- Philtrum (5) ---

    def test_philtrum_defaults(self):
        philtrum = Philtrum()

        assert philtrum.is_valid()
        assert philtrum.component_type == "philtrum"
        assert philtrum.length == 1.5
        assert philtrum.width == 1.1
        assert philtrum.depth == 0.5
        assert philtrum.shape == "average"

    def test_philtrum_rejects_non_positive(self):
        with pytest.raises(ValueError, match="Philtrum length"):
            Philtrum(length=0.0)

        with pytest.raises(ValueError, match="Philtrum width"):
            Philtrum(width=-1.0)

        with pytest.raises(ValueError, match="Philtrum depth"):
            Philtrum(depth=0.0)

    def test_philtrum_rejects_invalid_shape(self):
        with pytest.raises(ValueError, match="Invalid philtrum shape"):
            Philtrum(shape="spiral")

    def test_philtrum_serialization(self):
        data = Philtrum(shape="deep").to_dict()

        assert data["component_type"] == "philtrum"
        assert data["shape"] == "deep"

    def test_philtrum_mutation_invalidates(self):
        philtrum = Philtrum()

        philtrum.depth = 0.0
        assert not philtrum.is_valid()

    # --- Mouth (8) ---

    def test_mouth_defaults_with_philtrum(self):
        mouth = Mouth()

        assert mouth.is_valid()
        assert mouth.component_type == "mouth"
        assert mouth.width == 5.0
        assert mouth.lip_upper_thickness == 0.9
        assert mouth.lip_lower_thickness == 1.1
        assert mouth.corner_position == "level"
        assert mouth.opening == 0.0
        assert mouth.shape == "full"
        assert isinstance(mouth.philtrum, Philtrum)

    def test_mouth_rejects_non_positive(self):
        with pytest.raises(ValueError, match="Mouth width"):
            Mouth(width=0.0)

        with pytest.raises(ValueError, match="upper lip thickness"):
            Mouth(lip_upper_thickness=0.0)

        with pytest.raises(ValueError, match="lower lip thickness"):
            Mouth(lip_lower_thickness=-1.0)

    def test_mouth_corner_positions(self):
        for position in ("downturned", "level", "upturned"):
            assert Mouth(corner_position=position).is_valid()

        with pytest.raises(ValueError, match="corner position"):
            Mouth(corner_position="sideways")

    def test_mouth_opening_range(self):
        assert Mouth(opening=0.0).is_valid()
        assert Mouth(opening=1.0).is_valid()

        with pytest.raises(ValueError, match="opening"):
            Mouth(opening=-0.1)

        with pytest.raises(ValueError, match="opening"):
            Mouth(opening=1.1)

    def test_mouth_rejects_invalid_shape(self):
        with pytest.raises(ValueError, match="Invalid mouth shape"):
            Mouth(shape="triangular")

    def test_mouth_rejects_non_philtrum(self):
        with pytest.raises(ValueError, match="philtrum"):
            Mouth(philtrum="groove")

    def test_mouth_serialization(self):
        mouth = Mouth(shape="heart", philtrum=Philtrum(shape="deep"))

        data = mouth.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["shape"] == "heart"
        assert data["philtrum"]["shape"] == "deep"
        assert data["opening"] == 0.0

    def test_mouth_mutation_invalidates(self):
        mouth = Mouth()

        assert mouth.is_valid()

        mouth.philtrum.depth = 0.0
        assert not mouth.is_valid()

    # --- Face / Head integration (7) ---

    def test_face_defaults_include_nose_and_mouth(self):
        face = Face()

        assert face.is_valid()
        assert isinstance(face.nose, Nose)
        assert isinstance(face.mouth, Mouth)
        assert isinstance(face.mouth.philtrum, Philtrum)

    def test_face_custom_nose_and_mouth(self):
        face = Face(
            nose=Nose(bridge="concave", projection=3.0),
            mouth=Mouth(width=4.5, shape="thin"),
        )

        assert face.nose.bridge == "concave"
        assert face.nose.projection == 3.0
        assert face.mouth.width == 4.5
        assert face.mouth.shape == "thin"
        assert face.is_valid()

    def test_face_mutation_nose_invalidates(self):
        face = Face()

        face.nose.width = 0.0
        assert not face.is_valid()

    def test_face_serialization_includes_nose_and_mouth(self):
        data = Face().to_dict()

        assert data["nose"]["component_type"] == "nose"
        assert data["mouth"]["component_type"] == "mouth"
        assert data["mouth"]["philtrum"]["component_type"] == "philtrum"

    def test_head_defaults_include_ears(self):
        head = Head()

        assert head.is_valid()
        assert isinstance(head.ears, Ears)
        assert head.ears.left.side is BodySide.LEFT
        assert head.ears.right.side is BodySide.RIGHT

    def test_head_custom_ears(self):
        head = Head(
            ears=Ears(
                left=Ear(side=BodySide.LEFT, lobe_attachment="free"),
                right=Ear(side=BodySide.RIGHT, lobe_attachment="free"),
            )
        )

        assert head.ears.left.lobe_attachment == "free"
        assert head.is_valid()

    def test_head_mutation_ears_invalidates(self):
        head = Head()

        head.ears.right.protrusion = 9.0
        assert not head.is_valid()

    # --- export / contract (3) ---

    def test_package_exports_h416a(self):
        for name in ("Ear", "Ears", "Nose", "Mouth", "Philtrum"):
            assert hasattr(anatomy_module, name)
            assert name in anatomy_module.__all__

    def test_all_new_components_are_anatomy_components(self):
        for component in (
            Ear(side=BodySide.LEFT),
            Ears(),
            Nose(),
            Philtrum(),
            Mouth(),
        ):
            assert isinstance(component, AnatomyComponent)
            assert component.is_valid()

    def test_contract_compliance(self):
        expected_types = {
            Ear(side=BodySide.LEFT): "ear",
            Ears(): "ears",
            Nose(): "nose",
            Philtrum(): "philtrum",
            Mouth(): "mouth",
        }

        for component, expected in expected_types.items():
            data = component.to_dict()

            assert component.component_type == expected
            assert data["component_type"] == expected
            assert data["schema_version"] == "1.0"
            assert data["enabled"] is True