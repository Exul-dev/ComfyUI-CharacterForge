from __future__ import annotations

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from human.anatomy import (
    AnatomyComponent,
    BodyFat,
    BodyType,
    Height,
    HumanAnatomy,
    Musculature,
    Proportions,
    Shoulders,
    Torso,
)


class TestHumanEngineH42(unittest.TestCase):

    def test_musculature_is_real_class(self):
        musculature = Musculature(
            level="high",
            definition=0.8,
            distribution="upper_body",
        )

        self.assertIsInstance(musculature, AnatomyComponent)
        self.assertEqual(musculature.level, "high")
        musculature.validate()

    def test_body_fat_is_real_class(self):
        body_fat = BodyFat(
            percentage=15,
            distribution="lower_body",
        )

        self.assertIsInstance(body_fat, AnatomyComponent)
        self.assertEqual(body_fat.percentage, 15.0)
        body_fat.validate()

    def test_shoulders_are_real_class(self):
        shoulders = Shoulders(
            width=1.2,
            shape="broad",
            slope="sloped",
        )

        self.assertIsInstance(shoulders, AnatomyComponent)
        self.assertEqual(shoulders.shape, "broad")
        shoulders.validate()

    def test_torso_is_real_class(self):
        torso = Torso(
            length=1.1,
            width=1.2,
            depth=1.05,
            shape="v_shape",
        )

        self.assertIsInstance(torso, AnatomyComponent)
        self.assertEqual(torso.shape, "v_shape")
        torso.validate()

    def test_human_anatomy_contains_h42_components(self):
        anatomy = HumanAnatomy(
            body_type=BodyType("athletic"),
            height=Height(180),
            proportions=Proportions(),
            musculature=Musculature("high"),
            body_fat=BodyFat(14),
            shoulders=Shoulders(width=1.2, shape="broad"),
            torso=Torso(shape="v_shape"),
        )

        self.assertIsInstance(anatomy.musculature, Musculature)
        self.assertIsInstance(anatomy.body_fat, BodyFat)
        self.assertIsInstance(anatomy.shoulders, Shoulders)
        self.assertIsInstance(anatomy.torso, Torso)

        anatomy.validate()

    def test_human_anatomy_serializes_h42_components(self):
        anatomy = HumanAnatomy(
            musculature=Musculature("high"),
            body_fat=BodyFat(12),
            shoulders=Shoulders(shape="broad"),
            torso=Torso(shape="v_shape"),
        )

        data = anatomy.to_dict()

        self.assertIn("musculature", data)
        self.assertIn("body_fat", data)
        self.assertIn("shoulders", data)
        self.assertIn("torso", data)

        self.assertEqual(data["musculature"]["level"], "high")
        self.assertEqual(data["body_fat"]["percentage"], 12.0)
        self.assertEqual(data["shoulders"]["shape"], "broad")
        self.assertEqual(data["torso"]["shape"], "v_shape")

    def test_invalid_musculature_level_is_rejected(self):
        with self.assertRaises(ValueError):
            Musculature("invalid")

    def test_invalid_musculature_definition_is_rejected(self):
        with self.assertRaises(ValueError):
            Musculature(definition=1.1)

    def test_invalid_body_fat_is_rejected(self):
        with self.assertRaises(ValueError):
            BodyFat(-1)

        with self.assertRaises(ValueError):
            BodyFat(101)

    def test_invalid_shoulders_are_rejected(self):
        with self.assertRaises(ValueError):
            Shoulders(width=0)

        with self.assertRaises(ValueError):
            Shoulders(shape="invalid")

    def test_invalid_torso_is_rejected(self):
        with self.assertRaises(ValueError):
            Torso(length=0)

        with self.assertRaises(ValueError):
            Torso(shape="invalid")


if __name__ == "__main__":
    unittest.main(verbosity=2)
