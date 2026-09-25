from __future__ import annotations

from typing import Any

from ..base.semantic import SemanticComponent
from ..anatomy.enums import BodySide
from .eye import Eye


class Eyes(SemanticComponent):
    """Composite appearance component representing both eyes.

    Fully bilateral model: each side owns a complete Eye, and the
    sides are cross-validated. Heterochromia needs no explicit
    field: it is simply left.iris_color != right.iris_color.
    """

    component_type = "eyes"

    def __init__(
        self,
        *,
        left: Eye | None = None,
        right: Eye | None = None,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.left = left or Eye(side=BodySide.LEFT)
        self.right = right or Eye(side=BodySide.RIGHT)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.left, Eye):
            raise ValueError(
                "Eyes.left must be an Eye instance."
            )

        if not isinstance(self.right, Eye):
            raise ValueError(
                "Eyes.right must be an Eye instance."
            )

        if self.left.side is not BodySide.LEFT:
            raise ValueError(
                "Eyes.left must have BodySide.LEFT."
            )

        if self.right.side is not BodySide.RIGHT:
            raise ValueError(
                "Eyes.right must have BodySide.RIGHT."
            )

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }