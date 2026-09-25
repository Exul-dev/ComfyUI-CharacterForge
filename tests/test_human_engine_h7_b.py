from __future__ import annotations

import pytest

from human.clothing import (
    CoverageRegion,
    Garment,
    GarmentLayer,
    GarmentMaterial,
    GarmentType,
    Outfit,
    OutfitPreset,
)
from human.human import Human


def _tee(name="tee"):
    return Garment(
        name=name,
        garment_type=GarmentType.TOP,
        coverage={CoverageRegion.TORSO, CoverageRegion.ARMS},
        layer=GarmentLayer.BASE,
    )


def _jeans():
    return Garment(
        name="jeans",
        garment_type=GarmentType.BOTTOM,
        coverage={CoverageRegion.LEGS, CoverageRegion.WAIST},
        layer=GarmentLayer.BASE,
        material=GarmentMaterial.DENIM,
    )


def _shoes():
    return Garment(
        name="shoes",
        garment_type=GarmentType.SHOES,
        coverage={CoverageRegion.FEET},
        layer=GarmentLayer.BASE,
    )


class TestHumanEngineH7B:

    def test_outfit_basic(self):
        outfit = Outfit(
            name="casual",
            garments=[_tee(), _jeans(), _shoes()],
        )

        assert outfit.is_valid()
        assert outfit.component_type == "outfit"
        assert len(outfit.garments) == 3

    def test_covered_and_uncovered(self):
        outfit = Outfit(
            name="casual",
            garments=[_tee(), _jeans(), _shoes()],
        )

        covered = outfit.covered_regions()
        assert CoverageRegion.TORSO in covered
        assert CoverageRegion.LEGS in covered
        assert CoverageRegion.FEET in covered

        uncovered = outfit.uncovered_regions()
        assert CoverageRegion.HEAD in uncovered
        assert CoverageRegion.NECK in uncovered
        assert CoverageRegion.HANDS in uncovered
        assert not uncovered & covered

    def test_empty_outfit_valid(self):
        empty = Outfit(name="nothing")

        assert empty.is_valid()
        assert empty.covered_regions() == set()
        assert empty.uncovered_regions() == set(CoverageRegion)

    def test_no_conflict_in_coherent_outfit(self):
        outfit = Outfit(name="ok", garments=[_tee(), _jeans()])

        assert outfit.conflicts() == []

    def test_conflict_detected(self):
        outfit = Outfit(
            name="bad",
            garments=[_tee("tee A"), _tee("tee B")],
        )

        assert outfit.is_valid()
        pairs = outfit.conflicts()
        assert len(pairs) == 1
        assert pairs[0][0].name == "tee A"
        assert pairs[0][1].name == "tee B"

    def test_stacking_no_conflict(self):
        jacket = Garment(
            name="jacket",
            garment_type=GarmentType.OUTERWEAR,
            coverage={CoverageRegion.TORSO, CoverageRegion.ARMS},
            layer=GarmentLayer.OUTER,
        )
        outfit = Outfit(name="layered", garments=[_tee(), jacket])

        assert outfit.conflicts() == []

    def test_bilateral_no_conflict(self):
        left = Garment(
            name="glove L",
            garment_type=GarmentType.GLOVES,
            coverage={CoverageRegion.HANDS},
            side="left",
        )
        right = Garment(
            name="glove R",
            garment_type=GarmentType.GLOVES,
            coverage={CoverageRegion.HANDS},
            side="right",
        )
        outfit = Outfit(name="gloves", garments=[left, right])

        assert outfit.is_valid()
        assert outfit.conflicts() == []

    def test_add_remove_get(self):
        outfit = Outfit(name="dynamic")
        hat = Garment(
            name="cap",
            garment_type=GarmentType.HAT,
            coverage={CoverageRegion.HEAD},
        )

        outfit.add(hat)
        assert outfit.get("cap") is hat
        assert CoverageRegion.HEAD in outfit.covered_regions()

        removed = outfit.remove("cap")
        assert removed is hat
        assert outfit.get("cap") is None
        assert outfit.remove("nonexistent") is None

    def test_duplicate_name_rejected(self):
        outfit = Outfit(name="d", garments=[_tee()])

        with pytest.raises(ValueError, match="duplicate"):
            outfit.add(_tee())

    def test_rejected_add_leaves_no_trace(self):
        # ATOMICITY: a rejected add() must not leave the garment
        # in the list (the fix born from the H7-B smoke).
        outfit = Outfit(name="atomic", garments=[_tee()])

        assert len(outfit.garments) == 1

        with pytest.raises(ValueError, match="duplicate"):
            outfit.add(_tee())

        assert len(outfit.garments) == 1
        assert outfit.is_valid()

        try:
            outfit.add("not a garment")
            raise AssertionError("should have raised")
        except ValueError:
            pass

        assert len(outfit.garments) == 1

    def test_non_garment_rejected(self):
        with pytest.raises(ValueError, match="Garment"):
            Outfit(name="bad", garments=["not a garment"])

    def test_all_presets_valid_and_conflict_free(self):
        for preset in OutfitPreset:
            outfit = Outfit.from_preset(preset)

            assert outfit.is_valid(), preset
            assert outfit.conflicts() == [], preset

    def test_preset_casual_content(self):
        casual = Outfit.from_preset(OutfitPreset.CASUAL)

        assert len(casual.garments) == 3
        assert casual.get("casual tee") is not None
        assert casual.get("casual jeans") is not None
        assert casual.get("casual sneakers") is not None
        assert casual.name == "preset: casual"

    def test_preset_is_tunable(self):
        custom = Outfit.from_preset(OutfitPreset.CASUAL)

        custom.remove("casual sneakers")
        custom.add(
            Garment(
                name="boots",
                garment_type=GarmentType.SHOES,
                coverage={
                    CoverageRegion.FEET,
                    CoverageRegion.ANKLES,
                },
            )
        )

        assert custom.is_valid()
        assert custom.get("boots") is not None
        assert custom.get("casual sneakers") is None

    def test_serialization(self):
        outfit = Outfit(
            name="serialized",
            garments=[_tee(), _jeans()],
        )

        data = outfit.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "outfit"
        assert data["name"] == "serialized"
        assert len(data["garments"]) == 2
        assert data["garments"][0]["name"] == "tee"

    def test_human_registration_and_coexistence(self):
        from human.age import apparent_age
        from human.hair import Hair
        from human.skin import Skin

        human = Human(name="Full")
        human.register_component("skin", Skin())
        human.register_component("hair", Hair())

        outfit = Outfit.from_preset(OutfitPreset.CASUAL)
        human.register_component("outfit", outfit)

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
            "outfit",
        }

        data = human.to_dict()
        assert (
            data["human_engine"]["components"]["outfit"]["name"]
            == "preset: casual"
        )

    def test_package_exports_outfit(self):
        from human import clothing as pkg

        for name in ("Outfit", "OutfitPreset"):
            assert hasattr(pkg, name)
            assert name in pkg.__all__