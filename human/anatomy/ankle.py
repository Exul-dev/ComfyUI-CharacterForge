from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Ankle(AnatomyComponent):
    """Represents an anatomical ankle joint."""

    component_type = "ankle"

    def __init__(
        self,
        *,
        side: BodySide = BodySide.RIGHT,
        width: float = 7.0,
        circumference: float = 22.0,
        thickness: float = 6.0,
        flexion: float = 0.0,
        extension: float = 0.0,
        deviation: float = 0.0,
        prominence: float = 0.5,
    ) -> None:
        super().__init__()

        self.side = side
        self.width = float(width)
        self.circumference = float(circumference)
        self.thickness = float(thickness)
        self.flexion = float(flexion)
        self.extension = float(extension)
        self.deviation = float(deviation)
        self.prominence = float(prominence)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Ankle side must be a BodySide value.")

        if self.width <= 0:
            raise ValueError("Ankle width must be greater than zero.")

        if self.circumference <= 0:
            raise ValueError(
                "Ankle circumference must be greater than zero."
            )

        if self.thickness <= 0:
            raise ValueError("Ankle thickness must be greater than zero.")

        if not 0.0 <= self.flexion <= 60.0:
            raise ValueError(
                "Ankle flexion must be between 0 and 60 degrees."
            )

        if not 0.0 <= self.extension <= 30.0:
            raise ValueError(
                "Ankle extension must be between 0 and 30 degrees."
            )

        if not -30.0 <= self.deviation <= 30.0:
            raise ValueError(
                "Ankle deviation must be between -30 and 30 degrees."
            )

        if not 0.0 <= self.prominence <= 1.0:
            raise ValueError("Ankle prominence must be between 0 and 1.")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "width": self.width,
            "circumference": self.circumference,
            "thickness": self.thickness,
            "flexion": self.flexion,
            "extension": self.extension,
            "deviation": self.deviation,
            "prominence": self.prominence,
        }