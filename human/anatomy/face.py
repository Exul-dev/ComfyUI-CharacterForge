from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .cheek_structure import CheekStructure
from .chin import Chin
from .enums import BodySide
from .face_dimensions import FaceDimensions
from .facial_landmarks import FacialLandmarks
from .facial_proportions import FacialProportions
from .facial_symmetry import FacialSymmetry
from .forehead import Forehead
from .jaw import Jaw


class Face(AnatomyComponent):
    """Parametric morphometric structure of a human face."""

    component_type = "face"

    VALID_SHAPES = (
        "narrow",
        "average",
        "broad",
        "round",
        "oval",
        "square",
        "heart",
        "diamond",
        "oblong",
        "triangular",
    )

    def __init__(
        self,
        *,
        height: float = 18.0,
        width: float = 14.0,
        depth: float = 10.0,
        forehead_width: float = 12.0,
        cheekbone_width: float = 14.0,
        jaw_width: float = 12.0,
        jaw_depth: float = 8.0,
        shape: str = "oval",
        symmetry: float = 1.0,
        dimensions: FaceDimensions | None = None,
        proportions: FacialProportions | None = None,
        forehead: Forehead | None = None,
        left_cheek: CheekStructure | None = None,
        right_cheek: CheekStructure | None = None,
        left_jaw: Jaw | None = None,
        right_jaw: Jaw | None = None,
        chin: Chin | None = None,
        facial_symmetry: FacialSymmetry | None = None,
        landmarks: FacialLandmarks | None = None,
    ) -> None:
        super().__init__()

        self.height = float(height)
        self.width = float(width)
        self.depth = float(depth)
        self.forehead_width = float(forehead_width)
        self.cheekbone_width = float(cheekbone_width)
        self.jaw_width = float(jaw_width)
        self.jaw_depth = float(jaw_depth)
        self.shape = shape
        self.symmetry = float(symmetry)

        self.dimensions = dimensions or FaceDimensions()
        self.proportions = proportions or FacialProportions()
        self.forehead = forehead or Forehead()
        self.left_cheek = left_cheek or CheekStructure(side=BodySide.LEFT)
        self.right_cheek = right_cheek or CheekStructure(side=BodySide.RIGHT)
        self.left_jaw = left_jaw or Jaw(side=BodySide.LEFT)
        self.right_jaw = right_jaw or Jaw(side=BodySide.RIGHT)
        self.chin = chin or Chin()
        self.facial_symmetry = facial_symmetry or FacialSymmetry()
        self.landmarks = landmarks or FacialLandmarks()

        self.validate()

    def validate(self) -> None:
        super().validate()

        for name, value in {
            "height": self.height,
            "width": self.width,
            "depth": self.depth,
            "forehead_width": self.forehead_width,
            "cheekbone_width": self.cheekbone_width,
            "jaw_width": self.jaw_width,
            "jaw_depth": self.jaw_depth,
        }.items():
            if value <= 0:
                raise ValueError(
                    f"Face {name} must be greater than zero."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid face shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if not 0.0 <= self.symmetry <= 1.0:
            raise ValueError(
                "Face symmetry must be between 0 and 1."
            )

        if self.left_cheek.side is not BodySide.LEFT:
            raise ValueError("Face left_cheek must use BodySide.LEFT.")

        if self.right_cheek.side is not BodySide.RIGHT:
            raise ValueError("Face right_cheek must use BodySide.RIGHT.")

        if self.left_jaw.side is not BodySide.LEFT:
            raise ValueError("Face left_jaw must use BodySide.LEFT.")

        if self.right_jaw.side is not BodySide.RIGHT:
            raise ValueError("Face right_jaw must use BodySide.RIGHT.")

        for component in (
            self.dimensions,
            self.proportions,
            self.forehead,
            self.left_cheek,
            self.right_cheek,
            self.left_jaw,
            self.right_jaw,
            self.chin,
            self.facial_symmetry,
            self.landmarks,
        ):
            component.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "height": self.height,
            "width": self.width,
            "depth": self.depth,
            "forehead_width": self.forehead_width,
            "cheekbone_width": self.cheekbone_width,
            "jaw_width": self.jaw_width,
            "jaw_depth": self.jaw_depth,
            "shape": self.shape,
            "symmetry": self.symmetry,
            "dimensions": self.dimensions.to_dict(),
            "proportions": self.proportions.to_dict(),
            "forehead": self.forehead.to_dict(),
            "left_cheek": self.left_cheek.to_dict(),
            "right_cheek": self.right_cheek.to_dict(),
            "left_jaw": self.left_jaw.to_dict(),
            "right_jaw": self.right_jaw.to_dict(),
            "chin": self.chin.to_dict(),
            "facial_symmetry": self.facial_symmetry.to_dict(),
            "landmarks": self.landmarks.to_dict(),
        }
