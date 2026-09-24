from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide, FingerType
from .finger import Finger
from .palm import Palm


class Hand(AnatomyComponent):
    """Represents one complete human hand."""

    component_type = "hand"

    def __init__(
        self,
        *,
        side: BodySide = BodySide.RIGHT,
        length: float = 18.0,
        width: float = 8.0,
        thickness: float = 2.5,
        shape: str = "average",
        palm: Palm | None = None,
        fingers: dict[FingerType, Finger] | None = None,
        condition: str = "healthy",
    ) -> None:
        super().__init__()

        self.side = side
        self.length = float(length)
        self.width = float(width)
        self.thickness = float(thickness)
        self.shape = shape
        self.palm = palm or Palm()
        self.condition = condition

        default_fingers = {
            FingerType.THUMB: Finger(type=FingerType.THUMB, length=6.0),
            FingerType.INDEX: Finger(type=FingerType.INDEX, length=7.5),
            FingerType.MIDDLE: Finger(type=FingerType.MIDDLE, length=8.0),
            FingerType.RING: Finger(type=FingerType.RING, length=7.4),
            FingerType.LITTLE: Finger(type=FingerType.LITTLE, length=6.1),
        }

        self.fingers = fingers or default_fingers

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Hand side must be a BodySide value.")

        if self.length <= 0:
            raise ValueError("Hand length must be greater than zero.")

        if self.width <= 0:
            raise ValueError("Hand width must be greater than zero.")

        if self.thickness <= 0:
            raise ValueError("Hand thickness must be greater than zero.")

        if not self.shape:
            raise ValueError("Hand shape must not be empty.")

        if not self.condition:
            raise ValueError("Hand condition must not be empty.")

        self.palm.validate()

        required_types = set(FingerType)

        if set(self.fingers.keys()) != required_types:
            raise ValueError(
                "Hand must contain exactly one finger for every FingerType."
            )

        for finger_type, finger in self.fingers.items():
            if not isinstance(finger_type, FingerType):
                raise ValueError("Hand finger keys must be FingerType values.")

            if not isinstance(finger, Finger):
                raise ValueError("Hand finger values must be Finger instances.")

            if finger.type != finger_type:
                raise ValueError(
                    "Finger dictionary key and Finger.type must refer "
                    "to the same FingerType."
                )

            finger.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "length": self.length,
            "width": self.width,
            "thickness": self.thickness,
            "shape": self.shape,
            "palm": self.palm.to_dict(),
            "fingers": {
                finger_type.value: finger.to_dict()
                for finger_type, finger in self.fingers.items()
            },
            "condition": self.condition,
        }
