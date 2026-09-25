from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class FaceDimensions(AnatomyComponent):
    """Primary dimensional measurements of the human face."""

    component_type = "face_dimensions"

    def __init__(
        self,
        *,
        facial_height: float = 18.0,
        facial_width: float = 14.0,
        facial_depth: float = 10.0,
        upper_face_height: float = 5.8,
        mid_face_height: float = 6.2,
        lower_face_height: float = 6.0,
        forehead_width: float = 12.0,
        bizygomatic_width: float = 14.0,
        bigonial_width: float = 12.0,
        jaw_width: float = 12.0,
        chin_width: float = 5.0,
        chin_height: float = 4.0,
    ) -> None:
        super().__init__()

        self.facial_height = float(facial_height)
        self.facial_width = float(facial_width)
        self.facial_depth = float(facial_depth)
        self.upper_face_height = float(upper_face_height)
        self.mid_face_height = float(mid_face_height)
        self.lower_face_height = float(lower_face_height)
        self.forehead_width = float(forehead_width)
        self.bizygomatic_width = float(bizygomatic_width)
        self.bigonial_width = float(bigonial_width)
        self.jaw_width = float(jaw_width)
        self.chin_width = float(chin_width)
        self.chin_height = float(chin_height)

        self.validate()

    def validate(self) -> None:
        super().validate()

        values = {
            "facial_height": self.facial_height,
            "facial_width": self.facial_width,
            "facial_depth": self.facial_depth,
            "upper_face_height": self.upper_face_height,
            "mid_face_height": self.mid_face_height,
            "lower_face_height": self.lower_face_height,
            "forehead_width": self.forehead_width,
            "bizygomatic_width": self.bizygomatic_width,
            "bigonial_width": self.bigonial_width,
            "jaw_width": self.jaw_width,
            "chin_width": self.chin_width,
            "chin_height": self.chin_height,
        }

        for name, value in values.items():
            if value <= 0:
                raise ValueError(
                    f"FaceDimensions {name} must be greater than zero."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "facial_height": self.facial_height,
            "facial_width": self.facial_width,
            "facial_depth": self.facial_depth,
            "upper_face_height": self.upper_face_height,
            "mid_face_height": self.mid_face_height,
            "lower_face_height": self.lower_face_height,
            "forehead_width": self.forehead_width,
            "bizygomatic_width": self.bizygomatic_width,
            "bigonial_width": self.bigonial_width,
            "jaw_width": self.jaw_width,
            "chin_width": self.chin_width,
            "chin_height": self.chin_height,
        }
