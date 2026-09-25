from __future__ import annotations

import math
from typing import Any

from ..base.semantic import SemanticComponent
from .coordinate_space import CoordinateSpace
from .coordinate_system import CoordinateSystem


class Coordinate(SemanticComponent):
    """
    Semantic coordinate value bound to an explicit coordinate space
    and coordinate system.
    """

    component_type = "coordinate"

    def __init__(
        self,
        *,
        x: float,
        y: float,
        z: float | None = None,
        space: CoordinateSpace,
        system: CoordinateSystem | None = None,
    ) -> None:
        super().__init__()

        self.x = float(x)
        self.y = float(y)
        self.z = None if z is None else float(z)
        self.space = space
        self.system = system

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.space, CoordinateSpace):
            raise ValueError(
                "Coordinate space must be a CoordinateSpace."
            )

        values = [self.x, self.y]

        if self.z is not None:
            values.append(self.z)

        if not all(math.isfinite(value) for value in values):
            raise ValueError(
                "Coordinate values must be finite numbers."
            )

        expected_dimensions = self.space.dimensions

        if expected_dimensions == 2 and self.z is not None:
            raise ValueError(
                "IMAGE_2D coordinates must contain exactly x and y."
            )

        if expected_dimensions == 3 and self.z is None:
            raise ValueError(
                "3D coordinates require x, y and z."
            )

        if self.system is not None:
            if not isinstance(self.system, CoordinateSystem):
                raise ValueError(
                    "Coordinate system must be a CoordinateSystem."
                )

            if self.system.space is not self.space:
                raise ValueError(
                    "Coordinate space and coordinate system space "
                    "must match."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "space": self.space.value,
            "system": (
                self.system.to_dict()
                if self.system is not None
                else None
            ),
        }