from __future__ import annotations

from typing import Any

from ..base.semantic import SemanticComponent
from .coordinate_space import CoordinateSpace


class CoordinateSystem(SemanticComponent):
    """
    Explicit definition of a coordinate system.

    A coordinate system describes the semantic meaning of each axis,
    its dimensionality, handedness and origin.

    It does not contain coordinate values itself.
    """

    component_type = "coordinate_system"

    VALID_HANDEDNESS = (
        "right",
        "left",
        "none",
    )

    def __init__(
        self,
        *,
        name: str,
        space: CoordinateSpace,
        x_axis: str,
        y_axis: str,
        z_axis: str | None = None,
        handedness: str = "none",
        origin: str = "origin",
    ) -> None:
        super().__init__()

        self.name = str(name)
        self.space = space
        self.x_axis = str(x_axis)
        self.y_axis = str(y_axis)
        self.z_axis = None if z_axis is None else str(z_axis)
        self.handedness = str(handedness)
        self.origin = str(origin)

        self.validate()

    @classmethod
    def anatomical_normalized(cls) -> "CoordinateSystem":
        """
        Return CharacterForge's canonical normalized anatomical frame.

        X: left/right
        Y: superior/inferior
        Z: posterior/anterior

        Values remain normalized coordinates and are not physical
        measurements such as centimeters.
        """

        return cls(
            name="anatomical_normalized",
            space=CoordinateSpace.NORMALIZED_3D,
            x_axis="left_right",
            y_axis="superior_inferior",
            z_axis="posterior_anterior",
            handedness="right",
            origin="anatomical_origin",
        )

    def validate(self) -> None:
        super().validate()

        if not self.name.strip():
            raise ValueError(
                "CoordinateSystem name must not be empty."
            )

        if not isinstance(self.space, CoordinateSpace):
            raise ValueError(
                "CoordinateSystem space must be a CoordinateSpace."
            )

        if not self.x_axis.strip():
            raise ValueError(
                "CoordinateSystem x_axis must not be empty."
            )

        if not self.y_axis.strip():
            raise ValueError(
                "CoordinateSystem y_axis must not be empty."
            )

        if self.space.dimensions == 3 and not self.z_axis:
            raise ValueError(
                "3D CoordinateSystem requires z_axis."
            )

        if self.space.dimensions == 2 and self.z_axis is not None:
            raise ValueError(
                "2D CoordinateSystem must not define z_axis."
            )

        if self.handedness not in self.VALID_HANDEDNESS:
            raise ValueError(
                f"Invalid coordinate system handedness: "
                f"{self.handedness!r}."
            )

        if not self.origin.strip():
            raise ValueError(
                "CoordinateSystem origin must not be empty."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "name": self.name,
            "space": self.space.value,
            "x_axis": self.x_axis,
            "y_axis": self.y_axis,
            "z_axis": self.z_axis,
            "handedness": self.handedness,
            "origin": self.origin,
        }