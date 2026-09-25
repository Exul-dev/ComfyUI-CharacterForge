from __future__ import annotations

import pytest

from human.hair import Hair
from human.human import Human
from human.base.semantic import SemanticComponent


class TestHumanEngineH5B:

    # --- defaults / contract (5) ---

    def test_hair_defaults(self):
        hair = Hair()

        assert hair.is_valid()
        assert hair.component_type == "hair"
        assert hair.color == "brown"
        assert hair.color_hex is None
        assert hair.texture == "straight"
        assert hair.thickness == "medium"
        assert hair.length == "medium"
        assert hair.density == 0.6
        assert hair.volume == 0.5
        assert hair.gloss == 0.4
        assert hair.hairline == "straight"

    def test_hair_is_semantic_component_not_anatomy(self):
        hair = Hair()

        assert isinstance(hair, SemanticComponent)

        from human.anatomy.anatomy_component import AnatomyComponent

        assert not isinstance(hair, AnatomyComponent)

    def test_hair_serialization(self):
        hair = Hair(
            color="auburn",
            color_hex="#6A3524",
            texture="curly",
            length="long",
        )

        data = hair.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "hair"
        assert data["enabled"] is True
        assert data["color"] == "auburn"
        assert data["color_hex"] == "#6A3524"
        assert data["texture"] == "curly"
        assert data["length"] == "long"
        assert data["density"] == 0.6

    def test_hair_serialization_none_hex(self):
        data = Hair().to_dict()

        assert data["color_hex"] is None

    def test_hair_all_enums_complete(self):
        assert len(Hair.VALID_COLORS) == 12
        assert len(Hair.VALID_TEXTURES) == 4
        assert len(Hair.VALID_THICKNESSES) == 3
        assert len(Hair.VALID_LENGTHS) == 6
        assert len(Hair.VALID_HAIRLINES) == 5

    # --- nominal validation (5) ---

    def test_hair_rejects_invalid_color(self):
        with pytest.raises(ValueError, match="Invalid hair color"):
            Hair(color="purple")

    def test_hair_rejects_invalid_texture(self):
        with pytest.raises(ValueError, match="Invalid hair texture"):
            Hair(texture="frizzy")

    def test_hair_rejects_invalid_thickness(self):
        with pytest.raises(ValueError, match="Invalid hair thickness"):
            Hair(thickness="ultra")

    def test_hair_rejects_invalid_length(self):
        with pytest.raises(ValueError, match="Invalid hair length"):
            Hair(length="shoulder")

    def test_hair_rejects_invalid_hairline(self):
        with pytest.raises(ValueError, match="Invalid hair hairline"):
            Hair(hairline="m_shaped")

    # --- graded validation: standard stretto (3) ---

    def test_hair_range_boundaries(self):
        assert Hair(density=0.0, volume=0.0, gloss=0.0).is_valid()
        assert Hair(density=1.0, volume=1.0, gloss=1.0).is_valid()

        with pytest.raises(ValueError, match="density"):
            Hair(density=-0.1)

        with pytest.raises(ValueError, match="volume"):
            Hair(volume=1.1)

        with pytest.raises(ValueError, match="gloss"):
            Hair(gloss=float("inf"))

    def test_hair_rejects_non_numeric_graded(self):
        # The strict-input standard: strings and bools raise
        # ValueError (never TypeError, never silent acceptance).
        for bad in ("thick", "0.6", None, True, False):
            with pytest.raises(ValueError, match="density"):
                Hair(density=bad)

        with pytest.raises(ValueError, match="volume"):
            Hair(volume=True)

    def test_hair_mutation_invalidates(self):
        hair = Hair()

        assert hair.is_valid()

        hair.density = "high"
        assert not hair.is_valid()

    # --- hex validation (2) ---

    def test_hair_hex_formats(self):
        assert Hair(color_hex="#4A2C1A").is_valid()
        assert Hair(color_hex="#ffffff").is_valid()
        assert Hair(color_hex=None).is_valid()

        with pytest.raises(ValueError, match="color_hex"):
            Hair(color_hex="4A2C1A")

        with pytest.raises(ValueError, match="color_hex"):
            Hair(color_hex="#4A2")

        with pytest.raises(ValueError, match="color_hex"):
            Hair(color_hex="#HHHHHH")

    # --- bald orthogonality (1) ---

    def test_hair_bald_is_orthogonal(self):
        # bald describes current coverage; fiber attributes stay
        # meaningful and valid on their own.
        hair = Hair(
            length="bald",
            color="black",
            texture="coily",
            density=0.3,
        )

        assert hair.is_valid()

    # --- Human integration (2) ---

    def test_hair_attaches_to_human(self):
        human = Human(name="Hair Test")
        human.register_component("hair", Hair(color="red"))

        assert human.has_component("hair")
        assert human.get_component("hair").color == "red"
        assert human.validate() is None

        data = human.to_dict()
        assert data["human_engine"]["components"]["hair"]["color"] == "red"

    def test_hair_and_skin_coexist_on_human(self):
        from human.skin import Skin

        human = Human(name="Appearance Test")
        human.register_component("skin", Skin(tone="light"))
        human.register_component("hair", Hair(color="blonde"))

        assert human.has_component("skin")
        assert human.has_component("hair")
        assert human.validate() is None

        components = human.component_names()
        assert "skin" in components
        assert "hair" in components