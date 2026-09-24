from __future__ import annotations

import sys
from pathlib import Path
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from human.anatomy import BodySide, Shoulder, Shoulders


class TestHumanEngineH45(unittest.TestCase):

    def test_shoulder_is_real_component(self) -> None:
        shoulder = Shoulder(
            side=BodySide.LEFT,
            width=15.0,
            height=13.0,
            depth=6.0,
            shape="athletic",
        )

        self.assertEqual(shoulder.component_type, "shoulder")
        self.assertEqual(shoulder.side, BodySide.LEFT)
        self.assertEqual(shoulder.width, 15.0)
        self.assertEqual(shoulder.height, 13.0)
        self.assertEqual(shoulder.depth, 6.0)
        self.assertEqual(shoulder.shape, "athletic")
        self.assertTrue(shoulder.is_valid())

    def test_shoulders_are_bilateral(self) -> None:
        shoulders = Shoulders()

        self.assertIsInstance(shoulders.left, Shoulder)
        self.assertIsInstance(shoulders.right, Shoulder)

        self.assertEqual(shoulders.left.side, BodySide.LEFT)
        self.assertEqual(shoulders.right.side, BodySide.RIGHT)

        self.assertTrue(shoulders.is_valid())

    def test_custom_shoulders_are_preserved(self) -> None:
        left = Shoulder(
            side=BodySide.LEFT,
            width=16.0,
            muscularity=0.8,
        )

        right = Shoulder(
            side=BodySide.RIGHT,
            width=15.5,
            muscularity=0.7,
        )

        shoulders = Shoulders(
            left=left,
            right=right,
        )

        self.assertIs(shoulders.left, left)
        self.assertIs(shoulders.right, right)

        self.assertEqual(shoulders.left.width, 16.0)
        self.assertEqual(shoulders.right.width, 15.5)

    def test_invalid_shoulder_side(self) -> None:
        with self.assertRaises(ValueError):
            Shoulder(side="left")  # type: ignore[arg-type]

    def test_invalid_shoulder_width(self) -> None:
        with self.assertRaises(ValueError):
            Shoulder(width=0)

    def test_invalid_shoulder_height(self) -> None:
        with self.assertRaises(ValueError):
            Shoulder(height=0)

    def test_invalid_shoulder_depth(self) -> None:
        with self.assertRaises(ValueError):
            Shoulder(depth=0)

    def test_invalid_shoulder_shape(self) -> None:
        with self.assertRaises(ValueError):
            Shoulder(shape="invalid")

    def test_invalid_shoulder_slope(self) -> None:
        with self.assertRaises(ValueError):
            Shoulder(slope=1.1)

    def test_invalid_shoulder_muscularity(self) -> None:
        with self.assertRaises(ValueError):
            Shoulder(muscularity=-0.1)

    def test_invalid_bilateral_configuration(self) -> None:
        with self.assertRaises(ValueError):
            Shoulders(
                left=Shoulder(side=BodySide.RIGHT),
            )

    def test_serialization(self) -> None:
        shoulders = Shoulders()

        data = shoulders.to_dict()

        self.assertEqual(data["component_type"], "shoulders")
        self.assertIn("left", data)
        self.assertIn("right", data)

        self.assertEqual(data["left"]["side"], "left")
        self.assertEqual(data["right"]["side"], "right")
        self.assertEqual(data["left"]["component_type"], "shoulder")
        self.assertEqual(data["right"]["component_type"], "shoulder")


if __name__ == "__main__":
    unittest.main()
