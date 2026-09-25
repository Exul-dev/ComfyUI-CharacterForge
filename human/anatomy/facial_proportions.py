from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class FacialProportions(AnatomyComponent):
    """Derived proportional relationships of the human face."""

    component_type = "facial_proportions"

    def __init__(
        self,
        *,
        upper_to_mid_ratio: float = 0.94,
        mid_to_lower_ratio: float = 1.03,
        width_to_height_ratio: float = 0.78,
        forehead_to_cheek_ratio: float = 0.86,
        cheek_to_jaw_ratio: float = 1.17,
        jaw_to_chin_ratio: float = 2.40,
    ) -> None:
        super().__init__()

        self.upper_to_mid_ratio = float(upper_to_mid_ratio)
        self.mid_to_lower_ratio = float(mid_to_lower_ratio)
        self.width_to_height_ratio = float(width_to_height_ratio)
        self.forehead_to_cheek_ratio = float(forehead_to_cheek_ratio)
        self.cheek_to_jaw_ratio = float(cheek_to_jaw_ratio)
        self.jaw_to_chin_ratio = float(jaw_to_chin_ratio)

        self.validate()

    def validate(self) -> None:
        super().validate()

        values = {
            "upper_to_mid_ratio": self.upper_to_mid_ratio,
            "mid_to_lower_ratio": self.mid_to_lower_ratio,
            "width_to_height_ratio": self.width_to_height_ratio,
            "forehead_to_cheek_ratio": self.forehead_to_cheek_ratio,
            "cheek_to_jaw_ratio": self.cheek_to_jaw_ratio,
            "jaw_to_chin_ratio": self.jaw_to_chin_ratio,
        }

        for name, value in values.items():
            if value <= 0:
                raise ValueError(
                    f"FacialProportions {name} must be greater than zero."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "upper_to_mid_ratio": self.upper_to_mid_ratio,
            "mid_to_lower_ratio": self.mid_to_lower_ratio,
            "width_to_height_ratio": self.width_to_height_ratio,
            "forehead_to_cheek_ratio": self.forehead_to_cheek_ratio,
            "cheek_to_jaw_ratio": self.cheek_to_jaw_ratio,
            "jaw_to_chin_ratio": self.jaw_to_chin_ratio,
        }
