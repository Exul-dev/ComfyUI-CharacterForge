from __future__ import annotations

import math

import pytest

from human.anatomy import (
    HeadDimensions,
    HeadModification,
    HeadProportions,
    ModifyResult,
    PropertyChange,
    adjust_neurocranial_height,
    diff_properties,
    lengthen_cranial,
    modify_head_dimensions,
    widen_cranial,
)


def _expected_circumference(width: float, length: float) -> float:
    """Ramanujan perimeter, declared independently of the module."""

    a = width / 2.0
    b = length / 2.0

    return math.pi * (
        3.0 * (a + b)
        - math.sqrt((3.0 * a + b) * (a + 3.0 * b))
    )


class TestHumanEngineH414C:

    # --- generic operator ---

    def test_modify_generic_single_delta(self):
        modification = modify_head_dimensions(
            HeadDimensions(),
            {"neurocranial_height": 1.0},
            operation="grow vault",
        )

        assert modification.dimensions.neurocranial_height == (
            pytest.approx(14.0)
        )
        assert modification.dimension_report.changed_names() == [
            "neurocranial_height"
        ]
        assert len(modification.dimension_report.preserved_names()) == 9

    def test_modify_generic_multiple_deltas(self):
        modification = modify_head_dimensions(
            HeadDimensions(),
            {
                "cranial_width": 1.0,
                "cranial_breadth": 1.0,
            },
            operation="wider skull",
        )

        assert modification.dimensions.cranial_width == (
            pytest.approx(16.0)
        )
        assert modification.dimensions.cranial_breadth == (
            pytest.approx(16.0)
        )
        assert modification.dimension_report.changed_names() == [
            "cranial_width",
            "cranial_breadth",
        ]

    def test_modify_generic_zero_delta_is_noop(self):
        modification = modify_head_dimensions(
            HeadDimensions(),
            {"cranial_height": 0.0},
            operation="noop",
        )

        assert modification.is_valid()
        assert modification.dimension_report.changed_names() == []
        assert len(modification.dimension_report.preserved_names()) == 10

    def test_modify_rejects_unknown_property(self):
        with pytest.raises(ValueError, match="Unknown head dimension"):
            modify_head_dimensions(
                HeadDimensions(),
                {"nose_length": 1.0},
                operation="bad",
            )

    def test_modify_rejects_invalid_delta_values(self):
        for bad in (float("nan"), float("inf"), "wide", True, None):
            with pytest.raises(ValueError, match="finite number"):
                modify_head_dimensions(
                    HeadDimensions(),
                    {"cranial_height": bad},
                    operation="bad",
                )

    def test_modify_rejects_empty_deltas(self):
        for bad in ({}, None, "cranial_height"):
            with pytest.raises(ValueError, match="non-empty dict"):
                modify_head_dimensions(
                    HeadDimensions(),
                    bad,
                    operation="bad",
                )

    def test_modify_rejects_non_dimensions(self):
        with pytest.raises(ValueError, match="HeadDimensions"):
            modify_head_dimensions(
                "dimensions",
                {"cranial_height": 1.0},
                operation="bad",
            )

    def test_modify_rejects_resulting_non_positive(self):
        with pytest.raises(ValueError, match="greater than zero"):
            modify_head_dimensions(
                HeadDimensions(),
                {"cranial_width": -100.0},
                operation="bad",
            )

    # --- widen_cranial ---

    def test_widen_cranial_propagates_to_breadth_and_circumference(self):
        modification = widen_cranial(HeadDimensions(), 1.0)

        assert modification.dimensions.cranial_width == (
            pytest.approx(16.0)
        )
        assert modification.dimensions.cranial_breadth == (
            pytest.approx(16.0)
        )
        assert modification.dimensions.cranial_circumference == (
            pytest.approx(_expected_circumference(16.0, 19.0))
        )
        assert modification.dimension_report.changed_names() == [
            "cranial_width",
            "cranial_breadth",
            "cranial_circumference",
        ]

    def test_widen_cranial_facial_invariance(self):
        # THE cross invariance: a cranial operation leaves the
        # facial properties of the head model exactly as they were.
        before = HeadDimensions()
        modification = widen_cranial(before, 1.0)
        after = modification.dimensions

        assert after.facial_height == pytest.approx(before.facial_height)
        assert after.bizygomatic_width == pytest.approx(
            before.bizygomatic_width
        )
        assert after.bigonial_width == pytest.approx(
            before.bigonial_width
        )

        for name in ("facial_height", "bizygomatic_width", "bigonial_width"):
            assert name in modification.dimension_report.preserved_names()
            assert not modification.dimension_report.has_changed(name)

    def test_widen_cranial_proportion_report(self):
        modification = widen_cranial(HeadDimensions(), 1.0)

        assert modification.proportion_report.changed_names() == [
            "cephalic_index",
            "cranial_height_to_width",
            "cranial_depth_to_width",
            "face_to_head_width",
        ]
        assert modification.proportion_report.preserved_names() == [
            "face_to_head_height",
            "neurocranium_to_face_height",
            "bizygomatic_to_bigonial",
        ]

        proportions = modification.proportions
        assert proportions.cephalic_index == pytest.approx(16.0 / 19.0 * 100.0)
        assert proportions.face_to_head_width == pytest.approx(14.0 / 16.0)

    def test_widen_cranial_rejects_non_positive_delta(self):
        for bad in (0.0, -1.0, float("inf"), "big", True):
            with pytest.raises(ValueError, match="positive finite"):
                widen_cranial(HeadDimensions(), bad)

    # --- lengthen_cranial ---

    def test_lengthen_cranial_propagates_to_length_and_circumference(self):
        modification = lengthen_cranial(HeadDimensions(), 1.0)

        assert modification.dimensions.cranial_depth == (
            pytest.approx(20.0)
        )
        assert modification.dimensions.cranial_length == (
            pytest.approx(20.0)
        )
        assert modification.dimensions.cranial_circumference == (
            pytest.approx(_expected_circumference(15.0, 20.0))
        )
        assert modification.dimension_report.changed_names() == [
            "cranial_depth",
            "cranial_length",
            "cranial_circumference",
        ]

    def test_lengthen_cranial_proportion_report(self):
        modification = lengthen_cranial(HeadDimensions(), 1.0)

        assert modification.proportion_report.changed_names() == [
            "cephalic_index",
            "cranial_depth_to_width",
        ]
        assert modification.proportion_report.preserved_names() == [
            "cranial_height_to_width",
            "face_to_head_height",
            "face_to_head_width",
            "neurocranium_to_face_height",
            "bizygomatic_to_bigonial",
        ]

    def test_lengthen_cranial_facial_invariance(self):
        modification = lengthen_cranial(HeadDimensions(), 2.0)

        for name in ("facial_height", "bizygomatic_width", "bigonial_width"):
            assert name in modification.dimension_report.preserved_names()

    def test_lengthen_cranial_rejects_non_positive_delta(self):
        with pytest.raises(ValueError, match="positive finite"):
            lengthen_cranial(HeadDimensions(), -0.5)

    # --- adjust_neurocranial_height ---

    def test_adjust_neurocranial_height_selective(self):
        modification = adjust_neurocranial_height(
            HeadDimensions(),
            1.0,
        )

        assert modification.dimensions.neurocranial_height == (
            pytest.approx(14.0)
        )
        assert modification.dimension_report.changed_names() == [
            "neurocranial_height"
        ]
        assert len(modification.dimension_report.preserved_names()) == 9

        assert modification.proportion_report.changed_names() == [
            "cranial_height_to_width",
            "neurocranium_to_face_height",
        ]
        assert modification.proportion_report.preserved_names() == [
            "cephalic_index",
            "cranial_depth_to_width",
            "face_to_head_height",
            "face_to_head_width",
            "bizygomatic_to_bigonial",
        ]

    def test_adjust_neurocranial_height_accepts_negative(self):
        modification = adjust_neurocranial_height(
            HeadDimensions(),
            -1.0,
        )

        assert modification.dimensions.neurocranial_height == (
            pytest.approx(12.0)
        )
        assert modification.dimension_report.changed_names() == [
            "neurocranial_height"
        ]

    def test_adjust_neurocranial_height_rejects_zero(self):
        with pytest.raises(ValueError, match="non-zero"):
            adjust_neurocranial_height(HeadDimensions(), 0.0)

    # --- component contract ---

    def test_head_modification_contract(self):
        modification = widen_cranial(HeadDimensions(), 1.0)

        assert modification.component_type == "head_modification"
        assert modification.is_valid()

        data = modification.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["enabled"] is True
        assert data["dimensions"]["cranial_width"] == (
            pytest.approx(16.0)
        )
        assert data["proportions"]["cephalic_index"] == (
            pytest.approx(16.0 / 19.0 * 100.0)
        )
        assert data["dimension_report"]["operation"] == (
            "widen_cranial +1.0"
        )
        assert len(data["dimension_report"]["changes"]) == 3
        assert len(data["proportion_report"]["changes"]) == 4

    def test_modification_rejects_foreign_report_names(self):
        dimensions = HeadDimensions()
        proportions = HeadProportions()

        foreign_dimension_report = ModifyResult(
            operation="bad",
            changes=[
                PropertyChange(name="nose_length", before=1.0, after=2.0)
            ],
        )

        ok_proportion_report = diff_properties(
            proportions,
            proportions,
            ["cephalic_index"],
            operation="ok",
        )

        with pytest.raises(ValueError, match="unknown property"):
            HeadModification(
                dimensions=dimensions,
                proportions=proportions,
                dimension_report=foreign_dimension_report,
                proportion_report=ok_proportion_report,
            )

        foreign_proportion_report = ModifyResult(
            operation="bad",
            preserved=["upper_to_mid_ratio"],
        )

        ok_dimension_report = diff_properties(
            dimensions,
            dimensions,
            ["cranial_height"],
            operation="ok",
        )

        with pytest.raises(ValueError, match="unknown property"):
            HeadModification(
                dimensions=dimensions,
                proportions=proportions,
                dimension_report=ok_dimension_report,
                proportion_report=foreign_proportion_report,
            )

    def test_modification_rejects_wrong_component_types(self):
        dimensions = HeadDimensions()
        proportions = HeadProportions()
        ok_dimension_report = diff_properties(
            dimensions,
            dimensions,
            ["cranial_height"],
            operation="ok",
        )
        ok_proportion_report = diff_properties(
            proportions,
            proportions,
            ["cephalic_index"],
            operation="ok",
        )

        with pytest.raises(ValueError, match="must be"):
            HeadModification(
                dimensions="dimensions",
                proportions=proportions,
                dimension_report=ok_dimension_report,
                proportion_report=ok_proportion_report,
            )

        with pytest.raises(ValueError, match="must be a ModifyResult"):
            HeadModification(
                dimensions=dimensions,
                proportions=proportions,
                dimension_report=ok_dimension_report,
                proportion_report="report",
            )

    def test_serialization_nested(self):
        modification = adjust_neurocranial_height(
            HeadDimensions(),
            -1.0,
        )

        data = modification.to_dict()

        assert data["dimensions"]["neurocranial_height"] == (
            pytest.approx(12.0)
        )
        assert data["dimension_report"]["changes"][0]["name"] == (
            "neurocranial_height"
        )
        assert data["dimension_report"]["changes"][0]["before"] == (
            pytest.approx(13.0)
        )
        assert data["dimension_report"]["changes"][0]["after"] == (
            pytest.approx(12.0)
        )