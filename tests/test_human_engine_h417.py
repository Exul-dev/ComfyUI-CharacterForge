from __future__ import annotations

import pytest

import human.anatomy as anatomy_module
from human.anatomy import (
    Arm,
    Arms,
    BodySide,
    Elbow,
    Forearm,
    Hand,
    Hands,
    HumanAnatomy,
    UpperArm,
    Wrist,
)
from human.anatomy.anatomy_component import AnatomyComponent


class TestHumanEngineH417:

    # --- Arm (8) ---

    def test_arm_defaults_side_matching(self):
        left = Arm(side=BodySide.LEFT)
        right = Arm(side=BodySide.RIGHT)

        assert left.is_valid()
        assert left.side is BodySide.LEFT
        assert left.elbow.side is BodySide.LEFT
        assert left.wrist.side is BodySide.LEFT
        assert left.hand.side is BodySide.LEFT

        assert right.is_valid()
        assert right.elbow.side is BodySide.RIGHT
        assert right.wrist.side is BodySide.RIGHT
        assert right.hand.side is BodySide.RIGHT

        assert left.upper_arm.component_type == "upper_arm"
        assert left.forearm.component_type == "forearm"

    def test_arm_requires_side(self):
        with pytest.raises(TypeError):
            Arm()

    def test_arm_rejects_invalid_side(self):
        with pytest.raises(ValueError, match="Arm side"):
            Arm(
                side="left",
                upper_arm=UpperArm(),
                elbow=Elbow(),
                forearm=Forearm(),
                wrist=Wrist(),
                hand=Hand(),
            )

    def test_arm_rejects_mismatched_elbow_side(self):
        with pytest.raises(ValueError, match="elbow side must match"):
            Arm(
                side=BodySide.LEFT,
                elbow=Elbow(side=BodySide.RIGHT),
            )

    def test_arm_rejects_mismatched_wrist_side(self):
        with pytest.raises(ValueError, match="wrist side must match"):
            Arm(
                side=BodySide.LEFT,
                wrist=Wrist(side=BodySide.RIGHT),
            )

    def test_arm_rejects_mismatched_hand_side(self):
        with pytest.raises(ValueError, match="hand side must match"):
            Arm(
                side=BodySide.LEFT,
                hand=Hand(side=BodySide.RIGHT),
            )

    def test_arm_explicit_components_honored(self):
        arm = Arm(
            side=BodySide.RIGHT,
            upper_arm=UpperArm(length=33.0, shape="muscular"),
            forearm=Forearm(length=27.0),
        )

        assert arm.upper_arm.length == 33.0
        assert arm.upper_arm.shape == "muscular"
        assert arm.forearm.length == 27.0
        assert arm.elbow.side is BodySide.RIGHT
        assert arm.hand.side is BodySide.RIGHT

    def test_arm_serialization_and_mutation(self):
        arm = Arm(side=BodySide.LEFT)

        data = arm.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "arm"
        assert data["side"] == "left"
        assert data["elbow"]["side"] == "left"
        assert data["hand"]["side"] == "left"
        assert data["hand"]["fingers"]["thumb"]["type"] == "thumb"

        arm.elbow.flexion = 999.0
        assert not arm.is_valid()

    # --- Arms dual-mode (10) ---

    def test_arms_legacy_attributes_survive(self):
        arms = Arms()

        assert arms.is_valid()
        assert isinstance(arms.upper_arm, UpperArm)
        assert isinstance(arms.forearm, Forearm)
        assert isinstance(arms.hands, Hands)

    def test_arms_legacy_explicit_parameters(self):
        arms = Arms(
            upper_arm=UpperArm(length=32.0),
            forearm=Forearm(length=28.0),
            hands=Hands(size="large"),
        )

        assert arms.upper_arm.length == 32.0
        assert arms.forearm.length == 28.0
        assert arms.hands.size == "large"
        assert arms.is_valid()

    def test_arms_bilateral_defaults(self):
        arms = Arms()

        assert isinstance(arms.left, Arm)
        assert isinstance(arms.right, Arm)
        assert arms.left.side is BodySide.LEFT
        assert arms.right.side is BodySide.RIGHT
        assert arms.left.hand.side is BodySide.LEFT
        assert arms.right.hand.side is BodySide.RIGHT

    def test_arms_rejects_wrong_sides(self):
        with pytest.raises(ValueError, match="Arms.left"):
            Arms(left=Arm(side=BodySide.RIGHT))

        with pytest.raises(ValueError, match="Arms.right"):
            Arms(right=Arm(side=BodySide.LEFT))

    def test_arms_asymmetry_is_representable(self):
        arms = Arms(
            left=Arm(
                side=BodySide.LEFT,
                upper_arm=UpperArm(
                    shape="muscular", circumference=34.0
                ),
            ),
            right=Arm(
                side=BodySide.RIGHT,
                upper_arm=UpperArm(
                    shape="slender", circumference=26.0
                ),
            ),
        )

        assert arms.is_valid()
        assert arms.left.upper_arm.shape == "muscular"
        assert arms.right.upper_arm.shape == "slender"
        assert arms.left.upper_arm.circumference == 34.0
        assert arms.right.upper_arm.circumference == 26.0

    def test_arms_legacy_and_bilateral_are_independent(self):
        arms = Arms(upper_arm=UpperArm(length=40.0))

        assert arms.upper_arm.length == 40.0
        assert arms.left.upper_arm.length == 30.0
        assert arms.right.upper_arm.length == 30.0
        assert arms.is_valid()

    def test_arms_serialization_contains_both_models(self):
        data = Arms().to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "arms"

        for key in (
            "shoulders",
            "upper_arm",
            "elbow",
            "forearm",
            "wrist",
            "hands",
        ):
            assert key in data

        assert data["left"]["component_type"] == "arm"
        assert data["right"]["component_type"] == "arm"
        assert data["left"]["side"] == "left"
        assert data["right"]["side"] == "right"

    def test_arms_hands_model_untouched(self):
        arms = Arms()

        assert arms.hands.left.side is BodySide.LEFT
        assert arms.hands.right.side is BodySide.RIGHT

        for hand in (arms.hands.left, arms.hands.right):
            assert len(hand.fingers) == 5

    def test_arms_mutation_invalidates(self):
        arms = Arms()

        assert arms.is_valid()

        arms.left.elbow.flexion = 999.0
        assert not arms.is_valid()

    def test_arms_rejects_non_component_parameters(self):
        with pytest.raises(ValueError, match="upper_arm"):
            Arms(upper_arm="strong")

        with pytest.raises(ValueError, match="Arms.left"):
            Arms(left="left arm")

    # --- HumanAnatomy integration (3) ---

    def test_human_anatomy_arms_have_bilateral_model(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()
        assert isinstance(anatomy.arms, Arms)
        assert anatomy.arms.left.side is BodySide.LEFT
        assert anatomy.arms.right.side is BodySide.RIGHT

    def test_human_anatomy_arms_legacy_intact(self):
        anatomy = HumanAnatomy()

        assert isinstance(anatomy.arms.upper_arm, UpperArm)
        assert isinstance(anatomy.arms.forearm, Forearm)
        assert isinstance(anatomy.arms.hands, Hands)

    def test_human_anatomy_arms_mutation_invalidates(self):
        anatomy = HumanAnatomy()

        anatomy.arms.right.wrist.deviation = 500.0
        assert not anatomy.is_valid()

    # --- export / contract (3) ---

    def test_package_exports_h417(self):
        assert hasattr(anatomy_module, "Arm")
        assert "Arm" in anatomy_module.__all__

    def test_arm_is_anatomy_component(self):
        arm = Arm(side=BodySide.LEFT)

        assert isinstance(arm, AnatomyComponent)
        assert arm.is_valid()

    def test_component_types(self):
        assert Arm(side=BodySide.LEFT).component_type == "arm"
        assert Arms().component_type == "arms"

        data = Arm(side=BodySide.RIGHT).to_dict()
        assert data["component_type"] == "arm"
        assert data["schema_version"] == "1.0"
        assert data["enabled"] is True