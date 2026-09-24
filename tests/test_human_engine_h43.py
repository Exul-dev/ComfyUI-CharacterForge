from __future__ import annotations

import sys
from pathlib import Path
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from human.anatomy import (
    Arms,
    Forearm,
    Hands,
    HumanAnatomy,
    UpperArm,
)


class TestHumanEngineH43(unittest.TestCase):

    def test_upper_arm_is_real_component(self) -> None:
        upper_arm = UpperArm(
            length=31.0,
            circumference=30.0,
            shape="athletic",
        )

        self.assertEqual(upper_arm.component_type, "upper_arm")
        self.assertEqual(upper_arm.length, 31.0)
        self.assertEqual(upper_arm.circumference, 30.0)
        self.assertEqual(upper_arm.shape, "athletic")
        self.assertTrue(upper_arm.is_valid())

    def test_forearm_is_real_component(self) -> None:
        forearm = Forearm(
            length=27.0,
            circumference=25.0,
            shape="muscular",
        )

        self.assertEqual(forearm.component_type, "forearm")
        self.assertEqual(forearm.length, 27.0)
        self.assertEqual(forearm.circumference, 25.0)
        self.assertEqual(forearm.shape, "muscular")
        self.assertTrue(forearm.is_valid())

    def test_hands_are_real_component(self) -> None:
        hands = Hands(
            size="large",
            shape="long_fingered",
            finger_length=8.2,
            palm_width=9.0,
        )

        self.assertEqual(hands.component_type, "hands")
        self.assertEqual(hands.size, "large")
        self.assertEqual(hands.shape, "long_fingered")
        self.assertEqual(hands.finger_length, 8.2)
        self.assertEqual(hands.palm_width, 9.0)
        self.assertTrue(hands.is_valid())

    def test_arms_contains_upper_limbs(self) -> None:
        arms = Arms()

        self.assertIsInstance(arms.upper_arm, UpperArm)
        self.assertIsInstance(arms.forearm, Forearm)
        self.assertIsInstance(arms.hands, Hands)
        self.assertTrue(arms.is_valid())

    def test_human_anatomy_contains_arms(self) -> None:
        anatomy = HumanAnatomy()

        self.assertIsInstance(anatomy.arms, Arms)
        self.assertIsInstance(anatomy.arms.upper_arm, UpperArm)
        self.assertIsInstance(anatomy.arms.forearm, Forearm)
        self.assertIsInstance(anatomy.arms.hands, Hands)
        self.assertTrue(anatomy.is_valid())

    def test_arms_serialization(self) -> None:
        arms = Arms(
            upper_arm=UpperArm(length=32.0),
            forearm=Forearm(length=28.0),
            hands=Hands(size="large"),
        )

        data = arms.to_dict()

        self.assertEqual(data["component_type"], "arms")
        self.assertEqual(data["upper_arm"]["length"], 32.0)
        self.assertEqual(data["forearm"]["length"], 28.0)
        self.assertEqual(data["hands"]["size"], "large")

    def test_invalid_upper_arm(self) -> None:
        with self.assertRaises(ValueError):
            UpperArm(length=0)

    def test_invalid_forearm(self) -> None:
        with self.assertRaises(ValueError):
            Forearm(circumference=0)

    def test_invalid_hands(self) -> None:
        with self.assertRaises(ValueError):
            Hands(finger_length=-1)

    def test_invalid_upper_arm_shape(self) -> None:
        with self.assertRaises(ValueError):
            UpperArm(shape="invalid")

    def test_invalid_hand_shape(self) -> None:
        with self.assertRaises(ValueError):
            Hands(shape="invalid")


if __name__ == "__main__":
    unittest.main()
