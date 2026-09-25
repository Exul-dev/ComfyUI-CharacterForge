"""Morphometric derivation layer for the human head.

Extends the H4.13 derivation chain above the face:

- FaceDimensions (derived or declared) become HeadDimensions through
  explicit cranial fallbacks (legacy H4.13-B path);
- with cranial landmarks available, HeadDimensions become fully
  derived: CranialLandmarks become CranialMeasurements (width,
  length, vault height above the Frankfurt plane, circumference),
  which scale into the physical cranial model (H4.13-C path);
- HeadDimensions become HeadProportions (finally derived, not
  declared).

Design notes:

- the facial and cranial landmark sets live in DIFFERENT
  normalizations (face bounding box vs head bounding box): each set
  is scaled to physical units with its own scale factor, and the
  combined physical model is coherent because both sides are
  expressed in the same physical units;
- cranial_length follows cranial_depth and cranial_breadth follows
  cranial_width, mirroring the declared H4.11 defaults where the
  two pairs are identical (19/19 and 15/15);
- the neurocranial height is measured as the perpendicular distance
  of the vertex from the Frankfurt plane (porion L/R + orbitale):
  the H4.12-E plane geometry becomes the measuring instrument;
- the cranial circumference is approximated with the Ramanujan
  perimeter of an ellipse built on the cranial width and depth;
- cranial_height (vertex to menton) cannot be measured from the
  cranial landmark set alone (the menton belongs to the face): it
  is approximated as neurocranial height + facial height, or can
  be provided explicitly;
- cranial_height_to_width uses the neurocranial height (the vault
  height above the Frankfurt plane), which is the anthropometric
  reading that reproduces the declared H4.11 default (13/15=0.87);
- the cephalic index is the classic breadth/length * 100 ratio: the
  declared H4.11 default (78.0) is the tabulated mesocephalic mean,
  while the value derived from the dimensional defaults is 78.95.
"""

from __future__ import annotations

import math

from .anatomy_component import AnatomyComponent
from .coordinate import Coordinate
from .coordinate_space import CoordinateSpace
from .cranial_landmarks import CranialLandmarks
from .face_dimensions import FaceDimensions
from .head_dimensions import HeadDimensions
from .head_proportions import HeadProportions
from .landmark_geometry import euclidean_distance, signed_distance_to_plane

# Cranial landmarks required to derive the cranial measurement set.
# nasion and right_orbitale are valid but optional.
_REQUIRED_CRANIAL_LANDMARKS = frozenset(
    {
        "vertex",
        "left_euryon",
        "right_euryon",
        "opisthocranion",
        "glabella",
        "left_porion",
        "right_porion",
        "left_orbitale",
    }
)


def _require_positive_finite(
    value: object,
    name: str,
    context: str,
) -> None:
    """Raise ValueError unless value is a positive finite number."""

    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(float(value))
        or value <= 0
    ):
        raise ValueError(
            f"{context} {name} must be a positive finite number."
        )


def _to_coordinate(point: tuple[float, float, float]) -> Coordinate:
    """Convert a normalized landmark tuple into a Coordinate."""

    x, y, z = (float(value) for value in point)

    return Coordinate(
        x=x,
        y=y,
        z=z,
        space=CoordinateSpace.NORMALIZED_3D,
    )


def _ramanujan_perimeter(
    semi_axis_a: float,
    semi_axis_b: float,
) -> float:
    """Return the Ramanujan approximation of an ellipse perimeter."""

    return math.pi * (
        3.0 * (semi_axis_a + semi_axis_b)
        - math.sqrt(
            (3.0 * semi_axis_a + semi_axis_b)
            * (semi_axis_a + 3.0 * semi_axis_b)
        )
    )


class CranialMeasurements(AnatomyComponent):
    """Cranial measurements calculated from landmark coordinates.

    All values are expressed in the normalized units of the cranial
    landmark coordinate space (before any physical scaling).
    """

    component_type = "cranial_measurements"

    def __init__(
        self,
        *,
        cranial_width: float,
        cranial_length: float,
        cranial_depth: float,
        neurocranial_height: float,
        cranial_circumference: float,
    ) -> None:
        super().__init__()

        self.cranial_width = float(cranial_width)
        self.cranial_length = float(cranial_length)
        self.cranial_depth = float(cranial_depth)
        self.neurocranial_height = float(neurocranial_height)
        self.cranial_circumference = float(cranial_circumference)

        self.validate()

    def validate(self) -> None:
        super().validate()

        values = {
            "cranial_width": self.cranial_width,
            "cranial_length": self.cranial_length,
            "cranial_depth": self.cranial_depth,
            "neurocranial_height": self.neurocranial_height,
            "cranial_circumference": self.cranial_circumference,
        }

        for name, value in values.items():
            if value <= 0:
                raise ValueError(
                    f"CranialMeasurements {name} must be greater "
                    "than zero."
                )

    def to_dict(self) -> dict:
        return {
            **super().to_dict(),
            "cranial_width": self.cranial_width,
            "cranial_length": self.cranial_length,
            "cranial_depth": self.cranial_depth,
            "neurocranial_height": self.neurocranial_height,
            "cranial_circumference": self.cranial_circumference,
        }


