from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class CharacterForgeObject(ABC):
    """
    Base class for every semantic CharacterForge object.

    Every Human Engine object must ultimately derive from this class.
    """

    schema_version: str = "1.0"

    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        """Return the canonical serialized representation."""
        raise NotImplementedError

    @abstractmethod
    def validate(self) -> None:
        """Raise ValueError if the object is invalid."""
        raise NotImplementedError

    def is_valid(self) -> bool:
        try:
            self.validate()
        except ValueError:
            return False

        return True
