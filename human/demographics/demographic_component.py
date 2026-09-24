from __future__ import annotations

from typing import Any

from ..base.semantic import SemanticComponent


class DemographicComponent(SemanticComponent):
    """
    Base class for all Human demographic components.

    Demographic information describes relatively stable identity/context
    attributes. It must remain separate from temporary visual state,
    clothing, pose, expression and style.
    """

    component_type = "demographic"

    def __init__(self, *, enabled: bool = True) -> None:
        super().__init__(enabled=enabled)

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "component_type": self.component_type,
        }
