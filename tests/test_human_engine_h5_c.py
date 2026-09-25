from __future__ import annotations

import pytest

from human.anatomy import BodySide
from human.base.semantic import SemanticComponent
from human.eyes import Eye, Eyes
from human.hair import Hair
from human.human import Human
from human.skin import Skin


class TestHumanEngineH5C:

    # --- Eye defaults / contract (5) ---

    def test_eye_defaults(self):
        eye = Eye(side=BodySide.LEFT)

        assert eye.is_valid()
        assert eye.component_type == "eye"
        assert eye.side is BodySide.LEFT
        assert eye.iris_color == "brown"
        assert eye.iris_color_hex is None
        assert eye.iris_pattern == "uniform"
        assert eye.sclera_tint == "white"
        assert eye.lash_length == "medium"
        assert eye.lash_density == "average"

    def test_eye_is_semantic_component_not_anatomy(self):
        eye = Eye(side=BodySide.RIGHT)

        assert isinstance(eye, SemanticComponent)

        from human.anatomy.anatomy_component import AnatomyComponent

        assert not isinstance(eye, AnatomyComponent)

    def test_eye_requires_side(self):
        with pytest.raises(TypeError):
            Eye()

    def test_eye_serialization(self):
        eye = Eye(
            side=BodySide.LEFT,
            iris_color="green",
            iris_color_hex="#6AA84F",
            iris_pattern="starburst",
        )

        data = eye.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "eye"
        assert data["enabled"] is True
        assert data["side"] == "left"
        assert data["iris_color"] == "green"
        assert data["iris_color_hex"] == "#6AA84F"
        assert data["iris_pattern"] == "starburst"
        assert data["lash_density"] == "average"

    def test_eye_all_enums_complete(self):
        assert len(Eye.VALID_IRIS_COLORS) == 9
        assert len(Eye.VALID_IRIS_PATTERNS) == 4
        assert len(Eye.VALID_SCLERA_TINTS) == 4
        assert len(Eye.VALID_LASH_LENGTHS) == 3
        assert len(Eye.VALID_LASH_DENSITIES) == 3

    # --- Eye validation (6) ---

    def test_eye_rejects_invalid_side(self):
        with pytest.raises(ValueError, match="side"):
            Eye(side="left")

        with pytest.raises(ValueError, match="side"):
            Eye(side=None)

    def test_eye_rejects_invalid_iris_color(self):
        with pytest.raises(ValueError, match="iris color"):
            Eye(side=BodySide.LEFT, iris_color="crimson")

    def test_eye_rejects_invalid_iris_pattern(self):
        with pytest.raises(ValueError, match="iris pattern"):
            Eye(side=BodySide.LEFT, iris_pattern="swirl")

    def test_eye_rejects_invalid_sclera_tint(self):
        with pytest.raises(ValueError, match="sclera tint"):
            Eye(side=BodySide.LEFT, sclera_tint="pink")

    def test_eye_rejects_invalid_lashes(self):
        with pytest.raises(ValueError, match="lash length"):
            Eye(side=BodySide.LEFT, lash_length="huge")

        with pytest.raises(ValueError, match="lash density"):
            Eye(side=BodySide.LEFT, lash_density="mascara")

    def test_eye_hex_formats(self):
        assert Eye(
            side=BodySide.LEFT, iris_color_hex="#5B8FB9"
        ).is_valid()
        assert Eye(
            side=BodySide.LEFT, iris_color_hex=None
        ).is_valid()

        with pytest.raises(ValueError, match="iris_color_hex"):
            Eye(side=BodySide.LEFT, iris_color_hex="5B8FB9")

        with pytest.raises(ValueError, match="iris_color_hex"):
            Eye(side=BodySide.LEFT, iris_color_hex="#5B8")

        with pytest.raises(ValueError, match="iris_color_hex"):
            Eye(side=BodySide.LEFT, iris_color_hex="#ZZZZZZ")

    # --- Eyes container (6) ---

    def test_eyes_defaults_bilateral(self):
        eyes = Eyes()

        assert eyes.is_valid()
        assert eyes.component_type == "eyes"
        assert eyes.left.side is BodySide.LEFT
        assert eyes.right.side is BodySide.RIGHT

    def test_eyes_rejects_wrong_sides(self):
        with pytest.raises(ValueError, match="Eyes.left"):
            Eyes(left=Eye(side=BodySide.RIGHT))

        with pytest.raises(ValueError, match="Eyes.right"):
            Eyes(right=Eye(side=BodySide.LEFT))

    def test_eyes_heterochromia_is_representable(self):
        # No explicit field: heterochromia emerges from the
        # bilateral model itself.
        eyes = Eyes(
            left=Eye(side=BodySide.LEFT, iris_color="blue"),
            right=Eye(side=BodySide.RIGHT, iris_color="brown"),
        )

        assert eyes.is_valid()
        assert eyes.left.iris_color != eyes.right.iris_color

    def test_eyes_asymmetry_in_lashes(self):
        eyes = Eyes(
            left=Eye(
                side=BodySide.LEFT,
                lash_density="dense",
                lash_length="long",
            ),
            right=Eye(
                side=BodySide.RIGHT,
                lash_density="sparse",
                lash_length="short",
            ),
        )

        assert eyes.is_valid()
        assert eyes.left.lash_density != eyes.right.lash_density

    def test_eyes_serialization(self):
        data = Eyes().to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "eyes"
        assert data["left"]["side"] == "left"
        assert data["right"]["side"] == "right"
        assert data["left"]["component_type"] == "eye"

    def test_eyes_mutation_invalidates(self):
        eyes = Eyes()

        assert eyes.is_valid()

        eyes.left.iris_color = "crimson"
        assert not eyes.is_valid()

    # --- Human integration (2) ---

    def test_eyes_attaches_to_human(self):
        human = Human(name="Eyes Test")
        human.register_component("eyes", Eyes())

        assert human.has_component("eyes")
        assert human.validate() is None

        data = human.to_dict()
        assert (
            data["human_engine"]["components"]["eyes"]["left"][
                "iris_color"
            ]
            == "brown"
        )

    def test_full_appearance_layer_coexists(self):
        # skin + hair + eyes: the complete base appearance layer
        # lives together on the Human registry.
        human = Human(name="Full Appearance")
        human.register_component("skin", Skin(tone="medium"))
        human.register_component("hair", Hair(color="dark_brown"))
        human.register_component(
            "eyes",
            Eyes(
                left=Eye(side=BodySide.LEFT, iris_color="hazel"),
                right=Eye(side=BodySide.RIGHT, iris_color="hazel"),
            ),
        )

        assert human.validate() is None
        assert set(human.component_names()) >= {
            "human_identity",
            "demographics",
            "skin",
            "hair",
            "eyes",
        }

        data = human.to_dict()
        assert (
            data["human_engine"]["components"]["skin"]["tone"]
            == "medium"
        )
        assert (
            data["human_engine"]["components"]["hair"]["color"]
            == "dark_brown"
        )
        assert (
            data["human_engine"]["components"]["eyes"]["left"][
                "iris_color"
            ]
            == "hazel"
        )