def cranial_measurements(
    landmarks: CranialLandmarks,
) -> CranialMeasurements:
    """Derive cranial measurements from canonical cranial landmarks.

    The neurocranial height is the perpendicular distance of the
    vertex from the Frankfurt plane, defined by the left porion,
    right porion and left orbitale: the H4.12-E plane geometry
    becomes the measuring instrument.
    """

    if not isinstance(landmarks, CranialLandmarks):
        raise ValueError(
            "cranial_measurements requires a CranialLandmarks "
            "instance."
        )

    landmarks.validate()

    if not landmarks.points:
        raise ValueError(
            "cranial_measurements requires at least one landmark "
            "point."
        )

    missing = sorted(
        name
        for name in _REQUIRED_CRANIAL_LANDMARKS
        if name not in landmarks.points
    )

    if missing:
        raise ValueError(
            "cranial_measurements requires landmarks that are "
            f"missing: {', '.join(missing)}."
        )

    coordinates = {
        name: _to_coordinate(point)
        for name, point in landmarks.points.items()
    }

    cranial_width = euclidean_distance(
        coordinates["left_euryon"],
        coordinates["right_euryon"],
    )
    cranial_length = euclidean_distance(
        coordinates["glabella"],
        coordinates["opisthocranion"],
    )
    neurocranial_height = abs(
        signed_distance_to_plane(
            coordinates["vertex"],
            coordinates["left_porion"],
            coordinates["right_porion"],
            coordinates["left_orbitale"],
        )
    )
    cranial_circumference = _ramanujan_perimeter(
        cranial_width / 2.0,
        cranial_length / 2.0,
    )

    return CranialMeasurements(
        cranial_width=cranial_width,
        cranial_length=cranial_length,
        cranial_depth=cranial_length,
        neurocranial_height=neurocranial_height,
        cranial_circumference=cranial_circumference,
    )


def cranial_scale_factor(
    measurements: CranialMeasurements,
    target_cranial_length: float,
) -> float:
    """Return the scale factor mapping normalized cranial
    measurements to a target physical cranial length."""

    if not isinstance(measurements, CranialMeasurements):
        raise ValueError(
            "cranial_scale_factor requires a CranialMeasurements "
            "instance."
        )

    if (
        isinstance(target_cranial_length, bool)
        or not isinstance(target_cranial_length, (int, float))
        or not math.isfinite(float(target_cranial_length))
        or target_cranial_length <= 0
    ):
        raise ValueError(
            "cranial_scale_factor target_cranial_length must be a "
            "positive finite number."
        )

    measurements.validate()

    return float(target_cranial_length) / measurements.cranial_length


def head_dimensions_from_cranial_measurements(
    face_dimensions: FaceDimensions,
    measurements: CranialMeasurements,
    scale: float = 1.0,
    *,
    cranial_height: float | None = None,
) -> HeadDimensions:
    """Build HeadDimensions from derived cranial measurements.

    The cranial model is fully derived from the cranial landmarks:
    width, depth, length, breadth, circumference and vault height
    come from the measurements scaled into physical units, while
    the facial values are injected from the given FaceDimensions so
    that the head model stays consistent with the derived face.

    cranial_height (vertex to menton) cannot be measured from the
    cranial landmark set alone: by default it is approximated as
    neurocranial height + facial height (documented approximation),
    or it can be provided explicitly as a physical value.
    """

    if not isinstance(face_dimensions, FaceDimensions):
        raise ValueError(
            "head_dimensions_from_cranial_measurements requires a "
            "FaceDimensions instance."
        )

    if not isinstance(measurements, CranialMeasurements):
        raise ValueError(
            "head_dimensions_from_cranial_measurements requires a "
            "CranialMeasurements instance."
        )

    if (
        isinstance(scale, bool)
        or not isinstance(scale, (int, float))
        or not math.isfinite(float(scale))
        or scale <= 0
    ):
        raise ValueError(
            "head_dimensions_from_cranial_measurements scale "
            "must be a positive finite number."
        )

    if cranial_height is not None:
        _require_positive_finite(
            cranial_height,
            "cranial_height",
            "head_dimensions_from_cranial_measurements",
        )
        resolved_cranial_height = float(cranial_height)
    else:
        resolved_cranial_height = (
            measurements.neurocranial_height * scale
            + face_dimensions.facial_height
        )

    face_dimensions.validate()
    measurements.validate()

    return HeadDimensions(
        cranial_height=resolved_cranial_height,
        cranial_width=measurements.cranial_width * scale,
        cranial_depth=measurements.cranial_depth * scale,
        cranial_length=measurements.cranial_length * scale,
        cranial_breadth=measurements.cranial_width * scale,
        cranial_circumference=(
            measurements.cranial_circumference * scale
        ),
        neurocranial_height=(
            measurements.neurocranial_height * scale
        ),
        facial_height=face_dimensions.facial_height,
        bizygomatic_width=face_dimensions.bizygomatic_width,
        bigonial_width=face_dimensions.bigonial_width,
    )


