from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide, FingerType
from .finger import Finger
from .hand import Hand
from .palm import Palm


class Hands(AnatomyComponent):
    """Composite anatomical component representing both human hands.

    H4.4 provides a fully structured left/right hand model while
    preserving the public H4.3 constructor API for compatibility.
    """

    component_type = "hands"

    VALID_SIZES = (
        "very_small",
        "small",
        "average",
        "large",
        "very_large",
    )

    VALID_SHAPES = (
        "delicate",
        "average",
        "broad",
        "long_fingered",
        "compact",
    )

    def __init__(
        self,
        *,
        left: Hand | None = None,
        right: Hand | None = None,
        size: str = "average",
        shape: str = "average",
        finger_length: float = 7.5,
        palm_width: float = 8.5,
    ) -> None:
        super().__init__()

        self.size = size
        self.shape = shape
        self.finger_length = float(finger_length)
        self.palm_width = float(palm_width)

        self.left = left or self._build_hand(BodySide.LEFT)
        self.right = right or self._build_hand(BodySide.RIGHT)

        self.validate()

    def _build_hand(self, side: BodySide) -> Hand:
        palm = Palm(
            width=self.palm_width,
        )

        fingers = {
            FingerType.THUMB: Finger(
                type=FingerType.THUMB,
                length=self.finger_length * 0.80,
            ),
            FingerType.INDEX: Finger(
                type=FingerType.INDEX,
                length=self.finger_length,
            ),
            FingerType.MIDDLE: Finger(
                type=FingerType.MIDDLE,
                length=self.finger_length * 1.07,
            ),
            FingerType.RING: Finger(
                type=FingerType.RING,
                length=self.finger_length * 0.99,
            ),
            FingerType.LITTLE: Finger(
                type=FingerType.LITTLE,
                length=self.finger_length * 0.81,
            ),
        }

        return Hand(
            side=side,
            shape=self.shape,
            palm=palm,
            fingers=fingers,
        )

    def validate(self) -> None:
        super().validate()

        if self.size not in self.VALID_SIZES:
            raise ValueError(
                f"Invalid hand size: {self.size!r}. "
                f"Expected one of {self.VALID_SIZES}."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid hand shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if self.finger_length <= 0:
            raise ValueError(
                "Finger length must be greater than zero."
            )

        if self.palm_width <= 0:
            raise ValueError(
                "Palm width must be greater than zero."
            )

        if not isinstance(self.left, Hand):
            raise ValueError("Left hand must be a Hand instance.")

        if not isinstance(self.right, Hand):
            raise ValueError("Right hand must be a Hand instance.")

        if self.left.side != BodySide.LEFT:
            raise ValueError("Hands.left must have BodySide.LEFT.")

        if self.right.side != BodySide.RIGHT:
            raise ValueError("Hands.right must have BodySide.RIGHT.")

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "size": self.size,
            "shape": self.shape,
            "finger_length": self.finger_length,
            "palm_width": self.palm_width,
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }
