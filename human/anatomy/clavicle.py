from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Clavicle(AnatomyComponent):
    """Represents one clavicle (collarbone).

    Visibility is how much the bone reads under the skin — the
    difference between a delicate and an emaciated collarbone.
    """

    component_type = "clavicle"

    def __init__(
        self,
        *,
        side: BodySide,
        length: float = 15.0,
        prominence: float = 0.5,
        slope: float = 0.5,
        visibility: float = 0.5,
    ) -> None:
        super().__init__()

        self.side = side
        self.length = float(length)
        self.prominence = float(prominence)
        self.slope = float(slope)
        self.visibility = float(visibility)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError(
                "Clavicle side must be a BodySide value."
            )

        if self.length <= 0:
            raise ValueError(
                "Clavicle length must be greater than zero."
            )

        for name in ("prominence", "slope", "visibility"):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Clavicle {name} must be between 0 and 1."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "length": self.length,
            "prominence": self.prominence,
            "slope": self.slope,
            "visibility": self.visibility,
        }


class Clavicles(AnatomyComponent):
    """Bilateral clavicle container."""

    component_type = "clavicles"

    def __init__(
        self,
        *,
        left: Clavicle | None = None,
        right: Clavicle | None = None,
    ) -> None:
        super().__init__()

        self.left = left or Clavicle(side=BodySide.LEFT)
        self.right = right or Clavicle(side=BodySide.RIGHT)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.left, Clavicle):
            raise ValueError(
                "Clavicles.left must be a Clavicle instance."
            )

        if not isinstance(self.right, Clavicle):
            raise ValueError(
                "Clavicles.right must be a Clavicle instance."
            )

        if self.left.side is not BodySide.LEFT:
            raise ValueError(
                "Clavicles.left must have BodySide.LEFT."
            )

        if self.right.side is not BodySide.RIGHT:
            raise ValueError(
                "Clavicles.right must have BodySide.RIGHT."
            )

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }