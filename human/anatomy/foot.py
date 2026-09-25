from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide, ToeType
from .toe import Toe


class Foot(AnatomyComponent):
    """Represents one complete human foot."""

    component_type = "foot"

    VALID_SHAPES = (
        "narrow",
        "average",
        "broad",
        "long",
        "flat",
        "high_arched",
    )

    def __init__(
        self,
        *,
        side: BodySide = BodySide.RIGHT,
        length: float = 26.0,
        width: float = 9.5,
        thickness: float = 3.5,
        shape: str = "average",
        arch: float = 0.5,
        heel_width: float = 6.0,
        ball_width: float = 9.0,
        toes: dict[ToeType, Toe] | None = None,
        condition: str = "healthy",
    ) -> None:
        super().__init__()

        self.side = side
        self.length = float(length)
        self.width = float(width)
        self.thickness = float(thickness)
        self.shape = shape
        self.arch = float(arch)
        self.heel_width = float(heel_width)
        self.ball_width = float(ball_width)
        self.condition = condition

        default_toes = {
            ToeType.HALLUX: Toe(
                type=ToeType.HALLUX, length=2.7
            ),
            ToeType.SECOND: Toe(
                type=ToeType.SECOND, length=2.5
            ),
            ToeType.THIRD: Toe(
                type=ToeType.THIRD, length=2.3
            ),
            ToeType.FOURTH: Toe(
                type=ToeType.FOURTH, length=2.2
            ),
            ToeType.FIFTH: Toe(
                type=ToeType.FIFTH, length=2.0
            ),
        }

        self.toes = toes or default_toes

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Foot side must be a BodySide value.")

        if self.length <= 0:
            raise ValueError("Foot length must be greater than zero.")

        if self.width <= 0:
            raise ValueError("Foot width must be greater than zero.")

        if self.thickness <= 0:
            raise ValueError(
                "Foot thickness must be greater than zero."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid foot shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if not 0.0 <= self.arch <= 1.0:
            raise ValueError("Foot arch must be between 0 and 1.")

        if self.heel_width <= 0:
            raise ValueError(
                "Foot heel width must be greater than zero."
            )

        if self.ball_width <= 0:
            raise ValueError(
                "Foot ball width must be greater than zero."
            )

        if not self.condition:
            raise ValueError("Foot condition must not be empty.")

        required_types = set(ToeType)

        if set(self.toes.keys()) != required_types:
            raise ValueError(
                "Foot must contain exactly one toe for every ToeType."
            )

        for toe_type, toe in self.toes.items():
            if not isinstance(toe_type, ToeType):
                raise ValueError("Foot toe keys must be ToeType values.")

            if not isinstance(toe, Toe):
                raise ValueError("Foot toe values must be Toe instances.")

            if toe.type != toe_type:
                raise ValueError(
                    "Toe dictionary key and Toe.type must refer "
                    "to the same ToeType."
                )

            toe.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "length": self.length,
            "width": self.width,
            "thickness": self.thickness,
            "shape": self.shape,
            "arch": self.arch,
            "heel_width": self.heel_width,
            "ball_width": self.ball_width,
            "toes": {
                toe_type.value: toe.to_dict()
                for toe_type, toe in self.toes.items()
            },
            "condition": self.condition,
        }