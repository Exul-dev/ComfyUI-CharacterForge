from __future__ import annotations

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.entity import Entity
from human import Human
from human.identity import (
    IdentityAnchor,
    DistinctiveTrait,
)


class TestHumanEngineH2(unittest.TestCase):

    def test_human_is_entity(self):
        human = Human(name="Test Human")

        self.assertIsInstance(human, Entity)
        self.assertEqual(
            human.identity.entity_type,
            "human",
        )

    def test_human_has_real_identity_component(self):
        human = Human(name="Test Human")

        self.assertTrue(
            human.has_component("human_identity")
        )

        self.assertIs(
            human.human_identity,
            human.get_component("human_identity"),
        )

    def test_identity_anchor_is_real_class(self):
        anchor = IdentityAnchor(
            "jaw_shape",
            "strong",
            weight=1.0,
        )

        self.assertEqual(anchor.name, "jaw_shape")
        self.assertEqual(anchor.value, "strong")
        self.assertTrue(anchor.is_valid())

    def test_distinctive_trait_is_real_class(self):
        trait = DistinctiveTrait(
            "scar_left_cheek",
            "thin_vertical_scar",
        )

        self.assertEqual(
            trait.name,
            "scar_left_cheek",
        )

        self.assertEqual(
            trait.value,
            "thin_vertical_scar",
        )

        self.assertTrue(trait.is_valid())

    def test_human_identity_composition(self):
        human = Human(name="Massimo")

        anchor = IdentityAnchor(
            "eye_spacing",
            "medium",
        )

        trait = DistinctiveTrait(
            "facial_scar",
            "left_cheek",
        )

        human.human_identity.anchors.add(anchor)
        human.human_identity.distinctive_traits.add(trait)

        self.assertTrue(
            human.human_identity.anchors.contains(
                "eye_spacing"
            )
        )

        self.assertTrue(
            human.human_identity.distinctive_traits.contains(
                "facial_scar"
            )
        )

    def test_human_serialization_contains_human_engine(self):
        human = Human(name="Test Human")

        data = human.to_dict()

        self.assertIn("human_engine", data)

        self.assertEqual(
            data["human_engine"]["engine"],
            "human",
        )

        self.assertIn(
            "human_identity",
            data["human_engine"]["components"],
        )

    def test_human_validation(self):
        human = Human(name="Valid Human")

        human.human_identity.anchors.add(
            IdentityAnchor(
                "nose_shape",
                "straight",
            )
        )

        human.validate()

    def test_inheritance_chain(self):
        human = Human()

        mro = Human.__mro__

        self.assertIn(Entity, mro)
        self.assertIn(object, mro)

        self.assertIsInstance(human, Human)
        self.assertIsInstance(human, Entity)


if __name__ == "__main__":
    unittest.main(verbosity=2)
