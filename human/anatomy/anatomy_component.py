from __future__ import annotations

from typing import Any

from ..base.semantic import SemanticComponent


class AnatomyComponent(SemanticComponent):
    """Base class for all Human Engine anatomical components."""

    component_type = "anatomy"

    def validate(self) -> None:
        super().validate()

    def to_dict(self) -> dict[str, Any]:
        return super().to_dict()
