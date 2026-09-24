from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .body_fat import BodyFat
from .body_type import BodyType, Height, Proportions
from .musculature import Musculature
from .shoulders import Shoulders
from .torso import Torso


class HumanAnatomy(AnatomyComponent):
    """Root anatomical component of a Human entity."""

    component_type = "human_anatomy"

    def __init__(
        self,
        *,
        body_type: BodyType | None = None,
        height: Height | None = None,
        proportions: Proportions | None = None,
        musculature: Musculature | None = None,
        body_fat: BodyFat | None = None,
        shoulders: Shoulders | None = None,
        torso: Torso | None = None,
    ) -> None:
        super().__init__()

        self.body_type = body_type or BodyType()
        self.height = height or Height()
        self.proportions = proportions or Proportions()
        self.musculature = musculature or Musculature()
        self.body_fat = body_fat or BodyFat()
        self.shoulders = shoulders or Shoulders()
        self.torso = torso or Torso()

        self.validate()

    def validate(self) -> None:
        super().validate()

        components = (
            self.body_type,
            self.height,
            self.proportions,
            self.musculature,
            self.body_fat,
            self.shoulders,
            self.torso,
        )

        for component in components:
            component.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "body_type": self.body_type.to_dict(),
            "height": self.height.to_dict(),
            "proportions": self.proportions.to_dict(),
            "musculature": self.musculature.to_dict(),
            "body_fat": self.body_fat.to_dict(),
            "shoulders": self.shoulders.to_dict(),
            "torso": self.torso.to_dict(),
        }
