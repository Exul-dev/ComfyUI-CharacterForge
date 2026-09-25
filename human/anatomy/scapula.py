from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Scapula(AnatomyComponent):
    """Represents one scapula (shoulder blade).

    winging describes scapular winging (the medial border lifting
    off the rib cage — a real clinical condition): per-side, so
    UNILATERAL winging stays representable.
    """

    component_type = "scapula"

    VALID_SHAPES = (
        "flat",
        "average",
        "broad",
        "prominent",
    )

    def __init__(
        self,
        *,
        side: BodySide,
        width: float = 11.0,
        height: float = 14.0,
        prominence: float = 0.4,
        winging: float = 0.05,
        shape: str = "average",
    ) -> None:
        super().__init__()

        self.side = side
        self.width = float(width)
        self.height = float(height)
        self.prominence = float(prominence)
        self.winging = float(winging)
        self.shape = shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError(
                "Scapula side must be a BodySide value."
            )

        if self.width <= 0:
            raise ValueError(
                "Scapula width must be greater than zero."
            )

        if self.height <= 0:
            raise ValueError(
                "Scapula height must be greater than zero."
            )

        for name in ("prominence", "winging"):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Scapula {name} must be between 0 and 1."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid scapula shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "width": self.width,
            "height": self.height,
            "prominence": self.prominence,
            "winging": self.winging,
            "shape": self.shape,
        }


class Scapulae(AnatomyComponent):
    """Bilateral scapula container."""

    component_type = "scapulae"

    def __init__(
        self,
        *,
        left: Scapula | None = None,
        right: Scapula | None = None,
    ) -> None:
        super().__init__()

        self.left = left or Scapula(side=BodySide.LEFT)
        self.right = right or Scapula(side=BodySide.RIGHT)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.left, Scapula):
            raise ValueError(
                "Scapulae.left must be a Scapula instance."
            )

        if not isinstance(self.right, Scapula):
            raise ValueError(
                "Scapulae.right must be a Scapula instance."
            )

        if self.left.side is not BodySide.LEFT:
            raise ValueError(
                "Scapulae.left must have BodySide.LEFT."
            )

        if self.right.side is not BodySide.RIGHT:
            raise ValueError(
                "Scapulae.right must have BodySide.RIGHT."
            )

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }