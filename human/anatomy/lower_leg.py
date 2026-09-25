from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class LowerLeg(AnatomyComponent):
    """Represents the lower leg (shank) anatomical structure.

    H4.15-A foundation, enriched in H4.18-B (shin and calf
    definition). Legacy parameters and error messages preserved.
    """

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
        width: float = 11.0,
        depth: float = 12.0,
        shape: str = "average",
        calf_prominence: float = 0.5,
        calf_definition: float = 0.5,
        shin_definition: float = 0.5,
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

        if width <= 0:
            raise ValueError(
                "Lower leg width must be greater than zero."
            )

        if depth <= 0:
            raise ValueError(
                "Lower leg depth must be greater than zero."
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
        self.width = float(width)
        self.depth = float(depth)
        self.shape = shape
        self.calf_prominence = float(calf_prominence)
        self.calf_definition = float(calf_definition)
        self.shin_definition = float(shin_definition)

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

        if self.width <= 0:
            raise ValueError(
                "Lower leg width must be greater than zero."
            )

        if self.depth <= 0:
            raise ValueError(
                "Lower leg depth must be greater than zero."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid lower leg shape: {self.shape!r}.")

        for name in (
            "calf_prominence",
            "calf_definition",
            "shin_definition",
        ):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Lower leg {name.replace('_', ' ')} must be "
                    "between 0 and 1."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "length": self.length,
            "circumference": self.circumference,
            "width": self.width,
            "depth": self.depth,
            "shape": self.shape,
            "calf_prominence": self.calf_prominence,
            "calf_definition": self.calf_definition,
            "shin_definition": self.shin_definition,
        }