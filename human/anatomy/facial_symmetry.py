from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class FacialSymmetry(AnatomyComponent):
    """Global and regional facial symmetry measurements."""

    component_type = "facial_symmetry"

    def __init__(
        self,
        *,
        global_symmetry: float = 1.0,
        upper_face: float = 1.0,
        mid_face: float = 1.0,
        lower_face: float = 1.0,
        left_right_alignment: float = 1.0,
    ) -> None:
        super().__init__()

        self.global_symmetry = float(global_symmetry)
        self.upper_face = float(upper_face)
        self.mid_face = float(mid_face)
        self.lower_face = float(lower_face)
        self.left_right_alignment = float(left_right_alignment)

        self.validate()

    def validate(self) -> None:
        super().validate()

        values = {
            "global_symmetry": self.global_symmetry,
            "upper_face": self.upper_face,
            "mid_face": self.mid_face,
            "lower_face": self.lower_face,
            "left_right_alignment": self.left_right_alignment,
        }

        for name, value in values.items():
            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"FacialSymmetry {name} must be between 0 and 1."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "global_symmetry": self.global_symmetry,
            "upper_face": self.upper_face,
            "mid_face": self.mid_face,
            "lower_face": self.lower_face,
            "left_right_alignment": self.left_right_alignment,
        }
