from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Pelvis(AnatomyComponent):
    """Represents the anatomical pelvis structure."""

    component_type = "pelvis"

    VALID_SHAPES = (
        "narrow",
        "average",
        "broad",
        "wide",
    )

    def __init__(
        self,
        *,
        width: float = 36.0,
        depth: float = 22.0,
        circumference: float = 95.0,
        tilt: float = 0.0,
        shape: str = "average",
        iliac_flare: float = 0.5,
    ) -> None:
        super().__init__()

        self.width = float(width)
        self.depth = float(depth)
        self.circumference = float(circumference)
        self.tilt = float(tilt)
        self.shape = shape
        self.iliac_flare = float(iliac_flare)

        self.validate()

    def validate(self) -> None:
        super().validate()

        dimensions = {
            "width": self.width,
            "depth": self.depth,
            "circumference": self.circumference,
        }

        for name, value in dimensions.items():
            if value <= 0:
                raise ValueError(
                    f"Pelvis {name} must be greater than zero."
                )

        if not -20.0 <= self.tilt <= 20.0:
            raise ValueError(
                "Pelvis tilt must be between -20 and 20 degrees."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid pelvis shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if not 0.0 <= self.iliac_flare <= 1.0:
            raise ValueError(
                "Pelvis iliac flare must be between 0 and 1."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "width": self.width,
            "depth": self.depth,
            "circumference": self.circumference,
            "tilt": self.tilt,
            "shape": self.shape,
            "iliac_flare": self.iliac_flare,
        }