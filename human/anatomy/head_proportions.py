from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class HeadProportions(AnatomyComponent):
    """Derived proportional relationships of the human head."""

    component_type = "head_proportions"

    def __init__(
        self,
        *,
        cephalic_index: float = 78.0,
        cranial_height_to_width: float = 0.87,
        cranial_depth_to_width: float = 1.27,
        face_to_head_height: float = 0.82,
        face_to_head_width: float = 0.93,
        neurocranium_to_face_height: float = 0.72,
        bizygomatic_to_bigonial: float = 1.17,
    ) -> None:
        super().__init__()

        self.cephalic_index = float(cephalic_index)
        self.cranial_height_to_width = float(cranial_height_to_width)
        self.cranial_depth_to_width = float(cranial_depth_to_width)
        self.face_to_head_height = float(face_to_head_height)
        self.face_to_head_width = float(face_to_head_width)
        self.neurocranium_to_face_height = float(neurocranium_to_face_height)
        self.bizygomatic_to_bigonial = float(bizygomatic_to_bigonial)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.cephalic_index <= 0:
            raise ValueError(
                "HeadProportions cephalic_index must be greater than zero."
            )

        values = {
            "cranial_height_to_width": self.cranial_height_to_width,
            "cranial_depth_to_width": self.cranial_depth_to_width,
            "face_to_head_height": self.face_to_head_height,
            "face_to_head_width": self.face_to_head_width,
            "neurocranium_to_face_height": self.neurocranium_to_face_height,
            "bizygomatic_to_bigonial": self.bizygomatic_to_bigonial,
        }

        for name, value in values.items():
            if value <= 0:
                raise ValueError(
                    f"HeadProportions {name} must be greater than zero."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "cephalic_index": self.cephalic_index,
            "cranial_height_to_width": self.cranial_height_to_width,
            "cranial_depth_to_width": self.cranial_depth_to_width,
            "face_to_head_height": self.face_to_head_height,
            "face_to_head_width": self.face_to_head_width,
            "neurocranium_to_face_height": self.neurocranium_to_face_height,
            "bizygomatic_to_bigonial": self.bizygomatic_to_bigonial,
        }
