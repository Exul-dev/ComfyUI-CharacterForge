from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Shoulder(AnatomyComponent):
    """Represents one anatomical shoulder."""

    component_type = "shoulder"

    VALID_SHAPES = (
        "narrow",
        "average",
        "broad",
        "square",
        "sloping",
        "rounded",
        "athletic",
    )

    def __init__(
        self,
        *,
        side: BodySide = BodySide.RIGHT,
        width: float = 14.0,
        height: float = 12.0,
        depth: float = 5.5,
        slope: float = 0.5,
        roundness: float = 0.5,
        prominence: float = 0.5,
        muscularity: float = 0.5,
        shape: str = "average",
    ) -> None:
        super().__init__()

        self.side = side
        self.width = float(width)
        self.height = float(height)
        self.depth = float(depth)
        self.slope = float(slope)
        self.roundness = float(roundness)
        self.prominence = float(prominence)
        self.muscularity = float(muscularity)
        self.shape = shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Shoulder side must be a BodySide value.")

        if self.width <= 0:
            raise ValueError("Shoulder width must be greater than zero.")

        if self.height <= 0:
            raise ValueError("Shoulder height must be greater than zero.")

        if self.depth <= 0:
            raise ValueError("Shoulder depth must be greater than zero.")

        if not 0.0 <= self.slope <= 1.0:
            raise ValueError("Shoulder slope must be between 0 and 1.")

        if not 0.0 <= self.roundness <= 1.0:
            raise ValueError("Shoulder roundness must be between 0 and 1.")

        if not 0.0 <= self.prominence <= 1.0:
            raise ValueError("Shoulder prominence must be between 0 and 1.")

        if not 0.0 <= self.muscularity <= 1.0:
            raise ValueError("Shoulder muscularity must be between 0 and 1.")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid shoulder shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "width": self.width,
            "height": self.height,
            "depth": self.depth,
            "slope": self.slope,
            "roundness": self.roundness,
            "prominence": self.prominence,
            "muscularity": self.muscularity,
            "shape": self.shape,
        }
