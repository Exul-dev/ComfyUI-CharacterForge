from __future__ import annotations

import pytest

from human.anatomy import (
    Ankle,
    BodySide,
    Forearm,
    Hand,
    HumanAnatomy,
    UpperArm,
)


class TestHumanEngineH419D:

    # --- UpperArm arricchito (3) ---

    def test_upper_arm_enriched_defaults(self):
        arm = UpperArm()

        assert arm.is_valid()
        assert arm.width == 9.5
        assert arm.depth == 9.0
        assert arm.bicep_prominence == 0.5
        assert arm.tricep_prominence == 0.5
        assert arm.inner_definition == 0.4

    def test_upper_arm_legacy_contract_intact(self):
        # Legacy eager checks with exact messages.
        with pytest.raises(ValueError, match="Upper arm length"):
            UpperArm(length=0.0)

        with pytest.raises(ValueError, match="Upper arm circumference"):
            UpperArm(circumference=-1.0)

        with pytest.raises(ValueError, match="Invalid upper arm shape"):
            UpperArm(shape="enormous")

        assert UpperArm(length=32.0).length == 32.0

    def test_upper_arm_new_params_validation(self):
        with pytest.raises(ValueError, match="Upper arm width"):
            UpperArm(width=0.0)

        with pytest.raises(ValueError, match="Upper arm depth"):
            UpperArm(depth=-1.0)

        with pytest.raises(ValueError, match="bicep_prominence"):
            UpperArm(bicep_prominence=1.5)

        with pytest.raises(ValueError, match="tricep_prominence"):
            UpperArm(tricep_prominence=-0.1)

        assert UpperArm(
            bicep_prominence=0.0, tricep_prominence=1.0
        ).is_valid()

    # --- Forearm arricchito (3) ---

    def test_forearm_enriched_defaults(self):
        forearm = Forearm()

        assert forearm.is_valid()
        assert forearm.width == 7.5
        assert forearm.depth == 7.0
        assert forearm.brachioradialis_definition == 0.4
        assert forearm.ulna_definition == 0.4
        assert forearm.vascularity == 0.3

    def test_forearm_legacy_contract_intact(self):
        with pytest.raises(ValueError, match="Forearm length"):
            Forearm(length=0.0)

        with pytest.raises(ValueError, match="Forearm circumference"):
            Forearm(circumference=-1.0)

        with pytest.raises(ValueError, match="Invalid forearm shape"):
            Forearm(shape="skeletal")

    def test_forearm_new_params_validation(self):
        with pytest.raises(ValueError, match="Forearm width"):
            Forearm(width=0.0)

        with pytest.raises(ValueError, match="brachioradialis_definition"):
            Forearm(brachioradialis_definition=1.5)

        with pytest.raises(ValueError, match="vascularity"):
            Forearm(vascularity=-0.1)

        assert Forearm(vascularity=1.0).is_valid()

    # --- Ankle malleoli (3) ---

    def test_ankle_enriched_defaults(self):
        ankle = Ankle(side=BodySide.LEFT)

        assert ankle.is_valid()
        assert ankle.malleolus_prominence == 0.5
        assert ankle.malleolus_width == 1.5

    def test_ankle_legacy_contract_intact(self):
        with pytest.raises(ValueError, match="Ankle flexion"):
            Ankle(flexion=60.1)

        with pytest.raises(ValueError, match="Ankle deviation"):
            Ankle(deviation=30.1)

        with pytest.raises(ValueError, match="side"):
            Ankle(side="left")

    def test_ankle_malleoli_validation(self):
        with pytest.raises(ValueError, match="malleolus_prominence"):
            Ankle(malleolus_prominence=1.5)

        with pytest.raises(ValueError, match="malleolus_width"):
            Ankle(malleolus_width=0.0)

        assert Ankle(
            malleolus_prominence=0.0, malleolus_width=2.0
        ).is_valid()

    # --- Hand nocche (2) ---

    def test_hand_knuckle_defaults(self):
        hand = Hand(side=BodySide.RIGHT)

        assert hand.is_valid()
        assert hand.knuckle_prominence == 0.4

    def test_hand_knuckle_validation_and_legacy(self):
        with pytest.raises(ValueError, match="knuckle_prominence"):
            Hand(side=BodySide.LEFT, knuckle_prominence=1.5)

        assert Hand(
            side=BodySide.LEFT, knuckle_prominence=0.9
        ).is_valid()

        # legacy intact
        with pytest.raises(ValueError, match="Hand length"):
            Hand(side=BodySide.LEFT, length=0.0)

    # --- HumanAnatomy end-to-end (3) ---

    def test_anatomy_limb_parity(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()
        assert (
            anatomy.arms.left.upper_arm.bicep_prominence == 0.5
        )
        assert (
            anatomy.arms.left.forearm.vascularity == 0.3
        )
        assert (
            anatomy.legs.left.ankle.malleolus_prominence == 0.5
        )
        assert (
            anatomy.arms.right.hand.knuckle_prominence == 0.4
        )

    def test_anatomy_serialization_limb_detail(self):
        data = HumanAnatomy().to_dict()

        assert (
            data["arms"]["left"]["upper_arm"][
                "bicep_prominence"
            ]
            == 0.5
        )
        assert (
            data["arms"]["left"]["forearm"]["vascularity"] == 0.3
        )
        assert (
            data["legs"]["left"]["ankle"]["malleolus_width"]
            == 1.5
        )
        assert (
            data["arms"]["right"]["hand"]["knuckle_prominence"]
            == 0.4
        )

    def test_segment_parameter_parity_upper_lower(self):
        # THE parity certification: thigh = upper_arm = 8,
        # lower_leg = forearm = 8 (constructor signature).
        import inspect

        thigh_params = set(
            inspect.signature(
                __import__(
                    "human.anatomy", fromlist=["Thigh"]
                ).Thigh.__init__
            ).parameters
        ) - {"self"}
        upper_arm_params = set(
            inspect.signature(UpperArm.__init__).parameters
        ) - {"self"}
        lower_leg_params = set(
            inspect.signature(
                __import__(
                    "human.anatomy", fromlist=["LowerLeg"]
                ).LowerLeg.__init__
            ).parameters
        ) - {"self"}
        forearm_params = set(
            inspect.signature(Forearm.__init__).parameters
        ) - {"self"}

        # H5-D-3: vascularity on all four limb segments and
        # flexor_definition completing Forearm — parity 8 -> 9.
        assert len(upper_arm_params) == len(thigh_params) == 9
        assert len(forearm_params) == len(lower_leg_params) == 9

    # --- export (2) ---

    def test_serialization_roundtrip_upper_limb(self):
        arm = UpperArm(bicep_prominence=0.8, width=10.5)
        data = arm.to_dict()

        assert data["bicep_prominence"] == 0.8
        assert data["width"] == 10.5
        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "upper_arm"

    def test_all_limb_components_valid(self):
        for component in (
            UpperArm(),
            Forearm(),
            Ankle(side=BodySide.LEFT),
            Hand(side=BodySide.LEFT),
        ):
            assert component.is_valid()
