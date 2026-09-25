from __future__ import annotations

import pytest

from human.hair import (
    GrayingPattern,
    Hair,
    HairAging,
)
from human.human import Human
from human.skin import Skin


class TestHumanEngineH6A2:

    # --- vocabolario pattern (2) ---

    def test_graying_patterns_vocabulary(self):
        expected = [
            "diffuse",
            "none",
            "patchy",
            "root_shadow",
            "salt_pepper",
            "temples_first",
        ]
        values = [
            pattern.value for pattern in GrayingPattern
        ]

        assert sorted(values) == expected
        assert len(GrayingPattern) == 6

    def test_default_is_age_neutral(self):
        aging = HairAging()

        assert aging.is_valid()
        assert aging.component_type == "hair_aging"
        assert aging.graying_pattern is GrayingPattern.NONE
        assert aging.scalp_gray_extent == 0.0
        assert aging.facial_gray_extent == 0.0
        assert aging.body_gray_extent == 0.0
        assert aging.gray_hair_texture == 0.0

    # --- extent per regione (4) ---

    def test_extents_are_independent(self):
        # The real male trait: beard grays BEFORE the scalp.
        man = HairAging(
            graying_pattern=GrayingPattern.TEMPLES_FIRST,
            scalp_gray_extent=0.3,
            facial_gray_extent=0.7,
            body_gray_extent=0.1,
        )

        assert man.is_valid()
        assert (
            man.facial_gray_extent > man.scalp_gray_extent
        )
        assert (
            man.body_gray_extent < man.scalp_gray_extent
        )

    def test_extent_scale_is_continuous(self):
        # Not binary: every intermediate value is valid.
        for extent in (0.0, 0.25, 0.5, 0.75, 1.0):
            assert HairAging(
                scalp_gray_extent=extent
            ).is_valid()

    def test_extent_validation(self):
        for field in (
            "scalp_gray_extent",
            "facial_gray_extent",
            "body_gray_extent",
            "gray_hair_texture",
        ):
            with pytest.raises(ValueError, match=field):
                HairAging(**{field: 1.5})

            with pytest.raises(ValueError, match=field):
                HairAging(**{field: -0.1})

    def test_full_white(self):
        white = HairAging(
            graying_pattern=GrayingPattern.DIFFUSE,
            scalp_gray_extent=1.0,
            facial_gray_extent=1.0,
            body_gray_extent=1.0,
        )

        assert white.is_valid()
        assert white.scalp_gray_extent == 1.0

    # --- pattern (3) ---

    def test_pattern_validation(self):
        with pytest.raises(ValueError, match="GrayingPattern"):
            HairAging(graying_pattern="temples")

        with pytest.raises(ValueError, match="GrayingPattern"):
            HairAging(graying_pattern=None)

        for pattern in GrayingPattern:
            assert HairAging(
                graying_pattern=pattern
            ).is_valid()

    def test_pattern_and_extent_are_independent_axes(self):
        # The pattern says WHERE, the extent says HOW MUCH:
        # any combination is representable (documented soft
        # consistency, never enforced — same principle as the
        # bun-on-buzz-cut).
        combo = HairAging(
            graying_pattern=GrayingPattern.SALT_PEPPER,
            scalp_gray_extent=0.1,
        )

        assert combo.is_valid()

        none_with_extent = HairAging(
            graying_pattern=GrayingPattern.NONE,
            scalp_gray_extent=0.6,
        )
        assert none_with_extent.is_valid()

    def test_root_shadow_pattern(self):
        # The missed retouch: light regrowth at the base.
        shadow = HairAging(
            graying_pattern=GrayingPattern.ROOT_SHADOW,
            scalp_gray_extent=0.2,
        )

        assert shadow.is_valid()
        assert (
            shadow.graying_pattern.value == "root_shadow"
        )

    # --- texture (1) ---

    def test_gray_hair_texture(self):
        # White hair is coarser and wire-like: a separate axis.
        coarse = HairAging(
            scalp_gray_extent=0.8,
            gray_hair_texture=0.7,
        )

        assert coarse.is_valid()
        assert coarse.gray_hair_texture == 0.7

    # --- serializzazione (2) ---

    def test_serialization(self):
        aging = HairAging(
            graying_pattern=GrayingPattern.TEMPLES_FIRST,
            scalp_gray_extent=0.4,
            facial_gray_extent=0.8,
        )

        data = aging.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "hair_aging"
        assert data["graying_pattern"] == "temples_first"
        assert data["scalp_gray_extent"] == 0.4
        assert data["facial_gray_extent"] == 0.8
        assert data["body_gray_extent"] == 0.0

    def test_mutation_invalidates(self):
        aging = HairAging()

        assert aging.is_valid()

        aging.scalp_gray_extent = 2.0
        assert not aging.is_valid()

    # --- Human integration (3) ---

    def test_human_registration_coexists(self):
        human = Human(name="HairAging Test")
        human.register_component(
            "hair",
            Hair(color="dark_brown"),
        )
        human.register_component(
            "hair_aging",
            HairAging(
                graying_pattern=GrayingPattern.TEMPLES_FIRST,
                scalp_gray_extent=0.3,
            ),
        )

        assert human.has_component("hair_aging")
        assert human.validate() is None

    def test_human_serialization(self):
        # registered instance == asserted instance (H6-A1 lesson)
        graying = HairAging(
            graying_pattern=GrayingPattern.DIFFUSE,
            scalp_gray_extent=0.5,
            gray_hair_texture=0.3,
        )
        human = Human(name="Serialization")
        human.register_component("hair_aging", graying)

        data = human.to_dict()
        ha = data["human_engine"]["components"]["hair_aging"]

        assert ha["graying_pattern"] == "diffuse"
        assert ha["scalp_gray_extent"] == 0.5
        assert ha["gray_hair_texture"] == 0.3

    def test_full_age_stack(self):
        # SkinAging + HairAging together: the Age Engine's first
        # two layers coexist.
        from human.skin import SkinAging

        human = Human(name="Age Stack")
        human.register_component("skin", Skin(tone="medium"))
        human.register_component(
            "skin_aging", SkinAging(elasticity=0.4)
        )
        human.register_component("hair", Hair(color="brown"))
        human.register_component(
            "hair_aging",
            HairAging(
                scalp_gray_extent=0.6,
                facial_gray_extent=0.5,
            ),
        )

        assert human.validate() is None
        assert set(human.component_names()) == {
            "human_identity",
            "demographics",
            "skin",
            "skin_aging",
            "hair",
            "hair_aging",
        }

    # --- export (1) ---

    def test_package_exports_h6a2(self):
        from human import hair as hair_pkg

        for name in ("HairAging", "GrayingPattern"):
            assert hasattr(hair_pkg, name)
            assert name in hair_pkg.__all__