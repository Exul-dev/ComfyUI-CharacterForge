from __future__ import annotations

import pytest

from human.clothing import (
    CoverageRegion,
    Garment,
    GarmentFit,
    GarmentLayer,
    GarmentMaterial,
    GarmentState,
    GarmentType,
)
from human.human import Human


class TestHumanEngineH7A:

    # --- vocabolari (2) ---

    def test_garment_types_vocabulary(self):
        expected = {
            "hat", "scarf", "top", "bottom", "full_body",
            "outerwear", "gloves", "socks", "shoes", "belt",
            "accessory",
        }
        assert {t.value for t in GarmentType} == expected
        assert len(list(GarmentType)) == 11

    def test_coverage_regions_vocabulary(self):
        expected = {
            "head", "neck", "torso", "arms", "hands",
            "waist", "legs", "feet", "ankles",
        }
        assert {r.value for r in CoverageRegion} == expected
        assert len(list(CoverageRegion)) == 9

    # --- il capo base (3) ---

    def test_garment_basic(self):
        tshirt = Garment(
            name="tee",
            garment_type=GarmentType.TOP,
            coverage={CoverageRegion.TORSO},
        )

        assert tshirt.is_valid()
        assert tshirt.component_type == "garment"
        assert tshirt.layer is GarmentLayer.BASE
        assert tshirt.fit is GarmentFit.REGULAR
        assert tshirt.state is GarmentState.NEW

    def test_garment_covers(self):
        jacket = Garment(
            name="bomber",
            garment_type=GarmentType.OUTERWEAR,
            coverage={
                CoverageRegion.TORSO,
                CoverageRegion.ARMS,
            },
        )

        assert jacket.covers(CoverageRegion.TORSO)
        assert jacket.covers(CoverageRegion.ARMS)
        assert not jacket.covers(CoverageRegion.HEAD)
        assert not jacket.covers(CoverageRegion.LEGS)

    def test_garment_bilateral_side(self):
        left = Garment(
            name="glove L",
            garment_type=GarmentType.GLOVES,
            coverage={CoverageRegion.HANDS},
            side="left",
        )
        both = Garment(
            name="socks",
            garment_type=GarmentType.SOCKS,
            coverage={CoverageRegion.FEET, CoverageRegion.ANKLES},
        )

        assert left.is_valid()
        assert left.side == "left"
        assert both.is_valid()
        assert both.side is None

    # --- validazione (4) ---

    def test_rejects_empty_name(self):
        with pytest.raises(ValueError, match="name"):
            Garment(
                name="  ",
                garment_type=GarmentType.TOP,
                coverage={CoverageRegion.TORSO},
            )

    def test_rejects_empty_coverage(self):
        with pytest.raises(ValueError, match="at least one"):
            Garment(
                name="ghost",
                garment_type=GarmentType.TOP,
                coverage=set(),
            )

    def test_rejects_invalid_enums(self):
        with pytest.raises(ValueError, match="garment_type"):
            Garment(
                name="bad",
                garment_type="top",
                coverage={CoverageRegion.TORSO},
            )

        with pytest.raises(ValueError, match="layer"):
            Garment(
                name="bad",
                garment_type=GarmentType.TOP,
                coverage={CoverageRegion.TORSO},
                layer="base",
            )

        with pytest.raises(ValueError, match="material"):
            Garment(
                name="bad",
                garment_type=GarmentType.TOP,
                coverage={CoverageRegion.TORSO},
                material="silk-ish",
            )

    def test_rejects_invalid_color_and_side(self):
        with pytest.raises(ValueError, match="color"):
            Garment(
                name="bad",
                garment_type=GarmentType.TOP,
                coverage={CoverageRegion.TORSO},
                color="chartreuse",
            )

        with pytest.raises(ValueError, match="hex"):
            Garment(
                name="bad",
                garment_type=GarmentType.TOP,
                coverage={CoverageRegion.TORSO},
                color_hex="bad",
            )

        with pytest.raises(ValueError, match="side"):
            Garment(
                name="bad",
                garment_type=GarmentType.GLOVES,
                coverage={CoverageRegion.HANDS},
                side="both",
            )

    # --- serializzazione (2) ---

    def test_serialization_sorted_coverage(self):
        dress = Garment(
            name="dress",
            garment_type=GarmentType.FULL_BODY,
            coverage={
                CoverageRegion.LEGS,
                CoverageRegion.TORSO,
                CoverageRegion.WAIST,
            },
        )

        data = dress.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "garment"
        assert data["coverage"] == [
            "legs",
            "torso",
            "waist",
        ]
        assert data["garment_type"] == "full_body"

    def test_serialization_robust_after_mutation(self):
        garment = Garment(
            name="mutant",
            garment_type=GarmentType.TOP,
            coverage={CoverageRegion.TORSO},
        )

        garment.state = "not-an-enum"

        data = garment.to_dict()

        assert data["state"] == "not-an-enum"
        assert not garment.is_valid()

    # --- Human integration (3) ---

    def test_human_registration(self):
        human = Human(name="Dressed")
        human.register_component(
            "garment_jacket",
            Garment(
                name="denim jacket",
                garment_type=GarmentType.OUTERWEAR,
                coverage={
                    CoverageRegion.TORSO,
                    CoverageRegion.ARMS,
                },
            ),
        )

        assert human.has_component("garment_jacket")
        assert human.validate() is None

    def test_stacking_multiple_layers(self):
        human = Human(name="Layered")

        base = Garment(
            name="tee",
            garment_type=GarmentType.TOP,
            coverage={CoverageRegion.TORSO, CoverageRegion.ARMS},
            layer=GarmentLayer.BASE,
        )
        mid = Garment(
            name="sweater",
            garment_type=GarmentType.TOP,
            coverage={CoverageRegion.TORSO, CoverageRegion.ARMS},
            layer=GarmentLayer.MID,
        )
        outer = Garment(
            name="jacket",
            garment_type=GarmentType.OUTERWEAR,
            coverage={CoverageRegion.TORSO, CoverageRegion.ARMS},
            layer=GarmentLayer.OUTER,
        )

        human.register_component("garment_base", base)
        human.register_component("garment_mid", mid)
        human.register_component("garment_outer", outer)

        assert human.validate() is None

        data = human.to_dict()
        layers = {
            data["human_engine"]["components"][name]["layer"]
            for name in ("garment_base", "garment_mid", "garment_outer")
        }
        assert layers == {"base", "mid", "outer"}

    def test_full_stack_clothing_appearance_aging(self):
        from human.age import apparent_age
        from human.hair import Hair
        from human.skin import Skin

        human = Human(name="Full Stack")

        human.register_component("skin", Skin(tone="light"))
        human.register_component("hair", Hair(color="brown"))

        human.register_component(
            "garment_shirt",
            Garment(
                name="shirt",
                garment_type=GarmentType.TOP,
                coverage={
                    CoverageRegion.TORSO,
                    CoverageRegion.ARMS,
                },
            ),
        )
        human.register_component(
            "garment_pants",
            Garment(
                name="pants",
                garment_type=GarmentType.BOTTOM,
                coverage={CoverageRegion.LEGS, CoverageRegion.WAIST},
            ),
        )
        human.register_component(
            "garment_shoes",
            Garment(
                name="sneakers",
                garment_type=GarmentType.SHOES,
                coverage={CoverageRegion.FEET},
            ),
        )

        apparent_age(human, 70)

        assert human.validate() is None

        assert set(human.component_names()) == {
            "human_identity",
            "demographics",
            "skin",
            "hair",
            "skin_aging",
            "hair_aging",
            "face_aging",
            "body_aging",
            "garment_shirt",
            "garment_pants",
            "garment_shoes",
        }

    # --- export (2) ---

    def test_package_exports(self):
        from human import clothing as clothing_pkg

        for name in (
            "GarmentType",
            "CoverageRegion",
            "GarmentLayer",
            "GarmentFit",
            "GarmentMaterial",
            "GarmentState",
            "Garment",
        ):
            assert hasattr(clothing_pkg, name)
            assert name in clothing_pkg.__all__

    def test_all_enums_comprehensive(self):
        assert len(list(GarmentFit)) == 4
        assert len(list(GarmentMaterial)) == 10
        assert len(list(GarmentState)) == 4
        assert len(list(GarmentLayer)) == 3