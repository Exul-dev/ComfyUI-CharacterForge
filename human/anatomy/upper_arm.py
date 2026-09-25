from __future__ import annotations

from .anatomy_component import AnatomyComponent


class UpperArm(AnatomyComponent):
    """Represents the upper-arm anatomical structure.

    H4.4 foundation, enriched in H4.19-D to thigh parity and in
    H5-D-3 with vascularity (four-segment limb parity). Legacy
    constructor checks (eager, exact messages) preserved verbatim.
    """

    component_type = "upper_arm"

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
        length: float = 30.0,
        circumference: float = 28.0,
        width: float = 9.5,
        depth: float = 9.0,
        shape: str = "average",
        bicep_prominence: float = 0.5,
        tricep_prominence: float = 0.5,
        inner_definition: float = 0.4,
        vascularity: float = 0.3,
    ) -> None:
        super().__init__()

        if length <= 0:
            raise ValueError("Upper arm length must be greater than zero.")

        if circumference <= 0:
            raise ValueError("Upper arm circumference must be greater than zero.")

        if shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid upper arm shape: {shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        self.length = float(length)
        self.circumference = float(circumference)
        self.width = float(width)
        self.depth = float(depth)
        self.shape = shape
        self.bicep_prominence = float(bicep_prominence)
        self.tricep_prominence = float(tricep_prominence)
        self.inner_definition = float(inner_definition)
        self.vascularity = float(vascularity)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.length <= 0:
            raise ValueError("Upper arm length must be greater than zero.")

        if self.circumference <= 0:
            raise ValueError("Upper arm circumference must be greater than zero.")

        if self.width <= 0:
            raise ValueError("Upper arm width must be greater than zero.")

        if self.depth <= 0:
            raise ValueError("Upper arm depth must be greater than zero.")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid upper arm shape: {self.shape!r}.")

        for name in (
            "bicep_prominence",
            "tricep_prominence",
            "inner_definition",
            "vascularity",
        ):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Upper arm {name} must be between 0 and 1."
                )

    def to_dict(self) -> dict:
        return {
            **super().to_dict(),
            "length": self.length,
            "circumference": self.circumference,
            "width": self.width,
            "depth": self.depth,
            "shape": self.shape,
            "bicep_prominence": self.bicep_prominence,
            "tricep_prominence": self.tricep_prominence,
            "inner_definition": self.inner_definition,
            "vascularity": self.vascularity,
        }