from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Thigh(AnatomyComponent):
    """Represents the thigh anatomical structure.

    H4.15-A foundation, enriched in H4.18-B to the detail standard
    of the project's reference segments and in H5-D-3 with
    vascularity (four-segment limb parity). Legacy constructor
    parameters and error messages are preserved.
    """

    component_type = "thigh"

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
        length: float = 44.0,
        circumference: float = 56.0,
        width: float = 18.0,
        depth: float = 19.0,
        shape: str = "average",
        quad_prominence: float = 0.5,
        hamstring_prominence: float = 0.5,
        inner_fullness: float = 0.4,
        vascularity: float = 0.3,
    ) -> None:
        super().__init__()

        if length <= 0:
            raise ValueError("Thigh length must be greater than zero.")

        if circumference <= 0:
            raise ValueError(
                "Thigh circumference must be greater than zero."
            )

        if shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid thigh shape: {shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        self.length = float(length)
        self.circumference = float(circumference)
        self.width = float(width)
        self.depth = float(depth)
        self.shape = shape
        self.quad_prominence = float(quad_prominence)
        self.hamstring_prominence = float(hamstring_prominence)
        self.inner_fullness = float(inner_fullness)
        self.vascularity = float(vascularity)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.length <= 0:
            raise ValueError("Thigh length must be greater than zero.")

        if self.circumference <= 0:
            raise ValueError(
                "Thigh circumference must be greater than zero."
            )

        if self.width <= 0:
            raise ValueError("Thigh width must be greater than zero.")

        if self.depth <= 0:
            raise ValueError("Thigh depth must be greater than zero.")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid thigh shape: {self.shape!r}.")

        for name in (
            "quad_prominence",
            "hamstring_prominence",
            "inner_fullness",
            "vascularity",
        ):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Thigh {name} must be between 0 and 1."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "length": self.length,
            "circumference": self.circumference,
            "width": self.width,
            "depth": self.depth,
            "shape": self.shape,
            "quad_prominence": self.quad_prominence,
            "hamstring_prominence": self.hamstring_prominence,
            "inner_fullness": self.inner_fullness,
            "vascularity": self.vascularity,
        }