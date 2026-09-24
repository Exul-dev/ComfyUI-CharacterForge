"""
Tests for CharacterForge Domain Core Registry and Contracts.
"""

import sys
import unittest
from pathlib import Path


PROJECT_ROOT = r"D:\AVVIO PULITO di ComfyUI\ComfyUI\custom_nodes\ComfyUI-CharacterForge"

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from core.contracts import EntityContract
from core.registry import (
    DEFAULT_REGISTRY,
    EntityRegistry,
    RegistryError,
    create_default_registry,
)


class TestEntityContract(unittest.TestCase):

    def test_contract_creation(self):
        contract = EntityContract(
            entity_type="human",
            required_identity_properties=frozenset({"name"}),
            required_state_properties=frozenset({"age"}),
            description="Human entity.",
        )

        self.assertEqual(contract.entity_type, "human")
        self.assertIn("name", contract.required_identity_properties)
        self.assertIn("age", contract.required_state_properties)

    def test_empty_entity_type_rejected(self):
        with self.assertRaises(ValueError):
            EntityContract(entity_type="")

    def test_contract_serialization(self):
        contract = EntityContract(
            entity_type="creature",
            required_identity_properties=frozenset({"species"}),
        )

        data = contract.to_dict()

        self.assertEqual(data["entity_type"], "creature")
        self.assertEqual(data["required_identity_properties"], ["species"])


class TestEntityRegistry(unittest.TestCase):

    def test_empty_registry(self):
        registry = EntityRegistry()

        self.assertEqual(len(registry), 0)
        self.assertEqual(registry.entity_types(), ())

    def test_register_and_get(self):
        registry = EntityRegistry()

        contract = EntityContract(entity_type="human")

        registry.register(contract)

        self.assertEqual(len(registry), 1)
        self.assertTrue(registry.contains("human"))
        self.assertIs(registry.get("human"), contract)

    def test_duplicate_registration_rejected(self):
        registry = EntityRegistry()
        contract = EntityContract(entity_type="human")

        registry.register(contract)

        with self.assertRaises(RegistryError):
            registry.register(contract)

    def test_replace_registration(self):
        registry = EntityRegistry()

        first = EntityContract(
            entity_type="human",
            description="First",
        )

        second = EntityContract(
            entity_type="human",
            description="Second",
        )

        registry.register(first)
        registry.register(second, replace=True)

        self.assertIs(registry.get("human"), second)

    def test_missing_contract(self):
        registry = EntityRegistry()

        with self.assertRaises(RegistryError):
            registry.get("human")

        self.assertIsNone(registry.get_optional("human"))

    def test_unregister(self):
        registry = EntityRegistry()

        contract = EntityContract(entity_type="human")
        registry.register(contract)

        removed = registry.unregister("human")

        self.assertIs(removed, contract)
        self.assertFalse(registry.contains("human"))
        self.assertEqual(len(registry), 0)

    def test_unregister_missing_rejected(self):
        registry = EntityRegistry()

        with self.assertRaises(RegistryError):
            registry.unregister("human")

    def test_entity_types_are_deterministic(self):
        registry = EntityRegistry()

        registry.register(EntityContract(entity_type="vehicle"))
        registry.register(EntityContract(entity_type="human"))
        registry.register(EntityContract(entity_type="creature"))

        self.assertEqual(
            registry.entity_types(),
            ("creature", "human", "vehicle"),
        )

    def test_registry_serialization(self):
        registry = EntityRegistry()

        registry.register(
            EntityContract(
                entity_type="human",
                required_identity_properties=frozenset({"name"}),
            )
        )

        data = registry.to_dict()

        self.assertIn("human", data)
        self.assertEqual(
            data["human"]["required_identity_properties"],
            ["name"],
        )


class TestDefaultRegistry(unittest.TestCase):

    def test_default_registry_exists(self):
        self.assertIsInstance(DEFAULT_REGISTRY, EntityRegistry)
        self.assertTrue(DEFAULT_REGISTRY.contains("entity"))

    def test_default_registry_factory(self):
        registry = create_default_registry()

        self.assertIsInstance(registry, EntityRegistry)
        self.assertEqual(registry.entity_types(), ("entity",))


if __name__ == "__main__":
    unittest.main(verbosity=2)
