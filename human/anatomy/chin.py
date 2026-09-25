from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Chin(AnatomyComponent):
    """Central structural morphology of the chin."""

    component_type = "chin"

    VALID_SHAPES = (
        "narrow",
        "average",
        "broad",
        "round",
        "square",
        "pointed",
        "prominent",
        "receding",
    )

    def __init__(
        self,
        *,
        width: float = 5.0,
        height: float = 4.0,
        projection: float = 2.0,
        depth: float = 3.0,
        vertical_position: float = 0.5,
        shape: str = "average",
        symmetry: float = 1.0,
    ) -> None:
        super().__init__()

        self.width = float(width)
        self.height = float(height)
        self.projection = float(projection)
        self.depth = float(depth)
        self.vertical_position = float(vertical_position)
        self.shape = shape
        self.symmetry = float(symmetry)

        self.validate()

    def validate(self) -> None:
        super().validate()

        for name, value in {
            "width": self.width,
            "height": self.height,
            "projection": self.projection,
            "depth": self.depth,
        }.items():
            if value <= 0:
                raise ValueError(
                    f"Chin {name} must be greater than zero."
                )

        for name, value in {
            "vertical_position": self.vertical_position,
            "symmetry": self.symmetry,
        }.items():
            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Chin {name} must be between 0 and 1."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid chin shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "width": self.width,
            "height": self.height,
            "projection": self.projection,
            "depth": self.depth,
            "vertical_position": self.vertical_position,
            "shape": self.shape,
            "symmetry": self.symmetry,
        }
