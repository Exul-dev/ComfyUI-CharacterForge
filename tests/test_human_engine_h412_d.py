from __future__ import annotations

import math

import pytest

from human.anatomy import (
    Coordinate,
    CoordinateSpace,
    Landmark,
    LandmarkGraph,
    LandmarkRelationType,
    angle_at_vertex,
    computed_relation,
    depth_offset,
    euclidean_distance,
    horizontal_offset,
    vertical_offset,
)


def _coord_2d(x: float, y: float) -> Coordinate:
    return Coordinate(x=x, y=y, space=CoordinateSpace.IMAGE_2D)


def _coord_3d(x: float, y: float, z: float) -> Coordinate:
    return Coordinate(
        x=x, y=y, z=z, space=CoordinateSpace.NORMALIZED_3D
    )


def _landmark(name: str, x: float, y: float, z: float) -> Landmark:
    return Landmark(name=name, coordinate=_coord_3d(x, y, z))


class TestHumanEngineH412D:

    # --- pure math: euclidean distance ---

    def test_euclidean_distance_2d(self):
        distance = euclidean_distance(
            _coord_2d(0.0, 0.0),
            _coord_2d(3.0, 4.0),
        )

        assert distance == pytest.approx(5.0)

    def test_euclidean_distance_3d(self):
        distance = euclidean_distance(
            _coord_3d(0.0, 0.0, 0.0),
            _coord_3d(1.0, 1.0, 1.0),
        )

        assert distance == pytest.approx(math.sqrt(3.0))

    def test_euclidean_distance_is_symmetric(self):
        first = _coord_3d(0.36, 0.50, 0.80)
        second = _coord_3d(0.64, 0.50, 0.80)

        assert euclidean_distance(first, second) == pytest.approx(
            euclidean_distance(second, first)
        )

    def test_euclidean_distance_space_mismatch_is_rejected(self):
        with pytest.raises(ValueError, match="same coordinate space"):
            euclidean_distance(
                _coord_2d(0.1, 0.2),
                _coord_3d(0.1, 0.2, 0.3),
            )

    def test_math_functions_reject_non_coordinate(self):
        coordinate = _coord_3d(0.1, 0.2, 0.3)

        with pytest.raises(ValueError, match="must be a Coordinate"):
            euclidean_distance("left_zygion", coordinate)

        with pytest.raises(ValueError, match="must be a Coordinate"):
            vertical_offset(coordinate, None)

        with pytest.raises(ValueError, match="must be a Coordinate"):
            angle_at_vertex("glabella", coordinate, coordinate)

    # --- pure math: signed offsets ---

    def test_horizontal_offset_is_signed(self):
        first = _coord_3d(0.36, 0.50, 0.80)
        second = _coord_3d(0.64, 0.50, 0.80)

        assert horizontal_offset(first, second) == pytest.approx(0.28)
        assert horizontal_offset(second, first) == pytest.approx(-0.28)

    def test_horizontal_offset_works_in_2d(self):
        assert horizontal_offset(
            _coord_2d(0.2, 0.5), _coord_2d(0.5, 0.5)
        ) == pytest.approx(0.3)

    def test_vertical_offset_is_signed(self):
        first = _coord_3d(0.50, 0.40, 0.92)
        second = _coord_3d(0.50, 0.44, 0.95)

        assert vertical_offset(first, second) == pytest.approx(0.04)
        assert vertical_offset(second, first) == pytest.approx(-0.04)

    def test_depth_offset_is_signed(self):
        first = _coord_3d(0.50, 0.40, 0.92)
        second = _coord_3d(0.50, 0.44, 0.95)

        assert depth_offset(first, second) == pytest.approx(0.03)
        assert depth_offset(second, first) == pytest.approx(-0.03)

    def test_depth_offset_requires_3d(self):
        with pytest.raises(ValueError, match="3D coordinate space"):
            depth_offset(
                _coord_2d(0.1, 0.2), _coord_2d(0.3, 0.4)
            )

    def test_offsets_space_mismatch_is_rejected(self):
        with pytest.raises(ValueError, match="same coordinate space"):
            vertical_offset(
                _coord_2d(0.1, 0.2), _coord_3d(0.1, 0.2, 0.3)
            )

    # --- pure math: angles ---

    def test_angle_right_angle_2d(self):
        angle = angle_at_vertex(
            _coord_2d(1.0, 0.0),
            _coord_2d(0.0, 0.0),
            _coord_2d(0.0, 1.0),
        )

        assert angle == pytest.approx(90.0)

    def test_angle_right_angle_3d(self):
        angle = angle_at_vertex(
            _coord_3d(1.0, 0.0, 0.0),
            _coord_3d(0.0, 0.0, 0.0),
            _coord_3d(0.0, 1.0, 0.0),
        )

        assert angle == pytest.approx(90.0)

    def test_angle_sixty_degrees_3d(self):
        angle = angle_at_vertex(
            _coord_3d(1.0, 0.0, 0.0),
            _coord_3d(0.0, 0.0, 0.0),
            _coord_3d(0.5, math.sqrt(3.0) / 2.0, 0.0),
        )

        assert angle == pytest.approx(60.0)

    def test_angle_collinear_is_straight(self):
        angle = angle_at_vertex(
            _coord_3d(1.0, 0.0, 0.0),
            _coord_3d(0.0, 0.0, 0.0),
            _coord_3d(-1.0, 0.0, 0.0),
        )

        assert angle == pytest.approx(180.0)

    def test_angle_same_direction_is_zero(self):
        angle = angle_at_vertex(
            _coord_3d(1.0, 0.0, 0.0),
            _coord_3d(0.0, 0.0, 0.0),
            _coord_3d(2.0, 0.0, 0.0),
        )

        assert angle == pytest.approx(0.0)

    def test_angle_is_symmetric(self):
        nasion = _coord_3d(0.50, 0.44, 0.95)
        left = _coord_3d(0.44, 0.46, 0.90)
        right = _coord_3d(0.56, 0.46, 0.90)

        assert angle_at_vertex(left, nasion, right) == pytest.approx(
            angle_at_vertex(right, nasion, left)
        )

    def test_angle_coincident_with_vertex_is_rejected(self):
        vertex = _coord_3d(0.5, 0.5, 0.5)

        with pytest.raises(ValueError, match="coincides"):
            angle_at_vertex(vertex, vertex, _coord_3d(0.6, 0.5, 0.5))

    def test_angle_space_mismatch_is_rejected(self):
        with pytest.raises(ValueError, match="same coordinate space"):
            angle_at_vertex(
                _coord_2d(1.0, 0.0),
                _coord_3d(0.0, 0.0, 0.0),
                _coord_2d(0.0, 1.0),
            )

    # --- computed relations ---

    def test_computed_distance_relation(self):
        left = _landmark("left_zygion", 0.36, 0.50, 0.80)
        right = _landmark("right_zygion", 0.64, 0.50, 0.80)

        relation = computed_relation(
            left,
            right,
            LandmarkRelationType.DISTANCE,
            unit="normalized",
        )

        assert relation.landmark_a == "left_zygion"
        assert relation.landmark_b == "right_zygion"
        assert relation.relation_type is LandmarkRelationType.DISTANCE
        assert relation.value == pytest.approx(0.28)
        assert relation.unit == "normalized"
        assert relation.is_valid()

    def test_computed_offset_relations(self):
        glabella = _landmark("glabella", 0.50, 0.40, 0.92)
        nasion = _landmark("nasion", 0.50, 0.44, 0.95)

        horizontal = computed_relation(
            glabella, nasion, LandmarkRelationType.HORIZONTAL_OFFSET
        )
        vertical = computed_relation(
            glabella, nasion, LandmarkRelationType.VERTICAL_OFFSET
        )
        depth = computed_relation(
            glabella, nasion, LandmarkRelationType.DEPTH_OFFSET
        )

        assert (
            horizontal.relation_type
            is LandmarkRelationType.HORIZONTAL_OFFSET
        )
        assert (
            vertical.relation_type
            is LandmarkRelationType.VERTICAL_OFFSET
        )
        assert (
            depth.relation_type
            is LandmarkRelationType.DEPTH_OFFSET
        )

        assert horizontal.value == pytest.approx(0.0)
        assert vertical.value == pytest.approx(0.04)
        assert depth.value == pytest.approx(0.03)

        assert horizontal.unit is None
        assert horizontal.is_valid()
        assert vertical.is_valid()
        assert depth.is_valid()

    def test_computed_relation_rejects_angle_type(self):
        first = _landmark("left_endocanthion", 0.44, 0.46, 0.90)
        second = _landmark("right_endocanthion", 0.56, 0.46, 0.90)

        with pytest.raises(ValueError, match="vertex"):
            computed_relation(
                first, second, LandmarkRelationType.ANGLE
            )

    def test_computed_relation_rejects_invalid_relation_type(self):
        first = _landmark("glabella", 0.50, 0.40, 0.92)
        second = _landmark("nasion", 0.50, 0.44, 0.95)

        with pytest.raises(ValueError, match="relation_type"):
            computed_relation(first, second, "distance")

    def test_computed_relation_rejects_non_landmark(self):
        nasion = _landmark("nasion", 0.50, 0.44, 0.95)

        with pytest.raises(ValueError, match="must be a Landmark"):
            computed_relation(
                "glabella", nasion, LandmarkRelationType.DISTANCE
            )

    # --- end to end ---

    def test_end_to_end_computed_relations_in_graph(self):
        graph = LandmarkGraph(
            landmarks=[
                _landmark("glabella", 0.50, 0.40, 0.92),
                _landmark("nasion", 0.50, 0.44, 0.95),
                _landmark("left_zygion", 0.36, 0.50, 0.80),
                _landmark("right_zygion", 0.64, 0.50, 0.80),
            ]
        )

        bizygomatic = computed_relation(
            graph.get_landmark("left_zygion"),
            graph.get_landmark("right_zygion"),
            LandmarkRelationType.DISTANCE,
            unit="normalized",
        )
        assert bizygomatic.value == pytest.approx(0.28)

        glabella_nasion = computed_relation(
            graph.get_landmark("glabella"),
            graph.get_landmark("nasion"),
            LandmarkRelationType.VERTICAL_OFFSET,
            unit="normalized",
        )
        assert glabella_nasion.value == pytest.approx(0.04)

        graph.add_relation(bizygomatic)
        graph.add_relation(glabella_nasion)

        assert graph.is_valid()

        data = graph.to_dict()
        by_endpoint = {
            relation["landmark_a"]: relation["value"]
            for relation in data["relations"]
        }
        assert by_endpoint["left_zygion"] == pytest.approx(0.28)
        assert by_endpoint["glabella"] == pytest.approx(0.04)

    def test_end_to_end_nasional_angle(self):
        nasion = _landmark("nasion", 0.50, 0.44, 0.95)
        left = _landmark("left_endocanthion", 0.44, 0.46, 0.90)
        right = _landmark("right_endocanthion", 0.56, 0.46, 0.90)

        angle = angle_at_vertex(
            left.coordinate,
            nasion.coordinate,
            right.coordinate,
        )

        vector_left = (-0.06, 0.02, -0.05)
        vector_right = (0.06, 0.02, -0.05)
        dot = sum(
            a * b for a, b in zip(vector_left, vector_right)
        )
        length = math.sqrt(
            sum(c * c for c in vector_left)
        ) * math.sqrt(sum(c * c for c in vector_right))
        expected = math.degrees(math.acos(dot / length))

        assert angle == pytest.approx(expected)
        assert 90.0 < angle < 180.0