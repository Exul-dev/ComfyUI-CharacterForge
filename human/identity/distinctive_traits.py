from __future__ import annotations

from typing import Any

from ..base.semantic import SemanticComponent
from .distinctive_trait import DistinctiveTrait


class DistinctiveTraits(SemanticComponent):
    """
    Collection of distinctive human traits.
    """

    component_type = "distinctive_traits"

    def __init__(self) -> None:
        super().__init__()
        self._traits: dict[str, DistinctiveTrait] = {}

    def add(self, trait: DistinctiveTrait) -> None:
        trait.validate()

        if trait.name in self._traits:
            raise ValueError(
                f"Distinctive trait already exists: {trait.name}"
            )

        self._traits[trait.name] = trait

    def get(self, name: str) -> DistinctiveTrait:
        return self._traits[name]

    def contains(self, name: str) -> bool:
        return name in self._traits

    def __len__(self) -> int:
        return len(self._traits)

    def __iter__(self):
        return iter(self._traits.values())

    def validate(self) -> None:
        super().validate()

        for trait in self._traits.values():
            trait.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "traits": {
                name: trait.to_dict()
                for name, trait in self._traits.items()
            },
        }
