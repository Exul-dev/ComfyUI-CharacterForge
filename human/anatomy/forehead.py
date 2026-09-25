from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Forehead(AnatomyComponent):
    """Structural morphology of the forehead."""

    component_type = "forehead"

    VALID_SHAPES = (
        "flat",
        "average",
        "rounded",
        "sloped",
        "prominent",
        "receding",
    )

    def __init__(
        self,
        *,
        height: float = 5.8,
        width: float = 12.0,
        projection: float = 2.5,
        slope: float = 0.0,
        curvature: float = 0.5,
        temporal_width: float = 10.0,
        shape: str = "average",
        symmetry: float = 1.0,
    ) -> None:
        super().__init__()

        self.height = float(height)
        self.width = float(width)
        self.projection = float(projection)
        self.slope = float(slope)
        self.curvature = float(curvature)
        self.temporal_width = float(temporal_width)
        self.shape = shape
        self.symmetry = float(symmetry)

        self.validate()

    def validate(self) -> None:
        super().validate()

        for name, value in {
            "height": self.height,
            "width": self.width,
            "projection": self.projection,
            "temporal_width": self.temporal_width,
        }.items():
            if value <= 0:
                raise ValueError(
                    f"Forehead {name} must be greater than zero."
                )

        for name, value in {
            "curvature": self.curvature,
            "symmetry": self.symmetry,
        }.items():
            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Forehead {name} must be between 0 and 1."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid forehead shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "height": self.height,
            "width": self.width,
            "projection": self.projection,
            "slope": self.slope,
            "curvature": self.curvature,
            "temporal_width": self.temporal_width,
            "shape": self.shape,
            "symmetry": self.symmetry,
        }
