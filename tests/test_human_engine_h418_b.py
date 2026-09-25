from __future__ import annotations

import pytest

import human.anatomy as anatomy_module
from human.anatomy import (
    Abdomen,
    BodySide,
    Flank,
    Flanks,
    HumanAnatomy,
    LowerLeg,
    Thigh,
)


class TestHumanEngineH418B:

    # --- Flank (4) ---

    def test_flank_defaults(self):
        flank = Flank(side=BodySide.LEFT)

        assert flank.is_valid()
        assert flank.component_type == "flank"
        assert flank.width == 9.0
        assert flank.fullness == 0.4
        assert flank.definition == 0.4
        assert flank.love_handle_prominence == 0.2
        assert flank.shape == "straight"

    def test_flank_requires_side(self):
        with pytest.raises(TypeError):
            Flank()

    def test_flank_validation(self):
        with pytest.raises(ValueError, match="side"):
            Flank(side="left")

        with pytest.raises(ValueError, match="Invalid flank shape"):
            Flank(side=BodySide.LEFT, shape="rippled")

        with pytest.raises(ValueError, match="Flank width"):
            Flank(side=BodySide.LEFT, width=0.0)

        with pytest.raises(ValueError, match="fullness"):
            Flank(side=BodySide.LEFT, fullness=1.5)

        with pytest.raises(ValueError, match="love_handle_prominence"):
            Flank(side=BodySide.LEFT, love_handle_prominence=-0.1)

    def test_flank_serialization_and_mutation(self):
        flank = Flank(side=BodySide.RIGHT, shape="full")

        data = flank.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "flank"
        assert data["side"] == "right"
        assert data["shape"] == "full"

        flank.definition = 9.0
        assert not flank.is_valid()

    # --- Flanks (3) ---

    def test_flanks_bilateral(self):
        flanks = Flanks()

        assert flanks.is_valid()
        assert flanks.component_type == "flanks"
        assert flanks.left.side is BodySide.LEFT
        assert flanks.right.side is BodySide.RIGHT

    def test_flanks_rejects_wrong_sides(self):
        with pytest.raises(ValueError, match="Flanks.left"):
            Flanks(left=Flank(side=BodySide.RIGHT))

        with pytest.raises(ValueError, match="Flanks.right"):
            Flanks(right=Flank(side=BodySide.LEFT))

    def test_flanks_asymmetry_is_representable(self):
        flanks = Flanks(
            left=Flank(
                side=BodySide.LEFT,
                love_handle_prominence=0.05,
                shape="hollow",
            ),
            right=Flank(
                side=BodySide.RIGHT,
                love_handle_prominence=0.6,
                shape="full",
            ),
        )

        assert flanks.is_valid()
        assert (
            flanks.left.love_handle_prominence
            != flanks.right.love_handle_prominence
        )

    # --- Abdomen composito (5) ---

    def test_abdomen_is_composite(self):
        abdomen = Abdomen()

        assert abdomen.is_valid()
        assert isinstance(abdomen.flanks, Flanks)
        assert abdomen.flanks.left.component_type == "flank"

    def test_abdomen_custom_flanks(self):
        abdomen = Abdomen(
            flanks=Flanks(
                left=Flank(side=BodySide.LEFT, fullness=0.9),
                right=Flank(side=BodySide.RIGHT, fullness=0.9),
            )
        )

        assert abdomen.flanks.left.fullness == 0.9
        assert abdomen.is_valid()

    def test_abdomen_rejects_wrong_flanks_type(self):
        with pytest.raises(ValueError, match="flanks must be"):
            Abdomen(flanks="sides")

    def test_abdomen_serialization_nested(self):
        data = Abdomen().to_dict()

        assert data["component_type"] == "abdomen"
        assert data["flanks"]["left"]["component_type"] == "flank"
        assert data["flanks"]["left"]["shape"] == "straight"

    def test_abdomen_mutation_invalidates(self):
        abdomen = Abdomen()

        abdomen.flanks.right.width = 0.0
        assert not abdomen.is_valid()

    # --- Thigh arricchito (5) ---

    def test_thigh_enriched_defaults(self):
        thigh = Thigh()

        assert thigh.is_valid()
        assert thigh.length == 44.0
        assert thigh.circumference == 56.0
        assert thigh.width == 18.0
        assert thigh.depth == 19.0
        assert thigh.shape == "average"
        assert thigh.quad_prominence == 0.5
        assert thigh.hamstring_prominence == 0.5
        assert thigh.inner_fullness == 0.4

    def test_thigh_legacy_contract_intact(self):
        # The H4.15-A contract survives the enrichment.
        thigh = Thigh(length=46.0, shape="muscular")

        assert thigh.length == 46.0
        assert thigh.shape == "muscular"

        with pytest.raises(ValueError, match="Thigh length"):
            Thigh(length=0.0)

        with pytest.raises(ValueError, match="Thigh circumference"):
            Thigh(circumference=-1.0)

        with pytest.raises(ValueError, match="Invalid thigh shape"):
            Thigh(shape="enormous")

    def test_thigh_new_params_validation(self):
        with pytest.raises(ValueError, match="Thigh width"):
            Thigh(width=0.0)

        with pytest.raises(ValueError, match="Thigh depth"):
            Thigh(depth=-1.0)

        with pytest.raises(ValueError, match="quad_prominence"):
            Thigh(quad_prominence=1.5)

        with pytest.raises(ValueError, match="hamstring_prominence"):
            Thigh(hamstring_prominence=-0.1)

        with pytest.raises(ValueError, match="inner_fullness"):
            Thigh(inner_fullness=2.0)

    def test_thigh_serialization_includes_new_fields(self):
        data = Thigh(quad_prominence=0.8).to_dict()

        assert data["width"] == 18.0
        assert data["depth"] == 19.0
        assert data["quad_prominence"] == 0.8
        assert data["inner_fullness"] == 0.4

    def test_thigh_mutation_new_field_invalidates(self):
        thigh = Thigh()

        thigh.shin = None  # noqa: guard against typos
        thigh.inner_fullness = 5.0
        assert not thigh.is_valid()

    # --- LowerLeg arricchito (5) ---

    def test_lower_leg_enriched_defaults(self):
        lower = LowerLeg()

        assert lower.is_valid()
        assert lower.length == 42.0
        assert lower.circumference == 36.0
        assert lower.width == 11.0
        assert lower.depth == 12.0
        assert lower.calf_prominence == 0.5
        assert lower.calf_definition == 0.5
        assert lower.shin_definition == 0.5

    def test_lower_leg_legacy_contract_intact(self):
        with pytest.raises(ValueError, match="Lower leg length"):
            LowerLeg(length=0.0)

        with pytest.raises(ValueError, match="Lower leg circumference"):
            LowerLeg(circumference=-1.0)

        with pytest.raises(ValueError, match="Invalid lower leg shape"):
            LowerLeg(shape="colossal")

        with pytest.raises(ValueError, match="calf prominence"):
            LowerLeg(calf_prominence=1.1)

        assert LowerLeg(
            calf_prominence=0.0, shape="athletic"
        ).is_valid()

    def test_lower_leg_new_params_validation(self):
        with pytest.raises(ValueError, match="Lower leg width"):
            LowerLeg(width=0.0)

        with pytest.raises(ValueError, match="Lower leg depth"):
            LowerLeg(depth=-1.0)

        with pytest.raises(ValueError, match="calf definition"):
            LowerLeg(calf_definition=1.5)

        with pytest.raises(ValueError, match="shin definition"):
            LowerLeg(shin_definition=-0.1)

    def test_lower_leg_serialization_includes_new_fields(self):
        data = LowerLeg(shin_definition=0.8).to_dict()

        assert data["width"] == 11.0
        assert data["depth"] == 12.0
        assert data["calf_definition"] == 0.5
        assert data["shin_definition"] == 0.8

    def test_lower_leg_mutation_new_field_invalidates(self):
        lower = LowerLeg()

        lower.calf_definition = 9.0
        assert not lower.is_valid()

    # --- HumanAnatomy end-to-end (2) ---

    def test_anatomy_flank_detail(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()
        assert (
            anatomy.abdomen.flanks.left.side is BodySide.LEFT
        )
        assert (
            anatomy.abdomen.flanks.left.love_handle_prominence
            == 0.2
        )

        data = anatomy.to_dict()
        assert data["abdomen"]["flanks"]["right"][
            "component_type"
        ] == "flank"

    def test_anatomy_leg_segments_enriched(self):
        anatomy = HumanAnatomy()

        assert (
            anatomy.legs.left.thigh.quad_prominence == 0.5
        )
        assert (
            anatomy.legs.right.lower_leg.shin_definition == 0.5
        )

        data = anatomy.to_dict()
        assert data["legs"]["left"]["thigh"]["width"] == 18.0
        assert (
            data["legs"]["right"]["lower_leg"]["depth"] == 12.0
        )

    # --- export (1) ---

    def test_package_exports_h418b(self):
        for name in ("Flank", "Flanks"):
            assert hasattr(anatomy_module, name)
            assert name in anatomy_module.__all__