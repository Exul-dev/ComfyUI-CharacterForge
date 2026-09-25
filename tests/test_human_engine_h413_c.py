from __future__ import annotations

import math

import pytest

from human.anatomy import (
    AnatomicalPlane,
    AnatomicalPlaneType,
    Coordinate,
    CoordinateSpace,
    CranialLandmarks,
    CranialMeasurements,
    FaceDimensions,
    FacialLandmarks,
    cranial_measurements,
    cranial_scale_factor,
    face_dimensions_from_measurements,
    facial_measurements,
    facial_scale_factor,
    head_dimensions_from_cranial_measurements,
    head_dimensions_from_face_dimensions,
    head_proportions_from_dimensions,
    is_on_plane,
)

# Cranial fixture: normalized to the head bounding box. The
# Frankfurt trio (porion L/R + orbitale L) sits exactly at y=0.48,
# so the Frankfurt plane is horizontal in this fixture.
CRANIAL_FIXTURE = {
    "vertex": (0.50, 0.05, 0.00),
    "left_euryon": (0.08, 0.30, -0.10),
    "right_euryon": (0.92, 0.30, -0.10),
    "opisthocranion": (0.50, 0.40, -1.00),
    "glabella": (0.50, 0.40, 0.90),
    "left_porion": (0.16, 0.48, 0.00),
    "right_porion": (0.84, 0.48, 0.00),
    "left_orbitale": (0.36, 0.48, 0.70),
    "right_orbitale": (0.64, 0.48, 0.70),
    "nasion": (0.50, 0.42, 0.85),
}

# Facial fixture: same as H4.13-A/B (normalized to the face box).
FACIAL_FIXTURE = {
    "trichion": (0.50, 0.02, -0.40),
    "glabella": (0.50, 0.18, 0.55),
    "nasion": (0.50, 0.22, 0.45),
    "pronasale": (0.50, 0.44, 0.95),
    "subnasale": (0.50, 0.52, 0.70),
    "labiale_superius": (0.50, 0.62, 0.65),
    "stomion": (0.50, 0.68, 0.65),
    "labiale_inferius": (0.50, 0.72, 0.65),
    "gnathion": (0.50, 0.98, 0.40),
    "left_zygion": (0.16, 0.42, 0.10),
    "right_zygion": (0.84, 0.42, 0.10),
    "left_gonion": (0.24, 0.80, 0.00),
    "right_gonion": (0.76, 0.80, 0.00),
    "left_endocanthion": (0.42, 0.34, 0.55),
    "right_endocanthion": (0.58, 0.34, 0.55),
    "left_exocanthion": (0.22, 0.34, 0.50),
    "right_exocanthion": (0.78, 0.34, 0.50),
    "left_cheilion": (0.38, 0.68, 0.60),
    "right_cheilion": (0.62, 0.68, 0.60),
}


def _cranial_landmarks() -> CranialLandmarks:
    return CranialLandmarks(points=dict(CRANIAL_FIXTURE))


def _fixture_face_dimensions() -> FaceDimensions:
    measurements = facial_measurements(
        FacialLandmarks(points=dict(FACIAL_FIXTURE))
    )
    factor = facial_scale_factor(measurements, 18.0)
    return face_dimensions_from_measurements(
        measurements,
        scale=factor,
    )


def _expected_circumference(scale: float = 1.0) -> float:
    # Ramanujan perimeter of the ellipse built on the fixture
    # width (0.84) and depth (1.90), stated independently.
    a = 0.84 / 2.0
    b = 1.90 / 2.0
    return math.pi * (
        3.0 * (a + b)
        - math.sqrt((3.0 * a + b) * (a + 3.0 * b))
    ) * scale


