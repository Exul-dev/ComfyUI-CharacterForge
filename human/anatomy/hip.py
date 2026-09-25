from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Hip(AnatomyComponent):
    """Represents one hip (trochanteric / lateral pelvic region).

    Per-side model: the greater trochanter, iliac crest contribution
    and hip fat distribution are independently adjustable per side.
    """

    component_type = "hip"

    VALID_SHAPES = (
        "narrow",
        "average",
        "broad",
        "round",
        "high",
        "low",
    )

    def __init__(
        self,
        *,
        side: BodySide,
        width: float = 9.0,
        depth: float = 10.0,
        prominence: float = 0.5,
        trochanter_prominence: float = 0.4,
        iliac_crest_prominence: float = 0.5,
        fat_distribution: float = 0.5,
        muscularity: float = 0.4,
        shape: str = "average",
    ) -> None:
        super().__init__()

        self.side = side
        self.width = float(width)
        self.depth = float(depth)
        self.prominence = float(prominence)
        self.trochanter_prominence = float(trochanter_prominence)
        self.iliac_crest_prominence = float(iliac_crest_prominence)
        self.fat_distribution = float(fat_distribution)
        self.muscularity = float(muscularity)
        self.shape = shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Hip side must be a BodySide value.")

        if self.width <= 0:
            raise ValueError("Hip width must be greater than zero.")

        if self.depth <= 0:
            raise ValueError("Hip depth must be greater than zero.")

        for name in (
            "prominence",
            "trochanter_prominence",
            "iliac_crest_prominence",
            "fat_distribution",
            "muscularity",
        ):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Hip {name} must be between 0 and 1."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid hip shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "width": self.width,
            "depth": self.depth,
            "prominence": self.prominence,
            "trochanter_prominence": self.trochanter_prominence,
            "iliac_crest_prominence": self.iliac_crest_prominence,
            "fat_distribution": self.fat_distribution,
            "muscularity": self.muscularity,
            "shape": self.shape,
        }