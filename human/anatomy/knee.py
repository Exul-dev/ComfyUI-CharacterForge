from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Knee(AnatomyComponent):
    """Represents an anatomical knee joint."""

    component_type = "knee"

    def __init__(
        self,
        *,
        side: BodySide = BodySide.RIGHT,
        flexion: float = 0.0,
        rotation: float = 0.0,
        width: float = 10.0,
        circumference: float = 37.0,
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
            raise ValueError("Knee side must be a BodySide value.")

        if not 0.0 <= self.flexion <= 150.0:
            raise ValueError(
                "Knee flexion must be between 0 and 150 degrees."
            )

        if not -45.0 <= self.rotation <= 45.0:
            raise ValueError(
                "Knee rotation must be between -45 and 45 degrees."
            )

        if self.width <= 0:
            raise ValueError("Knee width must be greater than zero.")

        if self.circumference <= 0:
            raise ValueError(
                "Knee circumference must be greater than zero."
            )

        if not 0.0 <= self.prominence <= 1.0:
            raise ValueError("Knee prominence must be between 0 and 1.")

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