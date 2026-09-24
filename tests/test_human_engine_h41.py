from __future__ import annotations

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.entity import Entity
from human.human import Human
from human.anatomy import (
    AnatomyComponent,
    BodyType,
    Height,
    HumanAnatomy,
    Proportions,
)


class TestHumanEngineH41(unittest.TestCase):

    def test_anatomy_component_inheritance(self):
        self.assertTrue(issubclass(AnatomyComponent, object))
        self.assertEqual(AnatomyComponent.component_type, "anatomy")

    def test_body_type_is_real_class(self):
        body_type = BodyType("athletic")

        self.assertIsInstance(body_type, AnatomyComponent)
        self.assertEqual(body_type.value, "athletic")
        body_type.validate()

    def test_height_is_real_class(self):
        height = Height(180)

        self.assertIsInstance(height, AnatomyComponent)
        self.assertEqual(height.centimeters, 180.0)
        height.validate()

    def test_proportions_are_real_class(self):
        proportions = Proportions(
            head_to_body=8.0,
            shoulder_width=1.1,
            torso_length=1.05,
            arm_length=1.02,
            leg_length=1.08,
        )

        self.assertIsInstance(proportions, AnatomyComponent)
        proportions.validate()

    def test_human_anatomy_composition(self):
        anatomy = HumanAnatomy(
            body_type=BodyType("slender"),
            height=Height(175),
            proportions=Proportions(),
        )

        self.assertIsInstance(anatomy, AnatomyComponent)
        self.assertIsInstance(anatomy.body_type, BodyType)
        self.assertIsInstance(anatomy.height, Height)
        self.assertIsInstance(anatomy.proportions, Proportions)

        anatomy.validate()

    def test_human_anatomy_serialization(self):
        anatomy = HumanAnatomy(
            body_type=BodyType("muscular"),
            height=Height(182),
        )

        data = anatomy.to_dict()

        self.assertEqual(data["component_type"], "human_anatomy")
        self.assertEqual(data["body_type"]["value"], "muscular")
        self.assertEqual(data["height"]["centimeters"], 182.0)
        self.assertIn("proportions", data)

    def test_invalid_height_is_rejected(self):
        with self.assertRaises(ValueError):
            Height(0)

    def test_invalid_body_type_is_rejected(self):
        with self.assertRaises(ValueError):
            BodyType("").validate()

    def test_invalid_proportions_are_rejected(self):
        with self.assertRaises(ValueError):
            Proportions(arm_length=0).validate()

    def test_human_is_still_entity(self):
        human = Human(name="Anatomy Test")

        self.assertIsInstance(human, Entity)

    def test_anatomy_can_be_attached_to_human(self):
        human = Human(name="Anatomy Test")
        anatomy = HumanAnatomy(
            body_type=BodyType("athletic"),
            height=Height(178),
        )

        human.register_component("anatomy", anatomy)

        self.assertTrue(human.has_component("anatomy"))
        self.assertIs(human.get_component("anatomy"), anatomy)

        human.validate()


if __name__ == "__main__":
    unittest.main(verbosity=2)
