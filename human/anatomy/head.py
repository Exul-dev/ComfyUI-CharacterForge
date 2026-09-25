from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .face import Face


class Head(AnatomyComponent):
    """Represents the anatomical head structure."""

    component_type = "head"

    VALID_SHAPES = (
        "narrow",
        "average",
        "broad",
        "round",
        "oval",
        "square",
        "heart",
        "long",
    )

    def __init__(
        self,
        *,
        height: float = 22.0,
        width: float = 15.0,
        depth: float = 19.0,
        shape: str = "oval",
        face: Face | None = None,
    ) -> None:
        super().__init__()

        self.height = float(height)
        self.width = float(width)
        self.depth = float(depth)
        self.shape = shape
        self.face = face or Face()

        self.validate()

    def validate(self) -> None:
        super().validate()

        dimensions = {
            "height": self.height,
            "width": self.width,
            "depth": self.depth,
        }

        for name, value in dimensions.items():
            if value <= 0:
                raise ValueError(
                    f"Head {name} must be greater than zero."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid head shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        self.face.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "height": self.height,
            "width": self.width,
            "depth": self.depth,
            "shape": self.shape,
            "face": self.face.to_dict(),
        }
