"""
Tests for CharacterForge Engine Contract.
"""

import sys
import unittest
from pathlib import Path
from typing import Any


PROJECT_ROOT = r"D:\AVVIO PULITO di ComfyUI\ComfyUI\custom_nodes\ComfyUI-CharacterForge"

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from core.contracts import EntityContract
from core.engine_contract import (
    EngineContract,
    EngineContractError,
)


class EngineContractTestDouble(EngineContract):

    engine_id = "test_engine"
    entity_type = "test_entity"

    def __init__(self) -> None:
        self._contract = EntityContract(
            entity_type=self.entity_type,
            required_identity_properties=frozenset({"name"}),
            description="Test entity contract.",
        )
        super().__init__()

    @property
    def contract(self) -> EntityContract:
        return self._contract

    def validate_config(self, config: dict[str, Any]) -> None:
        if "name" not in config:
            raise EngineContractError(
                "Test engine requires 'name'."
            )

    def build_payload(self, config: dict[str, Any]) -> dict[str, Any]:
        self.validate_config(config)

        return {
            "entity_type": self.entity_type,
            "properties": dict(config),
        }


class InvalidEngine(EngineContract):
    """Engine volutamente invalido per verificare i contratti."""

    @property
    def contract(self) -> EntityContract:
        return EntityContract(entity_type="invalid")

    def validate_config(self, config: dict[str, Any]) -> None:
        pass

    def build_payload(self, config: dict[str, Any]) -> dict[str, Any]:
        return dict(config)


class TestEngineContract(unittest.TestCase):

    def test_engine_implements_contract(self):
        engine = EngineContractTestDouble()

        self.assertIsInstance(engine, EngineContract)
        self.assertEqual(engine.engine_id, "test_engine")
        self.assertEqual(engine.entity_type, "test_entity")

    def test_contract_is_available(self):
        engine = EngineContractTestDouble()

        self.assertIsInstance(
            engine.contract,
            EntityContract,
        )

        self.assertEqual(
            engine.contract.entity_type,
            "test_entity",
        )

    def test_validate_config_accepts_valid_config(self):
        engine = EngineContractTestDouble()

        engine.validate_config({
            "name": "Example",
        })

    def test_validate_config_rejects_invalid_config(self):
        engine = EngineContractTestDouble()

        with self.assertRaises(EngineContractError):
            engine.validate_config({})

    def test_build_payload(self):
        engine = EngineContractTestDouble()

        payload = engine.build_payload({
            "name": "Example",
        })

        self.assertEqual(
            payload["entity_type"],
            "test_entity",
        )
        self.assertEqual(
            payload["properties"]["name"],
            "Example",
        )

    def test_describe(self):
        engine = EngineContractTestDouble()

        description = engine.describe()

        self.assertEqual(
            description["engine_id"],
            "test_engine",
        )
        self.assertEqual(
            description["entity_type"],
            "test_entity",
        )
        self.assertIn(
            "contract",
            description,
        )

    def test_invalid_engine_without_engine_id_rejected(self):
        class NoEngineId(EngineContract):
            entity_type = "test"

            @property
            def contract(self) -> EntityContract:
                return EntityContract(entity_type="test")

            def validate_config(self, config: dict[str, Any]) -> None:
                pass

            def build_payload(
                self,
                config: dict[str, Any],
            ) -> dict[str, Any]:
                return dict(config)

        with self.assertRaises(EngineContractError):
            NoEngineId()

    def test_invalid_engine_without_entity_type_rejected(self):
        class NoEntityType(EngineContract):
            engine_id = "invalid"

            @property
            def contract(self) -> EntityContract:
                return EntityContract(entity_type="invalid")

            def validate_config(self, config: dict[str, Any]) -> None:
                pass

            def build_payload(
                self,
                config: dict[str, Any],
            ) -> dict[str, Any]:
                return dict(config)

        with self.assertRaises(EngineContractError):
            NoEntityType()

    def test_abstract_engine_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            EngineContract()

    def test_engine_contract_error_is_value_error(self):
        self.assertTrue(
            issubclass(
                EngineContractError,
                ValueError,
            )
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

