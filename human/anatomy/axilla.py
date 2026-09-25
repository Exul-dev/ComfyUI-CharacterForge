from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Axilla(AnatomyComponent):
    """Represents one axilla (armpit).

    hair_density is structural coverage (0 = none, the shaved or
    hairless case); hair color and texture belong to the future
    body-hair appearance component.
    """

    component_type = "axilla"

    def __init__(
        self,
        *,
        side: BodySide,
        depth: float = 0.4,
        hollow_visibility: float = 0.5,
        hair_density: float = 0.5,
    ) -> None:
        super().__init__()

        self.side = side
        self.depth = float(depth)
        self.hollow_visibility = float(hollow_visibility)
        self.hair_density = float(hair_density)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError(
                "Axilla side must be a BodySide value."
            )

        for name in ("depth", "hollow_visibility", "hair_density"):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Axilla {name} must be between 0 and 1."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "depth": self.depth,
            "hollow_visibility": self.hollow_visibility,
            "hair_density": self.hair_density,
        }


class Axillae(AnatomyComponent):
    """Bilateral axilla container."""

    component_type = "axillae"

    def __init__(
        self,
        *,
        left: Axilla | None = None,
        right: Axilla | None = None,
    ) -> None:
        super().__init__()

        self.left = left or Axilla(side=BodySide.LEFT)
        self.right = right or Axilla(side=BodySide.RIGHT)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.left, Axilla):
            raise ValueError(
                "Axillae.left must be an Axilla instance."
            )

        if not isinstance(self.right, Axilla):
            raise ValueError(
                "Axillae.right must be an Axilla instance."
            )

        if self.left.side is not BodySide.LEFT:
            raise ValueError(
                "Axillae.left must have BodySide.LEFT."
            )

        if self.right.side is not BodySide.RIGHT:
            raise ValueError(
                "Axillae.right must have BodySide.RIGHT."
            )

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }