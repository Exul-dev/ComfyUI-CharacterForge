from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .body_type import BodyType, Height, Proportions


class HumanAnatomy(AnatomyComponent):
    """Root anatomical component of a Human entity."""

    component_type = "human_anatomy"

    def __init__(
        self,
        *,
        body_type: BodyType | None = None,
        height: Height | None = None,
        proportions: Proportions | None = None,
    ) -> None:
        super().__init__()
        self.body_type = body_type or BodyType()
        self.height = height or Height()
        self.proportions = proportions or Proportions()

    def validate(self) -> None:
        super().validate()
        self.body_type.validate()
        self.height.validate()
        self.proportions.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "body_type": self.body_type.to_dict(),
            "height": self.height.to_dict(),
            "proportions": self.proportions.to_dict(),
        }
