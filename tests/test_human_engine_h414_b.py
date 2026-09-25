from __future__ import annotations

import pytest

from human.anatomy import (
    FaceDimensions,
    FacialModification,
    FacialProportions,
    ModifyResult,
    PropertyChange,
    adjust_facial_height,
    diff_properties,
    modify_face_dimensions,
    widen_bizygomatic,
    widen_jaw,
)


class TestHumanEngineH414B:

    # --- generic operator ---

    def test_modify_generic_single_delta(self):
        modification = modify_face_dimensions(
            FaceDimensions(),
            {"chin_height": 0.5},
            operation="grow chin height",
        )

        assert modification.dimensions.chin_height == pytest.approx(4.5)
        assert modification.dimension_report.changed_names() == [
            "chin_height"
        ]
        assert len(modification.dimension_report.preserved_names()) == 11

    def test_modify_generic_multiple_deltas(self):
        modification = modify_face_dimensions(
            FaceDimensions(),
            {
                "bizygomatic_width": 1.0,
                "facial_width": 1.0,
                "forehead_width": -0.5,
            },
            operation="cheekbones out, forehead in",
        )

        assert modification.dimension_report.changed_names() == [
            "facial_width",
            "forehead_width",
            "bizygomatic_width",
        ]
        assert (
            modification.dimensions.bizygomatic_width
            == pytest.approx(15.0)
        )
        assert (
            modification.dimensions.forehead_width
            == pytest.approx(11.5)
        )

    def test_modify_generic_zero_delta_is_noop(self):
        modification = modify_face_dimensions(
            FaceDimensions(),
            {"facial_height": 0.0},
            operation="noop",
        )

        assert modification.is_valid()
        assert modification.dimension_report.changed_names() == []
        assert len(modification.dimension_report.preserved_names()) == 12

    def test_modify_rejects_unknown_property(self):
        with pytest.raises(ValueError, match="Unknown facial dimension"):
            modify_face_dimensions(
                FaceDimensions(),
                {"nose_length": 1.0},
                operation="bad",
            )

    def test_modify_rejects_invalid_delta_values(self):
        for bad in (float("nan"), float("inf"), "wide", True, None):
            with pytest.raises(ValueError, match="finite number"):
                modify_face_dimensions(
                    FaceDimensions(),
                    {"facial_height": bad},
                    operation="bad",
                )

    def test_modify_rejects_empty_deltas(self):
        for bad in ({}, None, "facial_height"):
            with pytest.raises(ValueError, match="non-empty dict"):
                modify_face_dimensions(
                    FaceDimensions(),
                    bad,
                    operation="bad",
                )

    def test_modify_rejects_non_dimensions(self):
        with pytest.raises(ValueError, match="FaceDimensions"):
            modify_face_dimensions(
                "dimensions",
                {"facial_height": 1.0},
                operation="bad",
            )

    def test_modify_rejects_resulting_non_positive(self):
        # FaceDimensions itself rejects non-positive values: the
        # operator must not swallow that error.
        with pytest.raises(ValueError, match="greater than zero"):
            modify_face_dimensions(
                FaceDimensions(),
                {"facial_height": -100.0},
                operation="bad",
            )

    def test_modify_rejects_empty_operation(self):
        with pytest.raises(ValueError, match="non-empty"):
            modify_face_dimensions(
                FaceDimensions(),
                {"facial_height": 1.0},
                operation="   ",
            )

    # --- semantic wrappers ---

    def test_widen_bizygomatic_propagates_to_facial_width(self):
        modification = widen_bizygomatic(FaceDimensions(), 1.0)

        assert modification.dimensions.bizygomatic_width == (
            pytest.approx(15.0)
        )
        assert modification.dimensions.facial_width == (
            pytest.approx(15.0)
        )
        assert modification.dimension_report.changed_names() == [
            "facial_width",
            "bizygomatic_width",
        ]

    def test_widen_bizygomatic_preserves_everything_else(self):
        before = FaceDimensions()
        modification = widen_bizygomatic(before, 1.0)
        after = modification.dimensions

        for name in (
            "facial_height",
            "facial_depth",
            "upper_face_height",
            "mid_face_height",
            "lower_face_height",
            "forehead_width",
            "bigonial_width",
            "jaw_width",
            "chin_width",
            "chin_height",
        ):
            assert getattr(after, name) == pytest.approx(
                getattr(before, name)
            )

        assert modification.dimension_report.preserved_names() == [
            "facial_height",
            "facial_depth",
            "upper_face_height",
            "mid_face_height",
            "lower_face_height",
            "forehead_width",
            "bigonial_width",
            "jaw_width",
            "chin_width",
            "chin_height",
        ]

    def test_widen_bizygomatic_rejects_non_positive_delta(self):
        for bad in (0.0, -1.0, float("inf"), "big", True):
            with pytest.raises(ValueError, match="positive finite"):
                widen_bizygomatic(FaceDimensions(), bad)

    def test_widen_jaw_propagates_to_jaw_width(self):
        modification = widen_jaw(FaceDimensions(), 1.5)

        assert modification.dimensions.bigonial_width == (
            pytest.approx(13.5)
        )
        assert modification.dimensions.jaw_width == pytest.approx(13.5)
        assert modification.dimension_report.changed_names() == [
            "bigonial_width",
            "jaw_width",
        ]

    def test_widen_jaw_rejects_non_positive_delta(self):
        with pytest.raises(ValueError, match="positive finite"):
            widen_jaw(FaceDimensions(), -0.5)

    def test_adjust_facial_height_changes_only_height(self):
        modification = adjust_facial_height(FaceDimensions(), 1.0)

        assert modification.dimensions.facial_height == (
            pytest.approx(19.0)
        )
        assert modification.dimension_report.changed_names() == [
            "facial_height"
        ]
        assert len(modification.dimension_report.preserved_names()) == 11

    def test_adjust_facial_height_accepts_negative_delta(self):
        modification = adjust_facial_height(FaceDimensions(), -2.0)

        assert modification.dimensions.facial_height == (
            pytest.approx(16.0)
        )
        assert modification.dimension_report.changed_names() == [
            "facial_height"
        ]

    def test_adjust_facial_height_rejects_zero(self):
        with pytest.raises(ValueError, match="non-zero"):
            adjust_facial_height(FaceDimensions(), 0.0)

    # --- rederived proportions ---

    def test_proportions_are_rederived(self):
        modification = widen_bizygomatic(FaceDimensions(), 1.0)
        proportions = modification.proportions

        assert proportions.cheek_to_jaw_ratio == pytest.approx(15.0 / 12.0)
        assert proportions.width_to_height_ratio == pytest.approx(
            15.0 / 18.0
        )
        assert proportions.forehead_to_cheek_ratio == pytest.approx(
            12.0 / 15.0
        )
        # The vertical thirds are untouched by a width operation.
        assert proportions.upper_to_mid_ratio == pytest.approx(5.8 / 6.2)
        assert proportions.mid_to_lower_ratio == pytest.approx(6.2 / 6.0)
        assert proportions.jaw_to_chin_ratio == pytest.approx(12.0 / 5.0)

    def test_proportion_report_selective(self):
        modification = widen_bizygomatic(FaceDimensions(), 1.0)

        assert modification.proportion_report.changed_names() == [
            "width_to_height_ratio",
            "forehead_to_cheek_ratio",
            "cheek_to_jaw_ratio",
        ]
        assert modification.proportion_report.preserved_names() == [
            "upper_to_mid_ratio",
            "mid_to_lower_ratio",
            "jaw_to_chin_ratio",
        ]

    def test_height_change_only_moves_width_to_height(self):
        modification = adjust_facial_height(FaceDimensions(), 1.0)

        assert modification.proportion_report.changed_names() == [
            "width_to_height_ratio"
        ]
        assert len(modification.proportion_report.preserved_names()) == 5

    # --- the Part III narrative, proven ---

    def test_entity_a_to_entity_b_narrative(self):
        entity_a = FaceDimensions()
        modification = widen_bizygomatic(entity_a, 1.0)
        entity_b = modification.dimensions

        # ENTITY B knows exactly what changed...
        assert modification.dimension_report.changed_names() == [
            "facial_width",
            "bizygomatic_width",
        ]

        # ...and what was preserved.
        assert set(modification.dimension_report.preserved_names()) == {
            "facial_height",
            "facial_depth",
            "upper_face_height",
            "mid_face_height",
            "lower_face_height",
            "forehead_width",
            "bigonial_width",
            "jaw_width",
            "chin_width",
            "chin_height",
        }

        # And the derived proportions moved only where they had to.
        assert set(modification.proportion_report.preserved_names()) == {
            "upper_to_mid_ratio",
            "mid_to_lower_ratio",
            "jaw_to_chin_ratio",
        }

    # --- component contract ---

    def test_facial_modification_contract(self):
        modification = widen_bizygomatic(FaceDimensions(), 1.0)

        assert modification.component_type == "facial_modification"
        assert modification.is_valid()

        data = modification.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["enabled"] is True
        assert data["dimensions"]["bizygomatic_width"] == (
            pytest.approx(15.0)
        )
        assert data["proportions"]["cheek_to_jaw_ratio"] == (
            pytest.approx(15.0 / 12.0)
        )
        assert data["dimension_report"]["operation"] == (
            "widen_bizygomatic +1.0"
        )
        assert len(data["dimension_report"]["changes"]) == 2
        assert len(data["proportion_report"]["changes"]) == 3

    def test_modification_rejects_foreign_report_names(self):
        dimensions = FaceDimensions()
        proportions = FacialProportions()

        foreign_dimension_report = ModifyResult(
            operation="bad",
            changes=[
                PropertyChange(name="nose_length", before=1.0, after=2.0)
            ],
        )

        ok_proportion_report = diff_properties(
            proportions,
            proportions,
            ["upper_to_mid_ratio"],
            operation="ok",
        )

        with pytest.raises(ValueError, match="unknown property"):
            FacialModification(
                dimensions=dimensions,
                proportions=proportions,
                dimension_report=foreign_dimension_report,
                proportion_report=ok_proportion_report,
            )

        foreign_proportion_report = ModifyResult(
            operation="bad",
            preserved=["cephalic_index"],
        )

        ok_dimension_report = diff_properties(
            dimensions,
            dimensions,
            ["facial_height"],
            operation="ok",
        )

        with pytest.raises(ValueError, match="unknown property"):
            FacialModification(
                dimensions=dimensions,
                proportions=proportions,
                dimension_report=ok_dimension_report,
                proportion_report=foreign_proportion_report,
            )

    def test_modification_rejects_wrong_component_types(self):
        dimensions = FaceDimensions()
        proportions = FacialProportions()
        ok_dimension_report = diff_properties(
            dimensions,
            dimensions,
            ["facial_height"],
            operation="ok",
        )
        ok_proportion_report = diff_properties(
            proportions,
            proportions,
            ["upper_to_mid_ratio"],
            operation="ok",
        )

        with pytest.raises(ValueError, match="must be"):
            FacialModification(
                dimensions="dimensions",
                proportions=proportions,
                dimension_report=ok_dimension_report,
                proportion_report=ok_proportion_report,
            )

        with pytest.raises(ValueError, match="must be a ModifyResult"):
            FacialModification(
                dimensions=dimensions,
                proportions=proportions,
                dimension_report=ok_dimension_report,
                proportion_report="report",
            )

    def test_serialization_nested(self):
        modification = adjust_facial_height(FaceDimensions(), -1.0)

        data = modification.to_dict()

        assert data["dimensions"]["facial_height"] == (
            pytest.approx(17.0)
        )
        assert data["dimension_report"]["changes"][0]["name"] == (
            "facial_height"
        )
        assert data["dimension_report"]["changes"][0]["before"] == (
            pytest.approx(18.0)
        )
        assert data["dimension_report"]["changes"][0]["after"] == (
            pytest.approx(17.0)
        )