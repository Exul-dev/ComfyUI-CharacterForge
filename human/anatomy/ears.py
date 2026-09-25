from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .ear import Ear
from .enums import BodySide


class Ears(AnatomyComponent):
    """Composite anatomical component representing both ears.

    Fully bilateral model: each side owns a complete Ear, and the
    sides are cross-validated. Bilateral asymmetry stays
    representable.
    """

    component_type = "ears"

    def __init__(
        self,
        *,
        left: Ear | None = None,
        right: Ear | None = None,
    ) -> None:
        super().__init__()

        self.left = left or Ear(side=BodySide.LEFT)
        self.right = right or Ear(side=BodySide.RIGHT)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.left, Ear):
            raise ValueError("Ears.left must be an Ear instance.")

        if not isinstance(self.right, Ear):
            raise ValueError("Ears.right must be an Ear instance.")

        if self.left.side is not BodySide.LEFT:
            raise ValueError("Ears.left must have BodySide.LEFT.")

        if self.right.side is not BodySide.RIGHT:
            raise ValueError("Ears.right must have BodySide.RIGHT.")

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }