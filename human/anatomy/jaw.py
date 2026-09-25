from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Jaw(AnatomyComponent):
    """One lateral mandibular structural region."""

    component_type = "jaw"

    VALID_SHAPES = (
        "narrow",
        "average",
        "broad",
        "angular",
        "rounded",
        "square",
        "tapered",
    )

    def __init__(
        self,
        *,
        side: BodySide = BodySide.RIGHT,
        width: float = 6.0,
        height: float = 8.0,
        depth: float = 5.0,
        angle: float = 125.0,
        projection: float = 2.0,
        ramus_height: float = 6.0,
        ramus_width: float = 3.0,
        gonial_angle: float = 125.0,
        shape: str = "average",
    ) -> None:
        super().__init__()

        self.side = side
        self.width = float(width)
        self.height = float(height)
        self.depth = float(depth)
        self.angle = float(angle)
        self.projection = float(projection)
        self.ramus_height = float(ramus_height)
        self.ramus_width = float(ramus_width)
        self.gonial_angle = float(gonial_angle)
        self.shape = shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Jaw side must be a BodySide value.")

        for name, value in {
            "width": self.width,
            "height": self.height,
            "depth": self.depth,
            "projection": self.projection,
            "ramus_height": self.ramus_height,
            "ramus_width": self.ramus_width,
        }.items():
            if value <= 0:
                raise ValueError(
                    f"Jaw {name} must be greater than zero."
                )

        for name, value in {
            "angle": self.angle,
            "gonial_angle": self.gonial_angle,
        }.items():
            if not 0.0 < value < 180.0:
                raise ValueError(
                    f"Jaw {name} must be between 0 and 180 degrees."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid jaw shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "width": self.width,
            "height": self.height,
            "depth": self.depth,
            "angle": self.angle,
            "projection": self.projection,
            "ramus_height": self.ramus_height,
            "ramus_width": self.ramus_width,
            "gonial_angle": self.gonial_angle,
            "shape": self.shape,
        }
