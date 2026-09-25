from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class CheekStructure(AnatomyComponent):
    """One lateral cheek and zygomatic structural region."""

    component_type = "cheek_structure"

    VALID_SHAPES = (
        "flat",
        "average",
        "rounded",
        "angular",
        "prominent",
        "broad",
    )

    def __init__(
        self,
        *,
        side: BodySide = BodySide.RIGHT,
        width: float = 7.0,
        projection: float = 2.0,
        height: float = 5.0,
        lateral_projection: float = 1.5,
        anterior_projection: float = 1.5,
        vertical_position: float = 0.5,
        prominence: float = 0.5,
        shape: str = "average",
    ) -> None:
        super().__init__()

        self.side = side
        self.width = float(width)
        self.projection = float(projection)
        self.height = float(height)
        self.lateral_projection = float(lateral_projection)
        self.anterior_projection = float(anterior_projection)
        self.vertical_position = float(vertical_position)
        self.prominence = float(prominence)
        self.shape = shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("CheekStructure side must be a BodySide value.")

        for name, value in {
            "width": self.width,
            "projection": self.projection,
            "height": self.height,
            "lateral_projection": self.lateral_projection,
            "anterior_projection": self.anterior_projection,
        }.items():
            if value <= 0:
                raise ValueError(
                    f"CheekStructure {name} must be greater than zero."
                )

        for name, value in {
            "vertical_position": self.vertical_position,
            "prominence": self.prominence,
        }.items():
            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"CheekStructure {name} must be between 0 and 1."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid cheek structure shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "width": self.width,
            "projection": self.projection,
            "height": self.height,
            "lateral_projection": self.lateral_projection,
            "anterior_projection": self.anterior_projection,
            "vertical_position": self.vertical_position,
            "prominence": self.prominence,
            "shape": self.shape,
        }
