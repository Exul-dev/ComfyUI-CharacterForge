from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Waist(AnatomyComponent):
    """Represents the anatomical waist (narrowest trunk section).

    Midline component (pattern Neck): physical dimensions in
    centimeters. Derived waist-to-hip proportions belong to the
    future proportional layer, not here.
    """

    component_type = "waist"

    VALID_SHAPES = (
        "tapered",
        "straight",
        "full",
    )

    def __init__(
        self,
        *,
        circumference: float = 80.0,
        width: float = 27.0,
        depth: float = 18.5,
        shape: str = "straight",
    ) -> None:
        super().__init__()

        self.circumference = float(circumference)
        self.width = float(width)
        self.depth = float(depth)
        self.shape = shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        dimensions = {
            "circumference": self.circumference,
            "width": self.width,
            "depth": self.depth,
        }

        for name, value in dimensions.items():
            if value <= 0:
                raise ValueError(
                    f"Waist {name} must be greater than zero."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid waist shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "circumference": self.circumference,
            "width": self.width,
            "depth": self.depth,
            "shape": self.shape,
        }