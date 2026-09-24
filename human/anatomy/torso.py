from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Torso(AnatomyComponent):
    """Representation of torso geometry."""

    component_type = "torso"

    VALID_SHAPES = (
        "straight",
        "v_shape",
        "rectangle",
        "oval",
        "hourglass",
    )

    def __init__(
        self,
        *,
        length: float = 1.0,
        width: float = 1.0,
        depth: float = 1.0,
        shape: str = "straight",
    ) -> None:
        super().__init__()

        self.length = float(length)
        self.width = float(width)
        self.depth = float(depth)
        self.shape = shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        dimensions = {
            "length": self.length,
            "width": self.width,
            "depth": self.depth,
        }

        for name, value in dimensions.items():
            if value <= 0:
                raise ValueError(f"Torso {name} must be greater than zero")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid torso shape: {self.shape}")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "length": self.length,
            "width": self.width,
            "depth": self.depth,
            "shape": self.shape,
        }