class TestHumanEngineH413C:

    # --- CranialLandmarks component ---

    def test_cranial_landmark_names(self):
        landmarks = _cranial_landmarks()

        assert landmarks.is_valid()
        assert set(CranialLandmarks.VALID_LANDMARKS) == {
            "vertex",
            "left_euryon",
            "right_euryon",
            "opisthocranion",
            "left_porion",
            "right_porion",
            "left_orbitale",
            "right_orbitale",
            "glabella",
            "nasion",
        }

    def test_unknown_cranial_landmark_is_rejected(self):
        with pytest.raises(ValueError, match="Unknown cranial"):
            CranialLandmarks(points={"menton": (0.5, 0.9, 0.4)})

    def test_point_cardinality_and_ranges_are_enforced(self):
        with pytest.raises(ValueError, match="exactly three"):
            CranialLandmarks(points={"vertex": (0.5, 0.05)})

        with pytest.raises(ValueError, match="x coordinate"):
            CranialLandmarks(points={"vertex": (1.5, 0.05, 0.0)})

        with pytest.raises(ValueError, match="y coordinate"):
            CranialLandmarks(points={"vertex": (0.5, -0.1, 0.0)})

        with pytest.raises(ValueError, match="z coordinate"):
            CranialLandmarks(points={"vertex": (0.5, 0.05, 1.5)})

    def test_cranial_landmarks_serialization(self):
        landmarks = _cranial_landmarks()

        data = landmarks.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "cranial_landmarks"
        assert data["enabled"] is True
        assert data["points"]["vertex"] == [0.50, 0.05, 0.00]
        assert data["points"]["nasion"] == [0.50, 0.42, 0.85]

    # --- cranial measurements ---

    def test_measurements_from_fixture(self):
        measurements = cranial_measurements(_cranial_landmarks())

        assert measurements.cranial_width == pytest.approx(0.84)
        assert measurements.cranial_length == pytest.approx(1.90)
        assert measurements.cranial_depth == pytest.approx(1.90)
        assert measurements.neurocranial_height == pytest.approx(0.43)
        assert measurements.cranial_circumference == pytest.approx(
            _expected_circumference()
        )
        assert measurements.is_valid()
        assert measurements.component_type == "cranial_measurements"

    def test_missing_required_landmarks_are_listed(self):
        points = {
            name: point
            for name, point in CRANIAL_FIXTURE.items()
            if name not in ("vertex", "left_euryon")
        }

        with pytest.raises(ValueError) as excinfo:
            cranial_measurements(CranialLandmarks(points=points))

        message = str(excinfo.value)
        assert "left_euryon" in message
        assert "vertex" in message

    def test_optional_landmarks_are_not_required(self):
        points = {
            name: point
            for name, point in CRANIAL_FIXTURE.items()
            if name not in ("nasion", "right_orbitale")
        }

        measurements = cranial_measurements(
            CranialLandmarks(points=points)
        )

        assert measurements.is_valid()
        assert measurements.cranial_width == pytest.approx(0.84)

    def test_non_cranial_landmarks_are_rejected(self):
        with pytest.raises(ValueError, match="CranialLandmarks"):
            cranial_measurements("not landmarks")

    def test_empty_points_are_rejected(self):
        with pytest.raises(ValueError, match="at least one"):
            cranial_measurements(CranialLandmarks(points={}))

    def test_measurements_reject_non_positive_values(self):
        base = dict(
            cranial_width=0.84,
            cranial_length=1.90,
            cranial_depth=1.90,
            neurocranial_height=0.43,
            cranial_circumference=4.47,
        )

        with pytest.raises(ValueError, match="cranial_width"):
            CranialMeasurements(**{**base, "cranial_width": 0.0})

        with pytest.raises(ValueError, match="neurocranial_height"):
            CranialMeasurements(
                **{**base, "neurocranial_height": -0.43}
            )

    def test_neurocranial_height_follows_frankfurt_plane(self):
        # Shifting the whole Frankfurt trio down by 0.10 moves the
        # plane: the vault height must grow by the same amount
        # (0.43 -> 0.53). Proves the height is measured from the
        # actual plane, not from a fixed constant.
        shifted = dict(CRANIAL_FIXTURE)

        for name in ("left_porion", "right_porion", "left_orbitale"):
            x, y, z = shifted[name]
            shifted[name] = (x, y + 0.10, z)

        measurements = cranial_measurements(
            CranialLandmarks(points=shifted)
        )

        assert measurements.neurocranial_height == pytest.approx(0.53)
        assert measurements.cranial_width == pytest.approx(0.84)

    def test_frankfurt_plane_end_to_end(self):
        # The three defining landmarks also form a valid H4.12-E
        # AnatomicalPlane, and the geometry agrees: right orbitale
        # lies on the same plane, nasion and vertex do not.
        plane = AnatomicalPlane(
            AnatomicalPlaneType.FRANKFURT,
            landmark_names=[
                "left_porion",
                "right_porion",
                "left_orbitale",
            ],
        )

        assert plane.is_valid()

        coordinates = {
            name: Coordinate(
                x=point[0],
                y=point[1],
                z=point[2],
                space=CoordinateSpace.NORMALIZED_3D,
            )
            for name, point in CRANIAL_FIXTURE.items()
        }

        a = coordinates["left_porion"]
        b = coordinates["right_porion"]
        c = coordinates["left_orbitale"]

        assert is_on_plane(coordinates["right_orbitale"], a, b, c)
        assert not is_on_plane(coordinates["nasion"], a, b, c)
        assert not is_on_plane(coordinates["vertex"], a, b, c)

    # --- scale factor ---

    def test_cranial_scale_factor(self):
        measurements = cranial_measurements(_cranial_landmarks())

        factor = cranial_scale_factor(measurements, 19.0)

        assert factor == pytest.approx(10.0)

    def test_cranial_scale_factor_rejects_invalid_target(self):
        measurements = cranial_measurements(_cranial_landmarks())

        for invalid in (0.0, -19.0, float("inf"), "long"):
            with pytest.raises(ValueError, match="target_cranial_length"):
                cranial_scale_factor(measurements, invalid)

        with pytest.raises(ValueError, match="CranialMeasurements"):
            cranial_scale_factor("measurements", 19.0)

    # --- head dimensions from cranial measurements ---

    def test_head_dimensions_from_cranial_measurements(self):
        face = _fixture_face_dimensions()
        measurements = cranial_measurements(_cranial_landmarks())
        scale = cranial_scale_factor(measurements, 19.0)

        head = head_dimensions_from_cranial_measurements(
            face,
            measurements,
            scale=scale,
        )

        assert head.is_valid()
        assert head.cranial_width == pytest.approx(8.4)
        assert head.cranial_breadth == pytest.approx(8.4)
        assert head.cranial_depth == pytest.approx(19.0)
        assert head.cranial_length == pytest.approx(19.0)
        assert head.neurocranial_height == pytest.approx(4.3)
        assert head.cranial_circumference == pytest.approx(
            _expected_circumference(10.0)
        )
        # cranial_height approximated as vault + facial height.
        assert head.cranial_height == pytest.approx(22.3)
        # Facial values injected from the derived face model.
        assert head.facial_height == pytest.approx(18.0)
        assert head.bizygomatic_width == pytest.approx(12.75)
        assert head.bigonial_width == pytest.approx(9.75)

    def test_head_dimensions_cranial_height_override(self):
        face = _fixture_face_dimensions()
        measurements = cranial_measurements(_cranial_landmarks())

        head = head_dimensions_from_cranial_measurements(
            face,
            measurements,
            scale=10.0,
            cranial_height=24.0,
        )

        assert head.cranial_height == pytest.approx(24.0)

    def test_head_dimensions_reject_invalid_inputs(self):
        face = _fixture_face_dimensions()
        measurements = cranial_measurements(_cranial_landmarks())

        with pytest.raises(ValueError, match="FaceDimensions"):
            head_dimensions_from_cranial_measurements(
                "face",
                measurements,
            )

        with pytest.raises(ValueError, match="CranialMeasurements"):
            head_dimensions_from_cranial_measurements(
                face,
                "measurements",
            )

        for invalid in (0.0, -1.0, float("inf"), "big", True):
            with pytest.raises(ValueError, match="scale"):
                head_dimensions_from_cranial_measurements(
                    face,
                    measurements,
                    scale=invalid,
                )

        with pytest.raises(ValueError, match="cranial_height"):
            head_dimensions_from_cranial_measurements(
                face,
                measurements,
                scale=1.0,
                cranial_height=0.0,
            )

    # --- end to end ---

    def test_end_to_end_full_chain(self):
        # The complete head, everything derived:
        # FacialLandmarks -> FacialMeasurements -> FaceDimensions
        # CranialLandmarks -> CranialMeasurements -> scale
        # -> HeadDimensions -> HeadProportions.
        face = _fixture_face_dimensions()
        measurements = cranial_measurements(_cranial_landmarks())
        scale = cranial_scale_factor(measurements, 19.0)

        head = head_dimensions_from_cranial_measurements(
            face,
            measurements,
            scale=scale,
        )
        proportions = head_proportions_from_dimensions(head)

        assert head.is_valid()
        assert proportions.is_valid()

        assert head.cranial_length == pytest.approx(19.0)
        assert head.cranial_breadth == pytest.approx(8.4)
        assert head.neurocranial_height == pytest.approx(4.3)

        assert proportions.cephalic_index == pytest.approx(
            8.4 / 19.0 * 100.0
        )
        assert proportions.cranial_depth_to_width == pytest.approx(
            19.0 / 8.4
        )
        assert proportions.cranial_height_to_width == pytest.approx(
            4.3 / 8.4
        )
        assert proportions.face_to_head_height == pytest.approx(
            18.0 / 22.3
        )
        assert proportions.face_to_head_width == pytest.approx(
            12.75 / 8.4
        )
        assert proportions.neurocranium_to_face_height == (
            pytest.approx(4.3 / 18.0)
        )
        assert proportions.bizygomatic_to_bigonial == pytest.approx(
            12.75 / 9.75
        )

    def test_legacy_fallback_derivation_still_works(self):
        face = _fixture_face_dimensions()

        head = head_dimensions_from_face_dimensions(face)

        assert head.is_valid()
        assert head.cranial_width == pytest.approx(15.0)
        assert head.facial_height == pytest.approx(18.0)