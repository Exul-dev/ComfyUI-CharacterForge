from __future__ import annotations

import pytest

import human.anatomy as anatomy_module
from human.anatomy import (
    Back,
    BodySide,
    HumanAnatomy,
    Neck,
    Scapula,
    Scapulae,
)
from human.anatomy.anatomy_component import AnatomyComponent


class TestHumanEngineH419C:

    # --- Scapula/Scapulae (5) ---

    def test_scapula_defaults(self):
        scapula = Scapula(side=BodySide.LEFT)

        assert scapula.is_valid()
        assert scapula.component_type == "scapula"
        assert scapula.width == 11.0
        assert scapula.height == 14.0
        assert scapula.prominence == 0.4
        assert scapula.winging == 0.05
        assert scapula.shape == "average"

    def test_scapula_requires_side(self):
        with pytest.raises(TypeError):
            Scapula()

    def test_scapula_validation(self):
        with pytest.raises(ValueError, match="side"):
            Scapula(side="left")

        with pytest.raises(ValueError, match="Scapula width"):
            Scapula(side=BodySide.LEFT, width=0.0)

        with pytest.raises(ValueError, match="Scapula height"):
            Scapula(side=BodySide.LEFT, height=-1.0)

        with pytest.raises(ValueError, match="winging"):
            Scapula(side=BodySide.LEFT, winging=1.5)

        with pytest.raises(ValueError, match="Invalid scapula shape"):
            Scapula(side=BodySide.LEFT, shape="winged")

    def test_scapulae_unilateral_winging(self):
        # Scapular winging: real clinical condition, monolateral.
        winged = Scapulae(
            left=Scapula(side=BodySide.LEFT, winging=0.8),
            right=Scapula(side=BodySide.RIGHT, winging=0.05),
        )

        assert winged.is_valid()
        assert winged.left.winging != winged.right.winging

    def test_scapulae_rejects_wrong_sides(self):
        with pytest.raises(ValueError, match="Scapulae.left"):
            Scapulae(left=Scapula(side=BodySide.RIGHT))

        with pytest.raises(ValueError, match="Scapulae.right"):
            Scapulae(right=Scapula(side=BodySide.LEFT))

    # --- Back composito (6) ---

    def test_back_enriched_defaults(self):
        back = Back()

        assert back.is_valid()
        assert isinstance(back.scapulae, Scapulae)
        assert back.spine_groove_depth == 0.4
        assert back.lumbar_fossa_depth == 0.3
        assert back.trapezius_definition == 0.5

    def test_back_legacy_contract_intact(self):
        # Legacy messages preserved verbatim (no trailing period
        # on the shape message, exactly as in H4.7).
        with pytest.raises(ValueError, match="Back width"):
            Back(width=0.0)

        with pytest.raises(ValueError, match="Back length"):
            Back(length=-1.0)

        with pytest.raises(ValueError, match="Back muscularity"):
            Back(muscularity=1.5)

        with pytest.raises(ValueError, match="Invalid back shape"):
            Back(shape="hunched")

        assert Back(width=33.0, shape="athletic").is_valid()

    def test_back_new_params_validation(self):
        with pytest.raises(ValueError, match="spine_groove_depth"):
            Back(spine_groove_depth=1.5)

        with pytest.raises(ValueError, match="lumbar_fossa_depth"):
            Back(lumbar_fossa_depth=-0.1)

        with pytest.raises(ValueError, match="trapezius_definition"):
            Back(trapezius_definition=2.0)

        with pytest.raises(ValueError, match="scapulae must be"):
            Back(scapulae="blades")

    def test_back_custom_scapulae(self):
        back = Back(
            scapulae=Scapulae(
                left=Scapula(
                    side=BodySide.LEFT, prominence=0.8
                ),
                right=Scapula(
                    side=BodySide.RIGHT, prominence=0.8
                ),
            )
        )

        assert back.scapulae.left.prominence == 0.8
        assert back.is_valid()

    def test_back_serialization_nested(self):
        data = Back().to_dict()

        assert data["component_type"] == "back"
        assert data["scapulae"]["left"]["component_type"] == "scapula"
        assert data["spine_groove_depth"] == 0.4
        assert data["scapulae"]["right"]["winging"] == 0.05

    def test_back_mutation_scapula_invalidates(self):
        back = Back()

        back.scapulae.left.winging = 9.0
        assert not back.is_valid()

    # --- Neck arricchito (5) ---

    def test_neck_enriched_defaults(self):
        neck = Neck()

        assert neck.is_valid()
        assert neck.adam_apple_prominence == 0.3
        assert neck.adam_apple_size == 2.5

    def test_neck_legacy_contract_intact(self):
        with pytest.raises(ValueError, match="Neck length"):
            Neck(length=0.0)

        with pytest.raises(ValueError, match="Neck circumference"):
            Neck(circumference=-1.0)

        with pytest.raises(ValueError, match="Invalid neck shape"):
            Neck(shape="giraffe")

    def test_neck_adam_apple_validation(self):
        with pytest.raises(ValueError, match="adam_apple_prominence"):
            Neck(adam_apple_prominence=1.5)

        with pytest.raises(ValueError, match="adam_apple_size"):
            Neck(adam_apple_size=0.0)

        assert Neck(
            adam_apple_prominence=0.0, adam_apple_size=1.0
        ).is_valid()

    def test_neck_dimorphism_representable(self):
        # Feminine vs masculine profiles stay expressible.
        subtle = Neck(adam_apple_prominence=0.05)
        pronounced = Neck(adam_apple_prominence=0.9, adam_apple_size=4.0)

        assert subtle.is_valid()
        assert pronounced.is_valid()
        assert (
            subtle.adam_apple_prominence
            != pronounced.adam_apple_prominence
        )

    def test_neck_serialization_includes_adam_apple(self):
        data = Neck(adam_apple_prominence=0.7).to_dict()

        assert data["adam_apple_prominence"] == 0.7
        assert data["adam_apple_size"] == 2.5
        assert data["shape"] == "average"

    # --- HumanAnatomy end-to-end (2) ---

    def test_anatomy_back_and_neck_detail(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()
        assert (
            anatomy.back.scapulae.left.side is BodySide.LEFT
        )
        assert anatomy.back.spine_groove_depth == 0.4
        assert anatomy.neck.adam_apple_prominence == 0.3

    def test_anatomy_serialization_back_neck(self):
        data = HumanAnatomy().to_dict()

        assert (
            data["back"]["scapulae"]["right"]["component_type"]
            == "scapula"
        )
        assert data["back"]["lumbar_fossa_depth"] == 0.3
        assert data["neck"]["adam_apple_size"] == 2.5

    # --- export (1) ---

    def test_package_exports_h419c(self):
        for name in ("Scapula", "Scapulae"):
            assert hasattr(anatomy_module, name)
            assert name in anatomy_module.__all__

        for component in (
            Scapula(side=BodySide.LEFT),
            Scapulae(),
        ):
            assert isinstance(component, AnatomyComponent)
            assert component.is_valid()