"""
CharacterForge Domain Core tests.
"""

import json
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core import (
    Entity,
    Identity,
    Metadata,
    Transformation,
    Variant,
)


class TestDomainCore(unittest.TestCase):

    def test_identity_creation(self):
        identity = Identity(
            name="Elena",
            entity_type="human",
        )

        self.assertTrue(identity.identity_id.startswith("identity_"))
        self.assertEqual(identity.name, "Elena")
        self.assertEqual(identity.entity_type, "human")
        self.assertEqual(identity.version, 1)

    def test_state_belongs_to_entity(self):
        entity = Entity(
            identity=Identity(
                name="Elena",
                entity_type="human",
            )
        )

        self.assertIsNotNone(entity.state)
        self.assertEqual(entity.state.entity_id, entity.entity_id)

    def test_variant_registration(self):
        entity = Entity(
            identity=Identity(
                name="Elena",
                entity_type="human",
            )
        )

        variant = Variant(
            source_entity_id=entity.entity_id,
            name="Summer Outfit",
            changes={
                "clothing.color": "white",
            },
        )

        entity.add_variant(variant)

        self.assertIn(variant.variant_id, entity.variants)
        self.assertIs(entity.get_variant(variant.variant_id), variant)
        self.assertEqual(
            variant.source_entity_id,
            entity.entity_id,
        )

    def test_invalid_variant_source_is_rejected(self):
        entity = Entity()

        variant = Variant(
            source_entity_id="entity_different",
            name="Invalid",
        )

        with self.assertRaises(ValueError):
            entity.add_variant(variant)

    def test_duplicate_variant_is_rejected(self):
        entity = Entity()
        variant = Variant()

        entity.add_variant(variant)

        with self.assertRaises(ValueError):
            entity.add_variant(variant)

    def test_transformation_creation(self):
        entity = Entity()

        transformation = Transformation(
            source_entity_id=entity.entity_id,
            source_state_id=entity.state.state_id,
            target_state_id="state_target",
            operations=[
                {
                    "path": "hair.length",
                    "from": "long",
                    "to": "short",
                }
            ],
            reversible=True,
            preserves_identity=True,
        )

        self.assertEqual(
            transformation.source_entity_id,
            entity.entity_id,
        )
        self.assertEqual(
            transformation.source_state_id,
            entity.state.state_id,
        )
        self.assertEqual(
            transformation.target_state_id,
            "state_target",
        )
        self.assertTrue(transformation.reversible)
        self.assertTrue(transformation.preserves_identity)

    def test_metadata_creation(self):
        metadata = Metadata(
            source="test",
            tags=["domain-core"],
        )

        self.assertEqual(metadata.schema_version, "1.0")
        self.assertEqual(metadata.source, "test")
        self.assertEqual(metadata.tags, ["domain-core"])

    def test_entity_serialization(self):
        entity = Entity(
            identity=Identity(
                name="Elena",
                entity_type="human",
                anchors={
                    "face_structure": "oval",
                },
            ),
            metadata=Metadata(
                source="test",
            ),
        )

        entity.state.properties["age"] = 30

        variant = Variant(
            source_entity_id=entity.entity_id,
            name="Summer Outfit",
            changes={
                "clothing.color": "white",
            },
        )

        entity.add_variant(variant)

        serialized = entity.to_dict()

        json.dumps(serialized, ensure_ascii=False)

        self.assertEqual(
            serialized["entity_id"],
            entity.entity_id,
        )
        self.assertEqual(
            serialized["identity"]["name"],
            "Elena",
        )
        self.assertEqual(
            serialized["identity"]["anchors"]["face_structure"],
            "oval",
        )
        self.assertEqual(
            serialized["state"]["entity_id"],
            entity.entity_id,
        )
        self.assertEqual(
            serialized["state"]["properties"]["age"],
            30,
        )
        self.assertIn(
            variant.variant_id,
            serialized["variants"],
        )
        self.assertEqual(
            serialized["metadata"]["source"],
            "test",
        )

    def test_identity_survives_state_changes(self):
        entity = Entity(
            identity=Identity(
                name="Elena",
                entity_type="human",
            )
        )

        identity_id = entity.identity.identity_id

        entity.state.properties["hair"] = {
            "length": "long",
            "color": "black",
        }

        entity.state.properties["clothing"] = {
            "type": "dress",
            "color": "blue",
        }

        self.assertEqual(
            entity.identity.identity_id,
            identity_id,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
