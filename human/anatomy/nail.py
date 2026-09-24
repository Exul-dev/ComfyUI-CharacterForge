from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Nail(AnatomyComponent):
    """Represents an individual anatomical nail."""

    component_type = "nail"

    VALID_SHAPES = (
        "round",
        "square",
        "squoval",
        "almond",
        "pointed",
    )

    VALID_CONDITIONS = (
        "healthy",
        "damaged",
        "cracked",
        "chipped",
        "dirty",
        "brittle",
    )

    def __init__(
        self,
        *,
        shape: str = "squoval",
        length: float = 1.2,
        width: float = 1.4,
        thickness: float = 0.2,
        curvature: float = 0.5,
        color: str = "natural",
        texture: str = "smooth",
        gloss: float = 0.5,
        condition: str = "healthy",
        growth: float = 0.5,
    ) -> None:
        super().__init__()

        self.shape = shape
        self.length = float(length)
        self.width = float(width)
        self.thickness = float(thickness)
        self.curvature = float(curvature)
        self.color = color
        self.texture = texture
        self.gloss = float(gloss)
        self.condition = condition
        self.growth = float(growth)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid nail shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if self.length <= 0:
            raise ValueError("Nail length must be greater than zero.")

        if self.width <= 0:
            raise ValueError("Nail width must be greater than zero.")

        if self.thickness <= 0:
            raise ValueError("Nail thickness must be greater than zero.")

        if not 0.0 <= self.curvature <= 1.0:
            raise ValueError("Nail curvature must be between 0 and 1.")

        if not self.color:
            raise ValueError("Nail color must not be empty.")

        if not self.texture:
            raise ValueError("Nail texture must not be empty.")

        if not 0.0 <= self.gloss <= 1.0:
            raise ValueError("Nail gloss must be between 0 and 1.")

        if self.condition not in self.VALID_CONDITIONS:
            raise ValueError(
                f"Invalid nail condition: {self.condition!r}. "
                f"Expected one of {self.VALID_CONDITIONS}."
            )

        if not 0.0 <= self.growth <= 1.0:
            raise ValueError("Nail growth must be between 0 and 1.")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "shape": self.shape,
            "length": self.length,
            "width": self.width,
            "thickness": self.thickness,
            "curvature": self.curvature,
            "color": self.color,
            "texture": self.texture,
            "gloss": self.gloss,
            "condition": self.condition,
            "growth": self.growth,
        }
