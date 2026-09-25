from __future__ import annotations

import pytest

from human.hair import (
    FacialHair,
    FacialHairGrooming,
    FacialHairLength,
    FacialHairRegion,
    FacialHairStyle,
    Hair,
    HairBaldnessPattern,
    HairStyle,
)
from human.human import Human
from human.skin import Skin


class TestHumanEngineH5D2:

    # --- regioni e vocabolari (4) ---

    def test_regions_vocabulary(self):
        expected = [
            "cheeks",
            "chin",
            "jawline",
            "moustache",
            "neck",
            "sideburns",
        ]
        values = [
            region.value for region in FacialHairRegion
        ]

        assert sorted(values) == expected
        assert len(FacialHairRegion) == 6

    def test_length_and_grooming_vocabularies(self):
        assert len(FacialHairLength) == 4
        assert len(FacialHairGrooming) == 3

        for length in FacialHairLength:
            assert FacialHair(length=length).is_valid()

        for grooming in FacialHairGrooming:
            assert FacialHair(grooming=grooming).is_valid()

    def test_styles_vocabulary(self):
        assert len(FacialHairStyle) == 11

        expected = {
            "clean_shaven",
            "stubble",
            "moustache",
            "goatee",
            "van_dyke",
            "chin_strip",
            "full_beard",
            "mutton_chops",
            "sideburns_only",
            "balbo",
            "anchor",
        }
        assert {
            style.value for style in FacialHairStyle
        } == expected

    def test_default_is_clean_shaven(self):
        hair = FacialHair()

        assert hair.is_valid()
        assert hair.component_type == "facial_hair"
        assert all(
            value == 0.0 for value in hair.coverage.values()
        )
        assert hair.color == "brown"
        assert hair.length is FacialHairLength.STUBBLE
        assert hair.grooming is FacialHairGrooming.NATURAL

    # --- coverage validation (3) ---

    def test_coverage_requires_all_regions(self):
        partial = {
            FacialHairRegion.MOUSTACHE: 1.0,
            FacialHairRegion.CHIN: 1.0,
        }

        with pytest.raises(
            ValueError, match="every FacialHairRegion"
        ):
            FacialHair(coverage=partial)

    def test_coverage_range_validation(self):
        bad = {
            region: 0.0 for region in FacialHairRegion
        }
        bad[FacialHairRegion.NECK] = 1.5

        with pytest.raises(ValueError, match="neck"):
            FacialHair(coverage=bad)

        bad2 = {
            region: 0.0 for region in FacialHairRegion
        }
        bad2[FacialHairRegion.CHIN] = True

        with pytest.raises(ValueError, match="chin"):
            FacialHair(coverage=bad2)

    def test_full_custom_coverage(self):
        custom = {
            FacialHairRegion.MOUSTACHE: 0.9,
            FacialHairRegion.CHIN: 0.7,
            FacialHairRegion.JAWLINE: 0.5,
            FacialHairRegion.SIDEBURNS: 0.3,
            FacialHairRegion.NECK: 0.1,
            FacialHairRegion.CHEEKS: 0.6,
        }

        hair = FacialHair(coverage=custom)

        assert hair.is_valid()
        assert (
            hair.coverage[FacialHairRegion.MOUSTACHE] == 0.9
        )
        assert hair.coverage[FacialHairRegion.NECK] == 0.1

    # --- factory e preset (4) ---

    def test_from_style_goatee(self):
        goatee = FacialHair.from_style(
            FacialHairStyle.GOATEE,
            color="black",
            length=FacialHairLength.SHORT,
        )

        assert goatee.is_valid()
        assert (
            goatee.coverage[FacialHairRegion.MOUSTACHE] == 1.0
        )
        assert goatee.coverage[FacialHairRegion.CHIN] == 1.0
        assert (
            goatee.coverage[FacialHairRegion.SIDEBURNS] == 0.0
        )
        assert goatee.color == "black"
        assert goatee.length is FacialHairLength.SHORT

    def test_from_style_full_beard_neck_coverage(self):
        # The beard line IS the neck coverage: full beard
        # carries a groomed 0.7 neckline by design.
        beard = FacialHair.from_style(
            FacialHairStyle.FULL_BEARD
        )

        assert beard.coverage[FacialHairRegion.NECK] == 0.7
        assert beard.coverage[FacialHairRegion.CHEEKS] == 1.0

    def test_set_style_reconfigures(self):
        hair = FacialHair(color="red")
        assert all(
            value == 0.0 for value in hair.coverage.values()
        )

        hair.set_style(FacialHairStyle.MUTTON_CHOPS)

        assert (
            hair.coverage[FacialHairRegion.SIDEBURNS] == 1.0
        )
        assert (
            hair.coverage[FacialHairRegion.MOUSTACHE] == 0.0
        )
        assert hair.is_valid()
        assert hair.color == "red"  # style non tocca il colore

    def test_preset_is_starting_point_not_cage(self):
        goatee = FacialHair.from_style(
            FacialHairStyle.GOATEE
        )
        goatee.coverage[FacialHairRegion.JAWLINE] = 0.4

        assert goatee.is_valid()
        assert (
            goatee.coverage[FacialHairRegion.JAWLINE] == 0.4
        )

    # --- validazione campi (3) ---

    def test_rejects_invalid_enums(self):
        with pytest.raises(ValueError, match="length"):
            FacialHair(length="long")

        with pytest.raises(ValueError, match="grooming"):
            FacialHair(grooming="trimmed")

    def test_rejects_invalid_texture(self):
        with pytest.raises(
            ValueError, match="Invalid facial hair texture"
        ):
            FacialHair(texture="silky")

    def test_rejects_invalid_color_and_hex(self):
        with pytest.raises(ValueError, match="color"):
            FacialHair(color="")

        with pytest.raises(ValueError, match="color_hex"):
            FacialHair(color_hex="4A2C1A")

        assert FacialHair(
            color_hex="#4A2C1A"
        ).is_valid()

    # --- serializzazione + Human (5) ---

    def test_serialization_sorted_coverage(self):
        data = FacialHair.from_style(
            FacialHairStyle.FULL_BEARD
        ).to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "facial_hair"
        assert list(data["coverage"].keys()) == sorted(
            data["coverage"].keys()
        )
        assert data["coverage"]["cheeks"] == 1.0
        assert data["length"] == "stubble"

    def test_human_registration(self):
        human = Human(name="FacialHair Test")
        human.register_component(
            "facial_hair",
            FacialHair.from_style(
                FacialHairStyle.VAN_DYKE,
                length=FacialHairLength.MEDIUM,
            ),
        )

        assert human.has_component("facial_hair")
        assert human.validate() is None

        data = human.to_dict()
        fh = data["human_engine"]["components"]["facial_hair"]
        assert fh["length"] == "medium"
        assert fh["coverage"]["moustache"] == 1.0

    def test_full_appearance_stack(self):
        from human.eyes import Eyes

        human = Human(name="Full Stack")
        human.register_component("skin", Skin(tone="light"))
        human.register_component(
            "hair",
            Hair(
                baldness_pattern=(
                    HairBaldnessPattern.NORWOOD_IV
                ),
                style=HairStyle.FADE,
            ),
        )
        human.register_component(
            "facial_hair",
            FacialHair.from_style(
                FacialHairStyle.GOATEE,
                color="gray",
            ),
        )
        human.register_component("eyes", Eyes())

        assert human.validate() is None
        # 4 appearance components + the 2 Human defaults
        # (human_identity, demographics — registered by
        # Human.__init__ since H2): the full registry.
        assert set(human.component_names()) == {
            "human_identity",
            "demographics",
            "skin",
            "hair",
            "facial_hair",
            "eyes",
        }

    def test_mutation_invalidates(self):
        hair = FacialHair()

        assert hair.is_valid()

        hair.coverage[FacialHairRegion.CHIN] = 2.0
        assert not hair.is_valid()

    def test_independent_color_from_scalp(self):
        # The beard color is independent by design: gray beard
        # on brown scalp hair is a real trait.
        scalp = FacialHair(color="brown")
        beard = FacialHair(color="gray")

        assert scalp.is_valid()
        assert beard.is_valid()
        assert scalp.color != beard.color
