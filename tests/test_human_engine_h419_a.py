from __future__ import annotations

import pytest

import human.anatomy as anatomy_module
from human.anatomy import (
    BodySide,
    Brow,
    Brows,
    Eyelid,
    Eyelids,
    Face,
    HumanAnatomy,
    Mouth,
    Teeth,
    Tongue,
)
from human.anatomy.anatomy_component import AnatomyComponent


class TestHumanEngineH419A:

    # --- Teeth (5) ---

    def test_teeth_defaults(self):
        teeth = Teeth()

        assert teeth.is_valid()
        assert teeth.component_type == "teeth"
        assert teeth.alignment == "straight"
        assert teeth.size == 0.5
        assert teeth.whiteness == 0.6
        assert teeth.shape == "oval"
        assert teeth.condition == "healthy"

    def test_teeth_alignments(self):
        for alignment in (
            "straight",
            "slightly_uneven",
            "uneven",
            "crowded",
            "gapped",
        ):
            assert Teeth(alignment=alignment).is_valid()

        with pytest.raises(ValueError, match="Invalid teeth alignment"):
            Teeth(alignment="crooked")

    def test_teeth_ranges(self):
        assert Teeth(size=0.0, whiteness=0.0).is_valid()
        assert Teeth(size=1.0, whiteness=1.0).is_valid()

        with pytest.raises(ValueError, match="size"):
            Teeth(size=1.5)

        with pytest.raises(ValueError, match="whiteness"):
            Teeth(whiteness=-0.1)

    def test_teeth_rejects_invalid_enums(self):
        with pytest.raises(ValueError, match="Invalid teeth shape"):
            Teeth(shape="square_ish")

        with pytest.raises(ValueError, match="Invalid teeth condition"):
            Teeth(condition="rotten")

    def test_teeth_serialization(self):
        data = Teeth(alignment="gapped", whiteness=0.3).to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "teeth"
        assert data["alignment"] == "gapped"
        assert data["whiteness"] == 0.3

    # --- Tongue (3) ---

    def test_tongue_defaults(self):
        tongue = Tongue()

        assert tongue.is_valid()
        assert tongue.component_type == "tongue"
        assert tongue.length == 8.0
        assert tongue.width == 4.0
        assert tongue.thickness == 1.8
        assert tongue.tip == "rounded"

    def test_tongue_validation(self):
        with pytest.raises(ValueError, match="Tongue length"):
            Tongue(length=0.0)

        with pytest.raises(ValueError, match="Tongue width"):
            Tongue(width=-1.0)

        with pytest.raises(ValueError, match="Invalid tongue tip"):
            Tongue(tip="forked")

        assert Tongue(tip="pointed").is_valid()

    def test_tongue_serialization(self):
        data = Tongue(tip="broad").to_dict()

        assert data["component_type"] == "tongue"
        assert data["tip"] == "broad"
        assert data["thickness"] == 1.8

    # --- Eyelid/Eyelids (7) ---

    def test_eyelid_defaults(self):
        lid = Eyelid(side=BodySide.LEFT)

        assert lid.is_valid()
        assert lid.component_type == "eyelid"
        assert lid.side is BodySide.LEFT
        assert lid.eye_shape == "almond"
        assert lid.crease == "double"
        assert lid.upper_exposure == 0.6
        assert lid.lower_exposure == 0.4
        assert lid.thickness == 0.4

    def test_eyelid_requires_side(self):
        with pytest.raises(TypeError):
            Eyelid()

    def test_eyelid_eye_shapes(self):
        for shape in (
            "round",
            "almond",
            "hooded",
            "monolid",
            "upturned",
            "downturned",
        ):
            assert Eyelid(
                side=BodySide.LEFT, eye_shape=shape
            ).is_valid()

        with pytest.raises(ValueError, match="eye_shape"):
            Eyelid(side=BodySide.LEFT, eye_shape="squinty")

    def test_eyelid_creases(self):
        for crease in ("single", "double", "hooded"):
            assert Eyelid(
                side=BodySide.LEFT, crease=crease
            ).is_valid()

        with pytest.raises(ValueError, match="crease"):
            Eyelid(side=BodySide.LEFT, crease="triple")

    def test_eyelid_ranges(self):
        with pytest.raises(ValueError, match="upper_exposure"):
            Eyelid(side=BodySide.LEFT, upper_exposure=1.5)

        with pytest.raises(ValueError, match="lower_exposure"):
            Eyelid(side=BodySide.LEFT, lower_exposure=-0.1)

        with pytest.raises(ValueError, match="thickness"):
            Eyelid(side=BodySide.LEFT, thickness=2.0)

    def test_eyelids_bilateral_and_ptosis(self):
        lids = Eyelids()

        assert lids.is_valid()
        assert lids.left.side is BodySide.LEFT
        assert lids.right.side is BodySide.RIGHT

        # Unilateral ptosis: a real-world case, representable.
        ptosis = Eyelids(
            left=Eyelid(
                side=BodySide.LEFT, upper_exposure=0.15
            ),
        )
        assert ptosis.is_valid()
        assert (
            ptosis.left.upper_exposure
            != ptosis.right.upper_exposure
        )

    def test_eyelids_rejects_wrong_sides(self):
        with pytest.raises(ValueError, match="Eyelids.left"):
            Eyelids(left=Eyelid(side=BodySide.RIGHT))

        with pytest.raises(ValueError, match="Eyelids.right"):
            Eyelids(right=Eyelid(side=BodySide.LEFT))

    # --- Brow/Brows (6) ---

    def test_brow_defaults(self):
        brow = Brow(side=BodySide.RIGHT)

        assert brow.is_valid()
        assert brow.component_type == "brow"
        assert brow.thickness == "medium"
        assert brow.arch == "gentle"
        assert brow.height == 0.5
        assert brow.length == 5.5
        assert brow.shape == "curved"
        assert brow.density == 0.6

    def test_brow_requires_side(self):
        with pytest.raises(TypeError):
            Brow()

    def test_brow_enums(self):
        with pytest.raises(ValueError, match="thickness"):
            Brow(side=BodySide.LEFT, thickness="bushy")

        with pytest.raises(ValueError, match="arch"):
            Brow(side=BodySide.LEFT, arch="wavy")

        with pytest.raises(ValueError, match="Invalid brow shape"):
            Brow(side=BodySide.LEFT, shape="zigzag")

        assert Brow(
            side=BodySide.LEFT,
            thickness="thick",
            arch="high",
            shape="angled",
        ).is_valid()

    def test_brow_ranges(self):
        with pytest.raises(ValueError, match="height"):
            Brow(side=BodySide.LEFT, height=1.1)

        with pytest.raises(ValueError, match="length"):
            Brow(side=BodySide.LEFT, length=0.0)

        with pytest.raises(ValueError, match="density"):
            Brow(side=BodySide.LEFT, density=-0.1)

    def test_brows_asymmetry_is_representable(self):
        brows = Brows(
            left=Brow(
                side=BodySide.LEFT,
                arch="flat",
                height=0.3,
            ),
            right=Brow(
                side=BodySide.RIGHT,
                arch="high",
                height=0.8,
            ),
        )

        assert brows.is_valid()
        assert brows.left.arch != brows.right.arch
        assert brows.left.height != brows.right.height

    def test_brows_rejects_wrong_sides(self):
        with pytest.raises(ValueError, match="Brows.left"):
            Brows(left=Brow(side=BodySide.RIGHT))

        with pytest.raises(ValueError, match="Brows.right"):
            Brows(right=Brow(side=BodySide.LEFT))

    # --- Mouth composito (4) ---

    def test_mouth_is_composite(self):
        mouth = Mouth()

        assert mouth.is_valid()
        assert isinstance(mouth.teeth, Teeth)
        assert isinstance(mouth.tongue, Tongue)
        assert mouth.philtrum.component_type == "philtrum"

    def test_mouth_custom_interior(self):
        mouth = Mouth(
            teeth=Teeth(alignment="gapped"),
            tongue=Tongue(tip="pointed"),
        )

        assert mouth.teeth.alignment == "gapped"
        assert mouth.tongue.tip == "pointed"
        assert mouth.is_valid()

    def test_mouth_rejects_wrong_interior_types(self):
        with pytest.raises(ValueError, match="teeth must be"):
            Mouth(teeth="white")

        with pytest.raises(ValueError, match="tongue must be"):
            Mouth(tongue="muscular")

    def test_mouth_legacy_contract_intact(self):
        mouth = Mouth(width=4.5, shape="thin")

        assert mouth.width == 4.5
        assert mouth.shape == "thin"

        with pytest.raises(ValueError, match="upper lip thickness"):
            Mouth(lip_upper_thickness=0.0)

    # --- Face composito + HumanAnatomy (5) ---

    def test_face_has_eyelids_and_brows(self):
        face = Face()

        assert face.is_valid()
        assert isinstance(face.eyelids, Eyelids)
        assert isinstance(face.brows, Brows)
        assert face.eyelids.left.side is BodySide.LEFT
        assert face.brows.right.side is BodySide.RIGHT

    def test_face_custom_eyelids(self):
        face = Face(
            eyelids=Eyelids(
                left=Eyelid(
                    side=BodySide.LEFT, eye_shape="monolid"
                ),
                right=Eyelid(
                    side=BodySide.RIGHT, eye_shape="monolid"
                ),
            )
        )

        assert face.eyelids.left.eye_shape == "monolid"
        assert face.is_valid()

    def test_anatomy_face_internal_detail(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()
        assert (
            anatomy.head.face.mouth.teeth.alignment
            == "straight"
        )
        assert (
            anatomy.head.face.mouth.tongue.tip == "rounded"
        )
        assert (
            anatomy.head.face.eyelids.right.eye_shape == "almond"
        )
        assert (
            anatomy.head.face.brows.left.thickness == "medium"
        )

    def test_anatomy_serialization_internal_detail(self):
        data = HumanAnatomy().to_dict()

        face_data = data["head"]["face"]
        assert (
            face_data["mouth"]["teeth"]["alignment"] == "straight"
        )
        assert face_data["mouth"]["tongue"]["tip"] == "rounded"
        assert (
            face_data["eyelids"]["left"]["eye_shape"] == "almond"
        )
        assert (
            face_data["brows"]["right"]["arch"] == "gentle"
        )

    def test_anatomy_eyelid_mutation_invalidates(self):
        anatomy = HumanAnatomy()

        anatomy.head.face.eyelids.right.crease = "impossible"
        assert not anatomy.is_valid()

    # --- export / contract (1) ---

    def test_package_exports_h419a(self):
        for name in (
            "Teeth",
            "Tongue",
            "Eyelid",
            "Eyelids",
            "Brow",
            "Brows",
        ):
            assert hasattr(anatomy_module, name)
            assert name in anatomy_module.__all__

        for component in (
            Teeth(),
            Tongue(),
            Eyelid(side=BodySide.LEFT),
            Eyelids(),
            Brow(side=BodySide.LEFT),
            Brows(),
        ):
            assert isinstance(component, AnatomyComponent)
            assert component.is_valid()