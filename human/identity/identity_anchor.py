from __future__ import annotations

from typing import Any

from ..base.semantic import SemanticComponent


class IdentityAnchor(SemanticComponent):
    """
    A single feature used to preserve identity across generations,
    variants, transformations and reference-sheet views.
    """

    component_type = "identity_anchor"

    def __init__(
        self,
        name: str,
        value: Any,
        *,
        weight: float = 1.0,
        locked: bool = True,
    ) -> None:
        super().__init__()

        if not name or not name.strip():
            raise ValueError("IdentityAnchor name must be non-empty")

        if weight < 0:
            raise ValueError("IdentityAnchor weight must be >= 0")

        self.name = name
        self.value = value
        self.weight = float(weight)
        self.locked = bool(locked)

    def validate(self) -> None:
        super().validate()

        if not self.name.strip():
            raise ValueError("IdentityAnchor name must be non-empty")

        if self.weight < 0:
            raise ValueError("IdentityAnchor weight must be >= 0")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "name": self.name,
            "value": self.value,
            "weight": self.weight,
            "locked": self.locked,
        }
