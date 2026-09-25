from __future__ import annotations

import pytest

import human.anatomy as anatomy_module
from human.anatomy import (
    BodySide,
    Glute,
    GlutealRegion,
    Hip,
    Hips,
    HumanAnatomy,
    Pelvis,
)
from human.anatomy.anatomy_component import AnatomyComponent


class TestHumanEngineH418A:

    # --- Glute (5) ---

    def test_glute_defaults(self):
        glute = Glute(side=BodySide.LEFT)

        assert glute.is_valid()
        assert glute.component_type == "glute"
        assert glute.side is BodySide.LEFT
        assert glute.width == 12.0
        assert glute.height == 12.5
        assert glute.projection == 0.5
        assert glute.volume == 0.5
        assert glute.shape == "round"
        assert glute.firmness == 0.5
        assert glute.muscularity == 0.5
        assert glute.fat_distribution == 0.5
        assert glute.fold_prominence == 0.4

    def test_glute_requires_side(self):
        with pytest.raises(TypeError):
            Glute()

    def test_glute_rejects_invalid_side_and_shape(self):
        with pytest.raises(ValueError, match="side"):
            Glute(side="left")

        with pytest.raises(ValueError, match="Invalid glute shape"):
            Glute(side=BodySide.LEFT, shape="angular")

    def test_glute_range_validation(self):
        with pytest.raises(ValueError, match="width"):
            Glute(side=BodySide.LEFT, width=0.0)

        with pytest.raises(ValueError, match="height"):
            Glute(side=BodySide.LEFT, height=-1.0)

        for field in (
            "projection",
            "volume",
            "firmness",
            "muscularity",
            "fat_distribution",
            "fold_prominence",
        ):
            with pytest.raises(ValueError, match=field):
                Glute(side=BodySide.LEFT, **{field: 1.5})

    def test_glute_serialization_and_mutation(self):
        glute = Glute(side=BodySide.RIGHT, shape="heart")

        data = glute.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "glute"
        assert data["side"] == "right"
        assert data["shape"] == "heart"
        assert data["fold_prominence"] == 0.4

        glute.volume = 9.0
        assert not glute.is_valid()

    # --- GlutealRegion (4) ---

    def test_gluteal_region_defaults(self):
        region = GlutealRegion()

        assert region.is_valid()
        assert region.component_type == "gluteal_region"
        assert region.left.side is BodySide.LEFT
        assert region.right.side is BodySide.RIGHT
        assert region.cleft_depth == 0.5

    def test_gluteal_region_rejects_wrong_sides(self):
        with pytest.raises(ValueError, match="GlutealRegion.left"):
            GlutealRegion(left=Glute(side=BodySide.RIGHT))

        with pytest.raises(ValueError, match="GlutealRegion.right"):
            GlutealRegion(right=Glute(side=BodySide.LEFT))

    def test_gluteal_region_asymmetry_is_representable(self):
        region = GlutealRegion(
            left=Glute(
                side=BodySide.LEFT,
                volume=0.2,
                shape="flat",
            ),
            right=Glute(
                side=BodySide.RIGHT,
                volume=0.8,
                shape="pear",
            ),
        )

        assert region.is_valid()
        assert region.left.volume != region.right.volume
        assert region.left.shape != region.right.shape

    def test_gluteal_region_cleft_range(self):
        assert GlutealRegion(cleft_depth=0.0).is_valid()
        assert GlutealRegion(cleft_depth=1.0).is_valid()

        with pytest.raises(ValueError, match="cleft_depth"):
            GlutealRegion(cleft_depth=-0.1)

        with pytest.raises(ValueError, match="cleft_depth"):
            GlutealRegion(cleft_depth=1.1)

    # --- Hip / Hips (5) ---

    def test_hip_defaults(self):
        hip = Hip(side=BodySide.RIGHT)

        assert hip.is_valid()
        assert hip.component_type == "hip"
        assert hip.width == 9.0
        assert hip.depth == 10.0
        assert hip.prominence == 0.5
        assert hip.trochanter_prominence == 0.4
        assert hip.iliac_crest_prominence == 0.5
        assert hip.shape == "average"

    def test_hip_validation(self):
        with pytest.raises(ValueError, match="side"):
            Hip(side=None)

        with pytest.raises(ValueError, match="Hip width"):
            Hip(side=BodySide.LEFT, width=0.0)

        with pytest.raises(ValueError, match="trochanter"):
            Hip(side=BodySide.LEFT, trochanter_prominence=2.0)

        with pytest.raises(ValueError, match="Invalid hip shape"):
            Hip(side=BodySide.LEFT, shape="wide")

    def test_hips_bilateral(self):
        hips = Hips()

        assert hips.is_valid()
        assert hips.component_type == "hips"
        assert hips.left.side is BodySide.LEFT
        assert hips.right.side is BodySide.RIGHT

    def test_hips_rejects_wrong_sides(self):
        with pytest.raises(ValueError, match="Hips.left"):
            Hips(left=Hip(side=BodySide.RIGHT))

        with pytest.raises(ValueError, match="Hips.right"):
            Hips(right=Hip(side=BodySide.LEFT))

    def test_hips_asymmetry_is_representable(self):
        hips = Hips(
            left=Hip(
                side=BodySide.LEFT,
                trochanter_prominence=0.1,
            ),
            right=Hip(
                side=BodySide.RIGHT,
                trochanter_prominence=0.8,
            ),
        )

        assert hips.is_valid()
        assert (
            hips.left.trochanter_prominence
            != hips.right.trochanter_prominence
        )

    # --- Pelvis composito (6) ---

    def test_pelvis_is_now_composite(self):
        pelvis = Pelvis()

        assert pelvis.is_valid()
        assert isinstance(pelvis.hips, Hips)
        assert isinstance(pelvis.gluteal_region, GlutealRegion)
        assert pelvis.hips.left.component_type == "hip"
        assert (
            pelvis.gluteal_region.left.component_type == "glute"
        )

    def test_pelvis_legacy_params_intact(self):
        pelvis = Pelvis(
            width=40.0,
            depth=24.0,
            circumference=102.0,
            tilt=5.0,
            shape="broad",
        )

        assert pelvis.width == 40.0
        assert pelvis.shape == "broad"
        assert pelvis.is_valid()

    def test_pelvis_custom_sub_components(self):
        pelvis = Pelvis(
            hips=Hips(
                left=Hip(side=BodySide.LEFT, width=11.0),
                right=Hip(side=BodySide.RIGHT, width=11.0),
            ),
            gluteal_region=GlutealRegion(
                left=Glute(side=BodySide.LEFT, volume=0.3),
                right=Glute(side=BodySide.RIGHT, volume=0.9),
            ),
        )

        assert pelvis.hips.left.width == 11.0
        assert pelvis.gluteal_region.right.volume == 0.9
        assert pelvis.is_valid()

    def test_pelvis_rejects_wrong_sub_types(self):
        with pytest.raises(ValueError, match="hips must be"):
            Pelvis(hips="wide")

        with pytest.raises(ValueError, match="gluteal_region"):
            Pelvis(gluteal_region="round")

    def test_pelvis_serialization_nested(self):
        data = Pelvis().to_dict()

        assert data["component_type"] == "pelvis"
        assert data["hips"]["left"]["component_type"] == "hip"
        assert data["gluteal_region"]["right"]["component_type"] == "glute"
        assert data["gluteal_region"]["cleft_depth"] == 0.5

    def test_pelvis_mutation_invalidates(self):
        pelvis = Pelvis()

        pelvis.hips.left.trochanter_prominence = 5.0
        assert not pelvis.is_valid()

    # --- HumanAnatomy end-to-end (3) ---

    def test_human_anatomy_pelvic_detail(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()
        assert anatomy.pelvis.hips.left.side is BodySide.LEFT
        assert (
            anatomy.pelvis.gluteal_region.right.side
            is BodySide.RIGHT
        )

    def test_human_anatomy_pelvic_serialization(self):
        data = HumanAnatomy().to_dict()

        pelvis_data = data["pelvis"]
        assert pelvis_data["hips"]["left"]["shape"] == "average"
        assert (
            pelvis_data["gluteal_region"]["left"]["volume"] == 0.5
        )

    def test_human_anatomy_pelvic_mutation_invalidates(self):
        anatomy = HumanAnatomy()

        anatomy.pelvis.gluteal_region.left.volume = -1.0
        assert not anatomy.is_valid()

    # --- export / contract (1) ---

    def test_package_exports_h418a(self):
        for name in (
            "Glute",
            "GlutealRegion",
            "Hip",
            "Hips",
        ):
            assert hasattr(anatomy_module, name)
            assert name in anatomy_module.__all__

        for component in (
            Glute(side=BodySide.LEFT),
            GlutealRegion(),
            Hip(side=BodySide.LEFT),
            Hips(),
        ):
            assert isinstance(component, AnatomyComponent)
            assert component.is_valid()