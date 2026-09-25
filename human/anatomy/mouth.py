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


class Teeth(AnatomyComponent):
    """Represents the dental structure (mouth interior).

    Structural description: the color/whiteness scale is included
    here because it is intrinsic to the teeth, not applied
    appearance.
    """

    component_type = "teeth"

    VALID_ALIGNMENTS = (
        "straight",
        "slightly_uneven",
        "uneven",
        "crowded",
        "gapped",
    )

    VALID_SHAPES = (
        "square",
        "oval",
        "tapered",
    )

    VALID_CONDITIONS = (
        "healthy",
        "worn",
        "chipped",
        "damaged",
    )

    def __init__(
        self,
        *,
        alignment: str = "straight",
        size: float = 0.5,
        whiteness: float = 0.6,
        shape: str = "oval",
        condition: str = "healthy",
    ) -> None:
        super().__init__()

        self.alignment = alignment
        self.size = float(size)
        self.whiteness = float(whiteness)
        self.shape = shape
        self.condition = condition

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.alignment not in self.VALID_ALIGNMENTS:
            raise ValueError(
                f"Invalid teeth alignment: {self.alignment!r}. "
                f"Expected one of {self.VALID_ALIGNMENTS}."
            )

        if not 0.0 <= self.size <= 1.0:
            raise ValueError(
                "Teeth size must be between 0 and 1."
            )

        if not 0.0 <= self.whiteness <= 1.0:
            raise ValueError(
                "Teeth whiteness must be between 0 and 1."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid teeth shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if self.condition not in self.VALID_CONDITIONS:
            raise ValueError(
                f"Invalid teeth condition: {self.condition!r}. "
                f"Expected one of {self.VALID_CONDITIONS}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "alignment": self.alignment,
            "size": self.size,
            "whiteness": self.whiteness,
            "shape": self.shape,
            "condition": self.condition,
        }


class Tongue(AnatomyComponent):
    """Represents the tongue (mouth interior)."""

    component_type = "tongue"

    VALID_TIPS = (
        "pointed",
        "rounded",
        "broad",
    )

    def __init__(
        self,
        *,
        length: float = 8.0,
        width: float = 4.0,
        thickness: float = 1.8,
        tip: str = "rounded",
    ) -> None:
        super().__init__()

        self.length = float(length)
        self.width = float(width)
        self.thickness = float(thickness)
        self.tip = tip

        self.validate()

    def validate(self) -> None:
        super().validate()

        dimensions = {
            "length": self.length,
            "width": self.width,
            "thickness": self.thickness,
        }

        for name, value in dimensions.items():
            if value <= 0:
                raise ValueError(
                    f"Tongue {name} must be greater than zero."
                )

        if self.tip not in self.VALID_TIPS:
            raise ValueError(
                f"Invalid tongue tip: {self.tip!r}. "
                f"Expected one of {self.VALID_TIPS}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "length": self.length,
            "width": self.width,
            "thickness": self.thickness,
            "tip": self.tip,
        }


class Mouth(AnatomyComponent):
    """Represents the anatomical mouth.

    Composite since H4.19-A: the interior structure (teeth,
    tongue) joins the philtrum as a sub-component. Landmark
    anchors: stomion, labiale_superius/inferius, cheilion L/R.
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
        teeth: Teeth | None = None,
        tongue: Tongue | None = None,
    ) -> None:
        super().__init__()

        self.width = float(width)
        self.lip_upper_thickness = float(lip_upper_thickness)
        self.lip_lower_thickness = float(lip_lower_thickness)
        self.corner_position = corner_position
        self.opening = float(opening)
        self.shape = shape
        self.philtrum = philtrum or Philtrum()
        self.teeth = teeth or Teeth()
        self.tongue = tongue or Tongue()

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

        if not isinstance(self.teeth, Teeth):
            raise ValueError(
                "Mouth teeth must be a Teeth instance."
            )

        if not isinstance(self.tongue, Tongue):
            raise ValueError(
                "Mouth tongue must be a Tongue instance."
            )

        self.philtrum.validate()
        self.teeth.validate()
        self.tongue.validate()

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
            "teeth": self.teeth.to_dict(),
            "tongue": self.tongue.to_dict(),
        }