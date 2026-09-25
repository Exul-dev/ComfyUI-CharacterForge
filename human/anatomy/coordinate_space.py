from __future__ import annotations

from enum import Enum


class CoordinateSpace(Enum):
    """Semantic space in which a coordinate is expressed."""

    IMAGE_2D = "image_2d"
    NORMALIZED_3D = "normalized_3d"
    PHYSICAL_3D = "physical_3d"

    @property
    def dimensions(self) -> int:
        """Return the dimensionality of the coordinate space."""

        if self is CoordinateSpace.IMAGE_2D:
            return 2

        return 3