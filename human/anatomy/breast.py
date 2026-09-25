from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .areola import Areola
from .enums import BodySide
from .nipple import Nipple


class Breast(AnatomyComponent):
    """Represents one side of the anatomical mammary region."""

    component_type = "breast"

    VALID_SHAPES = (
        "flat",
        "average",
        "round",
        "teardrop",
        "conical",
        "athletic",
        "broad",
        "projected",
    )

    def __init__(
        self,
        *,
        side: BodySide = BodySide.RIGHT,
        volume: float = 500.0,
        width: float = 13.0,
        height: float = 12.0,
        projection: float = 5.0,
        base_diameter: float = 12.0,
        upper_fullness: float = 0.5,
        lower_fullness: float = 0.5,
        inner_fullness: float = 0.5,
        outer_fullness: float = 0.5,
        shape: str = "average",
        vertical_position: float = 0.5,
        horizontal_position: float = 0.5,
        orientation: float = 0.0,
        firmness: float = 0.5,
    ) -> None:
        super().__init__()

        self.side = side
        self.volume = float(volume)
        self.width = float(width)
        self.height = float(height)
        self.projection = float(projection)
        self.base_diameter = float(base_diameter)
        self.upper_fullness = float(upper_fullness)
        self.lower_fullness = float(lower_fullness)
        self.inner_fullness = float(inner_fullness)
        self.outer_fullness = float(outer_fullness)
        self.shape = shape
        self.vertical_position = float(vertical_position)
        self.horizontal_position = float(horizontal_position)
        self.orientation = float(orientation)
        self.firmness = float(firmness)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Breast side must be a BodySide value.")

        positive_dimensions = {
            "volume": self.volume,
            "width": self.width,
            "height": self.height,
            "projection": self.projection,
            "base_diameter": self.base_diameter,
        }

        for name, value in positive_dimensions.items():
            if value <= 0:
                raise ValueError(
                    f"Breast {name} must be greater than zero."
                )

        bounded_values = {
            "upper_fullness": self.upper_fullness,
            "lower_fullness": self.lower_fullness,
            "inner_fullness": self.inner_fullness,
            "outer_fullness": self.outer_fullness,
            "vertical_position": self.vertical_position,
            "horizontal_position": self.horizontal_position,
            "firmness": self.firmness,
        }

        for name, value in bounded_values.items():
            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Breast {name} must be between 0 and 1."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid breast shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "volume": self.volume,
            "width": self.width,
            "height": self.height,
            "projection": self.projection,
            "base_diameter": self.base_diameter,
            "upper_fullness": self.upper_fullness,
            "lower_fullness": self.lower_fullness,
            "inner_fullness": self.inner_fullness,
            "outer_fullness": self.outer_fullness,
            "shape": self.shape,
            "vertical_position": self.vertical_position,
            "horizontal_position": self.horizontal_position,
            "orientation": self.orientation,
            "firmness": self.firmness,
        }


class BreastUnit(AnatomyComponent):
    """Composite unit containing breast, areola and nipple."""

    component_type = "breast_unit"

    def __init__(
        self,
        *,
        side: BodySide,
        breast: Breast | None = None,
        areola: Areola | None = None,
        nipple: Nipple | None = None,
    ) -> None:
        super().__init__()

        self.side = side
        self.breast = breast or Breast(side=side)
        self.areola = areola or Areola(side=side)
        self.nipple = nipple or Nipple(side=side)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("BreastUnit side must be a BodySide value.")

        if not isinstance(self.breast, Breast):
            raise ValueError("BreastUnit.breast must be a Breast instance.")

        if not isinstance(self.areola, Areola):
            raise ValueError("BreastUnit.areola must be an Areola instance.")

        if not isinstance(self.nipple, Nipple):
            raise ValueError("BreastUnit.nipple must be a Nipple instance.")

        if self.breast.side != self.side:
            raise ValueError("Breast side does not match BreastUnit side.")

        if self.areola.side != self.side:
            raise ValueError("Areola side does not match BreastUnit side.")

        if self.nipple.side != self.side:
            raise ValueError("Nipple side does not match BreastUnit side.")

        self.breast.validate()
        self.areola.validate()
        self.nipple.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "breast": self.breast.to_dict(),
            "areola": self.areola.to_dict(),
            "nipple": self.nipple.to_dict(),
        }
