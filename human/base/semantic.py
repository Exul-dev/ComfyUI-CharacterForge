from __future__ import annotations

from typing import Any

from .component import CharacterForgeObject


class SemanticComponent(CharacterForgeObject):
    """
    Base class for semantic Human Engine components.
    """

    component_type: str = "semantic"

    def __init__(self, *, enabled: bool = True) -> None:
        self.enabled = enabled

    def validate(self) -> None:
        if not isinstance(self.enabled, bool):
            raise ValueError("enabled must be bool")

    def to_dict(self) -> dict[str, Any]:
        return {
            "component_type": self.component_type,
            "enabled": self.enabled,
            "schema_version": self.schema_version,
        }
