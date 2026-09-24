from __future__ import annotations

import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from human.anatomy import AnatomyComponent, HumanAnatomy, Neck


class TestHumanEngineH46(unittest.TestCase):

    def test_neck_is_real_component(self) -> None:
        neck = Neck(
            length=12.0,
            circumference=38.0,
            width=11.0,
            depth=9.0,
            shape="muscular",
        )

        self.assertIsInstance(neck, AnatomyComponent)
        self.assertEqual(neck.component_type, "neck")
        self.assertEqual(neck.length, 12.0)
        self.assertEqual(neck.circumference, 38.0)
        self.assertEqual(neck.width, 11.0)
        self.assertEqual(neck.depth, 9.0)
        self.assertEqual(neck.shape, "muscular")
        self.assertTrue(neck.is_valid())

    def test_default_neck_is_valid(self) -> None:
        neck = Neck()

        self.assertEqual(neck.shape, "average")
        self.assertTrue(neck.is_valid())

    def test_invalid_neck_length_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Neck(length=0)

    def test_invalid_neck_circumference_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Neck(circumference=0)

    def test_invalid_neck_width_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Neck(width=0)

    def test_invalid_neck_depth_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Neck(depth=0)

    def test_invalid_neck_shape_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Neck(shape="invalid")

    def test_neck_serialization(self) -> None:
        neck = Neck(
            length=12.0,
            circumference=38.0,
            width=11.0,
            depth=9.0,
            shape="muscular",
        )

        data = neck.to_dict()

        self.assertEqual(data["component_type"], "neck")
        self.assertEqual(data["length"], 12.0)
        self.assertEqual(data["circumference"], 38.0)
        self.assertEqual(data["width"], 11.0)
        self.assertEqual(data["depth"], 9.0)
        self.assertEqual(data["shape"], "muscular")

    def test_human_anatomy_contains_neck(self) -> None:
        anatomy = HumanAnatomy(
            neck=Neck(
                length=12.0,
                circumference=38.0,
                width=11.0,
                depth=9.0,
                shape="muscular",
            )
        )

        self.assertIsInstance(anatomy.neck, Neck)
        self.assertEqual(anatomy.neck.length, 12.0)
        self.assertEqual(anatomy.neck.shape, "muscular")
        anatomy.validate()

    def test_human_anatomy_serializes_neck(self) -> None:
        anatomy = HumanAnatomy(
            neck=Neck(shape="robust")
        )

        data = anatomy.to_dict()

        self.assertIn("neck", data)
        self.assertEqual(data["neck"]["component_type"], "neck")
        self.assertEqual(data["neck"]["shape"], "robust")


if __name__ == "__main__":
    unittest.main(verbosity=2)
