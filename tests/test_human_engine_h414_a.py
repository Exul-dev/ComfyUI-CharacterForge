from __future__ import annotations

import pytest

from human.anatomy import (
    Face,
    FaceDimensions,
    ModifyResult,
    PropertyChange,
    diff_properties,
)


class TestHumanEngineH414A:

    # --- PropertyChange ---

    def test_change_detects_numeric_difference(self):
        change = PropertyChange(
            name="bizygomatic_width",
            before=14.0,
            after=15.0,
        )

        assert change.name == "bizygomatic_width"
        assert change.before == 14.0
        assert change.after == 15.0
        assert change.changed is True

    def test_change_detects_equal_values(self):
        change = PropertyChange(
            name="facial_height",
            before=18.0,
            after=18.0,
        )

        assert change.changed is False

    def test_change_respects_tolerance(self):
        tiny = PropertyChange(
            name="facial_depth",
            before=10.0,
            after=10.0 + 1e-12,
            tolerance=1e-9,
        )
        big = PropertyChange(
            name="facial_depth",
            before=10.0,
            after=10.1,
            tolerance=1e-9,
        )

        assert tiny.changed is False
        assert big.changed is True

    def test_change_handles_strings_and_bools(self):
        text = PropertyChange(name="shape", before="oval", after="square")
        same_text = PropertyChange(name="shape", before="oval", after="oval")
        flag = PropertyChange(name="directed", before=False, after=True)
        same_flag = PropertyChange(name="directed", before=True, after=True)

        assert text.changed is True
        assert same_text.changed is False
        assert flag.changed is True
        assert same_flag.changed is False

    def test_change_rejects_empty_name_and_bad_tolerance(self):
        with pytest.raises(ValueError, match="non-empty"):
            PropertyChange(name="   ", before=1.0, after=2.0)

        with pytest.raises(ValueError, match="tolerance"):
            PropertyChange(name="depth", before=1.0, after=2.0, tolerance=-1.0)

        with pytest.raises(ValueError, match="tolerance"):
            PropertyChange(
                name="depth",
                before=1.0,
                after=2.0,
                tolerance=float("inf"),
            )

    def test_change_serialization(self):
        change = PropertyChange(
            name="bizygomatic_width",
            before=14.0,
            after=15.0,
        )

        assert change.to_dict() == {
            "name": "bizygomatic_width",
            "before": 14.0,
            "after": 15.0,
            "changed": True,
        }

    # --- ModifyResult contract ---

    def test_result_is_valid_component(self):
        result = ModifyResult(
            operation="widen_bizygomatic +1.0cm",
            changes=[
                PropertyChange(
                    name="bizygomatic_width",
                    before=14.0,
                    after=15.0,
                )
            ],
            preserved=["facial_height", "facial_width"],
        )

        assert result.component_type == "modify_result"
        assert result.is_valid()

        data = result.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["enabled"] is True
        assert data["operation"] == "widen_bizygomatic +1.0cm"
        assert data["changes"][0]["name"] == "bizygomatic_width"
        assert data["changes"][0]["changed"] is True
        assert data["preserved"] == ["facial_height", "facial_width"]

    def test_result_with_no_changes_is_valid(self):
        result = ModifyResult(
            operation="no-op",
            changes=[],
            preserved=["a", "b"],
        )

        assert result.is_valid()
        assert result.changed_names() == []
        assert result.preserved_names() == ["a", "b"]

    def test_result_rejects_unchanged_change(self):
        with pytest.raises(ValueError, match="declared as changed"):
            ModifyResult(
                operation="bad",
                changes=[
                    PropertyChange(name="x", before=1.0, after=1.0)
                ],
            )

    def test_result_rejects_duplicate_change(self):
        with pytest.raises(ValueError, match="duplicate change"):
            ModifyResult(
                operation="bad",
                changes=[
                    PropertyChange(name="x", before=1.0, after=2.0),
                    PropertyChange(name="x", before=2.0, after=3.0),
                ],
            )

    def test_result_rejects_duplicate_preserved(self):
        with pytest.raises(ValueError, match="duplicate preserved"):
            ModifyResult(
                operation="bad",
                preserved=["a", "a"],
            )

    def test_result_rejects_changed_and_preserved_overlap(self):
        with pytest.raises(ValueError, match="both changed and preserved"):
            ModifyResult(
                operation="bad",
                changes=[
                    PropertyChange(name="x", before=1.0, after=2.0)
                ],
                preserved=["x"],
            )

    def test_result_rejects_empty_operation(self):
        with pytest.raises(ValueError, match="non-empty"):
            ModifyResult(operation="   ")

    def test_result_query_helpers(self):
        result = ModifyResult(
            operation="op",
            changes=[
                PropertyChange(name="a", before=1.0, after=2.0),
                PropertyChange(name="b", before="oval", after="round"),
            ],
            preserved=["c", "d"],
        )

        assert result.has_changed("a") is True
        assert result.has_changed("c") is False

        change = result.change_of("b")
        assert change is not None
        assert change.before == "oval"
        assert change.after == "round"

        assert result.change_of("c") is None
        assert result.changed_names() == ["a", "b"]
        assert result.preserved_names() == ["c", "d"]

    # --- diff_properties ---

    def test_diff_between_dimensions(self):
        before = FaceDimensions()
        after = FaceDimensions(
            bizygomatic_width=15.0,
            facial_height=19.0,
        )

        result = diff_properties(
            before,
            after,
            [
                "facial_height",
                "facial_width",
                "facial_depth",
                "upper_face_height",
                "bizygomatic_width",
            ],
            operation="widen bizygomatic, raise facial height",
        )

        assert result.is_valid()
        assert result.changed_names() == [
            "facial_height",
            "bizygomatic_width",
        ]
        assert result.preserved_names() == [
            "facial_width",
            "facial_depth",
            "upper_face_height",
        ]

        change = result.change_of("bizygomatic_width")
        assert change is not None
        assert change.before == 14.0
        assert change.after == 15.0

    def test_diff_tolerance_classifies_preserved(self):
        before = FaceDimensions(facial_depth=10.0)
        after = FaceDimensions(facial_depth=10.0005)

        lenient = diff_properties(
            before,
            after,
            ["facial_depth"],
            operation="tolerant diff",
            tolerance=1e-2,
        )
        strict = diff_properties(
            before,
            after,
            ["facial_depth"],
            operation="strict diff",
        )

        assert lenient.preserved_names() == ["facial_depth"]
        assert strict.changed_names() == ["facial_depth"]

    def test_diff_unknown_property_is_rejected(self):
        with pytest.raises(ValueError, match="not found"):
            diff_properties(
                FaceDimensions(),
                FaceDimensions(),
                ["nonexistent_property"],
                operation="bad",
            )

    def test_diff_rejects_non_components(self):
        with pytest.raises(ValueError, match="components"):
            diff_properties(
                "before",
                FaceDimensions(),
                ["facial_height"],
                operation="bad",
            )

        with pytest.raises(ValueError, match="components"):
            diff_properties(
                FaceDimensions(),
                None,
                ["facial_height"],
                operation="bad",
            )

    def test_diff_rejects_duplicate_and_empty_names(self):
        with pytest.raises(ValueError, match="duplicate property"):
            diff_properties(
                FaceDimensions(),
                FaceDimensions(),
                ["facial_height", "facial_height"],
                operation="bad",
            )

        with pytest.raises(ValueError, match="non-empty"):
            diff_properties(
                FaceDimensions(),
                FaceDimensions(),
                ["facial_height", "  "],
                operation="bad",
            )

        with pytest.raises(ValueError, match="at least one"):
            diff_properties(
                FaceDimensions(),
                FaceDimensions(),
                [],
                operation="bad",
            )

    def test_diff_rejects_invalid_tolerance(self):
        for bad in (-1.0, float("inf"), "wide", True):
            with pytest.raises(ValueError, match="tolerance"):
                diff_properties(
                    FaceDimensions(),
                    FaceDimensions(),
                    ["facial_height"],
                    operation="bad",
                    tolerance=bad,
                )

    def test_diff_on_string_properties(self):
        before = Face()
        after = Face(shape="square")

        result = diff_properties(
            before,
            after,
            ["shape", "height"],
            operation="square face",
        )

        assert result.changed_names() == ["shape"]
        assert result.preserved_names() == ["height"]

    def test_end_to_end_contract_example(self):
        # The Part III promise, in miniature: modify a couple of
        # properties and PROVE that everything else survived.
        original = FaceDimensions()
        modified = FaceDimensions(
            bizygomatic_width=15.0,
            jaw_width=13.0,
        )

        names = [
            "facial_height",
            "facial_width",
            "facial_depth",
            "upper_face_height",
            "mid_face_height",
            "lower_face_height",
            "forehead_width",
            "bizygomatic_width",
            "bigonial_width",
            "jaw_width",
            "chin_width",
            "chin_height",
        ]

        result = diff_properties(
            original,
            modified,
            names,
            operation="widen cheekbones and jaw",
        )

        assert result.is_valid()
        assert result.changed_names() == [
            "bizygomatic_width",
            "jaw_width",
        ]
        assert len(result.preserved_names()) == 10
        assert (
            set(result.changed_names())
            & set(result.preserved_names())
            == set()
        )

        data = result.to_dict()
        assert data["operation"] == "widen cheekbones and jaw"
        assert len(data["changes"]) == 2
        assert len(data["preserved"]) == 10