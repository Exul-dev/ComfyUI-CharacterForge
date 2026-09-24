from __future__ import annotations

from .component import CharacterForgeObject


class Validatable(CharacterForgeObject):
    """
    Explicit validation contract.
    """

    def validate(self) -> None:
        raise NotImplementedError
