from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Glute(AnatomyComponent):
    """Represents one glute (buttock) of the gluteal region.

    Per-side model: bilateral gluteal asymmetry stays representable
    (pattern MammaryRegion / Ear).
    """

    component_type = "glute"

    VALID_SHAPES = (
        "flat",
        "round",
        "heart",
        "square",
        "pear",
        "athletic",
    )

    def __init__(
        self,
        *,
        side: BodySide,
        width: float = 12.0,
        height: float = 12.5,
        projection: float = 0.5,
        volume: float = 0.5,
        shape: str = "round",
        firmness: float = 0.5,
        muscularity: float = 0.5,
        fat_distribution: float = 0.5,
        fold_prominence: float = 0.4,
    ) -> None:
        super().__init__()

        self.side = side
        self.width = float(width)
        self.height = float(height)
        self.projection = float(projection)
        self.volume = float(volume)
        self.shape = shape
        self.firmness = float(firmness)
        self.muscularity = float(muscularity)
        self.fat_distribution = float(fat_distribution)
        self.fold_prominence = float(fold_prominence)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Glute side must be a BodySide value.")

        if self.width <= 0:
            raise ValueError(
                "Glute width must be greater than zero."
            )

        if self.height <= 0:
            raise ValueError(
                "Glute height must be greater than zero."
            )

        for name in (
            "projection",
            "volume",
            "firmness",
            "muscularity",
            "fat_distribution",
            "fold_prominence",
        ):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Glute {name} must be between 0 and 1."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid glute shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "width": self.width,
            "height": self.height,
            "projection": self.projection,
            "volume": self.volume,
            "shape": self.shape,
            "firmness": self.firmness,
            "muscularity": self.muscularity,
            "fat_distribution": self.fat_distribution,
            "fold_prominence": self.fold_prominence,
        }