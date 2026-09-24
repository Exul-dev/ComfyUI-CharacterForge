from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Neck(AnatomyComponent):
    """Represents the anatomical neck structure."""

    component_type = "neck"

    VALID_SHAPES = (
        "slender",
        "average",
        "thick",
        "muscular",
        "robust",
    )

    def __init__(
        self,
        *,
        length: float = 10.0,
        circumference: float = 36.0,
        width: float = 10.0,
        depth: float = 8.0,
        shape: str = "average",
    ) -> None:
        super().__init__()

        self.length = float(length)
        self.circumference = float(circumference)
        self.width = float(width)
        self.depth = float(depth)
        self.shape = shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        dimensions = {
            "length": self.length,
            "circumference": self.circumference,
            "width": self.width,
            "depth": self.depth,
        }

        for name, value in dimensions.items():
            if value <= 0:
                raise ValueError(
                    f"Neck {name} must be greater than zero."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid neck shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "length": self.length,
            "circumference": self.circumference,
            "width": self.width,
            "depth": self.depth,
            "shape": self.shape,
        }
