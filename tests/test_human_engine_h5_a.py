from __future__ import annotations

import pytest

from human.human import Human
from human.skin import Skin, SkinType
from human.base.semantic import SemanticComponent


class TestHumanEngineH5A:

    # --- defaults / contract (6) ---

    def test_skin_defaults(self):
        skin = Skin()

        assert skin.is_valid()
        assert skin.component_type == "skin"
        assert skin.tone == "medium"
        assert skin.tone_hex is None
        assert skin.undertone == "neutral"
        assert skin.skin_type is SkinType.III
        assert skin.texture == "average"
        assert skin.oiliness == 0.4
        assert skin.hydration == 0.6
        assert skin.sensitivity == 0.3
        assert skin.freckle_density == "none"
        assert skin.mole_count == 0

    def test_skin_is_semantic_component_not_anatomy(self):
        skin = Skin()

        assert isinstance(skin, SemanticComponent)

        from human.anatomy.anatomy_component import AnatomyComponent

        assert not isinstance(skin, AnatomyComponent)

    def test_skin_serialization(self):
        skin = Skin(tone="dark", tone_hex="#5D4037", skin_type=SkinType.V)

        data = skin.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "skin"
        assert data["enabled"] is True
        assert data["tone"] == "dark"
        assert data["tone_hex"] == "#5D4037"
        assert data["skin_type"] == "V"
        assert data["oiliness"] == 0.4
        assert data["mole_count"] == 0

    def test_skin_serialization_none_hex(self):
        data = Skin().to_dict()

        assert data["tone_hex"] is None

    def test_skin_mutation_invalidates(self):
        skin = Skin()

        assert skin.is_valid()

        skin.oiliness = 5.0
        assert not skin.is_valid()

    def test_skin_all_enums_complete(self):
        assert len(Skin.VALID_TONES) == 7
        assert len(Skin.VALID_UNDERTONES) == 3
        assert len(Skin.VALID_TEXTURES) == 4
        assert len(Skin.VALID_FRECKLE_DENSITIES) == 5
        assert len(list(SkinType)) == 6

    # --- enum / range validation (8) ---

    def test_skin_rejects_invalid_tone(self):
        with pytest.raises(ValueError, match="Invalid skin tone"):
            Skin(tone="pale")

    def test_skin_rejects_invalid_undertone(self):
        with pytest.raises(ValueError, match="Invalid skin undertone"):
            Skin(undertone="olive")

    def test_skin_rejects_invalid_skin_type(self):
        with pytest.raises(ValueError, match="skin_type"):
            Skin(skin_type="III")

        with pytest.raises(ValueError, match="skin_type"):
            Skin(skin_type=None)

    def test_skin_rejects_invalid_texture(self):
        with pytest.raises(ValueError, match="Invalid skin texture"):
            Skin(texture="silky")

    def test_skin_rejects_invalid_freckle_density(self):
        with pytest.raises(ValueError, match="freckle density"):
            Skin(freckle_density="extreme")

    def test_skin_range_boundaries(self):
        assert Skin(oiliness=0.0, hydration=0.0, sensitivity=0.0).is_valid()
        assert Skin(oiliness=1.0, hydration=1.0, sensitivity=1.0).is_valid()

        with pytest.raises(ValueError, match="oiliness"):
            Skin(oiliness=-0.1)

        with pytest.raises(ValueError, match="hydration"):
            Skin(hydration=1.1)

        with pytest.raises(ValueError, match="sensitivity"):
            Skin(sensitivity=float("inf"))

    def test_skin_rejects_invalid_mole_count(self):
        with pytest.raises(ValueError, match="mole_count"):
            Skin(mole_count=-1)

        with pytest.raises(ValueError, match="mole_count"):
            Skin(mole_count=2.5)

        with pytest.raises(ValueError, match="mole_count"):
            Skin(mole_count=True)

    def test_skin_mole_count_zero_and_positive(self):
        assert Skin(mole_count=0).is_valid()
        assert Skin(mole_count=37).is_valid()

    # --- tone_hex validation (4) ---

    def test_skin_hex_accepts_valid_formats(self):
        assert Skin(tone_hex="#FFFFFF").is_valid()
        assert Skin(tone_hex="#5d4037").is_valid()
        assert Skin(tone_hex=None).is_valid()

    def test_skin_hex_rejects_bad_prefix(self):
        with pytest.raises(ValueError, match="tone_hex"):
            Skin(tone_hex="FFFFFF")

        with pytest.raises(ValueError, match="tone_hex"):
            Skin(tone_hex="ffffff")

    def test_skin_hex_rejects_wrong_length(self):
        with pytest.raises(ValueError, match="tone_hex"):
            Skin(tone_hex="#FFF")

        with pytest.raises(ValueError, match="tone_hex"):
            Skin(tone_hex="#FFFFFFFF")

    def test_skin_hex_rejects_bad_characters(self):
        with pytest.raises(ValueError, match="tone_hex"):
            Skin(tone_hex="#GGGGGG")

        with pytest.raises(ValueError, match="tone_hex"):
            Skin(tone_hex="#5D403Z")

    # --- Human integration (2) ---

    def test_skin_attaches_to_human(self):
        human = Human(name="Skin Test")
        human.register_component("skin", Skin(tone="light"))

        assert human.has_component("skin")
        assert human.get_component("skin").tone == "light"
        assert human.validate() is None

        data = human.to_dict()
        assert data["human_engine"]["components"]["skin"]["tone"] == "light"

    def test_skin_duplicate_registration_rejected(self):
        human = Human(name="Dup Test")
        human.register_component("skin", Skin())

        with pytest.raises(ValueError, match="already registered"):
            human.register_component("skin", Skin())