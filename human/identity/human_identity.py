from __future__ import annotations

from typing import Any

from ..base.semantic import SemanticComponent
from .identity_anchors import IdentityAnchors
from .distinctive_traits import DistinctiveTraits
from .identity_persistence import IdentityPersistence


class HumanIdentity(SemanticComponent):
    """
    Complete identity layer of a Human.

    Identity is deliberately separated from temporary state,
    variants, transformations, clothing, pose, expression and style.
    """

    component_type = "human_identity"

    def __init__(
        self,
        *,
        name: str = "",
        anchors: IdentityAnchors | None = None,
        distinctive_traits: DistinctiveTraits | None = None,
        persistence: IdentityPersistence | None = None,
    ) -> None:
        super().__init__()

        self.name = name
        self.anchors = anchors or IdentityAnchors()
        self.distinctive_traits = (
            distinctive_traits or DistinctiveTraits()
        )
        self.persistence = (
            persistence or IdentityPersistence()
        )

    def validate(self) -> None:
        super().validate()

        self.anchors.validate()
        self.distinctive_traits.validate()
        self.persistence.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "name": self.name,
            "anchors": self.anchors.to_dict(),
            "distinctive_traits": (
                self.distinctive_traits.to_dict()
            ),
            "persistence": self.persistence.to_dict(),
        }
