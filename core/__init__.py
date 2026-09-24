"""
CharacterForge Domain Core.

Semantic foundation shared by all CharacterForge engines.
"""

from .entity import Entity
from .identity import Identity
from .metadata import Metadata
from .state import State
from .variant import Variant
from .transformation import Transformation

from .schema import (
    SCHEMA_VERSION,
    ENTITY_SCHEMA_VERSION,
)

from .validation import (
    ValidationError,
    validate_entity,
    validate_identity,
    validate_state,
    validate_variant,
    validate_transformation,
    validate_metadata,
    is_valid_entity,
)

from .serialization import (
    entity_to_dict,
    entity_to_json,
    entity_from_dict,
    entity_from_json,
)

from .contracts import (
    EntityContract,
    ENTITY_CONTRACT,
)

from .registry import (
    RegistryError,
    EntityRegistry,
    create_default_registry,
    DEFAULT_REGISTRY,
)

__all__ = [
    "Entity",
    "Identity",
    "Metadata",
    "State",
    "Variant",
    "Transformation",
    "SCHEMA_VERSION",
    "ENTITY_SCHEMA_VERSION",
    "ValidationError",
    "validate_entity",
    "validate_identity",
    "validate_state",
    "validate_variant",
    "validate_transformation",
    "validate_metadata",
    "is_valid_entity",
    "entity_to_dict",
    "entity_to_json",
    "entity_from_dict",
    "entity_from_json",
    "EntityContract",
    "ENTITY_CONTRACT",
    "RegistryError",
    "EntityRegistry",
    "create_default_registry",
    "DEFAULT_REGISTRY",
    "EngineContract",
    "EngineContractError",
]
from .engine_contract import (
    EngineContract,
    EngineContractError,
)

