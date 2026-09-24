from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import FingerType
from .nail import Nail


class Finger(AnatomyComponent):
    """Represents an individual human finger."""

    component_type = "finger"

    def __init__(
        self,
        *,
        type: FingerType = FingerType.INDEX,
        length: float = 7.5,
        width: float = 1.8,
        thickness: float = 1.6,
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

        if not isinstance(self.type, FingerType):
            raise ValueError("Finger type must be a FingerType value.")

        if self.length <= 0:
            raise ValueError("Finger length must be greater than zero.")

        if self.width <= 0:
            raise ValueError("Finger width must be greater than zero.")

        if self.thickness <= 0:
            raise ValueError("Finger thickness must be greater than zero.")

        if not 0.0 <= self.curvature <= 1.0:
            raise ValueError("Finger curvature must be between 0 and 1.")

        if not -90.0 <= self.orientation <= 90.0:
            raise ValueError(
                "Finger orientation must be between -90 and 90 degrees."
            )

        if not self.joint_structure:
            raise ValueError("Finger joint structure must not be empty.")

        if not self.skin:
            raise ValueError("Finger skin must not be empty.")

        if not self.condition:
            raise ValueError("Finger condition must not be empty.")

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
