from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Brow(AnatomyComponent):
    """Represents one eyebrow as a facial STRUCTURE.

    Position, arch, thickness and shape are identity-defining
    facial traits and live here (anatomy). The hair color and
    texture of the brow belong to the future facial-hair
    appearance component, by the H5-C design note.
    """

    component_type = "brow"

    VALID_THICKNESSES = (
        "fine",
        "medium",
        "thick",
    )

    VALID_ARCHES = (
        "flat",
        "gentle",
        "high",
        "angled",
    )

    VALID_SHAPES = (
        "straight",
        "curved",
        "angled",
        "rounded",
    )

    def __init__(
        self,
        *,
        side: BodySide,
        thickness: str = "medium",
        arch: str = "gentle",
        height: float = 0.5,
        length: float = 5.5,
        shape: str = "curved",
        density: float = 0.6,
    ) -> None:
        super().__init__()

        self.side = side
        self.thickness = thickness
        self.arch = arch
        self.height = float(height)
        self.length = float(length)
        self.shape = shape
        self.density = float(density)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError(
                "Brow side must be a BodySide value."
            )

        if self.thickness not in self.VALID_THICKNESSES:
            raise ValueError(
                f"Invalid brow thickness: {self.thickness!r}. "
                f"Expected one of {self.VALID_THICKNESSES}."
            )

        if self.arch not in self.VALID_ARCHES:
            raise ValueError(
                f"Invalid brow arch: {self.arch!r}. "
                f"Expected one of {self.VALID_ARCHES}."
            )

        if not 0.0 <= self.height <= 1.0:
            raise ValueError(
                "Brow height must be between 0 and 1."
            )

        if self.length <= 0:
            raise ValueError(
                "Brow length must be greater than zero."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid brow shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if not 0.0 <= self.density <= 1.0:
            raise ValueError(
                "Brow density must be between 0 and 1."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "thickness": self.thickness,
            "arch": self.arch,
            "height": self.height,
            "length": self.length,
            "shape": self.shape,
            "density": self.density,
        }


class Brows(AnatomyComponent):
    """Bilateral brow container."""

    component_type = "brows"

    def __init__(
        self,
        *,
        left: Brow | None = None,
        right: Brow | None = None,
    ) -> None:
        super().__init__()

        self.left = left or Brow(side=BodySide.LEFT)
        self.right = right or Brow(side=BodySide.RIGHT)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.left, Brow):
            raise ValueError(
                "Brows.left must be a Brow instance."
            )

        if not isinstance(self.right, Brow):
            raise ValueError(
                "Brows.right must be a Brow instance."
            )

        if self.left.side is not BodySide.LEFT:
            raise ValueError(
                "Brows.left must have BodySide.LEFT."
            )

        if self.right.side is not BodySide.RIGHT:
            raise ValueError(
                "Brows.right must have BodySide.RIGHT."
            )

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }