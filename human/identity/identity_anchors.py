from __future__ import annotations

from typing import Any

from ..base.semantic import SemanticComponent
from .identity_anchor import IdentityAnchor


class IdentityAnchors(SemanticComponent):
    """
    Collection of stable identity-defining features.
    """

    component_type = "identity_anchors"

    def __init__(self) -> None:
        super().__init__()
        self._anchors: dict[str, IdentityAnchor] = {}

    def add(self, anchor: IdentityAnchor) -> None:
        anchor.validate()

        if anchor.name in self._anchors:
            raise ValueError(
                f"Identity anchor already exists: {anchor.name}"
            )

        self._anchors[anchor.name] = anchor

    def get(self, name: str) -> IdentityAnchor:
        return self._anchors[name]

    def contains(self, name: str) -> bool:
        return name in self._anchors

    def __len__(self) -> int:
        return len(self._anchors)

    def __iter__(self):
        return iter(self._anchors.values())

    def validate(self) -> None:
        super().validate()

        for anchor in self._anchors.values():
            anchor.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "anchors": {
                name: anchor.to_dict()
                for name, anchor in self._anchors.items()
            },
        }
