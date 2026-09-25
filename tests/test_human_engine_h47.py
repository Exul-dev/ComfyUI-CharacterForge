from __future__ import annotations

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from human.anatomy import (
    AnatomyComponent,
    Back,
    Chest,
    HumanAnatomy,
    RibCage,
)


class TestHumanEngineH47(unittest.TestCase):

    def test_chest(self):
        chest = Chest(shape="broad")
        self.assertIsInstance(chest, AnatomyComponent)
        self.assertEqual(chest.shape, "broad")

    def test_ribcage(self):
        ribcage = RibCage(shape="barrel")
        self.assertEqual(ribcage.shape, "barrel")

    def test_back(self):
        back = Back(shape="athletic", muscularity=0.8)
        self.assertEqual(back.shape, "athletic")

    def test_human_anatomy_contains_h47(self):
        anatomy = HumanAnatomy()

        self.assertIsInstance(anatomy.chest, Chest)
        self.assertIsInstance(anatomy.ribcage, RibCage)
        self.assertIsInstance(anatomy.back, Back)

    def test_serialization(self):
        data = HumanAnatomy().to_dict()

        self.assertIn("chest", data)
        self.assertIn("ribcage", data)
        self.assertIn("back", data)

    def test_invalid_chest(self):
        with self.assertRaises(ValueError):
            Chest(width=0)

    def test_invalid_ribcage(self):
        with self.assertRaises(ValueError):
            RibCage(depth=0)

    def test_invalid_back(self):
        with self.assertRaises(ValueError):
            Back(muscularity=2)

    def test_validation(self):
        HumanAnatomy().validate()


if __name__ == "__main__":
    unittest.main(verbosity=2)
