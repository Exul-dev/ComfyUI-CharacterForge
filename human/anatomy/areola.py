from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Areola(AnatomyComponent):
    """Represents one anatomical areola."""

    component_type = "areola"

    VALID_SHAPES = (
        "round",
        "oval",
        "irregular",
    )

    def __init__(
        self,
        *,
        side: BodySide = BodySide.RIGHT,
        diameter: float = 4.0,
        height: float = 4.0,
        width: float = 4.0,
        shape: str = "round",
    ) -> None:
        super().__init__()

        self.side = side
        self.diameter = float(diameter)
        self.height = float(height)
        self.width = float(width)
        self.shape = shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Areola side must be a BodySide value.")

        if self.diameter <= 0:
            raise ValueError("Areola diameter must be greater than zero.")

        if self.height <= 0:
            raise ValueError("Areola height must be greater than zero.")

        if self.width <= 0:
            raise ValueError("Areola width must be greater than zero.")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid areola shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "diameter": self.diameter,
            "height": self.height,
            "width": self.width,
            "shape": self.shape,
        }
