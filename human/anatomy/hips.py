from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide
from .hip import Hip


class Hips(AnatomyComponent):
    """Bilateral hip container.

    Each side owns a complete Hip; cross-validated.
    """

    component_type = "hips"

    def __init__(
        self,
        *,
        left: Hip | None = None,
        right: Hip | None = None,
    ) -> None:
        super().__init__()

        self.left = left or Hip(side=BodySide.LEFT)
        self.right = right or Hip(side=BodySide.RIGHT)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.left, Hip):
            raise ValueError("Hips.left must be a Hip instance.")

        if not isinstance(self.right, Hip):
            raise ValueError("Hips.right must be a Hip instance.")

        if self.left.side is not BodySide.LEFT:
            raise ValueError("Hips.left must have BodySide.LEFT.")

        if self.right.side is not BodySide.RIGHT:
            raise ValueError("Hips.right must have BodySide.RIGHT.")

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }