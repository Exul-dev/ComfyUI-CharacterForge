"""
CharacterForge Domain Core serialization.
"""

from __future__ import annotations

import json
from typing import Any

from .entity import Entity
from .identity import Identity
from .metadata import Metadata
from .state import State
from .validation import validate_entity
from .variant import Variant


def entity_to_dict(entity: Entity) -> dict[str, Any]:
    data = entity.to_dict()
    validate_entity(data)
    return data


def entity_to_json(
    entity: Entity,
    *,
    indent: int | None = 2,
    ensure_ascii: bool = False,
) -> str:
    data = entity_to_dict(entity)

    return json.dumps(
        data,
        indent=indent,
        ensure_ascii=ensure_ascii,
    )


def entity_from_dict(data: dict[str, Any]) -> Entity:
    validate_entity(data)

    identity_data = data["identity"]

    identity = Identity(
        identity_id=identity_data["identity_id"],
        name=identity_data["name"],
        entity_type=identity_data["entity_type"],
        anchors=dict(identity_data["anchors"]),
        identity_properties=dict(identity_data["identity_properties"]),
        created_at=identity_data["created_at"],
        version=identity_data["version"],
    )

    metadata_data = data["metadata"]

    metadata = Metadata(
        schema_version=metadata_data["schema_version"],
        source=metadata_data["source"],
        provenance=dict(metadata_data["provenance"]),
        tags=list(metadata_data["tags"]),
        created_at=metadata_data["created_at"],
    )

    state_data = data["state"]

    state = State(
        state_id=state_data["state_id"],
        entity_id=state_data["entity_id"],
        properties=dict(state_data["properties"]),
        active_variant_id=state_data["active_variant_id"],
        timestamp=state_data["timestamp"],
        version=state_data["version"],
    )

    entity = Entity(
        entity_id=data["entity_id"],
        identity=identity,
        state=state,
        metadata=metadata,
    )

    for variant_id, variant_data in data["variants"].items():
        variant = Variant(
            variant_id=variant_data["variant_id"],
            source_entity_id=variant_data["source_entity_id"],
            name=variant_data["name"],
            changes=dict(variant_data["changes"]),
            preserves_identity=variant_data["preserves_identity"],
            version=variant_data["version"],
        )

        if variant.variant_id != variant_id:
            raise ValueError(
                "Serialized variant ID does not match dictionary key"
            )

        entity.add_variant(variant)

    return entity


def entity_from_json(payload: str) -> Entity:
    data = json.loads(payload)

    if not isinstance(data, dict):
        raise ValueError("Serialized Entity JSON must contain an object")

    return entity_from_dict(data)
