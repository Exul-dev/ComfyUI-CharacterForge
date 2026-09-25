from __future__ import annotations
import unittest
from pathlib import Path
import sys

PROJECT_ROOT=Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0,str(PROJECT_ROOT))

from human.anatomy import AnatomyComponent,Back,Chest,RibCage,HumanAnatomy

class TestHumanEngineH47(unittest.TestCase):

    def test_chest(self):
        c=Chest(shape="broad")
        self.assertIsInstance(c,AnatomyComponent)
        self.assertEqual(c.shape,"broad")

    def test_ribcage(self):
        r=RibCage(shape="barrel")
        self.assertEqual(r.shape,"barrel")

    def test_back(self):
        b=Back(shape="athletic",muscularity=0.8)
        self.assertEqual(b.shape,"athletic")

    def test_human_anatomy_contains_h47(self):
        h=HumanAnatomy()
        self.assertIsInstance(h.chest,Chest)
        self.assertIsInstance(h.ribcage,RibCage)
        self.assertIsInstance(h.back,Back)

    def test_serialization(self):
        d=HumanAnatomy().to_dict()
        self.assertIn("chest",d)
        self.assertIn("ribcage",d)
        self.assertIn("back",d)

    def test_invalid_chest(self):
        with self.assertRaises(ValueError): Chest(width=0)

    def test_invalid_ribcage(self):
        with self.assertRaises(ValueError): RibCage(depth=0)

    def test_invalid_back(self):
        with self.assertRaises(ValueError): Back(muscularity=2)

    def test_validation(self):
        HumanAnatomy().validate()

if __name__=="__main__":
    unittest.main(verbosity=2)
