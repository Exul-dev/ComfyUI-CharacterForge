from __future__ import annotations

import inspect

import pytest

from human.anatomy import (
    Forearm,
    HumanAnatomy,
    LowerLeg,
    Thigh,
    UpperArm,
)
from human.eyes import Eyes
from human.hair import (
    BodyHair,
    BodyHairRegion,
    FacialHair,
    FacialHairStyle,
    Hair,
    HairBaldnessPattern,
    HairStyle,
)
from human.human import Human
from human.skin import Skin


class TestHumanEngineH5D3:

    # --- BodyHair core (8) ---

    def test_regions_vocabulary(self):
        expected = [
            "abdomen",
            "arms",
            "back",
            "buttocks",
            "chest",
            "feet",
            "forearms",
            "hands",
            "legs",
            "shoulders",
            "thighs",
        ]
        values = [region.value for region in BodyHairRegion]

        assert sorted(values) == expected
        assert len(BodyHairRegion) == 11

    def test_default_is_glabrous(self):
        hair = BodyHair()

        assert hair.is_valid()
        assert hair.component_type == "body_hair"
        assert all(
            value == 0.0 for value in hair.coverage.values()
        )
        assert hair.color == "brown"
        assert hair.texture == "straight"

    def test_glabrous_is_emergent_not_a_flag(self):
        smooth = BodyHair()
        hairy = BodyHair(
            coverage={
                region: 0.9 for region in BodyHairRegion
            }
        )

        assert smooth.is_valid()
        assert hairy.is_valid()
        assert smooth.coverage != hairy.coverage
        assert not hasattr(smooth, "is_glabrous")

    def test_coverage_requires_all_regions(self):
        partial = {BodyHairRegion.CHEST: 0.5}

        with pytest.raises(
            ValueError, match="every BodyHairRegion"
        ):
            BodyHair(coverage=partial)

    def test_coverage_range_validation(self):
        base = {
            region: 0.0 for region in BodyHairRegion
        }
        bad = dict(base)
        bad[BodyHairRegion.BACK] = 1.5

        with pytest.raises(ValueError, match="back"):
            BodyHair(coverage=bad)

        bad2 = dict(base)
        bad2[BodyHairRegion.THIGHS] = True

        with pytest.raises(ValueError, match="thighs"):
            BodyHair(coverage=bad2)

    def test_full_hairy_pattern(self):
        hairy = BodyHair(
            color="dark_brown",
            coverage={
                BodyHairRegion.CHEST: 0.9,
                BodyHairRegion.ABDOMEN: 0.7,
                BodyHairRegion.BACK: 0.8,
                BodyHairRegion.SHOULDERS: 0.6,
                BodyHairRegion.ARMS: 0.5,
                BodyHairRegion.FOREARMS: 0.6,
                BodyHairRegion.HANDS: 0.2,
                BodyHairRegion.BUTTOCKS: 0.5,
                BodyHairRegion.THIGHS: 0.6,
                BodyHairRegion.LEGS: 0.4,
                BodyHairRegion.FEET: 0.1,
            },
        )

        assert hairy.is_valid()
        assert (
            hairy.coverage[BodyHairRegion.CHEST] == 0.9
        )
        assert hairy.coverage[BodyHairRegion.FEET] == 0.1

    def test_region_independence(self):
        hair = BodyHair(
            coverage={
                region: 0.0 for region in BodyHairRegion
            }
        )
        hair.coverage[BodyHairRegion.CHEST] = 0.5
        hair.coverage[BodyHairRegion.ABDOMEN] = 0.3

        assert hair.is_valid()
        assert hair.coverage[BodyHairRegion.BACK] == 0.0
        assert hair.coverage[BodyHairRegion.CHEST] == 0.5

    def test_color_texture_hex_validation(self):
        with pytest.raises(ValueError, match="color"):
            BodyHair(color="")

        with pytest.raises(ValueError, match="color_hex"):
            BodyHair(color_hex="4A2C1A")

        with pytest.raises(
            ValueError, match="Invalid body hair texture"
        ):
            BodyHair(texture="silky")

        assert BodyHair(
            color_hex="#4A2C1A", texture="wavy"
        ).is_valid()

    # --- serializzazione + Human (3) ---

    def test_serialization_sorted(self):
        data = BodyHair(
            coverage={
                region: 0.5 for region in BodyHairRegion
            }
        ).to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "body_hair"
        assert list(data["coverage"].keys()) == sorted(
            data["coverage"].keys()
        )
        assert data["coverage"]["chest"] == 0.5

    def test_human_registration_and_mutation(self):
        human = Human(name="BodyHair Test")
        human.register_component(
            "body_hair",
            BodyHair(
                coverage={
                    region: 0.6 for region in BodyHairRegion
                }
            ),
        )

        assert human.validate() is None

        data = human.to_dict()
        assert (
            data["human_engine"]["components"]["body_hair"][
                "coverage"
            ]["chest"]
            == 0.6
        )

        # Human exposes validate() (raising), not is_valid():
        # the invalidation is asserted through the raise.
        human.get_component(
            "body_hair"
        ).coverage[BodyHairRegion.CHEST] = 9.0
        with pytest.raises(ValueError):
            human.validate()

    def test_full_appearance_stack_seven_components(self):
        human = Human(name="Complete Appearance")
        human.register_component("skin", Skin(tone="light"))
        human.register_component(
            "hair",
            Hair(
                color="black",
                style=HairStyle.FADE,
                baldness_pattern=(
                    HairBaldnessPattern.NORWOOD_IV
                ),
            ),
        )
        human.register_component(
            "facial_hair",
            FacialHair.from_style(
                FacialHairStyle.FULL_BEARD,
                color="black",
            ),
        )
        human.register_component("body_hair", BodyHair())
        human.register_component("eyes", Eyes())

        assert human.validate() is None
        assert set(human.component_names()) == {
            "human_identity",
            "demographics",
            "skin",
            "hair",
            "facial_hair",
            "body_hair",
            "eyes",
        }

    # --- parita quattro segmenti (8) ---

    def test_lower_leg_vascularity_default(self):
        anatomy = HumanAnatomy()

        assert (
            anatomy.legs.left.lower_leg.vascularity == 0.3
        )
        assert (
            anatomy.legs.right.lower_leg.vascularity == 0.3
        )
        assert (
            anatomy.legs.left.lower_leg.calf_prominence
            == 0.5
        )

    def test_lower_leg_vascularity_validation(self):
        with pytest.raises(ValueError, match="vascularity"):
            LowerLeg(vascularity=1.5)

        assert LowerLeg(vascularity=0.0).is_valid()
        assert LowerLeg(vascularity=1.0).is_valid()

    def test_lower_leg_legacy_intact(self):
        with pytest.raises(
            ValueError, match="Lower leg length"
        ):
            LowerLeg(length=0.0)

        with pytest.raises(ValueError, match="calf prominence"):
            LowerLeg(calf_prominence=1.1)

    def test_forearm_flexor_definition(self):
        forearm = Forearm()

        assert forearm.flexor_definition == 0.4
        assert forearm.vascularity == 0.3

        with pytest.raises(
            ValueError, match="flexor_definition"
        ):
            Forearm(flexor_definition=1.5)

        assert Forearm(flexor_definition=0.0).is_valid()

        data = forearm.to_dict()
        assert data["flexor_definition"] == 0.4

    def test_vascularity_on_all_limb_segments(self):
        for cls in (UpperArm, Forearm, Thigh, LowerLeg):
            params = set(
                inspect.signature(cls.__init__).parameters
            )
            assert "vascularity" in params, cls.__name__

    def test_limb_segment_parity_nine(self):
        counts = {
            cls.__name__: len(
                set(
                    inspect.signature(
                        cls.__init__
                    ).parameters
                )
                - {"self"}
            )
            for cls in (UpperArm, Forearm, Thigh, LowerLeg)
        }

        assert counts == {
            "UpperArm": 9,
            "Forearm": 9,
            "Thigh": 9,
            "LowerLeg": 9,
        }

    def test_limb_vascularity_defaults_uniform(self):
        for cls in (UpperArm, Forearm, Thigh, LowerLeg):
            assert cls().vascularity == 0.3, cls.__name__

    def test_limb_vascularity_serialized(self):
        data = HumanAnatomy().to_dict()

        assert (
            data["arms"]["left"]["upper_arm"]["vascularity"]
            == 0.3
        )
        assert (
            data["arms"]["left"]["forearm"]["vascularity"]
            == 0.3
        )
        assert (
            data["legs"]["left"]["thigh"]["vascularity"] == 0.3
        )
        assert (
            data["legs"]["right"]["lower_leg"]["vascularity"]
            == 0.3
        )
