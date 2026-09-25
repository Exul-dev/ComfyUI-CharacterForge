from __future__ import annotations

import pytest

from human.anatomy import (
    FaceDimensions,
    FacialLandmarks,
    HeadDimensions,
    HeadProportions,
    face_dimensions_from_measurements,
    facial_measurements,
    facial_scale_factor,
    head_dimensions_from_face_dimensions,
    head_proportions_from_dimensions,
)

# Same realistic fixture as H4.13-A (tests stay self-contained).
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


def _fixture_face_dimensions() -> FaceDimensions:
    measurements = facial_measurements(
        FacialLandmarks(points=dict(FIXTURE_POINTS))
    )
    factor = facial_scale_factor(measurements, 18.0)
    return face_dimensions_from_measurements(
        measurements,
        scale=factor,
    )


class TestHumanEngineH413B:

    def test_head_dimensions_from_face_dimensions(self):
        face = _fixture_face_dimensions()

        head = head_dimensions_from_face_dimensions(face)

        assert head.is_valid()
        # Facial values injected from the derived face model.
        assert head.facial_height == pytest.approx(18.0)
        assert head.bizygomatic_width == pytest.approx(12.75)
        assert head.bigonial_width == pytest.approx(9.75)
        # Cranial fallbacks at their default values.
        assert head.cranial_height == pytest.approx(22.0)
        assert head.cranial_width == pytest.approx(15.0)
        assert head.cranial_depth == pytest.approx(19.0)
        assert head.cranial_circumference == pytest.approx(56.0)
        assert head.neurocranial_height == pytest.approx(13.0)

    def test_cranial_length_follows_depth_and_breadth_follows_width(
        self,
    ):
        face = _fixture_face_dimensions()

        head = head_dimensions_from_face_dimensions(
            face,
            cranial_depth=17.5,
            cranial_width=14.0,
        )

        assert head.cranial_length == pytest.approx(17.5)
        assert head.cranial_breadth == pytest.approx(14.0)

    def test_cranial_fallbacks_are_explicit(self):
        face = _fixture_face_dimensions()

        head = head_dimensions_from_face_dimensions(
            face,
            cranial_height=24.0,
            cranial_width=16.0,
            cranial_depth=20.0,
            cranial_circumference=58.0,
            neurocranial_height=14.0,
        )

        assert head.cranial_height == pytest.approx(24.0)
        assert head.cranial_width == pytest.approx(16.0)
        assert head.cranial_depth == pytest.approx(20.0)
        assert head.cranial_circumference == pytest.approx(58.0)
        assert head.neurocranial_height == pytest.approx(14.0)
        assert head.facial_height == pytest.approx(18.0)

    def test_face_values_are_preserved_in_head(self):
        face = FaceDimensions(
            facial_height=20.0,
            facial_width=13.0,
            facial_depth=11.0,
            upper_face_height=6.0,
            mid_face_height=7.0,
            lower_face_height=7.0,
            forehead_width=11.0,
            bizygomatic_width=13.0,
            bigonial_width=10.0,
            jaw_width=10.0,
            chin_width=4.5,
            chin_height=4.5,
        )

        head = head_dimensions_from_face_dimensions(face)

        assert head.facial_height == pytest.approx(20.0)
        assert head.bizygomatic_width == pytest.approx(13.0)
        assert head.bigonial_width == pytest.approx(10.0)

    def test_head_dimensions_reject_non_face_dimensions(self):
        with pytest.raises(ValueError, match="FaceDimensions"):
            head_dimensions_from_face_dimensions("face")

    def test_head_dimensions_reject_invalid_cranial_fallbacks(self):
        face = _fixture_face_dimensions()

        for kwargs in (
            {"cranial_height": 0.0},
            {"cranial_width": -15.0},
            {"cranial_depth": float("inf")},
            {"cranial_circumference": "wide"},
            {"neurocranial_height": True},
        ):
            with pytest.raises(ValueError, match="must be a positive"):
                head_dimensions_from_face_dimensions(face, **kwargs)

    def test_head_proportions_from_explicit_dimensions(self):
        dimensions = HeadDimensions(
            cranial_height=20.0,
            cranial_width=10.0,
            cranial_depth=15.0,
            cranial_length=12.0,
            cranial_breadth=8.0,
            cranial_circumference=50.0,
            neurocranial_height=6.0,
            facial_height=10.0,
            bizygomatic_width=9.0,
            bigonial_width=6.0,
        )

        proportions = head_proportions_from_dimensions(dimensions)

        assert proportions.cephalic_index == pytest.approx(
            8.0 / 12.0 * 100.0
        )
        assert proportions.cranial_height_to_width == pytest.approx(0.6)
        assert proportions.cranial_depth_to_width == pytest.approx(1.5)
        assert proportions.face_to_head_height == pytest.approx(0.5)
        assert proportions.face_to_head_width == pytest.approx(0.9)
        assert proportions.neurocranium_to_face_height == pytest.approx(
            0.6
        )
        assert proportions.bizygomatic_to_bigonial == pytest.approx(1.5)

    def test_cephalic_index_uses_breadth_and_length(self):
        # The classic formula is breadth/length * 100, which must be
        # distinct from width/depth when the pairs differ.
        dimensions = HeadDimensions(
            cranial_width=15.0,
            cranial_depth=19.0,
            cranial_length=24.0,
            cranial_breadth=12.0,
        )

        proportions = head_proportions_from_dimensions(dimensions)

        assert proportions.cephalic_index == pytest.approx(50.0)
        assert proportions.cephalic_index != pytest.approx(
            15.0 / 19.0 * 100.0
        )

    def test_cranial_height_to_width_uses_neurocranial_height(self):
        # The vault height (neurocranial) is the anthropometric
        # reading of "cranial height" in this ratio: 13/15 = 0.87
        # reproduces the declared H4.11 default, 22/15 would not.
        dimensions = HeadDimensions()

        proportions = head_proportions_from_dimensions(dimensions)

        assert proportions.cranial_height_to_width == pytest.approx(
            13.0 / 15.0
        )
        assert proportions.cranial_height_to_width != pytest.approx(
            22.0 / 15.0
        )

    def test_derivation_matches_declared_defaults(self):
        # Six of the seven declared HeadProportions defaults are the
        # HeadDimensions default ratios rounded to two decimals; the
        # cephalic index default (78.0) is the tabulated
        # mesocephalic mean, within 1 of the derived 78.95.
        dimensions = HeadDimensions()
        proportions = head_proportions_from_dimensions(dimensions)
        declared = HeadProportions()

        assert round(proportions.cranial_height_to_width, 2) == (
            pytest.approx(declared.cranial_height_to_width)
        )
        assert round(proportions.cranial_depth_to_width, 2) == (
            pytest.approx(declared.cranial_depth_to_width)
        )
        assert round(proportions.face_to_head_height, 2) == (
            pytest.approx(declared.face_to_head_height)
        )
        assert round(proportions.face_to_head_width, 2) == (
            pytest.approx(declared.face_to_head_width)
        )
        assert round(proportions.neurocranium_to_face_height, 2) == (
            pytest.approx(declared.neurocranium_to_face_height)
        )
        assert round(proportions.bizygomatic_to_bigonial, 2) == (
            pytest.approx(declared.bizygomatic_to_bigonial)
        )

        assert proportions.cephalic_index == pytest.approx(
            declared.cephalic_index,
            abs=1.0,
        )

    def test_head_proportions_reject_non_dimensions(self):
        with pytest.raises(ValueError, match="HeadDimensions"):
            head_proportions_from_dimensions("dimensions")

    def test_end_to_full_chain(self):
        # FacialLandmarks -> FacialMeasurements -> FaceDimensions
        # -> HeadDimensions -> HeadProportions.
        face = _fixture_face_dimensions()
        head = head_dimensions_from_face_dimensions(face)
        proportions = head_proportions_from_dimensions(head)

        assert head.is_valid()
        assert proportions.is_valid()

        assert head.facial_height == pytest.approx(18.0)
        assert head.cranial_length == pytest.approx(19.0)
        assert head.cranial_breadth == pytest.approx(15.0)

        assert proportions.face_to_head_height == pytest.approx(
            18.0 / 22.0
        )
        assert proportions.face_to_head_width == pytest.approx(
            12.75 / 15.0
        )
        assert proportions.bizygomatic_to_bigonial == pytest.approx(
            12.75 / 9.75
        )
        assert proportions.neurocranium_to_face_height == (
            pytest.approx(13.0 / 18.0)
        )
        assert proportions.cephalic_index == pytest.approx(
            15.0 / 19.0 * 100.0
        )

    def test_derived_head_proportions_component_contract(self):
        head = head_dimensions_from_face_dimensions(
            _fixture_face_dimensions()
        )
        proportions = head_proportions_from_dimensions(head)

        assert proportions.component_type == "head_proportions"
        assert proportions.is_valid()

        data = proportions.to_dict()
        assert data["schema_version"] == "1.0"
        for key in (
            "cephalic_index",
            "cranial_height_to_width",
            "cranial_depth_to_width",
            "face_to_head_height",
            "face_to_head_width",
            "neurocranium_to_face_height",
            "bizygomatic_to_bigonial",
        ):
            assert key in data

    def test_head_dimensions_component_contract(self):
        head = head_dimensions_from_face_dimensions(
            _fixture_face_dimensions()
        )

        assert head.component_type == "head_dimensions"
        assert head.is_valid()

        data = head.to_dict()
        assert data["schema_version"] == "1.0"
        assert data["facial_height"] == pytest.approx(18.0)
        assert data["cranial_length"] == pytest.approx(19.0)