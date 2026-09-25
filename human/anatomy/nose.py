from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Nose(AnatomyComponent):
    """Represents the anatomical nose.

    Landmark anchors: nasion (bridge root), pronasale (tip) and
    subnasale (base) — see FacialLandmarks for the coordinate-level
    counterparts.
    """

    component_type = "nose"

    VALID_BRIDGES = (
        "flat",
        "straight",
        "convex",
        "concave",
    )

    VALID_TIPS = (
        "upturned",
        "straight",
        "dropped",
    )

    VALID_NOSTRIL_SHAPES = (
        "oval",
        "round",
        "flared",
        "slit",
    )

    def __init__(
        self,
        *,
        height: float = 5.0,
        width: float = 3.5,
        projection: float = 2.5,
        bridge: str = "straight",
        tip: str = "straight",
        nostril_shape: str = "oval",
        nostril_visibility: float = 0.3,
    ) -> None:
        super().__init__()

        self.height = float(height)
        self.width = float(width)
        self.projection = float(projection)
        self.bridge = bridge
        self.tip = tip
        self.nostril_shape = nostril_shape
        self.nostril_visibility = float(nostril_visibility)

        self.validate()

    def validate(self) -> None:
        super().validate()

        dimensions = {
            "height": self.height,
            "width": self.width,
            "projection": self.projection,
        }

        for name, value in dimensions.items():
            if value <= 0:
                raise ValueError(
                    f"Nose {name} must be greater than zero."
                )

        if self.bridge not in self.VALID_BRIDGES:
            raise ValueError(
                f"Invalid nose bridge: {self.bridge!r}. "
                f"Expected one of {self.VALID_BRIDGES}."
            )

        if self.tip not in self.VALID_TIPS:
            raise ValueError(
                f"Invalid nose tip: {self.tip!r}. "
                f"Expected one of {self.VALID_TIPS}."
            )

        if self.nostril_shape not in self.VALID_NOSTRIL_SHAPES:
            raise ValueError(
                f"Invalid nostril shape: {self.nostril_shape!r}. "
                f"Expected one of {self.VALID_NOSTRIL_SHAPES}."
            )

        if not 0.0 <= self.nostril_visibility <= 1.0:
            raise ValueError(
                "Nose nostril visibility must be between 0 and 1."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "height": self.height,
            "width": self.width,
            "projection": self.projection,
            "bridge": self.bridge,
            "tip": self.tip,
            "nostril_shape": self.nostril_shape,
            "nostril_visibility": self.nostril_visibility,
        }