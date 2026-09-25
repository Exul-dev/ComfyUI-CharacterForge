from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Face(AnatomyComponent):
    """Represents the structural anatomy of a human face."""

    component_type = "face"

    VALID_SHAPES = (
        "narrow",
        "average",
        "broad",
        "round",
        "oval",
        "square",
        "heart",
        "diamond",
        "oblong",
        "triangular",
    )

    def __init__(
        self,
        *,
        height: float = 18.0,
        width: float = 14.0,
        depth: float = 10.0,
        forehead_width: float = 12.0,
        cheekbone_width: float = 14.0,
        jaw_width: float = 12.0,
        jaw_depth: float = 8.0,
        shape: str = "oval",
        symmetry: float = 1.0,
    ) -> None:
        super().__init__()

        self.height = float(height)
        self.width = float(width)
        self.depth = float(depth)
        self.forehead_width = float(forehead_width)
        self.cheekbone_width = float(cheekbone_width)
        self.jaw_width = float(jaw_width)
        self.jaw_depth = float(jaw_depth)
        self.shape = shape
        self.symmetry = float(symmetry)

        self.validate()

    def validate(self) -> None:
        super().validate()

        dimensions = {
            "height": self.height,
            "width": self.width,
            "depth": self.depth,
            "forehead_width": self.forehead_width,
            "cheekbone_width": self.cheekbone_width,
            "jaw_width": self.jaw_width,
            "jaw_depth": self.jaw_depth,
        }

        for name, value in dimensions.items():
            if value <= 0:
                raise ValueError(
                    f"Face {name} must be greater than zero."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid face shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if not 0.0 <= self.symmetry <= 1.0:
            raise ValueError(
                "Face symmetry must be between 0 and 1."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "height": self.height,
            "width": self.width,
            "depth": self.depth,
            "forehead_width": self.forehead_width,
            "cheekbone_width": self.cheekbone_width,
            "jaw_width": self.jaw_width,
            "jaw_depth": self.jaw_depth,
            "shape": self.shape,
            "symmetry": self.symmetry,
        }
