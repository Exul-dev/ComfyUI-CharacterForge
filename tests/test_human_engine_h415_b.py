from __future__ import annotations

import pytest

import human.anatomy as anatomy_module
from human.anatomy import (
    Ankle,
    BodySide,
    Foot,
    Knee,
    Leg,
    Legs,
    LowerLeg,
    Pelvis,
    Thigh,
    Toe,
    ToeType,
)
from human.anatomy.anatomy_component import AnatomyComponent
from human.anatomy.body_type import BodyType, Height, Proportions
from human.anatomy.human_anatomy import HumanAnatomy


class TestHumanEngineH415B:

    # --- ToeType (2) ---

    def test_toe_type_values(self):
        assert ToeType.HALLUX.value == "hallux"
        assert ToeType.SECOND.value == "second"
        assert ToeType.THIRD.value == "third"
        assert ToeType.FOURTH.value == "fourth"
        assert ToeType.FIFTH.value == "fifth"
        assert len(list(ToeType)) == 5

    def test_toe_type_distinct_from_finger_type(self):
        from human.anatomy import FingerType

        toe_values = {item.value for item in ToeType}
        finger_values = {item.value for item in FingerType}

        assert toe_values.isdisjoint(finger_values)

    # --- Toe (5) ---

    def test_toe_defaults_with_nail(self):
        toe = Toe()

        assert toe.is_valid()
        assert toe.component_type == "toe"
        assert toe.type is ToeType.HALLUX
        assert toe.length == 2.7
        assert toe.width == 1.5
        assert toe.thickness == 1.3
        assert toe.nail is not None
        assert toe.nail.component_type == "nail"

    def test_toe_rejects_invalid_type(self):
        with pytest.raises(ValueError, match="Toe type"):
            Toe(type="hallux")

        with pytest.raises(ValueError, match="Toe type"):
            Toe(type=None)

    def test_toe_rejects_non_positive_dimensions(self):
        with pytest.raises(ValueError, match="Toe length"):
            Toe(length=0.0)

        with pytest.raises(ValueError, match="Toe width"):
            Toe(width=-1.0)

        with pytest.raises(ValueError, match="Toe thickness"):
            Toe(thickness=0.0)

    def test_toe_curvature_and_orientation_ranges(self):
        assert Toe(curvature=0.0).is_valid()
        assert Toe(curvature=1.0).is_valid()

        with pytest.raises(ValueError, match="Toe curvature"):
            Toe(curvature=-0.1)

        with pytest.raises(ValueError, match="orientation"):
            Toe(orientation=90.1)

    def test_toe_serialization_and_mutation(self):
        toe = Toe(type=ToeType.SECOND)

        data = toe.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "toe"
        assert data["type"] == "second"
        assert data["nail"]["component_type"] == "nail"

        toe.length = -1.0
        assert not toe.is_valid()

    # --- Foot (8) ---

    def test_foot_defaults(self):
        foot = Foot()

        assert foot.is_valid()
        assert foot.component_type == "foot"
        assert foot.side is BodySide.RIGHT
        assert foot.length == 26.0
        assert foot.width == 9.5
        assert foot.thickness == 3.5
        assert foot.shape == "average"
        assert foot.arch == 0.5
        assert foot.heel_width == 6.0
        assert foot.ball_width == 9.0

    def test_foot_default_toe_set_complete_and_descending(self):
        foot = Foot()

        assert set(foot.toes.keys()) == set(ToeType)

        lengths = [foot.toes[item].length for item in ToeType]
        assert lengths == [2.7, 2.5, 2.3, 2.2, 2.0]

    def test_foot_rejects_invalid_side(self):
        with pytest.raises(ValueError, match="side"):
            Foot(side="left")

        with pytest.raises(ValueError, match="side"):
            Foot(side=None)

    def test_foot_rejects_invalid_shape(self):
        with pytest.raises(ValueError, match="Invalid foot shape"):
            Foot(shape="gigantic")

    def test_foot_arch_and_width_ranges(self):
        assert Foot(arch=0.0).is_valid()
        assert Foot(arch=1.0).is_valid()

        with pytest.raises(ValueError, match="arch"):
            Foot(arch=-0.1)

        with pytest.raises(ValueError, match="heel width"):
            Foot(heel_width=0.0)

        with pytest.raises(ValueError, match="ball width"):
            Foot(ball_width=-1.0)

        with pytest.raises(ValueError, match="Foot length"):
            Foot(length=0.0)

    def test_foot_requires_all_toe_types(self):
        partial = {
            ToeType.HALLUX: Toe(type=ToeType.HALLUX),
            ToeType.SECOND: Toe(type=ToeType.SECOND),
            ToeType.THIRD: Toe(type=ToeType.THIRD),
            ToeType.FOURTH: Toe(type=ToeType.FOURTH),
        }

        with pytest.raises(ValueError, match="exactly one toe"):
            Foot(toes=partial)

    def test_foot_toe_key_value_consistency(self):
        mismatched = {
            ToeType.HALLUX: Toe(type=ToeType.SECOND),
            ToeType.SECOND: Toe(type=ToeType.SECOND),
            ToeType.THIRD: Toe(type=ToeType.THIRD),
            ToeType.FOURTH: Toe(type=ToeType.FOURTH),
            ToeType.FIFTH: Toe(type=ToeType.FIFTH),
        }

        with pytest.raises(ValueError, match="must refer"):
            Foot(toes=mismatched)

    def test_foot_serialization_and_mutation(self):
        foot = Foot(side=BodySide.LEFT)

        data = foot.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["side"] == "left"
        assert data["arch"] == 0.5
        assert data["toes"]["hallux"]["type"] == "hallux"

        foot.arch = 5.0
        assert not foot.is_valid()

    # --- Leg (7) ---

    def test_leg_defaults_side_matching(self):
        left = Leg(side=BodySide.LEFT)
        right = Leg(side=BodySide.RIGHT)

        assert left.is_valid()
        assert left.side is BodySide.LEFT
        assert left.knee.side is BodySide.LEFT
        assert left.ankle.side is BodySide.LEFT
        assert left.foot.side is BodySide.LEFT

        assert right.is_valid()
        assert right.knee.side is BodySide.RIGHT
        assert right.ankle.side is BodySide.RIGHT
        assert right.foot.side is BodySide.RIGHT

        assert left.thigh.component_type == "thigh"
        assert left.lower_leg.component_type == "lower_leg"

    def test_leg_rejects_invalid_side(self):
        # Sub-components passed explicitly so the Leg side check
        # fires before any eager Knee/Ankle/Foot construction.
        with pytest.raises(ValueError, match="Leg side"):
            Leg(
                side="left",
                thigh=Thigh(),
                knee=Knee(),
                lower_leg=LowerLeg(),
                ankle=Ankle(),
                foot=Foot(),
            )

    def test_leg_rejects_mismatched_knee_side(self):
        with pytest.raises(ValueError, match="knee side must match"):
            Leg(
                side=BodySide.LEFT,
                knee=Knee(side=BodySide.RIGHT),
            )

    def test_leg_rejects_mismatched_ankle_side(self):
        with pytest.raises(ValueError, match="ankle side must match"):
            Leg(
                side=BodySide.LEFT,
                ankle=Ankle(side=BodySide.RIGHT),
            )

    def test_leg_rejects_mismatched_foot_side(self):
        with pytest.raises(ValueError, match="foot side must match"):
            Leg(
                side=BodySide.LEFT,
                foot=Foot(side=BodySide.RIGHT),
            )

    def test_leg_explicit_components_honored(self):
        leg = Leg(
            side=BodySide.RIGHT,
            thigh=Thigh(shape="muscular", length=46.0),
            lower_leg=LowerLeg(shape="athletic"),
        )

        assert leg.thigh.shape == "muscular"
        assert leg.thigh.length == 46.0
        assert leg.lower_leg.shape == "athletic"
        assert leg.knee.side is BodySide.RIGHT

    def test_leg_serialization_and_mutation(self):
        leg = Leg(side=BodySide.LEFT)

        data = leg.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["side"] == "left"
        assert data["knee"]["side"] == "left"
        assert data["foot"]["side"] == "left"
        assert data["foot"]["toes"]["hallux"]["type"] == "hallux"

        leg.knee.flexion = 999.0
        assert not leg.is_valid()

    # --- Legs (4) ---

    def test_legs_defaults_bilateral(self):
        legs = Legs()

        assert legs.is_valid()
        assert legs.component_type == "legs"
        assert legs.left.side is BodySide.LEFT
        assert legs.right.side is BodySide.RIGHT

    def test_legs_rejects_wrong_sides(self):
        with pytest.raises(ValueError, match="Legs.left"):
            Legs(left=Leg(side=BodySide.RIGHT))

        with pytest.raises(ValueError, match="Legs.right"):
            Legs(right=Leg(side=BodySide.LEFT))

    def test_legs_asymmetry_is_representable(self):
        legs = Legs(
            left=Leg(
                side=BodySide.LEFT,
                thigh=Thigh(shape="muscular", circumference=60.0),
            ),
            right=Leg(
                side=BodySide.RIGHT,
                thigh=Thigh(shape="slender", circumference=50.0),
            ),
        )

        assert legs.is_valid()
        assert legs.left.thigh.shape == "muscular"
        assert legs.right.thigh.shape == "slender"
        assert legs.left.thigh.circumference == 60.0
        assert legs.right.thigh.circumference == 50.0

    def test_legs_serialization(self):
        legs = Legs()

        data = legs.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["left"]["side"] == "left"
        assert data["right"]["side"] == "right"
        assert "foot" in data["left"]

    # --- HumanAnatomy integration (5) ---

    def test_human_anatomy_defaults_include_lower_body(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()
        assert isinstance(anatomy.pelvis, Pelvis)
        assert isinstance(anatomy.legs, Legs)

        hallux = anatomy.legs.left.foot.toes[ToeType.HALLUX]
        assert hallux.length == 2.7

    def test_human_anatomy_custom_lower_body(self):
        anatomy = HumanAnatomy(
            pelvis=Pelvis(width=40.0, shape="broad"),
            legs=Legs(
                left=Leg(
                    side=BodySide.LEFT,
                    thigh=Thigh(length=48.0),
                )
            ),
        )

        assert anatomy.pelvis.width == 40.0
        assert anatomy.pelvis.shape == "broad"
        assert anatomy.legs.left.thigh.length == 48.0
        assert anatomy.is_valid()

    def test_human_anatomy_serialization_includes_lower_body(self):
        anatomy = HumanAnatomy()

        data = anatomy.to_dict()

        assert "pelvis" in data
        assert "legs" in data
        assert data["pelvis"]["component_type"] == "pelvis"
        assert data["legs"]["component_type"] == "legs"
        assert (
            data["legs"]["left"]["foot"]["toes"]["hallux"]["type"]
            == "hallux"
        )

    def test_human_anatomy_backward_compatible_constructor(self):
        # The pre-H4.15 call style (body_type/height/proportions)
        # must keep working: pelvis and legs default in silently.
        anatomy = HumanAnatomy(
            body_type=BodyType("slender"),
            height=Height(175),
            proportions=Proportions(),
        )

        assert anatomy.is_valid()
        assert anatomy.pelvis is not None
        assert anatomy.legs is not None

    def test_human_anatomy_mutation_invalidates(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()

        anatomy.legs.left.knee.flexion = 999.0
        assert not anatomy.is_valid()

    # --- package exports (1) ---

    def test_package_exports_h415b(self):
        for name in ("ToeType", "Toe", "Foot", "Leg", "Legs"):
            assert hasattr(anatomy_module, name)
            assert name in anatomy_module.__all__

        for component in (
            Toe(),
            Foot(),
            Leg(side=BodySide.LEFT),
            Legs(),
        ):
            assert isinstance(component, AnatomyComponent)
            assert component.is_valid()