def head_dimensions_from_face_dimensions(
    face_dimensions: FaceDimensions,
    *,
    cranial_height: float = 22.0,
    cranial_width: float = 15.0,
    cranial_depth: float = 19.0,
    cranial_circumference: float = 56.0,
    neurocranial_height: float = 13.0,
) -> HeadDimensions:
    """Build HeadDimensions from facial dimensions plus cranial
    fallbacks.

    Legacy fallback-based derivation (H4.13-B): kept for
    compatibility. Prefer head_dimensions_from_cranial_measurements
    when cranial landmarks are available.

    The facial measurements (facial height, bizygomatic and bigonial
    widths) are injected from the given FaceDimensions so that the
    head model stays consistent with the derived face. The cranial
    measurements are explicit fallbacks because the canonical facial
    landmarks do not cover the neurocranium. cranial_length follows
    cranial_depth and cranial_breadth follows cranial_width.
    """

    if not isinstance(face_dimensions, FaceDimensions):
        raise ValueError(
            "head_dimensions_from_face_dimensions requires a "
            "FaceDimensions instance."
        )

    face_dimensions.validate()

    fallbacks = {
        "cranial_height": cranial_height,
        "cranial_width": cranial_width,
        "cranial_depth": cranial_depth,
        "cranial_circumference": cranial_circumference,
        "neurocranial_height": neurocranial_height,
    }

    for name, value in fallbacks.items():
        _require_positive_finite(
            value,
            name,
            "head_dimensions_from_face_dimensions",
        )

    return HeadDimensions(
        cranial_height=float(cranial_height),
        cranial_width=float(cranial_width),
        cranial_depth=float(cranial_depth),
        cranial_length=float(cranial_depth),
        cranial_breadth=float(cranial_width),
        cranial_circumference=float(cranial_circumference),
        neurocranial_height=float(neurocranial_height),
        facial_height=face_dimensions.facial_height,
        bizygomatic_width=face_dimensions.bizygomatic_width,
        bigonial_width=face_dimensions.bigonial_width,
    )


def head_proportions_from_dimensions(
    dimensions: HeadDimensions,
) -> HeadProportions:
    """Derive HeadProportions from HeadDimensions.

    This closes the H4.11 note for the head: proportions are finally
    derived from the dimensional model instead of being declared by
    hand. cranial_height_to_width reads the neurocranial height (the
    vault height above the facial plane), consistent with the
    declared H4.11 default.
    """

    if not isinstance(dimensions, HeadDimensions):
        raise ValueError(
            "head_proportions_from_dimensions requires a "
            "HeadDimensions instance."
        )

    dimensions.validate()

    return HeadProportions(
        cephalic_index=(
            dimensions.cranial_breadth
            / dimensions.cranial_length
            * 100.0
        ),
        cranial_height_to_width=(
            dimensions.neurocranial_height
            / dimensions.cranial_width
        ),
        cranial_depth_to_width=(
            dimensions.cranial_depth / dimensions.cranial_width
        ),
        face_to_head_height=(
            dimensions.facial_height / dimensions.cranial_height
        ),
        face_to_head_width=(
            dimensions.bizygomatic_width
            / dimensions.cranial_width
        ),
        neurocranium_to_face_height=(
            dimensions.neurocranial_height
            / dimensions.facial_height
        ),
        bizygomatic_to_bigonial=(
            dimensions.bizygomatic_width
            / dimensions.bigonial_width
        ),
    )