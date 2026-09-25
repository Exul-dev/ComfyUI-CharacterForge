from __future__ import annotations

import pytest

from human.anatomy import (
    FaceDimensions,
    FacialLandmarks,
    FacialMeasurements,
    FacialProportions,
    face_dimensions_from_measurements,
    facial_measurements,
    facial_proportions_from_dimensions,
    facial_scale_factor,
)

# Realistic fixture: y grows downwards (image convention), z points
# forward. All required landmarks present.
FIXTURE_POINTS = {
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


def _fixture_landmarks() -> FacialLandmarks:
    return FacialLandmarks(points=dict(FIXTURE_POINTS))


class TestHumanEngineH413A:

    def test_measurements_from_fixture(self):
        measurements = facial_measurements(_fixture_landmarks())

        assert measurements.facial_height == pytest.approx(0.96)
        assert measurements.upper_face_height == pytest.approx(0.16)
        assert measurements.mid_face_height == pytest.approx(0.34)
        assert measurements.lower_face_height == pytest.approx(0.46)
        assert measurements.chin_height == pytest.approx(0.30)
        assert measurements.bizygomatic_width == pytest.approx(0.68)
        assert measurements.bigonial_width == pytest.approx(0.52)
        assert measurements.eye_inner_width == pytest.approx(0.16)
        assert measurements.eye_outer_width == pytest.approx(0.56)
        assert measurements.mouth_width == pytest.approx(0.24)
        assert measurements.facial_depth == pytest.approx(1.35)

    def test_vertical_thirds_additivity(self):
        measurements = facial_measurements(_fixture_landmarks())

        total = (
            measurements.upper_face_height
            + measurements.mid_face_height
            + measurements.lower_face_height
        )

        assert total == pytest.approx(measurements.facial_height)

    def test_measurements_component_contract(self):
        measurements = facial_measurements(_fixture_landmarks())

        assert measurements.component_type == "facial_measurements"
        assert measurements.is_valid()

        data = measurements.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["enabled"] is True
        for key in (
            "facial_height",
            "upper_face_height",
            "mid_face_height",
            "lower_face_height",
            "chin_height",
            "bizygomatic_width",
            "bigonial_width",
            "eye_inner_width",
            "eye_outer_width",
            "mouth_width",
            "facial_depth",
        ):
            assert key in data

    def test_missing_required_landmark_is_rejected(self):
        points = {
            name: point
            for name, point in FIXTURE_POINTS.items()
            if name != "trichion"
        }

        with pytest.raises(ValueError, match="trichion"):
            facial_measurements(FacialLandmarks(points=points))

    def test_missing_landmarks_are_all_listed(self):
        points = {
            name: point
            for name, point in FIXTURE_POINTS.items()
            if name not in ("gnathion", "left_zygion")
        }

        with pytest.raises(ValueError) as excinfo:
            facial_measurements(FacialLandmarks(points=points))

        message = str(excinfo.value)
        assert "gnathion" in message
        assert "left_zygion" in message

    def test_empty_landmarks_are_rejected(self):
        with pytest.raises(ValueError, match="at least one"):
            facial_measurements(FacialLandmarks(points={}))

    def test_non_facial_landmarks_are_rejected(self):
        with pytest.raises(ValueError, match="FacialLandmarks"):
            facial_measurements("not landmarks")

    def test_measurements_reject_non_positive_values(self):
        with pytest.raises(ValueError, match="facial_height"):
            FacialMeasurements(
                facial_height=0.0,
                upper_face_height=0.16,
                mid_face_height=0.34,
                lower_face_height=0.46,
                chin_height=0.30,
                bizygomatic_width=0.68,
                bigonial_width=0.52,
                eye_inner_width=0.16,
                eye_outer_width=0.56,
                mouth_width=0.24,
                facial_depth=1.35,
            )

        with pytest.raises(ValueError, match="bizygomatic_width"):
            FacialMeasurements(
                facial_height=0.96,
                upper_face_height=0.16,
                mid_face_height=0.34,
                lower_face_height=0.46,
                chin_height=0.30,
                bizygomatic_width=-0.68,
                bigonial_width=0.52,
                eye_inner_width=0.16,
                eye_outer_width=0.56,
                mouth_width=0.24,
                facial_depth=1.35,
            )

    def test_facial_scale_factor(self):
        measurements = facial_measurements(_fixture_landmarks())

        factor = facial_scale_factor(measurements, 18.0)

        assert factor == pytest.approx(18.0 / 0.96)
        assert factor == pytest.approx(18.75)

    def test_facial_scale_factor_rejects_invalid_target(self):
        measurements = facial_measurements(_fixture_landmarks())

        for invalid in (0.0, -18.0, float("inf"), "tall"):
            with pytest.raises(ValueError, match="target_facial_height"):
                facial_scale_factor(measurements, invalid)

        with pytest.raises(ValueError, match="FacialMeasurements"):
            facial_scale_factor("measurements", 18.0)

    def test_face_dimensions_from_measurements(self):
        measurements = facial_measurements(_fixture_landmarks())
        scale = facial_scale_factor(measurements, 18.0)

        dimensions = face_dimensions_from_measurements(
            measurements,
            scale=scale,
        )

        assert dimensions.is_valid()
        assert dimensions.facial_height == pytest.approx(18.0)
        assert dimensions.facial_width == pytest.approx(12.75)
        assert dimensions.facial_depth == pytest.approx(25.3125)
        assert dimensions.upper_face_height == pytest.approx(3.0)
        assert dimensions.mid_face_height == pytest.approx(6.375)
        assert dimensions.lower_face_height == pytest.approx(8.625)
        assert dimensions.forehead_width == pytest.approx(12.0)
        assert dimensions.bizygomatic_width == pytest.approx(12.75)
        assert dimensions.bigonial_width == pytest.approx(9.75)
        assert dimensions.jaw_width == pytest.approx(9.75)
        assert dimensions.chin_width == pytest.approx(5.0)
        assert dimensions.chin_height == pytest.approx(5.625)

    def test_face_dimensions_fallbacks_are_explicit(self):
        measurements = facial_measurements(_fixture_landmarks())

        dimensions = face_dimensions_from_measurements(
            measurements,
            scale=1.0,
            forehead_width=13.5,
            chin_width=4.5,
        )

        assert dimensions.forehead_width == pytest.approx(13.5)
        assert dimensions.chin_width == pytest.approx(4.5)

    def test_face_dimensions_rejects_invalid_scale(self):
        measurements = facial_measurements(_fixture_landmarks())

        for invalid in (0.0, -2.0, float("inf"), "big", True):
            with pytest.raises(ValueError, match="scale"):
                face_dimensions_from_measurements(
                    measurements,
                    scale=invalid,
                )

    def test_face_dimensions_rejects_non_measurements(self):
        with pytest.raises(ValueError, match="FacialMeasurements"):
            face_dimensions_from_measurements("measurements")

    def test_facial_proportions_from_explicit_dimensions(self):
        dimensions = FaceDimensions(
            facial_height=12.0,
            facial_width=14.0,
            facial_depth=10.0,
            upper_face_height=6.0,
            mid_face_height=3.0,
            lower_face_height=2.0,
            forehead_width=12.0,
            bizygomatic_width=14.0,
            bigonial_width=12.0,
            jaw_width=12.0,
            chin_width=6.0,
            chin_height=4.0,
        )

        proportions = facial_proportions_from_dimensions(dimensions)

        assert proportions.upper_to_mid_ratio == pytest.approx(2.0)
        assert proportions.mid_to_lower_ratio == pytest.approx(1.5)
        assert proportions.width_to_height_ratio == pytest.approx(
            14.0 / 12.0
        )
        assert proportions.forehead_to_cheek_ratio == pytest.approx(
            12.0 / 14.0
        )
        assert proportions.cheek_to_jaw_ratio == pytest.approx(
            14.0 / 12.0
        )
        assert proportions.jaw_to_chin_ratio == pytest.approx(2.0)

    def test_derivation_matches_declared_defaults(self):
        # The H4.10 declared proportions are the FaceDimensions
        # default ratios ROUNDED to two decimals (5.8/6.2 = 0.9355 ->
        # 0.94, and so on). The derivation computes the exact ratios,
        # so it reproduces the declared model up to that rounding.
        # This closes the H4.10 note.
        dimensions = FaceDimensions()
        proportions = facial_proportions_from_dimensions(dimensions)
        declared = FacialProportions()

        assert round(proportions.upper_to_mid_ratio, 2) == (
            pytest.approx(declared.upper_to_mid_ratio)
        )
        assert round(proportions.mid_to_lower_ratio, 2) == (
            pytest.approx(declared.mid_to_lower_ratio)
        )
        assert round(proportions.width_to_height_ratio, 2) == (
            pytest.approx(declared.width_to_height_ratio)
        )
        assert round(proportions.forehead_to_cheek_ratio, 2) == (
            pytest.approx(declared.forehead_to_cheek_ratio)
        )
        assert round(proportions.cheek_to_jaw_ratio, 2) == (
            pytest.approx(declared.cheek_to_jaw_ratio)
        )
        assert round(proportions.jaw_to_chin_ratio, 2) == (
            pytest.approx(declared.jaw_to_chin_ratio)
        )

    def test_proportions_are_scale_invariant(self):
        # Proportions computed purely from landmark measurements are
        # invariant under the scale factor.
        measurements = facial_measurements(_fixture_landmarks())

        invariant_attrs = (
            "upper_to_mid_ratio",
            "mid_to_lower_ratio",
            "width_to_height_ratio",
            "cheek_to_jaw_ratio",
        )

        derived = [
            facial_proportions_from_dimensions(
                face_dimensions_from_measurements(
                    measurements,
                    scale=scale,
                )
            )
            for scale in (1.0, 18.75, 37.5)
        ]

        for attr in invariant_attrs:
            reference = getattr(derived[0], attr)
            for other in derived[1:]:
                assert reference == pytest.approx(getattr(other, attr))

    def test_fallback_proportions_are_scale_dependent(self):
        # forehead_width and chin_width are physical fallbacks (cm)
        # and are NOT scaled: the two proportions that involve them
        # change with the scale factor. This is documented design of
        # the derivation layer, not a defect.
        measurements = facial_measurements(_fixture_landmarks())

        small = facial_proportions_from_dimensions(
            face_dimensions_from_measurements(measurements, scale=1.0)
        )
        large = facial_proportions_from_dimensions(
            face_dimensions_from_measurements(
                measurements,
                scale=18.75,
            )
        )

        assert small.forehead_to_cheek_ratio != pytest.approx(
            large.forehead_to_cheek_ratio
        )
        assert small.jaw_to_chin_ratio != pytest.approx(
            large.jaw_to_chin_ratio
        )

        # At the physical scale the values are the meaningful ones.
        assert large.forehead_to_cheek_ratio == pytest.approx(
            12.0 / 12.75
        )
        assert large.jaw_to_chin_ratio == pytest.approx(9.75 / 5.0)

    def test_end_to_end_derivation_chain(self):
        landmarks = _fixture_landmarks()
        measurements = facial_measurements(landmarks)
        factor = facial_scale_factor(measurements, 18.0)
        dimensions = face_dimensions_from_measurements(
            measurements,
            scale=factor,
        )
        proportions = facial_proportions_from_dimensions(dimensions)

        assert dimensions.is_valid()
        assert proportions.is_valid()

        assert dimensions.facial_height == pytest.approx(18.0)
        assert dimensions.bizygomatic_width == pytest.approx(12.75)

        assert proportions.upper_to_mid_ratio == pytest.approx(
            0.16 / 0.34
        )
        assert proportions.mid_to_lower_ratio == pytest.approx(
            0.34 / 0.46
        )
        assert proportions.width_to_height_ratio == pytest.approx(
            0.68 / 0.96
        )
        assert proportions.forehead_to_cheek_ratio == pytest.approx(
            12.0 / 12.75
        )
        assert proportions.cheek_to_jaw_ratio == pytest.approx(
            0.68 / 0.52
        )
        assert proportions.jaw_to_chin_ratio == pytest.approx(
            9.75 / 5.0
        )

    def test_proportions_reject_non_dimensions(self):
        with pytest.raises(ValueError, match="FaceDimensions"):
            facial_proportions_from_dimensions("dimensions")

    def test_derived_proportions_component_contract(self):
        measurements = facial_measurements(_fixture_landmarks())
        dimensions = face_dimensions_from_measurements(
            measurements,
            scale=1.0,
        )
        proportions = facial_proportions_from_dimensions(dimensions)

        assert proportions.component_type == "facial_proportions"
        assert proportions.is_valid()

        data = proportions.to_dict()
        assert data["schema_version"] == "1.0"
        assert "upper_to_mid_ratio" in data