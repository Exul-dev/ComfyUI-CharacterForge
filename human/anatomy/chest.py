from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Chest(AnatomyComponent):
    """Thoracic chest component."""

    component_type = "chest"

    VALID_SHAPES = (
        "flat",
        "average",
        "broad",
        "defined",
        "barrel",
    )

    def __init__(
        self,
        *,
        width: float = 32.0,
        height: float = 28.0,
        projection: float = 12.0,
        shape: str = "average",
    ) -> None:
        super().__init__()
        self.width = float(width)
        self.height = float(height)
        self.projection = float(projection)
        self.shape = shape
        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.width <= 0:
            raise ValueError("Chest width must be greater than zero.")

        if self.height <= 0:
            raise ValueError("Chest height must be greater than zero.")

        if self.projection <= 0:
            raise ValueError("Chest projection must be greater than zero.")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid chest shape: {self.shape!r}")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "width": self.width,
            "height": self.height,
            "projection": self.projection,
            "shape": self.shape,
        }
