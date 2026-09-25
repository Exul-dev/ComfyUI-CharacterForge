from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class LowerLeg(AnatomyComponent):
    """Represents the lower leg (shank) anatomical structure."""

    component_type = "lower_leg"

    VALID_SHAPES = (
        "slender",
        "average",
        "athletic",
        "muscular",
        "robust",
    )

    def __init__(
        self,
        *,
        length: float = 42.0,
        circumference: float = 36.0,
        shape: str = "average",
        calf_prominence: float = 0.5,
    ) -> None:
        super().__init__()

        if length <= 0:
            raise ValueError(
                "Lower leg length must be greater than zero."
            )

        if circumference <= 0:
            raise ValueError(
                "Lower leg circumference must be greater than zero."
            )

        if shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid lower leg shape: {shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if not 0.0 <= calf_prominence <= 1.0:
            raise ValueError(
                "Lower leg calf prominence must be between 0 and 1."
            )

        self.length = float(length)
        self.circumference = float(circumference)
        self.shape = shape
        self.calf_prominence = float(calf_prominence)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.length <= 0:
            raise ValueError(
                "Lower leg length must be greater than zero."
            )

        if self.circumference <= 0:
            raise ValueError(
                "Lower leg circumference must be greater than zero."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid lower leg shape: {self.shape!r}.")

        if not 0.0 <= self.calf_prominence <= 1.0:
            raise ValueError(
                "Lower leg calf prominence must be between 0 and 1."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "length": self.length,
            "circumference": self.circumference,
            "shape": self.shape,
            "calf_prominence": self.calf_prominence,
        }