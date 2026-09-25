from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide
from .flank import Flank


class Flanks(AnatomyComponent):
    """Bilateral flank container.

    Each side owns a complete Flank; cross-validated.
    """

    component_type = "flanks"

    def __init__(
        self,
        *,
        left: Flank | None = None,
        right: Flank | None = None,
    ) -> None:
        super().__init__()

        self.left = left or Flank(side=BodySide.LEFT)
        self.right = right or Flank(side=BodySide.RIGHT)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.left, Flank):
            raise ValueError(
                "Flanks.left must be a Flank instance."
            )

        if not isinstance(self.right, Flank):
            raise ValueError(
                "Flanks.right must be a Flank instance."
            )

        if self.left.side is not BodySide.LEFT:
            raise ValueError(
                "Flanks.left must have BodySide.LEFT."
            )

        if self.right.side is not BodySide.RIGHT:
            raise ValueError(
                "Flanks.right must have BodySide.RIGHT."
            )

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }