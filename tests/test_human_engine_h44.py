from __future__ import annotations

import sys
from pathlib import Path
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from human.anatomy import (
    BodySide,
    Finger,
    FingerType,
    Hand,
    Hands,
    Nail,
    Palm,
)


class TestHumanEngineH44(unittest.TestCase):

    def test_hands_have_left_and_right(self) -> None:
        hands = Hands()

        self.assertIsInstance(hands.left, Hand)
        self.assertIsInstance(hands.right, Hand)

        self.assertEqual(hands.left.side, BodySide.LEFT)
        self.assertEqual(hands.right.side, BodySide.RIGHT)

    def test_each_hand_has_five_fingers(self) -> None:
        hands = Hands()

        expected = {
            FingerType.THUMB,
            FingerType.INDEX,
            FingerType.MIDDLE,
            FingerType.RING,
            FingerType.LITTLE,
        }

        self.assertEqual(set(hands.left.fingers.keys()), expected)
        self.assertEqual(set(hands.right.fingers.keys()), expected)

    def test_finger_types_are_consistent(self) -> None:
        hands = Hands()

        for hand in (hands.left, hands.right):
            for finger_type, finger in hand.fingers.items():
                self.assertIsInstance(finger, Finger)
                self.assertEqual(finger.type, finger_type)

    def test_every_finger_has_a_nail(self) -> None:
        hands = Hands()

        for hand in (hands.left, hands.right):
            for finger in hand.fingers.values():
                self.assertIsInstance(finger.nail, Nail)
                self.assertEqual(finger.nail.component_type, "nail")

    def test_hands_contain_palms(self) -> None:
        hands = Hands()

        self.assertIsInstance(hands.left.palm, Palm)
        self.assertIsInstance(hands.right.palm, Palm)

    def test_hand_structure_is_valid(self) -> None:
        hands = Hands()

        self.assertTrue(hands.is_valid())
        self.assertTrue(hands.left.is_valid())
        self.assertTrue(hands.right.is_valid())

    def test_h44_preserves_h43_properties(self) -> None:
        hands = Hands(
            size="large",
            shape="long_fingered",
            finger_length=8.2,
            palm_width=9.0,
        )

        self.assertEqual(hands.size, "large")
        self.assertEqual(hands.shape, "long_fingered")
        self.assertEqual(hands.finger_length, 8.2)
        self.assertEqual(hands.palm_width, 9.0)

    def test_custom_nail_is_preserved(self) -> None:
        nail = Nail(
            shape="almond",
            length=1.8,
            gloss=0.8,
        )

        finger = Finger(
            type=FingerType.INDEX,
            nail=nail,
        )

        self.assertIs(finger.nail, nail)
        self.assertEqual(finger.nail.shape, "almond")
        self.assertEqual(finger.nail.length, 1.8)
        self.assertEqual(finger.nail.gloss, 0.8)

    def test_invalid_finger_type(self) -> None:
        with self.assertRaises(ValueError):
            Finger(type="index")  # type: ignore[arg-type]

    def test_invalid_nail_shape(self) -> None:
        with self.assertRaises(ValueError):
            Nail(shape="invalid")

    def test_invalid_hand_side(self) -> None:
        with self.assertRaises(ValueError):
            Hand(side="left")  # type: ignore[arg-type]

    def test_invalid_finger_length(self) -> None:
        with self.assertRaises(ValueError):
            Finger(length=0)

    def test_invalid_nail_length(self) -> None:
        with self.assertRaises(ValueError):
            Nail(length=0)

    def test_hand_requires_all_finger_types(self) -> None:
        fingers = {
            FingerType.THUMB: Finger(type=FingerType.THUMB),
        }

        with self.assertRaises(ValueError):
            Hand(fingers=fingers)

    def test_serialization_contains_h44_structure(self) -> None:
        hands = Hands()

        data = hands.to_dict()

        self.assertEqual(data["component_type"], "hands")
        self.assertIn("left", data)
        self.assertIn("right", data)

        self.assertIn("palm", data["left"])
        self.assertIn("fingers", data["left"])

        self.assertIn("palm", data["right"])
        self.assertIn("fingers", data["right"])

        left_index = data["left"]["fingers"]["index"]

        self.assertEqual(left_index["type"], "index")
        self.assertIn("nail", left_index)
        self.assertEqual(left_index["nail"]["component_type"], "nail")

    def test_serialization_preserves_legacy_properties(self) -> None:
        hands = Hands(
            size="large",
            shape="long_fingered",
            finger_length=8.2,
            palm_width=9.0,
        )

        data = hands.to_dict()

        self.assertEqual(data["size"], "large")
        self.assertEqual(data["shape"], "long_fingered")
        self.assertEqual(data["finger_length"], 8.2)
        self.assertEqual(data["palm_width"], 9.0)


if __name__ == "__main__":
    unittest.main()
