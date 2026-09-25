from __future__ import annotations

import pytest

from human.human import Human
from human.skin import Skin, SkinAging, WrinkleZone


class TestHumanEngineH6A1:

    # --- vocabolario zone (2) ---

    def test_wrinkle_zones_vocabulary(self):
        expected = [
            "crow_feet",
            "decollete",
            "forehead",
            "glabella",
            "hands",
            "marionette",
            "nasolabial",
            "neck",
            "perioral",
            "under_eye",
        ]
        values = [zone.value for zone in WrinkleZone]

        assert sorted(values) == expected
        assert len(WrinkleZone) == 10

    def test_default_is_age_neutral(self):
        aging = SkinAging()

        assert aging.is_valid()
        assert aging.component_type == "skin_aging"
        assert all(
            value == 0.0 for value in aging.wrinkle_map.values()
        )
        assert aging.wrinkle_depth == 0.0
        assert aging.elasticity == 1.0  # youthful resilience
        assert aging.sagging == 0.0
        assert aging.thinning == 0.0
        assert aging.age_spots == 0.0
        assert aging.vascular_visibility == 0.0
        assert aging.sun_damage == 0.0

    # --- wrinkle_map contratto (3) ---

    def test_map_requires_all_zones(self):
        partial = {WrinkleZone.FOREHEAD: 0.5}

        with pytest.raises(
            ValueError, match="every WrinkleZone"
        ):
            SkinAging(wrinkle_map=partial)

    def test_map_range_validation(self):
        base = {
            zone: 0.0 for zone in WrinkleZone
        }
        bad = dict(base)
        bad[WrinkleZone.CROW_FEET] = 1.5

        with pytest.raises(ValueError, match="crow_feet"):
            SkinAging(wrinkle_map=bad)

        bad2 = dict(base)
        bad2[WrinkleZone.NECK] = True

        with pytest.raises(ValueError, match="neck"):
            SkinAging(wrinkle_map=bad2)

    def test_map_zonality(self):
        # THE zonal design: a deep nasolabial fold with a
        # barely-lined forehead is a real, common face.
        aging = SkinAging(
            wrinkle_map={
                zone: 0.0 for zone in WrinkleZone
            }
        )
        aging.wrinkle_map[WrinkleZone.NASOLABIAL] = 0.9
        aging.wrinkle_map[WrinkleZone.FOREHEAD] = 0.1

        assert aging.is_valid()
        assert (
            aging.wrinkle_map[WrinkleZone.NASOLABIAL]
            != aging.wrinkle_map[WrinkleZone.FOREHEAD]
        )

    # --- assi globali (3) ---

    def test_global_axes_ranges(self):
        with pytest.raises(ValueError, match="wrinkle_depth"):
            SkinAging(wrinkle_depth=1.5)

        with pytest.raises(ValueError, match="elasticity"):
            SkinAging(elasticity=-0.1)

        with pytest.raises(ValueError, match="elasticity"):
            SkinAging(elasticity=1.1)

        for field in (
            "sagging",
            "thinning",
            "age_spots",
            "vascular_visibility",
            "sun_damage",
        ):
            with pytest.raises(ValueError, match=field):
                SkinAging(**{field: 1.5})

        assert SkinAging(
            wrinkle_depth=1.0,
            elasticity=0.0,
            sagging=1.0,
        ).is_valid()

    def test_elasticity_semantics(self):
        # 1.0 = full youthful resilience, 0.0 = none: the
        # axis is INVERTED respect to the damage axes (0 = bad).
        young = SkinAging(elasticity=1.0)
        old = SkinAging(elasticity=0.2)

        assert young.is_valid()
        assert old.is_valid()
        assert young.elasticity > old.elasticity

    def test_fotoaging_independent_from_cronoaging(self):
        # The sailor: heavy sun damage, deep lines, but few
        # spots — individual variability, two separate axes.
        sailor = SkinAging(
            sun_damage=0.9,
            wrinkle_depth=0.7,
            age_spots=0.1,
        )

        assert sailor.is_valid()
        assert sailor.sun_damage > sailor.age_spots

        # The office worker: no sun, still aging (cronoaging).
        indoor = SkinAging(
            sun_damage=0.0,
            elasticity=0.4,
            sagging=0.3,
        )
        assert indoor.is_valid()

    # --- serializzazione (2) ---

    def test_serialization_sorted_map(self):
        aging = SkinAging(
            wrinkle_map={
                zone: 0.5 for zone in WrinkleZone
            }
        )

        data = aging.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "skin_aging"
        assert list(data["wrinkle_map"].keys()) == sorted(
            data["wrinkle_map"].keys()
        )
        assert data["wrinkle_map"]["nasolabial"] == 0.5
        assert data["elasticity"] == 1.0

    def test_mutation_invalidates(self):
        aging = SkinAging()

        assert aging.is_valid()

        aging.wrinkle_map[WrinkleZone.HANDS] = 2.0
        assert not aging.is_valid()

    # --- Human integration (4) ---

    def test_human_registration_coexists_with_skin(self):
        human = Human(name="SkinAging Test")
        human.register_component("skin", Skin(tone="medium"))
        human.register_component(
            "skin_aging",
            SkinAging(elasticity=0.5, sagging=0.3),
        )

        assert human.has_component("skin_aging")
        assert human.validate() is None

    def test_human_serialization(self):
        aged = SkinAging(
            wrinkle_map={
                zone: 0.5 for zone in WrinkleZone
            },
            elasticity=0.3,
        )
        human = Human(name="Serialization Test")
        human.register_component("skin_aging", aged)

        data = human.to_dict()
        sa = data["human_engine"]["components"]["skin_aging"]

        assert sa["elasticity"] == 0.3
        assert sa["wrinkle_map"]["nasolabial"] == 0.5
        assert sa["wrinkle_map"]["forehead"] == 0.5

    def test_human_mutation_invalidates(self):
        human = Human(name="Mutation Test")
        human.register_component(
            "skin_aging", SkinAging()
        )

        assert human.validate() is None

        human.get_component(
            "skin_aging"
        ).elasticity = 5.0
        with pytest.raises(ValueError):
            human.validate()

    def test_full_appearance_stack_with_aging(self):
        from human.eyes import Eyes
        from human.hair import Hair

        human = Human(name="Full Stack + Age")
        human.register_component("skin", Skin(tone="light"))
        human.register_component("skin_aging", SkinAging())
        human.register_component("hair", Hair(color="gray"))
        human.register_component("eyes", Eyes())

        assert human.validate() is None
        assert set(human.component_names()) == {
            "human_identity",
            "demographics",
            "skin",
            "skin_aging",
            "hair",
            "eyes",
        }

    # --- export (2) ---

    def test_package_exports_h6a1(self):
        from human import skin as skin_pkg

        for name in ("SkinAging", "WrinkleZone"):
            assert hasattr(skin_pkg, name)
            assert name in skin_pkg.__all__

    def test_skin_aging_is_semantic_component(self):
        from human.base.semantic import SemanticComponent

        aging = SkinAging()

        assert isinstance(aging, SemanticComponent)
        assert aging.is_valid()