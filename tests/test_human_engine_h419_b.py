from __future__ import annotations

import pytest

import human.anatomy as anatomy_module
from human.anatomy import (
    Abdomen,
    Axilla,
    Axillae,
    BodySide,
    Chest,
    Clavicle,
    Clavicles,
    HumanAnatomy,
    Navel,
    PubicRegion,
    Sternum,
)
from human.anatomy.anatomy_component import AnatomyComponent


class TestHumanEngineH419B:

    # --- Clavicle/Clavicles (4) ---

    def test_clavicle_defaults(self):
        clavicle = Clavicle(side=BodySide.LEFT)

        assert clavicle.is_valid()
        assert clavicle.component_type == "clavicle"
        assert clavicle.length == 15.0
        assert clavicle.prominence == 0.5
        assert clavicle.slope == 0.5
        assert clavicle.visibility == 0.5

    def test_clavicle_requires_side(self):
        with pytest.raises(TypeError):
            Clavicle()

    def test_clavicle_validation_and_asymmetry(self):
        with pytest.raises(ValueError, match="side"):
            Clavicle(side="left")

        with pytest.raises(ValueError, match="Clavicle length"):
            Clavicle(side=BodySide.LEFT, length=0.0)

        with pytest.raises(ValueError, match="visibility"):
            Clavicle(side=BodySide.LEFT, visibility=1.5)

        clavicles = Clavicles(
            left=Clavicle(side=BodySide.LEFT, visibility=0.9),
            right=Clavicle(side=BodySide.RIGHT, visibility=0.2),
        )
        assert clavicles.is_valid()
        assert (
            clavicles.left.visibility
            != clavicles.right.visibility
        )

    def test_clavicles_rejects_wrong_sides(self):
        with pytest.raises(ValueError, match="Clavicles.left"):
            Clavicles(left=Clavicle(side=BodySide.RIGHT))

        with pytest.raises(ValueError, match="Clavicles.right"):
            Clavicles(right=Clavicle(side=BodySide.LEFT))

    # --- Sternum (3) ---

    def test_sternum_defaults(self):
        sternum = Sternum()

        assert sternum.is_valid()
        assert sternum.component_type == "sternum"
        assert sternum.length == 17.0
        assert sternum.width == 2.5
        assert sternum.angle == 0.3
        assert sternum.prominence == 0.4
        assert sternum.xiphoid_shape == "rounded"

    def test_sternum_validation(self):
        with pytest.raises(ValueError, match="Sternum length"):
            Sternum(length=0.0)

        with pytest.raises(ValueError, match="Sternum width"):
            Sternum(width=-1.0)

        with pytest.raises(ValueError, match="angle"):
            Sternum(angle=1.5)

        with pytest.raises(ValueError, match="xiphoid shape"):
            Sternum(xiphoid_shape="forked")

        assert Sternum(xiphoid_shape="bifid").is_valid()

    def test_sternum_serialization(self):
        data = Sternum(xiphoid_shape="pointed").to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "sternum"
        assert data["xiphoid_shape"] == "pointed"

    # --- Navel (3) ---

    def test_navel_defaults(self):
        navel = Navel()

        assert navel.is_valid()
        assert navel.component_type == "navel"
        assert navel.depth == 0.5
        assert navel.size == 1.0
        assert navel.shape == "innie"
        assert navel.position == 0.5

    def test_navel_validation(self):
        with pytest.raises(ValueError, match="Invalid navel shape"):
            Navel(shape="spiral")

        with pytest.raises(ValueError, match="depth"):
            Navel(depth=1.5)

        with pytest.raises(ValueError, match="size"):
            Navel(size=0.0)

        with pytest.raises(ValueError, match="position"):
            Navel(position=-0.1)

        for shape in ("innie", "outie", "flat", "vertical", "horizontal"):
            assert Navel(shape=shape).is_valid()

    def test_navel_serialization(self):
        data = Navel(shape="outie").to_dict()

        assert data["component_type"] == "navel"
        assert data["shape"] == "outie"

    # --- Axilla/Axillae (3) ---

    def test_axilla_defaults(self):
        axilla = Axilla(side=BodySide.RIGHT)

        assert axilla.is_valid()
        assert axilla.component_type == "axilla"
        assert axilla.depth == 0.4
        assert axilla.hollow_visibility == 0.5
        assert axilla.hair_density == 0.5

    def test_axilla_validation_and_asymmetry(self):
        with pytest.raises(TypeError):
            Axilla()

        with pytest.raises(ValueError, match="hair_density"):
            Axilla(side=BodySide.LEFT, hair_density=1.5)

        axillae = Axillae(
            left=Axilla(side=BodySide.LEFT, hair_density=0.0),
            right=Axilla(side=BodySide.RIGHT, hair_density=0.8),
        )
        assert axillae.is_valid()
        assert (
            axillae.left.hair_density
            != axillae.right.hair_density
        )

    def test_axillae_rejects_wrong_sides(self):
        with pytest.raises(ValueError, match="Axillae.left"):
            Axillae(left=Axilla(side=BodySide.RIGHT))

    # --- Chest arricchito (3) ---

    def test_chest_enriched_defaults(self):
        chest = Chest()

        assert chest.is_valid()
        assert chest.pectoral_definition == 0.5
        assert chest.pectoral_separation == 0.4
        assert isinstance(chest.sternum, Sternum)

    def test_chest_legacy_contract_intact(self):
        with pytest.raises(ValueError, match="Chest width"):
            Chest(width=0.0)

        with pytest.raises(ValueError, match="Invalid chest shape"):
            Chest(shape="enormous")

        assert Chest(width=34.0).width == 34.0

    def test_chest_new_params_validation(self):
        with pytest.raises(ValueError, match="pectoral_definition"):
            Chest(pectoral_definition=1.5)

        with pytest.raises(ValueError, match="pectoral_separation"):
            Chest(pectoral_separation=-0.1)

        with pytest.raises(ValueError, match="sternum must be"):
            Chest(sternum="bone")

    # --- Abdomen composito (4) ---

    def test_abdomen_enriched_defaults(self):
        abdomen = Abdomen()

        assert abdomen.is_valid()
        assert isinstance(abdomen.navel, Navel)
        assert abdomen.rectus_definition == 0.5
        assert abdomen.linea_alba_prominence == 0.4
        assert abdomen.oblique_definition == 0.5

    def test_abdomen_legacy_contract_intact(self):
        with pytest.raises(ValueError, match="Abdomen length"):
            Abdomen(length=0.0)

        with pytest.raises(ValueError, match="Invalid abdomen shape"):
            Abdomen(shape="wavy")

        with pytest.raises(ValueError, match="flanks must be"):
            Abdomen(flanks="sides")

    def test_abdomen_new_params_validation(self):
        with pytest.raises(ValueError, match="rectus_definition"):
            Abdomen(rectus_definition=1.5)

        with pytest.raises(ValueError, match="linea_alba_prominence"):
            Abdomen(linea_alba_prominence=-0.1)

        with pytest.raises(ValueError, match="oblique_definition"):
            Abdomen(oblique_definition=2.0)

        with pytest.raises(ValueError, match="navel must be"):
            Abdomen(navel="button")

    def test_abdomen_custom_navel(self):
        abdomen = Abdomen(navel=Navel(shape="outie", position=0.8))

        assert abdomen.navel.shape == "outie"
        assert abdomen.navel.position == 0.8
        assert abdomen.is_valid()

    # --- PubicRegion + Pelvis (3) ---

    def test_pubic_region_defaults(self):
        region = PubicRegion()

        assert region.is_valid()
        assert region.component_type == "pubic_region"
        assert region.mons_prominence == 0.4
        assert region.hair_coverage == 0.5

    def test_pubic_region_validation(self):
        with pytest.raises(ValueError, match="mons_prominence"):
            PubicRegion(mons_prominence=1.5)

        with pytest.raises(ValueError, match="hair_coverage"):
            PubicRegion(hair_coverage=-0.1)

        assert PubicRegion(
            mons_prominence=0.0, hair_coverage=0.0
        ).is_valid()

    def test_pelvis_carries_pubic_region(self):
        from human.anatomy import Pelvis

        pelvis = Pelvis()

        assert isinstance(pelvis.pubic_region, PubicRegion)
        assert pelvis.is_valid()

        with pytest.raises(ValueError, match="pubic_region"):
            Pelvis(pubic_region="area")

    # --- HumanAnatomy end-to-end (3) ---

    def test_anatomy_anterior_trunk(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()
        assert isinstance(anatomy.clavicles, Clavicles)
        assert isinstance(anatomy.axillae, Axillae)
        assert anatomy.chest.sternum.xiphoid_shape == "rounded"
        assert anatomy.abdomen.navel.shape == "innie"
        assert anatomy.pelvis.pubic_region.mons_prominence == 0.4

    def test_anatomy_serialization_anterior(self):
        data = HumanAnatomy().to_dict()

        assert data["clavicles"]["right"]["side"] == "right"
        assert data["chest"]["sternum"]["length"] == 17.0
        assert data["abdomen"]["navel"]["shape"] == "innie"
        assert data["axillae"]["left"]["component_type"] == "axilla"
        assert (
            data["pelvis"]["pubic_region"]["hair_coverage"] == 0.5
        )

    def test_anatomy_mutation_navel_invalidates(self):
        anatomy = HumanAnatomy()

        anatomy.abdomen.navel.size = 0.0
        assert not anatomy.is_valid()

    # --- export (2) ---

    def test_package_exports_h419b(self):
        for name in (
            "Clavicle",
            "Clavicles",
            "Sternum",
            "Axilla",
            "Axillae",
            "Navel",
            "PubicRegion",
        ):
            assert hasattr(anatomy_module, name)
            assert name in anatomy_module.__all__

    def test_all_new_components_valid(self):
        for component in (
            Clavicle(side=BodySide.LEFT),
            Clavicles(),
            Sternum(),
            Axilla(side=BodySide.LEFT),
            Axillae(),
            Navel(),
            PubicRegion(),
        ):
            assert isinstance(component, AnatomyComponent)
            assert component.is_valid()