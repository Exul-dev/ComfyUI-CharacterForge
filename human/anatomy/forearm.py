from __future__ import annotations

from .anatomy_component import AnatomyComponent


class Forearm(AnatomyComponent):
    """Represents the forearm anatomical structure."""

    component_type = "forearm"

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
        length: float = 26.0,
        circumference: float = 24.0,
        shape: str = "average",
    ) -> None:
        super().__init__()

        if length <= 0:
            raise ValueError("Forearm length must be greater than zero.")

        if circumference <= 0:
            raise ValueError("Forearm circumference must be greater than zero.")

        if shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid forearm shape: {shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        self.length = float(length)
        self.circumference = float(circumference)
        self.shape = shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.length <= 0:
            raise ValueError("Forearm length must be greater than zero.")

        if self.circumference <= 0:
            raise ValueError("Forearm circumference must be greater than zero.")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid forearm shape: {self.shape!r}.")

    def to_dict(self) -> dict:
        return {
            **super().to_dict(),
            "length": self.length,
            "circumference": self.circumference,
            "shape": self.shape,
        }
