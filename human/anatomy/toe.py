from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import ToeType
from .nail import Nail


class Toe(AnatomyComponent):
    """Represents an individual human toe."""

    component_type = "toe"

    def __init__(
        self,
        *,
        type: ToeType = ToeType.HALLUX,
        length: float = 2.7,
        width: float = 1.5,
        thickness: float = 1.3,
        curvature: float = 0.0,
        orientation: float = 0.0,
        joint_structure: str = "standard",
        nail: Nail | None = None,
        skin: str = "normal",
        condition: str = "healthy",
    ) -> None:
        super().__init__()

        self.type = type
        self.length = float(length)
        self.width = float(width)
        self.thickness = float(thickness)
        self.curvature = float(curvature)
        self.orientation = float(orientation)
        self.joint_structure = joint_structure
        self.nail = nail or Nail()
        self.skin = skin
        self.condition = condition

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.type, ToeType):
            raise ValueError("Toe type must be a ToeType value.")

        if self.length <= 0:
            raise ValueError("Toe length must be greater than zero.")

        if self.width <= 0:
            raise ValueError("Toe width must be greater than zero.")

        if self.thickness <= 0:
            raise ValueError("Toe thickness must be greater than zero.")

        if not 0.0 <= self.curvature <= 1.0:
            raise ValueError("Toe curvature must be between 0 and 1.")

        if not -90.0 <= self.orientation <= 90.0:
            raise ValueError(
                "Toe orientation must be between -90 and 90 degrees."
            )

        if not self.joint_structure:
            raise ValueError("Toe joint structure must not be empty.")

        if not self.skin:
            raise ValueError("Toe skin must not be empty.")

        if not self.condition:
            raise ValueError("Toe condition must not be empty.")

        self.nail.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "type": self.type.value,
            "length": self.length,
            "width": self.width,
            "thickness": self.thickness,
            "curvature": self.curvature,
            "orientation": self.orientation,
            "joint_structure": self.joint_structure,
            "nail": self.nail.to_dict(),
            "skin": self.skin,
            "condition": self.condition,
        }