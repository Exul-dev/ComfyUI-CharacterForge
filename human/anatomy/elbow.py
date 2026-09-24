from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Elbow(AnatomyComponent):
    """Represents an anatomical elbow joint."""

    component_type = "elbow"

    def __init__(
        self,
        *,
        side: BodySide = BodySide.RIGHT,
        flexion: float = 0.0,
        rotation: float = 0.0,
        width: float = 7.0,
        circumference: float = 24.0,
        prominence: float = 0.5,
    ) -> None:
        super().__init__()

        self.side = side
        self.flexion = float(flexion)
        self.rotation = float(rotation)
        self.width = float(width)
        self.circumference = float(circumference)
        self.prominence = float(prominence)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Elbow side must be a BodySide value.")

        if not 0.0 <= self.flexion <= 150.0:
            raise ValueError("Elbow flexion must be between 0 and 150 degrees.")

        if not -180.0 <= self.rotation <= 180.0:
            raise ValueError("Elbow rotation must be between -180 and 180 degrees.")

        if self.width <= 0:
            raise ValueError("Elbow width must be greater than zero.")

        if self.circumference <= 0:
            raise ValueError("Elbow circumference must be greater than zero.")

        if not 0.0 <= self.prominence <= 1.0:
            raise ValueError("Elbow prominence must be between 0 and 1.")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "flexion": self.flexion,
            "rotation": self.rotation,
            "width": self.width,
            "circumference": self.circumference,
            "prominence": self.prominence,
        }
