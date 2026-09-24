from __future__ import annotations

from typing import Any

from ..base.semantic import SemanticComponent


class DistinctiveTrait(SemanticComponent):
    """
    A distinctive human feature that contributes to recognizability.
    """

    component_type = "distinctive_trait"

    def __init__(
        self,
        name: str,
        value: Any,
        *,
        identity_weight: float = 1.0,
    ) -> None:
        super().__init__()

        if not name or not name.strip():
            raise ValueError("DistinctiveTrait name must be non-empty")

        if identity_weight < 0:
            raise ValueError("identity_weight must be >= 0")

        self.name = name
        self.value = value
        self.identity_weight = float(identity_weight)

    def validate(self) -> None:
        super().validate()

        if not self.name.strip():
            raise ValueError("DistinctiveTrait name must be non-empty")

        if self.identity_weight < 0:
            raise ValueError("identity_weight must be >= 0")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "name": self.name,
            "value": self.value,
            "identity_weight": self.identity_weight,
        }
