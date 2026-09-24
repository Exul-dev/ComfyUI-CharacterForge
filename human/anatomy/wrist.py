from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Wrist(AnatomyComponent):
    """Represents an anatomical wrist joint."""

    component_type = "wrist"

    def __init__(
        self,
        *,
        side: BodySide = BodySide.RIGHT,
        width: float = 6.0,
        circumference: float = 16.5,
        thickness: float = 4.5,
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
            raise ValueError("Wrist side must be a BodySide value.")

        if self.width <= 0:
            raise ValueError("Wrist width must be greater than zero.")

        if self.circumference <= 0:
            raise ValueError("Wrist circumference must be greater than zero.")

        if self.thickness <= 0:
            raise ValueError("Wrist thickness must be greater than zero.")

        if not 0.0 <= self.flexion <= 90.0:
            raise ValueError("Wrist flexion must be between 0 and 90 degrees.")

        if not 0.0 <= self.extension <= 90.0:
            raise ValueError("Wrist extension must be between 0 and 90 degrees.")

        if not -90.0 <= self.deviation <= 90.0:
            raise ValueError("Wrist deviation must be between -90 and 90 degrees.")

        if not 0.0 <= self.prominence <= 1.0:
            raise ValueError("Wrist prominence must be between 0 and 1.")

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
