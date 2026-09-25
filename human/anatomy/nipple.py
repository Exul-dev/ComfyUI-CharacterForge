from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Nipple(AnatomyComponent):
    """Represents one anatomical nipple."""

    component_type = "nipple"

    VALID_SHAPES = (
        "flat",
        "average",
        "prominent",
        "inverted",
        "protruding",
    )

    def __init__(
        self,
        *,
        side: BodySide = BodySide.RIGHT,
        diameter: float = 1.0,
        projection: float = 0.5,
        shape: str = "average",
        vertical_position: float = 0.5,
        horizontal_position: float = 0.5,
        orientation: float = 0.0,
    ) -> None:
        super().__init__()

        self.side = side
        self.diameter = float(diameter)
        self.projection = float(projection)
        self.shape = shape
        self.vertical_position = float(vertical_position)
        self.horizontal_position = float(horizontal_position)
        self.orientation = float(orientation)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Nipple side must be a BodySide value.")

        if self.diameter <= 0:
            raise ValueError("Nipple diameter must be greater than zero.")

        if self.projection < 0:
            raise ValueError("Nipple projection cannot be negative.")

        if not 0.0 <= self.vertical_position <= 1.0:
            raise ValueError(
                "Nipple vertical position must be between 0 and 1."
            )

        if not 0.0 <= self.horizontal_position <= 1.0:
            raise ValueError(
                "Nipple horizontal position must be between 0 and 1."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid nipple shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "diameter": self.diameter,
            "projection": self.projection,
            "shape": self.shape,
            "vertical_position": self.vertical_position,
            "horizontal_position": self.horizontal_position,
            "orientation": self.orientation,
        }
