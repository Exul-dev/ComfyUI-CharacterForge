"""Geometric measurement layer for the landmark framework.

This module turns landmark coordinates into measurements:

- pure coordinate mathematics (euclidean distance, signed offsets,
  angles at a vertex);
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