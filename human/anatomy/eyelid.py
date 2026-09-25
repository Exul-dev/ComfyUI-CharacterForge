from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Eyelid(AnatomyComponent):
    """Represents the eyelid structure of one eye.

    The eye_shape field is the overall visible eye form (how the
    lids frame the eye); crease is the upper-lid fold. Hooded and
    monolid describe the two most identity-defining lid variants.
    """

    component_type = "eyelid"

    VALID_EYE_SHAPES = (
        "round",
        "almond",
        "hooded",
        "monolid",
        "upturned",
        "downturned",
    )

    VALID_CREASES = (
        "single",
        "double",
        "hooded",
    )

    def __init__(
        self,
        *,
        side: BodySide,
        eye_shape: str = "almond",
        crease: str = "double",
        upper_exposure: float = 0.6,
        lower_exposure: float = 0.4,
        thickness: float = 0.4,
    ) -> None:
        super().__init__()

        self.side = side
        self.eye_shape = eye_shape
        self.crease = crease
        self.upper_exposure = float(upper_exposure)
        self.lower_exposure = float(lower_exposure)
        self.thickness = float(thickness)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError(
                "Eyelid side must be a BodySide value."
            )

        if self.eye_shape not in self.VALID_EYE_SHAPES:
            raise ValueError(
                f"Invalid eyelid eye_shape: {self.eye_shape!r}. "
                f"Expected one of {self.VALID_EYE_SHAPES}."
            )

        if self.crease not in self.VALID_CREASES:
            raise ValueError(
                f"Invalid eyelid crease: {self.crease!r}. "
                f"Expected one of {self.VALID_CREASES}."
            )

        for name in (
            "upper_exposure",
            "lower_exposure",
            "thickness",
        ):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Eyelid {name} must be between 0 and 1."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "eye_shape": self.eye_shape,
            "crease": self.crease,
            "upper_exposure": self.upper_exposure,
            "lower_exposure": self.lower_exposure,
            "thickness": self.thickness,
        }


class Eyelids(AnatomyComponent):
    """Bilateral eyelid container."""

    component_type = "eyelids"

    def __init__(
        self,
        *,
        left: Eyelid | None = None,
        right: Eyelid | None = None,
    ) -> None:
        super().__init__()

        self.left = left or Eyelid(side=BodySide.LEFT)
        self.right = right or Eyelid(side=BodySide.RIGHT)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.left, Eyelid):
            raise ValueError(
                "Eyelids.left must be an Eyelid instance."
            )

        if not isinstance(self.right, Eyelid):
            raise ValueError(
                "Eyelids.right must be an Eyelid instance."
            )

        if self.left.side is not BodySide.LEFT:
            raise ValueError(
                "Eyelids.left must have BodySide.LEFT."
            )

        if self.right.side is not BodySide.RIGHT:
            raise ValueError(
                "Eyelids.right must have BodySide.RIGHT."
            )

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }