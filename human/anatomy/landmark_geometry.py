"""Geometric measurement layer for the landmark framework.

This module turns landmark coordinates into measurements:

- pure coordinate mathematics (euclidean distance, signed offsets,
  angles at a vertex, planes through three landmarks);
- computed relations, which package a measurement into a semantic
  LandmarkRelation ready to live inside a LandmarkGraph.

The module is deliberately functional: measurements are operations,
not entities. The semantic artifact is the resulting LandmarkRelation.
"""

from __future__ import annotations

import math

from .coordinate import Coordinate
from .landmark import Landmark
from .landmark_relation import LandmarkRelation, LandmarkRelationType


def _require_coordinate(value: object, name: str) -> None:
    """Raise ValueError unless value is a Coordinate."""

    if not isinstance(value, Coordinate):
        raise ValueError(f"{name} must be a Coordinate.")


def _require_same_space(first: Coordinate, second: Coordinate) -> None:
    """Raise ValueError unless both coordinates share the same space."""

    if first.space is not second.space:
        raise ValueError(
            "Coordinates must share the same coordinate space."
        )


def euclidean_distance(a: Coordinate, b: Coordinate) -> float:
    """Return the euclidean distance between two coordinates."""

    _require_coordinate(a, "a")
    _require_coordinate(b, "b")
    _require_same_space(a, b)

    if a.space.dimensions == 2:
        return math.hypot(b.x - a.x, b.y - a.y)

    return math.hypot(b.x - a.x, b.y - a.y, b.z - a.z)


def horizontal_offset(a: Coordinate, b: Coordinate) -> float:
    """Return the signed horizontal (x) offset from a to b."""

    _require_coordinate(a, "a")
    _require_coordinate(b, "b")
    _require_same_space(a, b)

    return b.x - a.x


def vertical_offset(a: Coordinate, b: Coordinate) -> float:
    """Return the signed vertical (y) offset from a to b."""

    _require_coordinate(a, "a")
    _require_coordinate(b, "b")
    _require_same_space(a, b)

    return b.y - a.y


def depth_offset(a: Coordinate, b: Coordinate) -> float:
    """Return the signed depth (z) offset from a to b (3D only)."""

    _require_coordinate(a, "a")
    _require_coordinate(b, "b")
    _require_same_space(a, b)

    if a.space.dimensions != 3:
        raise ValueError(
            "Depth offset requires a 3D coordinate space."
        )

    return b.z - a.z


def angle_at_vertex(
    a: Coordinate,
    vertex: Coordinate,
    b: Coordinate,
) -> float:
    """Return the angle in degrees at vertex between vertex->a and vertex->b."""

    _require_coordinate(a, "a")
    _require_coordinate(vertex, "vertex")
    _require_coordinate(b, "b")
    _require_same_space(a, vertex)
    _require_same_space(b, vertex)

    if a.space.dimensions == 2:
        vector_a = (a.x - vertex.x, a.y - vertex.y)
        vector_b = (b.x - vertex.x, b.y - vertex.y)
    else:
        vector_a = (a.x - vertex.x, a.y - vertex.y, a.z - vertex.z)
        vector_b = (b.x - vertex.x, b.y - vertex.y, b.z - vertex.z)

    length_a = math.sqrt(
        sum(component ** 2 for component in vector_a)
    )
    length_b = math.sqrt(
        sum(component ** 2 for component in vector_b)
    )

    if length_a == 0.0 or length_b == 0.0:
        raise ValueError(
            "Angle is undefined when a landmark coincides "
            "with the vertex."
        )

    dot_product = sum(
        component_a * component_b
        for component_a, component_b in zip(vector_a, vector_b)
    )

    cosine = dot_product / (length_a * length_b)
    cosine = max(-1.0, min(1.0, cosine))

    return math.degrees(math.acos(cosine))


def plane_normal(
    a: Coordinate,
    b: Coordinate,
    c: Coordinate,
) -> tuple[float, float, float]:
    """Return the unit normal of the plane through a, b, c.

    The normal follows the right-hand rule for the order
    (b - a) x (c - a).
    """

    _require_coordinate(a, "a")
    _require_coordinate(b, "b")
    _require_coordinate(c, "c")
    _require_same_space(a, b)
    _require_same_space(a, c)

    if a.space.dimensions != 3:
        raise ValueError(
            "Planes require a 3D coordinate space."
        )

    vector_1 = (b.x - a.x, b.y - a.y, b.z - a.z)
    vector_2 = (c.x - a.x, c.y - a.y, c.z - a.z)

    normal = (
        vector_1[1] * vector_2[2] - vector_1[2] * vector_2[1],
        vector_1[2] * vector_2[0] - vector_1[0] * vector_2[2],
        vector_1[0] * vector_2[1] - vector_1[1] * vector_2[0],
    )

    length = math.sqrt(
        normal[0] ** 2 + normal[1] ** 2 + normal[2] ** 2
    )

    if length == 0.0:
        raise ValueError(
            "Collinear landmarks do not define a plane."
        )

    return (
        normal[0] / length,
        normal[1] / length,
        normal[2] / length,
    )


def signed_distance_to_plane(
    point: Coordinate,
    a: Coordinate,
    b: Coordinate,
    c: Coordinate,
) -> float:
    """Return the signed distance from point to the plane through
    a, b, c.

    The distance is positive on the side of the plane normal and
    negative on the opposite side.
    """

    _require_coordinate(point, "point")

    normal = plane_normal(a, b, c)
    _require_same_space(point, a)

    vector = (point.x - a.x, point.y - a.y, point.z - a.z)

    return (
        normal[0] * vector[0]
        + normal[1] * vector[1]
        + normal[2] * vector[2]
    )


def is_on_plane(
    point: Coordinate,
    a: Coordinate,
    b: Coordinate,
    c: Coordinate,
    tolerance: float = 1e-9,
) -> bool:
    """Return True when point lies on plane abc within tolerance."""

    if (
        isinstance(tolerance, bool)
        or not isinstance(tolerance, (int, float))
        or not math.isfinite(tolerance)
        or tolerance < 0
    ):
        raise ValueError(
            "is_on_plane tolerance must be a non-negative "
            "finite number."
        )

    distance = signed_distance_to_plane(point, a, b, c)

    return abs(distance) <= tolerance


# Offset relation types mapped to their signed offset functions.
_OFFSET_BY_RELATION_TYPE = {
    LandmarkRelationType.HORIZONTAL_OFFSET: horizontal_offset,
    LandmarkRelationType.VERTICAL_OFFSET: vertical_offset,
    LandmarkRelationType.DEPTH_OFFSET: depth_offset,
}


def computed_relation(
    landmark_a: Landmark,
    landmark_b: Landmark,
    relation_type: LandmarkRelationType,
    unit: str | None = None,
) -> LandmarkRelation:
    """Compute the measurement between two landmarks and return it
    as a semantic LandmarkRelation.

    The relation value is calculated from the landmark coordinates,
    not declared by hand: this is the bridge between the geometric
    layer and the semantic layer of the landmark framework.
    """

    if not isinstance(landmark_a, Landmark):
        raise ValueError("landmark_a must be a Landmark.")

    if not isinstance(landmark_b, Landmark):
        raise ValueError("landmark_b must be a Landmark.")

    if not isinstance(relation_type, LandmarkRelationType):
        raise ValueError(
            "relation_type must be a LandmarkRelationType."
        )

    landmark_a.validate()
    landmark_b.validate()

    coordinate_a = landmark_a.coordinate
    coordinate_b = landmark_b.coordinate

    if relation_type is LandmarkRelationType.DISTANCE:
        value = euclidean_distance(coordinate_a, coordinate_b)
    elif relation_type in _OFFSET_BY_RELATION_TYPE:
        offset_function = _OFFSET_BY_RELATION_TYPE[relation_type]
        value = offset_function(coordinate_a, coordinate_b)
    else:
        raise ValueError(
            "ANGLE relations require a vertex landmark and cannot "
            "be computed from two landmarks alone."
        )

    return LandmarkRelation(
        landmark_a=landmark_a.name,
        landmark_b=landmark_b.name,
        relation_type=relation_type,
        value=value,
        unit=unit,
    )