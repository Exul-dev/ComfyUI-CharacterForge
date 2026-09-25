from __future__ import annotations

import math

import pytest

from human.anatomy import (
    AnatomicalPlane,
    AnatomicalPlaneType,
    Coordinate,
    CoordinateSpace,
    Landmark,
    LandmarkGraph,
    is_on_plane,
    plane_normal,
    signed_distance_to_plane,
)


def _coord_2d(x: float, y: float) -> Coordinate:
    return Coordinate(x=x, y=y, space=CoordinateSpace.IMAGE_2D)


def _coord_3d(x: float, y: float, z: float) -> Coordinate:
    return Coordinate(
        x=x, y=y, z=z, space=CoordinateSpace.NORMALIZED_3D
    )


def _landmark(name: str, x: float, y: float, z: float) -> Landmark:
    return Landmark(name=name, coordinate=_coord_3d(x, y, z))


class TestHumanEngineH412E:

    # --- AnatomicalPlaneType ---

    def test_plane_type_values(self):
        assert AnatomicalPlaneType.MID_SAGITTAL.value == "mid_sagittal"
        assert AnatomicalPlaneType.CORONAL.value == "coronal"
        assert AnatomicalPlaneType.AXIAL.value == "axial"
        assert AnatomicalPlaneType.FRANKFURT.value == "frankfurt"
        assert (
            AnatomicalPlaneType.LANDMARK_DEFINED.value
            == "landmark_defined"
        )

    # --- semantic planes ---

    def test_standard_planes_need_no_landmarks(self):
        for plane_type in (
            AnatomicalPlaneType.MID_SAGITTAL,
            AnatomicalPlaneType.CORONAL,
            AnatomicalPlaneType.AXIAL,
        ):
            plane = AnatomicalPlane(plane_type)

            assert plane.is_valid()
            assert plane.landmark_names is None

    def test_standard_plane_accepts_empty_landmark_list(self):
        plane = AnatomicalPlane(
            AnatomicalPlaneType.AXIAL,
            landmark_names=[],
        )

        assert plane.is_valid()
        assert plane.landmark_names == []

    def test_standard_plane_with_landmarks_is_rejected(self):
        with pytest.raises(ValueError, match="must not"):
            AnatomicalPlane(
                AnatomicalPlaneType.MID_SAGITTAL,
                landmark_names=["a", "b", "c"],
            )

    def test_landmark_defined_plane_requires_exactly_three_landmarks(self):
        with pytest.raises(ValueError, match="exactly 3"):
            AnatomicalPlane(AnatomicalPlaneType.LANDMARK_DEFINED)

        with pytest.raises(ValueError, match="exactly 3"):
            AnatomicalPlane(
                AnatomicalPlaneType.LANDMARK_DEFINED,
                landmark_names=["a", "b"],
            )

        with pytest.raises(ValueError, match="exactly 3"):
            AnatomicalPlane(
                AnatomicalPlaneType.LANDMARK_DEFINED,
                landmark_names=["a", "b", "c", "d"],
            )

    def test_frankfurt_plane_with_three_landmarks_is_valid(self):
        plane = AnatomicalPlane(
            AnatomicalPlaneType.FRANKFURT,
            landmark_names=[
                "left_porion",
                "right_porion",
                "left_orbitale",
            ],
        )

        assert plane.is_valid()
        assert plane.landmark_names == [
            "left_porion",
            "right_porion",
            "left_orbitale",
        ]

    def test_duplicate_defining_landmarks_are_rejected(self):
        with pytest.raises(ValueError, match="distinct"):
            AnatomicalPlane(
                AnatomicalPlaneType.LANDMARK_DEFINED,
                landmark_names=["a", "a", "b"],
            )

    def test_empty_landmark_name_is_rejected(self):
        with pytest.raises(ValueError, match="non-empty"):
            AnatomicalPlane(
                AnatomicalPlaneType.LANDMARK_DEFINED,
                landmark_names=["a", "b", " "],
            )

    def test_non_list_landmark_names_is_rejected(self):
        with pytest.raises(ValueError, match="list"):
            AnatomicalPlane(
                AnatomicalPlaneType.LANDMARK_DEFINED,
                landmark_names="left_porion",
            )

    def test_invalid_plane_type_is_rejected(self):
        with pytest.raises(ValueError, match="plane_type"):
            AnatomicalPlane("frankfurt")

    def test_serialization(self):
        plane = AnatomicalPlane(
            AnatomicalPlaneType.FRANKFURT,
            landmark_names=[
                "left_porion",
                "right_porion",
                "left_orbitale",
            ],
        )

        data = plane.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "anatomical_plane"
        assert data["enabled"] is True
        assert data["plane_type"] == "frankfurt"
        assert data["landmark_names"] == [
            "left_porion",
            "right_porion",
            "left_orbitale",
        ]

        standard = AnatomicalPlane(AnatomicalPlaneType.MID_SAGITTAL)
        standard_data = standard.to_dict()

        assert standard_data["plane_type"] == "mid_sagittal"
        assert standard_data["landmark_names"] is None

    def test_plane_is_anatomy_component(self):
        plane = AnatomicalPlane(AnatomicalPlaneType.AXIAL)

        assert plane.component_type == "anatomical_plane"
        assert plane.is_valid()

    # --- plane geometry ---

    def test_plane_normal_axis_aligned(self):
        normal = plane_normal(
            _coord_3d(0.0, 0.0, 0.0),
            _coord_3d(1.0, 0.0, 0.0),
            _coord_3d(0.0, 1.0, 0.0),
        )

        assert normal[0] == pytest.approx(0.0)
        assert normal[1] == pytest.approx(0.0)
        assert normal[2] == pytest.approx(1.0)

    def test_plane_normal_is_unit_length(self):
        normal = plane_normal(
            _coord_3d(0.1, 0.2, 0.3),
            _coord_3d(0.4, 0.5, 0.3),
            _coord_3d(0.1, 0.2, 0.9),
        )

        length = math.sqrt(
            sum(component ** 2 for component in normal)
        )

        assert length == pytest.approx(1.0)
        assert normal[0] == pytest.approx(math.sqrt(0.5))
        assert normal[1] == pytest.approx(-math.sqrt(0.5))
        assert normal[2] == pytest.approx(0.0)

    def test_collinear_landmarks_do_not_define_a_plane(self):
        with pytest.raises(ValueError, match="Collinear"):
            plane_normal(
                _coord_3d(0.0, 0.0, 0.0),
                _coord_3d(1.0, 0.0, 0.0),
                _coord_3d(2.0, 0.0, 0.0),
            )

    def test_plane_geometry_requires_3d(self):
        with pytest.raises(ValueError, match="3D coordinate space"):
            plane_normal(
                _coord_2d(0.1, 0.2),
                _coord_2d(0.3, 0.2),
                _coord_2d(0.1, 0.4),
            )

    def test_plane_geometry_space_mismatch_is_rejected(self):
        with pytest.raises(ValueError, match="same coordinate space"):
            plane_normal(
                _coord_2d(0.1, 0.2),
                _coord_3d(0.0, 0.0, 0.0),
                _coord_3d(0.0, 1.0, 0.0),
            )

        a = _coord_3d(0.0, 0.0, 0.0)
        b = _coord_3d(1.0, 0.0, 0.0)
        c = _coord_3d(0.0, 1.0, 0.0)

        with pytest.raises(ValueError, match="same coordinate space"):
            signed_distance_to_plane(_coord_2d(0.1, 0.2), a, b, c)

    def test_plane_geometry_rejects_non_coordinate(self):
        a = _coord_3d(0.1, 0.2, 0.3)
        b = _coord_3d(0.4, 0.5, 0.3)
        c = _coord_3d(0.1, 0.2, 0.9)

        with pytest.raises(ValueError, match="must be a Coordinate"):
            plane_normal("left_porion", b, c)

        with pytest.raises(ValueError, match="must be a Coordinate"):
            signed_distance_to_plane("nasion", a, b, c)

        with pytest.raises(ValueError, match="must be a Coordinate"):
            signed_distance_to_plane(
                _coord_3d(0.5, 0.5, 0.5), "a", b, c
            )

    def test_signed_distance_axis_aligned(self):
        a = _coord_3d(0.0, 0.0, 0.0)
        b = _coord_3d(1.0, 0.0, 0.0)
        c = _coord_3d(0.0, 1.0, 0.0)

        above = _coord_3d(0.3, 0.6, 0.4)
        below = _coord_3d(0.3, 0.6, -0.4)

        assert signed_distance_to_plane(above, a, b, c) == pytest.approx(0.4)
        assert signed_distance_to_plane(below, a, b, c) == pytest.approx(-0.4)
        assert is_on_plane(_coord_3d(0.3, 0.6, 0.0), a, b, c)

    def test_mid_sagittal_symmetry(self):
        a = _coord_3d(0.5, 0.0, 0.0)
        b = _coord_3d(0.5, 1.0, 0.0)
        c = _coord_3d(0.5, 0.0, 1.0)

        left = _coord_3d(0.36, 0.50, 0.80)
        right = _coord_3d(0.64, 0.50, 0.80)

        distance_left = signed_distance_to_plane(left, a, b, c)
        distance_right = signed_distance_to_plane(right, a, b, c)

        assert distance_left == pytest.approx(-0.14)
        assert distance_right == pytest.approx(0.14)
        assert distance_left == pytest.approx(-distance_right)

    def test_is_on_plane_with_tolerance(self):
        a = _coord_3d(0.0, 0.0, 0.0)
        b = _coord_3d(1.0, 0.0, 0.0)
        c = _coord_3d(0.0, 1.0, 0.0)

        near = _coord_3d(0.3, 0.6, 0.0005)
        far = _coord_3d(0.3, 0.6, 0.05)

        assert is_on_plane(near, a, b, c, tolerance=1e-3)
        assert not is_on_plane(far, a, b, c, tolerance=1e-3)
        assert not is_on_plane(near, a, b, c, tolerance=1e-5)

    def test_invalid_tolerance_is_rejected(self):
        a = _coord_3d(0.0, 0.0, 0.0)
        b = _coord_3d(1.0, 0.0, 0.0)
        c = _coord_3d(0.0, 1.0, 0.0)
        point = _coord_3d(0.3, 0.6, 0.0)

        with pytest.raises(ValueError, match="tolerance"):
            is_on_plane(point, a, b, c, tolerance=-1.0)

        with pytest.raises(ValueError, match="tolerance"):
            is_on_plane(point, a, b, c, tolerance=float("inf"))

        with pytest.raises(ValueError, match="tolerance"):
            is_on_plane(point, a, b, c, tolerance="wide")

    def test_end_to_end_frankfurt_plane(self):
        graph = LandmarkGraph(
            landmarks=[
                _landmark("left_porion", 0.42, 0.46, 0.86),
                _landmark("right_porion", 0.58, 0.46, 0.86),
                _landmark("left_orbitale", 0.44, 0.42, 0.92),
                _landmark("nasion", 0.50, 0.44, 0.95),
            ]
        )

        plane = AnatomicalPlane(
            AnatomicalPlaneType.FRANKFURT,
            landmark_names=[
                "left_porion",
                "right_porion",
                "left_orbitale",
            ],
        )

        assert plane.is_valid()

        a = graph.get_landmark("left_porion").coordinate
        b = graph.get_landmark("right_porion").coordinate
        c = graph.get_landmark("left_orbitale").coordinate

        for defining in (a, b, c):
            assert is_on_plane(defining, a, b, c)

        nasion = graph.get_landmark("nasion").coordinate

        assert not is_on_plane(nasion, a, b, c)
        assert signed_distance_to_plane(nasion, a, b, c) != 0.0