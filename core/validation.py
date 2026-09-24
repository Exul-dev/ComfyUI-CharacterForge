"""
CharacterForge Domain Core validation.
"""

from __future__ import annotations

from typing import Any

from .schema import (
    ENTITY_REQUIRED_FIELDS,
    IDENTITY_REQUIRED_FIELDS,
    METADATA_REQUIRED_FIELDS,
    STATE_REQUIRED_FIELDS,
    VARIANT_REQUIRED_FIELDS,
)


class ValidationError(ValueError):
    """Raised when Domain Core data violates its schema."""


def _require_fields(data: dict[str, Any], required: set[str], path: str) -> None:
    missing = sorted(required - set(data.keys()))

    if missing:
        raise ValidationError(
            f"{path}: missing required fields: {', '.join(missing)}"
        )


def _require_type(
    value: Any,
    expected_type: type | tuple[type, ...],
    path: str,
) -> None:
    if not isinstance(value, expected_type):
        raise ValidationError(
            f"{path}: expected {expected_type}, got {type(value).__name__}"
        )


def validate_identity(data: dict[str, Any], path: str = "identity") -> None:
    _require_type(data, dict, path)
    _require_fields(data, IDENTITY_REQUIRED_FIELDS, path)

    _require_type(data["identity_id"], str, f"{path}.identity_id")
    _require_type(data["name"], str, f"{path}.name")
    _require_type(data["entity_type"], str, f"{path}.entity_type")
    _require_type(data["anchors"], dict, f"{path}.anchors")
    _require_type(
        data["identity_properties"],
        dict,
        f"{path}.identity_properties",
    )
    _require_type(data["created_at"], str, f"{path}.created_at")
    _require_type(data["version"], int, f"{path}.version")


def validate_state(data: dict[str, Any], path: str = "state") -> None:
    _require_type(data, dict, path)
    _require_fields(data, STATE_REQUIRED_FIELDS, path)

    _require_type(data["state_id"], str, f"{path}.state_id")
    _require_type(data["entity_id"], str, f"{path}.entity_id")
    _require_type(data["properties"], dict, f"{path}.properties")

    if data["active_variant_id"] is not None:
        _require_type(
            data["active_variant_id"],
            str,
            f"{path}.active_variant_id",
        )

    _require_type(data["timestamp"], str, f"{path}.timestamp")
    _require_type(data["version"], int, f"{path}.version")


def validate_variant(data: dict[str, Any], path: str = "variant") -> None:
    _require_type(data, dict, path)
    _require_fields(data, VARIANT_REQUIRED_FIELDS, path)

    _require_type(data["variant_id"], str, f"{path}.variant_id")
    _require_type(data["source_entity_id"], str, f"{path}.source_entity_id")
    _require_type(data["name"], str, f"{path}.name")
    _require_type(data["changes"], dict, f"{path}.changes")
    _require_type(
        data["preserves_identity"],
        bool,
        f"{path}.preserves_identity",
    )
    _require_type(data["version"], int, f"{path}.version")


def validate_transformation(
    data: dict[str, Any],
    path: str = "transformation",
) -> None:
    _require_type(data, dict, path)
    _require_fields(data, TRANSFORMATION_REQUIRED_FIELDS, path)

    _require_type(
        data["transformation_id"],
        str,
        f"{path}.transformation_id",
    )
    _require_type(
        data["source_entity_id"],
        str,
        f"{path}.source_entity_id",
    )
    _require_type(
        data["source_state_id"],
        str,
        f"{path}.source_state_id",
    )
    _require_type(
        data["target_state_id"],
        str,
        f"{path}.target_state_id",
    )
    _require_type(data["operations"], list, f"{path}.operations")
    _require_type(data["reversible"], bool, f"{path}.reversible")
    _require_type(
        data["preserves_identity"],
        bool,
        f"{path}.preserves_identity",
    )
    _require_type(data["version"], int, f"{path}.version")


def validate_metadata(data: dict[str, Any], path: str = "metadata") -> None:
    _require_type(data, dict, path)
    _require_fields(data, METADATA_REQUIRED_FIELDS, path)

    _require_type(data["schema_version"], str, f"{path}.schema_version")
    _require_type(data["source"], str, f"{path}.source")
    _require_type(data["provenance"], dict, f"{path}.provenance")
    _require_type(data["tags"], list, f"{path}.tags")
    _require_type(data["created_at"], str, f"{path}.created_at")


def validate_entity(data: dict[str, Any]) -> None:
    _require_type(data, dict, "entity")
    _require_fields(data, ENTITY_REQUIRED_FIELDS, "entity")

    _require_type(data["entity_id"], str, "entity.entity_id")

    validate_identity(data["identity"])
    validate_state(data["state"])

    if data["state"]["entity_id"] != data["entity_id"]:
        raise ValidationError(
            "entity.state.entity_id must match entity.entity_id"
        )

    _require_type(data["variants"], dict, "entity.variants")

    for variant_id, variant_data in data["variants"].items():
        if not isinstance(variant_data, dict):
            raise ValidationError(
                f"entity.variants[{variant_id!r}] must be an object"
            )

        if variant_id != variant_data.get("variant_id"):
            raise ValidationError(
                f"entity.variants[{variant_id!r}].variant_id "
                "must match its dictionary key"
            )

        validate_variant(
            variant_data,
            f"entity.variants[{variant_id!r}]",
        )

        if variant_data["source_entity_id"] != data["entity_id"]:
            raise ValidationError(
                f"entity.variants[{variant_id!r}].source_entity_id "
                "must match entity.entity_id"
            )

    validate_metadata(data["metadata"])


def is_valid_entity(data: dict[str, Any]) -> bool:
    try:
        validate_entity(data)
    except ValidationError:
        return False

    return True
