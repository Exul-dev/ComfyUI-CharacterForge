from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class HeadDimensions(AnatomyComponent):
    """Primary dimensional measurements of the human head."""

    component_type = "head_dimensions"

    def __init__(
        self,
        *,
        cranial_height: float = 22.0,
        cranial_width: float = 15.0,
        cranial_depth: float = 19.0,
        cranial_length: float = 19.0,
        cranial_breadth: float = 15.0,
        cranial_circumference: float = 56.0,
        neurocranial_height: float = 13.0,
        facial_height: float = 18.0,
        bizygomatic_width: float = 14.0,
        bigonial_width: float = 12.0,
    ) -> None:
        super().__init__()

        self.cranial_height = float(cranial_height)
        self.cranial_width = float(cranial_width)
        self.cranial_depth = float(cranial_depth)
        self.cranial_length = float(cranial_length)
        self.cranial_breadth = float(cranial_breadth)
        self.cranial_circumference = float(cranial_circumference)
        self.neurocranial_height = float(neurocranial_height)
        self.facial_height = float(facial_height)
        self.bizygomatic_width = float(bizygomatic_width)
        self.bigonial_width = float(bigonial_width)

        self.validate()

    def validate(self) -> None:
        super().validate()

        values = {
            "cranial_height": self.cranial_height,
            "cranial_width": self.cranial_width,
            "cranial_depth": self.cranial_depth,
            "cranial_length": self.cranial_length,
            "cranial_breadth": self.cranial_breadth,
            "cranial_circumference": self.cranial_circumference,
            "neurocranial_height": self.neurocranial_height,
            "facial_height": self.facial_height,
            "bizygomatic_width": self.bizygomatic_width,
            "bigonial_width": self.bigonial_width,
        }

        for name, value in values.items():
            if value <= 0:
                raise ValueError(
                    f"HeadDimensions {name} must be greater than zero."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "cranial_height": self.cranial_height,
            "cranial_width": self.cranial_width,
            "cranial_depth": self.cranial_depth,
            "cranial_length": self.cranial_length,
            "cranial_breadth": self.cranial_breadth,
            "cranial_circumference": self.cranial_circumference,
            "neurocranial_height": self.neurocranial_height,
            "facial_height": self.facial_height,
            "bizygomatic_width": self.bizygomatic_width,
            "bigonial_width": self.bigonial_width,
        }
