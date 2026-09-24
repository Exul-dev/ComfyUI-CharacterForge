from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Palm(AnatomyComponent):
    """Represents the anatomical palm structure of a hand."""

    component_type = "palm"

    VALID_SHAPES = (
        "flat",
        "average",
        "cupped",
        "broad",
        "narrow",
        "square",
        "tapered",
    )

    def __init__(
        self,
        *,
        length: float = 10.0,
        width: float = 8.0,
        thickness: float = 2.2,
        shape: str = "average",
        arch: float = 0.5,
        pad_thickness: float = 0.5,
        texture: str = "average",
    ) -> None:
        super().__init__()

        self.length = float(length)
        self.width = float(width)
        self.thickness = float(thickness)
        self.shape = shape
        self.arch = float(arch)
        self.pad_thickness = float(pad_thickness)
        self.texture = texture

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.length <= 0:
            raise ValueError("Palm length must be greater than zero.")

        if self.width <= 0:
            raise ValueError("Palm width must be greater than zero.")

        if self.thickness <= 0:
            raise ValueError("Palm thickness must be greater than zero.")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid palm shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if not 0.0 <= self.arch <= 1.0:
            raise ValueError("Palm arch must be between 0 and 1.")

        if self.pad_thickness <= 0:
            raise ValueError("Palm pad thickness must be greater than zero.")

        if not self.texture:
            raise ValueError("Palm texture must not be empty.")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "length": self.length,
            "width": self.width,
            "thickness": self.thickness,
            "shape": self.shape,
            "arch": self.arch,
            "pad_thickness": self.pad_thickness,
            "texture": self.texture,
        }
