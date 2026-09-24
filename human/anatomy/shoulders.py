from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide
from .shoulder import Shoulder


class Shoulders(AnatomyComponent):
    """Composite anatomical component representing both shoulders.

    Preserves the H4.2 public API while providing the structured
    bilateral H4.5 shoulder model.
    """

    component_type = "shoulders"

    # H4.2 compatibility
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

    # H4.2 categorical slope -> H4.5 normalized slope.
    SLOPE_VALUES = {
        "level": 0.0,
        "sloped": 0.5,
        "steep": 1.0,
    }

    def __init__(
        self,
        width: float = 1.0,
        *,
        shape: str = "average",
        slope: str = "level",
        left: Shoulder | None = None,
        right: Shoulder | None = None,
    ) -> None:
        super().__init__()

        # Legacy H4.2 properties.
        self.width = float(width)
        self.shape = shape
        self.slope = slope

        # Structured H4.5 bilateral components.
        shoulder_slope = self.SLOPE_VALUES.get(slope, 0.0)

        self.left = left or Shoulder(
            side=BodySide.LEFT,
            slope=shoulder_slope,
            shape=self._map_shape(shape),
        )

        self.right = right or Shoulder(
            side=BodySide.RIGHT,
            slope=shoulder_slope,
            shape=self._map_shape(shape),
        )

        self.validate()

    @staticmethod
    def _map_shape(shape: str) -> str:
        """Map the legacy H4.2 shape into the H4.5 shoulder shape model."""

        return shape

    def validate(self) -> None:
        super().validate()

        # H4.2 validation.
        if self.width <= 0:
            raise ValueError("Shoulder width must be greater than zero")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid shoulder shape: {self.shape}")

        if self.slope not in self.VALID_SLOPES:
            raise ValueError(f"Invalid shoulder slope: {self.slope}")

        # H4.5 bilateral validation.
        if not isinstance(self.left, Shoulder):
            raise ValueError("Shoulders.left must be a Shoulder instance.")

        if not isinstance(self.right, Shoulder):
            raise ValueError("Shoulders.right must be a Shoulder instance.")

        if self.left.side != BodySide.LEFT:
            raise ValueError("Shoulders.left must have BodySide.LEFT.")

        if self.right.side != BodySide.RIGHT:
            raise ValueError("Shoulders.right must have BodySide.RIGHT.")

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            # H4.2 compatibility.
            "width": self.width,
            "shape": self.shape,
            "slope": self.slope,
            # H4.5 structured anatomy.
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }
