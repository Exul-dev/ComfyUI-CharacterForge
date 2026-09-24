"""
CharacterForge Domain Core schema, validation and serialization tests.
"""

import json
import sys
import unittest

PROJECT_ROOT = r"D:\AVVIO PULITO di ComfyUI\ComfyUI\custom_nodes\ComfyUI-CharacterForge"

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from core import (
    Entity,
    Identity,
    Metadata,
    ValidationError,
    Variant,
    entity_from_dict,
    entity_from_json,
    entity_to_dict,
    entity_to_json,
    validate_entity,
)


class TestDomainCoreSerialization(unittest.TestCase):

    def create_entity(self):
        entity = Entity(
            identity=Identity(
                name="Elena",
                entity_type="human",
                anchors={
                    "face_structure": "oval",
                    "eye_color": "green",
                },
                identity_properties={
                    "character_role": "protagonist",
                },
            ),
            metadata=Metadata(
                source="test",
                tags=["human", "test"],
            ),
        )

        entity.state.properties["age"] = 30
        entity.state.properties["hair"] = {
            "color": "black",
            "length": "long",
        }

        variant = Variant(
            source_entity_id=entity.entity_id,
            name="Summer Outfit",
            changes={
                "clothing.color": "white",
            },
        )

        entity.add_variant(variant)

        return entity

    def test_entity_to_dict_is_valid(self):
        entity = self.create_entity()

        data = entity_to_dict(entity)

        self.assertIsInstance(data, dict)
        self.assertTrue(data["entity_id"].startswith("entity_"))
        self.assertTrue(data["variants"])
        self.assertTrue(data["metadata"]["schema_version"])

        validate_entity(data)

    def test_entity_json_round_trip(self):
        entity = self.create_entity()

        payload = entity_to_json(entity)
        reconstructed = entity_from_json(payload)

        self.assertEqual(
            reconstructed.entity_id,
            entity.entity_id,
        )

        self.assertEqual(
            reconstructed.identity.identity_id,
            entity.identity.identity_id,
        )

        self.assertEqual(
            reconstructed.identity.name,
            "Elena",
        )

        self.assertEqual(
            reconstructed.state.properties["age"],
            30,
        )

        self.assertEqual(
            reconstructed.state.properties["hair"]["color"],
            "black",
        )

        self.assertEqual(
            len(reconstructed.variants),
            1,
        )

        self.assertEqual(
            reconstructed.metadata.tags,
            ["human", "test"],
        )

    def test_entity_dict_round_trip(self):
        entity = self.create_entity()

        data = entity_to_dict(entity)
        reconstructed = entity_from_dict(data)

        self.assertEqual(
            entity_to_dict(reconstructed),
            data,
        )

    def test_json_is_valid_json(self):
        entity = self.create_entity()

        payload = entity_to_json(entity)
        decoded = json.loads(payload)

        self.assertIsInstance(decoded, dict)
        self.assertEqual(
            decoded["entity_id"],
            entity.entity_id,
        )

    def test_missing_required_field_is_rejected(self):
        entity = self.create_entity()

        data = entity_to_dict(entity)
        del data["identity"]

        with self.assertRaises(ValidationError):
            validate_entity(data)

    def test_state_entity_mismatch_is_rejected(self):
        entity = self.create_entity()

        data = entity_to_dict(entity)
        data["state"]["entity_id"] = "entity_wrong"

        with self.assertRaises(ValidationError):
            validate_entity(data)

    def test_variant_entity_mismatch_is_rejected(self):
        entity = self.create_entity()

        data = entity_to_dict(entity)

        variant_id = next(iter(data["variants"]))

        data["variants"][variant_id]["source_entity_id"] = "entity_wrong"

        with self.assertRaises(ValidationError):
            validate_entity(data)

    def test_variant_key_mismatch_is_rejected(self):
        entity = self.create_entity()

        data = entity_to_dict(entity)

        variant_id = next(iter(data["variants"]))
        variant_data = data["variants"].pop(variant_id)

        data["variants"]["variant_wrong"] = variant_data

        with self.assertRaises(ValidationError):
            validate_entity(data)


if __name__ == "__main__":
    unittest.main(verbosity=2)
