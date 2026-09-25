from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide
from .leg import Leg


class Legs(AnatomyComponent):
    """Composite anatomical component representing both legs.

    Fully bilateral model: each side owns a complete Leg, and the
    sides are cross-validated. Bilateral asymmetry (one muscular
    thigh, one slender thigh) stays representable.
    """

    component_type = "legs"

    def __init__(
        self,
        *,
        left: Leg | None = None,
        right: Leg | None = None,
    ) -> None:
        super().__init__()

        self.left = left or Leg(side=BodySide.LEFT)
        self.right = right or Leg(side=BodySide.RIGHT)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.left, Leg):
            raise ValueError("Legs.left must be a Leg instance.")

        if not isinstance(self.right, Leg):
            raise ValueError("Legs.right must be a Leg instance.")

        if self.left.side is not BodySide.LEFT:
            raise ValueError("Legs.left must have BodySide.LEFT.")

        if self.right.side is not BodySide.RIGHT:
            raise ValueError("Legs.right must have BodySide.RIGHT.")

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }