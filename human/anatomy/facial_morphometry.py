"""Morphometric derivation layer for the human face.

This module closes the loop between the landmark framework (H4.12)
and the semantic morphometric model (H4.10 / H4.11):

- FacialLandmarks (normalized coordinates) become FacialMeasurements
  (calculated distances and offsets);
- FacialMeasurements become FaceDimensions through an explicit scale
  factor;
- FaceDimensions become FacialProportions (finally derived, not
  declared).

Measurement conventions (documented on purpose):

- vertical measurements (facial thirds, chin height) use the absolute
  difference of the y axis, which keeps the thirds additive:
  upper + mid + lower == facial_height for upright heads;
- bilateral widths (bizygomatic, bigonial, eye widths, mouth width)
  use the 3D euclidean distance, consistent with H4.12-D;
- facial depth is approximated by the z range across all available
  landmark points;
- facial_width follows the bizygomatic width and jaw_width follows
  the bigonial width (the declared defaults of H4.10 identify them);
- forehead_width and chin_width are NOT derivable from the canonical
  facial landmarks and must be provided as explicit fallbacks.
"""

from __future__ import annotations

import math
from typing import Any

from .anatomy_component import AnatomyComponent
from .coordinate import Coordinate
from .coordinate_space import CoordinateSpace
from .face_dimensions import FaceDimensions
from .facial_landmarks import FacialLandmarks
from .facial_proportions import FacialProportions
from .landmark_geometry import euclidean_distance, vertical_offset

# Landmarks required to derive the complete facial measurement set.
_REQUIRED_LANDMARKS = frozenset(
    {
        "trichion",
        "glabella",
        "subnasale",
        "stomion",
        "gnathion",
        "left_zygion",
        "right_zygion",
        "left_gonion",
        "right_gonion",
        "left_endocanthion",
        "right_endocanthion",
        "left_exocanthion",
        "right_exocanthion",
        "left_cheilion",
        "right_cheilion",
    }
)


class FacialMeasurements(AnatomyComponent):
    """Facial measurements calculated from landmark coordinates.

    All values are expressed in the normalized units of the landmark
    coordinate space (before any physical scaling).
    """

    component_type = "facial_measurements"

    def __init__(
        self,
        *,
        facial_height: float,
        upper_face_height: float,
        mid_face_height: float,
        lower_face_height: float,
        chin_height: float,
        bizygomatic_width: float,
        bigonial_width: float,
        eye_inner_width: float,
        eye_outer_width: float,
        mouth_width: float,
        facial_depth: float,
    ) -> None:
        super().__init__()

        self.facial_height = float(facial_height)
        self.upper_face_height = float(upper_face_height)
        self.mid_face_height = float(mid_face_height)
        self.lower_face_height = float(lower_face_height)
        self.chin_height = float(chin_height)
        self.bizygomatic_width = float(bizygomatic_width)
        self.bigonial_width = float(bigonial_width)
        self.eye_inner_width = float(eye_inner_width)
        self.eye_outer_width = float(eye_outer_width)
        self.mouth_width = float(mouth_width)
        self.facial_depth = float(facial_depth)

        self.validate()

    def validate(self) -> None:
        super().validate()

        values = {
            "facial_height": self.facial_height,
            "upper_face_height": self.upper_face_height,
            "mid_face_height": self.mid_face_height,
            "lower_face_height": self.lower_face_height,
            "chin_height": self.chin_height,
            "bizygomatic_width": self.bizygomatic_width,
            "bigonial_width": self.bigonial_width,
            "eye_inner_width": self.eye_inner_width,
            "eye_outer_width": self.eye_outer_width,
            "mouth_width": self.mouth_width,
            "facial_depth": self.facial_depth,
        }

        for name, value in values.items():
            if value <= 0:
                raise ValueError(
                    f"FacialMeasurements {name} must be greater "
                    "than zero."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "facial_height": self.facial_height,
            "upper_face_height": self.upper_face_height,
            "mid_face_height": self.mid_face_height,
            "lower_face_height": self.lower_face_height,
            "chin_height": self.chin_height,
            "bizygomatic_width": self.bizygomatic_width,
            "bigonial_width": self.bigonial_width,
            "eye_inner_width": self.eye_inner_width,
            "eye_outer_width": self.eye_outer_width,
            "mouth_width": self.mouth_width,
            "facial_depth": self.facial_depth,
        }


def _to_coordinate(point: tuple[float, float, float]) -> Coordinate:
    """Convert a normalized landmark tuple into a Coordinate."""

    x, y, z = (float(value) for value in point)

    return Coordinate(
        x=x,
        y=y,
        z=z,
        space=CoordinateSpace.NORMALIZED_3D,
    )


def facial_measurements(
    landmarks: FacialLandmarks,
) -> FacialMeasurements:
    """Derive facial measurements from canonical facial landmarks.

    Requires the fifteen landmarks used by the derivation; missing
    ones are reported explicitly.
    """

    if not isinstance(landmarks, FacialLandmarks):
        raise ValueError(
            "facial_measurements requires a FacialLandmarks instance."
        )

    landmarks.validate()

    if not landmarks.points:
        raise ValueError(
            "facial_measurements requires at least one landmark point."
        )

    missing = sorted(
        name
        for name in _REQUIRED_LANDMARKS
        if name not in landmarks.points
    )

    if missing:
        raise ValueError(
            "facial_measurements requires landmarks that are "
            f"missing: {', '.join(missing)}."
        )

    coordinates = {
        name: _to_coordinate(point)
        for name, point in landmarks.points.items()
    }

    trichion = coordinates["trichion"]
    glabella = coordinates["glabella"]
    subnasale = coordinates["subnasale"]
    stomion = coordinates["stomion"]
    gnathion = coordinates["gnathion"]

    facial_height = abs(vertical_offset(trichion, gnathion))
    upper_face_height = abs(vertical_offset(trichion, glabella))
    mid_face_height = abs(vertical_offset(glabella, subnasale))
    lower_face_height = abs(vertical_offset(subnasale, gnathion))
    chin_height = abs(vertical_offset(stomion, gnathion))

    bizygomatic_width = euclidean_distance(
        coordinates["left_zygion"],
        coordinates["right_zygion"],
    )
    bigonial_width = euclidean_distance(
        coordinates["left_gonion"],
        coordinates["right_gonion"],
    )
    eye_inner_width = euclidean_distance(
        coordinates["left_endocanthion"],
        coordinates["right_endocanthion"],
    )
    eye_outer_width = euclidean_distance(
        coordinates["left_exocanthion"],
        coordinates["right_exocanthion"],
    )
    mouth_width = euclidean_distance(
        coordinates["left_cheilion"],
        coordinates["right_cheilion"],
    )

    depth_values = [
        coordinate.z for coordinate in coordinates.values()
    ]
    facial_depth = max(depth_values) - min(depth_values)

    return FacialMeasurements(
        facial_height=facial_height,
        upper_face_height=upper_face_height,
        mid_face_height=mid_face_height,
        lower_face_height=lower_face_height,
        chin_height=chin_height,
        bizygomatic_width=bizygomatic_width,
        bigonial_width=bigonial_width,
        eye_inner_width=eye_inner_width,
        eye_outer_width=eye_outer_width,
        mouth_width=mouth_width,
        facial_depth=facial_depth,
    )


def facial_scale_factor(
    measurements: FacialMeasurements,
    target_facial_height: float,
) -> float:
    """Return the scale factor mapping normalized measurements to a
    target physical facial height."""

    if not isinstance(measurements, FacialMeasurements):
        raise ValueError(
            "facial_scale_factor requires a FacialMeasurements "
            "instance."
        )

    if (
        isinstance(target_facial_height, bool)
        or not isinstance(target_facial_height, (int, float))
        or not math.isfinite(float(target_facial_height))
        or target_facial_height <= 0
    ):
        raise ValueError(
            "facial_scale_factor target_facial_height must be a "
            "positive finite number."
        )

    measurements.validate()

    return float(target_facial_height) / measurements.facial_height


def face_dimensions_from_measurements(
    measurements: FacialMeasurements,
    scale: float = 1.0,
    *,
    forehead_width: float = 12.0,
    chin_width: float = 5.0,
) -> FaceDimensions:
    """Build FaceDimensions from calculated facial measurements.

    ``scale`` converts normalized units into physical units. The
    forehead and chin widths are not derivable from the canonical
    facial landmarks and must be provided explicitly (defaults follow
    the anthropometric reference values of H4.10).
    """

    if not isinstance(measurements, FacialMeasurements):
        raise ValueError(
            "face_dimensions_from_measurements requires a "
            "FacialMeasurements instance."
        )

    if (
        isinstance(scale, bool)
        or not isinstance(scale, (int, float))
        or not math.isfinite(float(scale))
        or scale <= 0
    ):
        raise ValueError(
            "face_dimensions_from_measurements scale must be a "
            "positive finite number."
        )

    measurements.validate()

    return FaceDimensions(
        facial_height=measurements.facial_height * scale,
        facial_width=measurements.bizygomatic_width * scale,
        facial_depth=measurements.facial_depth * scale,
        upper_face_height=measurements.upper_face_height * scale,
        mid_face_height=measurements.mid_face_height * scale,
        lower_face_height=measurements.lower_face_height * scale,
        forehead_width=float(forehead_width),
        bizygomatic_width=measurements.bizygomatic_width * scale,
        bigonial_width=measurements.bigonial_width * scale,
        jaw_width=measurements.bigonial_width * scale,
        chin_width=float(chin_width),
        chin_height=measurements.chin_height * scale,
    )


def facial_proportions_from_dimensions(
    dimensions: FaceDimensions,
) -> FacialProportions:
    """Derive FacialProportions from FaceDimensions.

    This closes the H4.10 note: proportions are finally derived from
    the dimensional model instead of being declared by hand.
    """

    if not isinstance(dimensions, FaceDimensions):
        raise ValueError(
            "facial_proportions_from_dimensions requires a "
            "FaceDimensions instance."
        )

    dimensions.validate()

    return FacialProportions(
        upper_to_mid_ratio=(
            dimensions.upper_face_height
            / dimensions.mid_face_height
        ),
        mid_to_lower_ratio=(
            dimensions.mid_face_height
            / dimensions.lower_face_height
        ),
        width_to_height_ratio=(
            dimensions.facial_width / dimensions.facial_height
        ),
        forehead_to_cheek_ratio=(
            dimensions.forehead_width
            / dimensions.bizygomatic_width
        ),
        cheek_to_jaw_ratio=(
            dimensions.bizygomatic_width
            / dimensions.bigonial_width
        ),
        jaw_to_chin_ratio=(
            dimensions.jaw_width / dimensions.chin_width
        ),
    )