from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Abdomen(AnatomyComponent):
    """Represents the anatomical abdomen (trunk region between
    diaphragm and pelvis)."""

    component_type = "abdomen"

    VALID_SHAPES = (
        "flat",
        "average",
        "rounded",
        "sculpted",
    )

    def __init__(
        self,
        *,
        length: float = 25.0,
        width: float = 28.0,
        depth: float = 19.0,
        muscularity: float = 0.5,
        fat_distribution: float = 0.5,
        shape: str = "average",
    ) -> None:
        super().__init__()

        self.length = float(length)
        self.width = float(width)
        self.depth = float(depth)
        self.muscularity = float(muscularity)
        self.fat_distribution = float(fat_distribution)
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
                raise ValueError(
                    f"Abdomen {name} must be greater than zero."
                )

        if not 0.0 <= self.muscularity <= 1.0:
            raise ValueError(
                "Abdomen muscularity must be between 0 and 1."
            )

        if not 0.0 <= self.fat_distribution <= 1.0:
            raise ValueError(
                "Abdomen fat distribution must be between 0 and 1."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid abdomen shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "length": self.length,
            "width": self.width,
            "depth": self.depth,
            "muscularity": self.muscularity,
            "fat_distribution": self.fat_distribution,
            "shape": self.shape,
        }