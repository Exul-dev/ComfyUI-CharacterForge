from __future__ import annotations

from typing import Any

from .component import CharacterForgeObject


class Identifiable(CharacterForgeObject):
    """
    Base class for objects possessing a stable semantic identifier.
    """

    def __init__(self, object_id: str) -> None:
        if not object_id or not object_id.strip():
            raise ValueError("object_id must be a non-empty string")

        self.object_id = object_id

    def validate(self) -> None:
        if not self.object_id.strip():
            raise ValueError("object_id must be non-empty")

    def to_dict(self) -> dict[str, Any]:
        return {
            "object_id": self.object_id,
            "schema_version": self.schema_version,
        }
