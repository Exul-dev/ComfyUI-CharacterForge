from __future__ import annotations

import pytest

from human.hair import (
    Hair,
    HairArrangement,
    HairBaldnessPattern,
    HairStyle,
)
from human.human import Human


class TestHumanEngineH5D1:

    # --- baldness patterns (4) ---

    def test_baldness_pattern_defaults_none(self):
        hair = Hair()

        assert hair.is_valid()
        assert (
            hair.baldness_pattern is HairBaldnessPattern.NONE
        )

    def test_baldness_patterns_complete_vocabulary(self):
        expected = [
            "none",
            "norwood_ii",
            "norwood_iii",
            "norwood_iv",
            "norwood_v",
            "norwood_vi",
            "norwood_vii",
            "ludwig_i",
            "ludwig_ii",
            "ludwig_iii",
            "alopecia_areata",
            "alopecia_totalis",
        ]
        values = [
            pattern.value for pattern in HairBaldnessPattern
        ]

        assert values == expected
        assert len(HairBaldnessPattern) == 12

    def test_baldness_patterns_are_configurable(self):
        balding = Hair(
            baldness_pattern=HairBaldnessPattern.NORWOOD_VII,
            hairline="receding",
            density=0.15,
        )

        assert balding.is_valid()
        assert (
            balding.baldness_pattern.value == "norwood_vii"
        )

        female = Hair(
            baldness_pattern=HairBaldnessPattern.LUDWIG_II
        )
        assert female.is_valid()

    def test_baldness_pattern_rejects_invalid(self):
        with pytest.raises(ValueError, match="baldness_pattern"):
            Hair(baldness_pattern="norwood_5")

        with pytest.raises(ValueError, match="baldness_pattern"):
            Hair(baldness_pattern=None)

    # --- shaved vs bald (3) ---

    def test_shaved_is_distinct_from_bald(self):
        shaved = Hair(length="shaved")
        bald = Hair(
            length="bald",
            baldness_pattern=(
                HairBaldnessPattern.ALOPECIA_TOTALIS
            ),
        )

        assert shaved.is_valid()
        assert bald.is_valid()
        assert shaved.length != bald.length

    def test_length_vocabulary_has_seven_entries(self):
        # The H5-D-1 contract: shaved joined bald, very_short...
        assert len(Hair.VALID_LENGTHS) == 7
        assert "shaved" in Hair.VALID_LENGTHS
        assert "bald" in Hair.VALID_LENGTHS

    def test_length_rejects_invalid(self):
        with pytest.raises(ValueError, match="Invalid hair length"):
            Hair(length="buzzed")

    # --- styles + arrangements (5) ---

    def test_style_vocabulary_complete(self):
        assert len(HairStyle) == 21

        for style in (
            HairStyle.BUZZ_CUT,
            HairStyle.FADE,
            HairStyle.MOHAWK,
            HairStyle.BOB,
            HairStyle.PIXIE,
            HairStyle.AFRO,
            HairStyle.DREADLOCKS,
            HairStyle.WOLF_CUT,
        ):
            assert Hair(style=style).is_valid()

    def test_arrangement_vocabulary_complete(self):
        assert len(HairArrangement) == 9

        for arrangement in (
            HairArrangement.LOOSE,
            HairArrangement.PONYTAIL,
            HairArrangement.BUN,
            HairArrangement.TOP_KNOT,
            HairArrangement.HALF_UP,
            HairArrangement.BRAIDED,
            HairArrangement.PIGTAILS,
            HairArrangement.PINNED,
            HairArrangement.SPACE_BUNS,
        ):
            assert Hair(arrangement=arrangement).is_valid()

    def test_style_and_arrangement_are_independent(self):
        # The two-axis design: a cut can be worn many ways.
        combos = [
            (HairStyle.BOB, HairArrangement.LOOSE),
            (HairStyle.BOB, HairArrangement.PINNED),
            (HairStyle.LOB, HairArrangement.PONYTAIL),
            (HairStyle.WOLF_CUT, HairArrangement.HALF_UP),
            (HairStyle.AFRO, HairArrangement.LOOSE),
            (HairStyle.MULLET, HairArrangement.BRAIDED),
        ]

        for style, arrangement in combos:
            hair = Hair(style=style, arrangement=arrangement)

            assert hair.is_valid()
            assert hair.style is style
            assert hair.arrangement is arrangement

    def test_soft_constraints_not_enforced(self):
        # A bun on a buzz cut is wrong for grown hair, right for
        # a wig: documented soft constraint, never a hard rule.
        assert Hair(
            style=HairStyle.BUZZ_CUT,
            arrangement=HairArrangement.BUN,
        ).is_valid()

    def test_style_rejects_invalid(self):
        with pytest.raises(ValueError, match="style"):
            Hair(style="pompadour")

        with pytest.raises(ValueError, match="style"):
            Hair(style=None)

        with pytest.raises(ValueError, match="arrangement"):
            Hair(arrangement="updo")

    # --- legacy H5-B intatto (3) ---

    def test_h5b_defaults_intact(self):
        hair = Hair()

        assert hair.color == "brown"
        assert hair.texture == "straight"
        assert hair.thickness == "medium"
        assert hair.length == "medium"
        assert hair.density == 0.6
        assert hair.volume == 0.5
        assert hair.gloss == 0.4
        assert hair.hairline == "straight"

    def test_h5b_messages_intact(self):
        with pytest.raises(ValueError, match="Invalid hair color"):
            Hair(color="purple")

        with pytest.raises(ValueError, match="density"):
            Hair(density="thick")

        with pytest.raises(ValueError, match="color_hex"):
            Hair(color_hex="4A2C1A")

    def test_h5b_bald_orthogonality_still_valid(self):
        hair = Hair(
            length="bald",
            color="black",
            texture="coily",
            density=0.3,
        )

        assert hair.is_valid()

    # --- serializzazione + Human (3) ---

    def test_serialization_new_fields(self):
        data = Hair(
            style=HairStyle.POMPADOUR,
            arrangement=HairArrangement.PONYTAIL,
            baldness_pattern=HairBaldnessPattern.NORWOOD_III,
        ).to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "hair"
        assert data["style"] == "pompadour"
        assert data["arrangement"] == "ponytail"
        assert data["baldness_pattern"] == "norwood_iii"
        assert data["length"] == "medium"

    def test_human_registration_with_full_control(self):
        human = Human(name="Full Hair Control")
        human.register_component(
            "hair",
            Hair(
                color="auburn",
                style=HairStyle.WOLF_CUT,
                arrangement=HairArrangement.HALF_UP,
                baldness_pattern=HairBaldnessPattern.NONE,
            ),
        )

        assert human.has_component("hair")
        assert human.validate() is None

        data = human.to_dict()
        hair_data = data["human_engine"]["components"]["hair"]
        assert hair_data["style"] == "wolf_cut"
        assert hair_data["arrangement"] == "half_up"

    def test_mutation_new_field_invalidates(self):
        hair = Hair()

        assert hair.is_valid()

        hair.baldness_pattern = "norwood_v"
        assert not hair.is_valid()