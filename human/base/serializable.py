from __future__ import annotations

from typing import Any

from .component import CharacterForgeObject


class Serializable(CharacterForgeObject):
    """
    Marker/base contract for serializable semantic components.
    """

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Serializable":
        raise NotImplementedError(
            f"{cls.__name__}.from_dict() must be implemented by concrete classes"
        )
