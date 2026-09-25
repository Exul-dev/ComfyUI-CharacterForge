from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Philtrum(AnatomyComponent):
    """Represents the philtrum (upper lip groove)."""

    component_type = "philtrum"

    VALID_SHAPES = (
        "shallow",
        "average",
        "deep",
        "broad",
        "narrow",
    )

    def __init__(
        self,
        *,
        length: float = 1.5,
        width: float = 1.1,
        depth: float = 0.5,
        shape: str = "average",
    ) -> None:
        super().__init__()

        self.length = float(length)
        self.width = float(width)
        self.depth = float(depth)
        self.shape = shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        dimensions = {
            "length": self.length,
            "width": self.width,
            "depth": self.depth,
        }

        for name, value in dimensions.items():
            if value <= 0:
                raise ValueError(
                    f"Philtrum {name} must be greater than zero."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid philtrum shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "length": self.length,
            "width": self.width,
            "depth": self.depth,
            "shape": self.shape,
        }


class Mouth(AnatomyComponent):
    """Represents the anatomical mouth.

    Landmark anchors: stomion (midline), labiale_superius and
    labiale_inferius (lip vermilions), left_cheilion and
    right_cheilion (corners) — see FacialLandmarks for the
    coordinate-level counterparts.
    """

    component_type = "mouth"

    VALID_SHAPES = (
        "full",
        "thin",
        "wide",
        "heart",
        "bow",
    )

    VALID_CORNER_POSITIONS = (
        "downturned",
        "level",
        "upturned",
    )

    def __init__(
        self,
        *,
        width: float = 5.0,
        lip_upper_thickness: float = 0.9,
        lip_lower_thickness: float = 1.1,
        corner_position: str = "level",
        opening: float = 0.0,
        shape: str = "full",
        philtrum: Philtrum | None = None,
    ) -> None:
        super().__init__()

        self.width = float(width)
        self.lip_upper_thickness = float(lip_upper_thickness)
        self.lip_lower_thickness = float(lip_lower_thickness)
        self.corner_position = corner_position
        self.opening = float(opening)
        self.shape = shape
        self.philtrum = philtrum or Philtrum()

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.width <= 0:
            raise ValueError("Mouth width must be greater than zero.")

        if self.lip_upper_thickness <= 0:
            raise ValueError(
                "Mouth upper lip thickness must be greater than zero."
            )

        if self.lip_lower_thickness <= 0:
            raise ValueError(
                "Mouth lower lip thickness must be greater than zero."
            )

        if self.corner_position not in self.VALID_CORNER_POSITIONS:
            raise ValueError(
                f"Invalid mouth corner position: "
                f"{self.corner_position!r}. "
                f"Expected one of {self.VALID_CORNER_POSITIONS}."
            )

        if not 0.0 <= self.opening <= 1.0:
            raise ValueError(
                "Mouth opening must be between 0 and 1."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid mouth shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if not isinstance(self.philtrum, Philtrum):
            raise ValueError(
                "Mouth philtrum must be a Philtrum instance."
            )

        self.philtrum.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "width": self.width,
            "lip_upper_thickness": self.lip_upper_thickness,
            "lip_lower_thickness": self.lip_lower_thickness,
            "corner_position": self.corner_position,
            "opening": self.opening,
            "shape": self.shape,
            "philtrum": self.philtrum.to_dict(),
        }