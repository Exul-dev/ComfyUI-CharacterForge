from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide
from .glute import Glute


class GlutealRegion(AnatomyComponent):
    """Bilateral gluteal region (pattern MammaryRegion).

    Each side owns a complete Glute; cleft_depth describes the
    intergluteal cleft (midline).
    """

    component_type = "gluteal_region"

    def __init__(
        self,
        *,
        left: Glute | None = None,
        right: Glute | None = None,
        cleft_depth: float = 0.5,
    ) -> None:
        super().__init__()

        self.left = left or Glute(side=BodySide.LEFT)
        self.right = right or Glute(side=BodySide.RIGHT)
        self.cleft_depth = float(cleft_depth)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.left, Glute):
            raise ValueError(
                "GlutealRegion.left must be a Glute instance."
            )

        if not isinstance(self.right, Glute):
            raise ValueError(
                "GlutealRegion.right must be a Glute instance."
            )

        if self.left.side is not BodySide.LEFT:
            raise ValueError(
                "GlutealRegion.left must have BodySide.LEFT."
            )

        if self.right.side is not BodySide.RIGHT:
            raise ValueError(
                "GlutealRegion.right must have BodySide.RIGHT."
            )

        if not 0.0 <= self.cleft_depth <= 1.0:
            raise ValueError(
                "GlutealRegion cleft_depth must be between 0 and 1."
            )

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
            "cleft_depth": self.cleft_depth,
        }