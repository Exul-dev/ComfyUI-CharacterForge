from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Shoulders(AnatomyComponent):
    """Representation of shoulder geometry."""

    component_type = "shoulders"

    VALID_SHAPES = (
        "narrow",
        "average",
        "broad",
    )

    VALID_SLOPES = (
        "level",
        "sloped",
        "steep",
    )

    def __init__(
        self,
        width: float = 1.0,
        *,
        shape: str = "average",
        slope: str = "level",
    ) -> None:
        super().__init__()

        self.width = float(width)
        self.shape = shape
        self.slope = slope

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.width <= 0:
            raise ValueError("Shoulder width must be greater than zero")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid shoulder shape: {self.shape}")

        if self.slope not in self.VALID_SLOPES:
            raise ValueError(f"Invalid shoulder slope: {self.slope}")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "width": self.width,
            "shape": self.shape,
            "slope": self.slope,
        }
