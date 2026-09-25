from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Neck(AnatomyComponent):
    """Represents the anatomical neck structure.

    Enriched in H4.19-C with the laryngeal prominence (Adam's
    apple) — a key sexual-dimorphism visual trait. Legacy
    parameters and error messages preserved verbatim.
    """

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
        adam_apple_prominence: float = 0.3,
        adam_apple_size: float = 2.5,
    ) -> None:
        super().__init__()

        self.length = float(length)
        self.circumference = float(circumference)
        self.width = float(width)
        self.depth = float(depth)
        self.shape = shape
        self.adam_apple_prominence = float(adam_apple_prominence)
        self.adam_apple_size = float(adam_apple_size)

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

        if not 0.0 <= self.adam_apple_prominence <= 1.0:
            raise ValueError(
                "Neck adam_apple_prominence must be between 0 and 1."
            )

        if self.adam_apple_size <= 0:
            raise ValueError(
                "Neck adam_apple_size must be greater than zero."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "length": self.length,
            "circumference": self.circumference,
            "width": self.width,
            "depth": self.depth,
            "shape": self.shape,
            "adam_apple_prominence": self.adam_apple_prominence,
            "adam_apple_size": self.adam_apple_size,
        }