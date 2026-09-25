from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .breast import BreastUnit
from .enums import BodySide


class MammaryRegion(AnatomyComponent):
    """Bilateral anatomical mammary region."""

    component_type = "mammary_region"

    def __init__(
        self,
        *,
        left: BreastUnit | None = None,
        right: BreastUnit | None = None,
        symmetry: float = 1.0,
    ) -> None:
        super().__init__()

        self.left = left or BreastUnit(side=BodySide.LEFT)
        self.right = right or BreastUnit(side=BodySide.RIGHT)
        self.symmetry = float(symmetry)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.left, BreastUnit):
            raise ValueError(
                "MammaryRegion.left must be a BreastUnit instance."
            )

        if not isinstance(self.right, BreastUnit):
            raise ValueError(
                "MammaryRegion.right must be a BreastUnit instance."
            )

        if self.left.side != BodySide.LEFT:
            raise ValueError("MammaryRegion.left must have BodySide.LEFT.")

        if self.right.side != BodySide.RIGHT:
            raise ValueError("MammaryRegion.right must have BodySide.RIGHT.")

        if not 0.0 <= self.symmetry <= 1.0:
            raise ValueError(
                "Mammary region symmetry must be between 0 and 1."
            )

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
            "symmetry": self.symmetry,
        }
