from __future__ import annotations

import math

import pytest

from human.anatomy import (
    CranialLandmarks,
    CranialLandmarkModification,
    FaceDimensions,
    FacialLandmarks,
    LandmarkModification,
    advance_pronasale,
    cranial_measurements,
    cranial_scale_factor,
    face_dimensions_from_measurements,
    facial_measurements,
    facial_scale_factor,
    head_dimensions_from_cranial_measurements,
    lower_gnathion,
    modify_cranial_landmarks,
    modify_facial_landmarks,
    widen_bizygomatic,
    widen_cranial,
    widen_euryons,
    widen_zygions,
)

# Same fixtures as H4.13-A / H4.13-C (tests stay self-contained).
FACIAL_POINTS = {
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

CRANIAL_POINTS = {
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


def _facial_landmarks() -> FacialLandmarks:
    return FacialLandmarks(points=dict(FACIAL_POINTS))


def _cranial_landmarks() -> CranialLandmarks:
    return CranialLandmarks(points=dict(CRANIAL_POINTS))


def _ramanujan(a: float, b: float) -> float:
    return math.pi * (
        3.0 * (a + b) - math.sqrt((3.0 * a + b) * (a + 3.0 * b))
    )


class TestFacialLandmarkModification:

    def test_move_semantic_only_landmark_changes_nothing_downstream(
        self,
    ):
        # nasion is a valid facial landmark but is not used by any
        # measurement: moving it changes the landmark set only.
        modification = modify_facial_landmarks(
            _facial_landmarks(),
            {"nasion": (0.0, 0.0, 0.05)},
            operation="adjust nasion",
        )

        assert modification.landmarks.points["nasion"] == (
            0.50,
            0.22,
            0.50,
        )
        assert modification.landmark_report.changed_names() == [
            "nasion"
        ]
        assert (
            len(modification.landmark_report.preserved_names()) == 18
        )
        assert modification.dimension_report.changed_names() == []
        assert (
            len(modification.dimension_report.preserved_names()) == 12
        )
        assert modification.proportion_report.changed_names() == []
        assert (
            len(modification.proportion_report.preserved_names()) == 6
        )
        assert modification.is_valid()

    def test_landmark_report_covers_all_points(self):
        modification = widen_zygions(_facial_landmarks(), 0.02)
        report = modification.landmark_report

        assert report.changed_names() == [
            "left_zygion",
            "right_zygion",
        ]
        assert len(report.preserved_names()) == 17
        assert (
            set(report.changed_names())
            | set(report.preserved_names())
            == set(FACIAL_POINTS)
        )

        change = report.change_of("left_zygion")
        assert change is not None
        assert change.before == (0.16, 0.42, 0.10)
        assert change.after == (0.14, 0.42, 0.10)

    def test_widen_zygions_dimension_report(self):
        modification = widen_zygions(_facial_landmarks(), 0.02)

        assert modification.dimensions.bizygomatic_width == (
            pytest.approx(13.5)
        )
        assert modification.dimensions.facial_width == (
            pytest.approx(13.5)
        )
        assert modification.dimensions.facial_height == (
            pytest.approx(18.0)
        )
        assert modification.dimension_report.changed_names() == [
            "facial_width",
            "bizygomatic_width",
        ]
        assert (
            len(modification.dimension_report.preserved_names()) == 10
        )

    def test_widen_zygions_proportion_report(self):
        modification = widen_zygions(_facial_landmarks(), 0.02)

        assert modification.proportions.cheek_to_jaw_ratio == (
            pytest.approx(13.5 / 9.75)
        )
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

    def test_widen_zygions_matches_widen_bizygomatic(self):
        # Bottom-up (move the zygions) and top-down (widen the
        # bizygomatic width) produce the same model.
        fixture = _facial_landmarks()
        bottom_up = widen_zygions(fixture, 0.02)

        measurements = facial_measurements(fixture)
        scale = facial_scale_factor(measurements, 18.0)
        dimensions = face_dimensions_from_measurements(
            measurements,
            scale,
        )
        top_down = widen_bizygomatic(dimensions, 0.75)

        assert top_down.dimensions.bizygomatic_width == (
            pytest.approx(13.5)
        )
        assert bottom_up.dimensions.bizygomatic_width == (
            pytest.approx(top_down.dimensions.bizygomatic_width)
        )
        assert bottom_up.dimensions.facial_width == pytest.approx(
            top_down.dimensions.facial_width
        )
        assert bottom_up.proportions.cheek_to_jaw_ratio == (
            pytest.approx(top_down.proportions.cheek_to_jaw_ratio)
        )
        assert bottom_up.dimension_report.changed_names() == (
            top_down.dimension_report.changed_names()
        )
        assert bottom_up.proportion_report.changed_names() == (
            top_down.proportion_report.changed_names()
        )

    def test_lower_gnathion_dimension_report(self):
        modification = lower_gnathion(_facial_landmarks(), 0.01)

        assert modification.dimensions.facial_height == (
            pytest.approx(18.1875)
        )
        assert modification.dimensions.lower_face_height == (
            pytest.approx(8.8125)
        )
        assert modification.dimensions.chin_height == (
            pytest.approx(5.8125)
        )
        assert modification.dimension_report.changed_names() == [
            "facial_height",
            "lower_face_height",
            "chin_height",
        ]
        assert (
            len(modification.dimension_report.preserved_names()) == 9
        )

    def test_lower_gnathion_proportion_report(self):
        modification = lower_gnathion(_facial_landmarks(), 0.01)

        assert modification.proportion_report.changed_names() == [
            "mid_to_lower_ratio",
            "width_to_height_ratio",
        ]
        assert modification.proportion_report.preserved_names() == [
            "upper_to_mid_ratio",
            "forehead_to_cheek_ratio",
            "cheek_to_jaw_ratio",
            "jaw_to_chin_ratio",
        ]

    def test_lower_gnathion_rejects_move_out_of_bounding_box(self):
        # y = 0.98 + 0.03 = 1.01 exceeds the 0..1 range: the
        # FacialLandmarks contract itself rejects the move.
        with pytest.raises(ValueError, match="y coordinate"):
            lower_gnathion(_facial_landmarks(), 0.03)

    def test_advance_pronasale_changes_only_depth(self):
        modification = advance_pronasale(_facial_landmarks(), 0.05)

        assert modification.dimensions.facial_depth == (
            pytest.approx(26.25)
        )
        assert modification.dimension_report.changed_names() == [
            "facial_depth"
        ]
        assert (
            len(modification.dimension_report.preserved_names()) == 11
        )
        # No facial proportion involves depth: they all survive.
        assert modification.proportion_report.changed_names() == []
        assert (
            len(modification.proportion_report.preserved_names()) == 6
        )

    def test_zero_move_is_noop(self):
        modification = modify_facial_landmarks(
            _facial_landmarks(),
            {"nasion": (0.0, 0.0, 0.0)},
            operation="noop",
        )

        assert modification.is_valid()
        assert modification.landmark_report.changed_names() == []
        assert (
            len(modification.landmark_report.preserved_names()) == 19
        )
        assert modification.dimension_report.changed_names() == []
        assert (
            len(modification.dimension_report.preserved_names()) == 12
        )
        assert modification.proportion_report.changed_names() == []

    def test_rejects_absent_or_unknown_landmark(self):
        with pytest.raises(ValueError, match="not present"):
            modify_facial_landmarks(
                _facial_landmarks(),
                {"menton": (0.0, 0.0, 0.0)},
                operation="bad",
            )

        with pytest.raises(ValueError, match="not present"):
            modify_facial_landmarks(
                _facial_landmarks(),
                {"not_a_landmark": (0.0, 0.0, 0.0)},
                operation="bad",
            )

    def test_rejects_invalid_delta_triples(self):
        with pytest.raises(ValueError, match="exactly three"):
            modify_facial_landmarks(
                _facial_landmarks(),
                {"nasion": (0.1, 0.2)},
                operation="bad",
            )

        with pytest.raises(ValueError, match="exactly three"):
            modify_facial_landmarks(
                _facial_landmarks(),
                {"nasion": "dx"},
                operation="bad",
            )

        with pytest.raises(ValueError, match="finite"):
            modify_facial_landmarks(
                _facial_landmarks(),
                {"nasion": (0.1, 0.2, float("inf"))},
                operation="bad",
            )

        with pytest.raises(ValueError, match="finite"):
            modify_facial_landmarks(
                _facial_landmarks(),
                {"nasion": (0.1, 0.2, True)},
                operation="bad",
            )

    def test_rejects_empty_moves(self):
        for bad in ({}, None, "nasion"):
            with pytest.raises(ValueError, match="non-empty dict"):
                modify_facial_landmarks(
                    _facial_landmarks(),
                    bad,
                    operation="bad",
                )

    def test_rejects_non_landmarks(self):
        with pytest.raises(ValueError, match="FacialLandmarks"):
            modify_facial_landmarks(
                "landmarks",
                {"nasion": (0.0, 0.0, 0.0)},
                operation="bad",
            )

    def test_rejects_invalid_target_height(self):
        for bad in (0.0, -18.0, float("inf"), "tall"):
            with pytest.raises(ValueError, match="target_facial_height"):
                modify_facial_landmarks(
                    _facial_landmarks(),
                    {"nasion": (0.0, 0.0, 0.01)},
                    operation="bad",
                    target_facial_height=bad,
                )

    def test_missing_required_landmark_propagates(self):
        points = {
            name: point
            for name, point in FACIAL_POINTS.items()
            if name != "trichion"
        }

        with pytest.raises(ValueError, match="trichion"):
            modify_facial_landmarks(
                FacialLandmarks(points=points),
                {"nasion": (0.0, 0.0, 0.01)},
                operation="bad",
            )

    def test_rejects_empty_operation(self):
        with pytest.raises(ValueError, match="non-empty"):
            modify_facial_landmarks(
                _facial_landmarks(),
                {"nasion": (0.0, 0.0, 0.01)},
                operation="   ",
            )

    def test_result_is_canonical_derivation_of_new_landmarks(self):
        # The after-model IS what a fresh derivation from the new
        # landmarks produces: the modification chain is
        # deterministic and canonical.
        modification = widen_zygions(_facial_landmarks(), 0.02)

        fresh_measurements = facial_measurements(
            modification.landmarks
        )
        fresh_scale = facial_scale_factor(fresh_measurements, 18.0)
        fresh_dimensions = face_dimensions_from_measurements(
            fresh_measurements,
            fresh_scale,
        )

        assert fresh_dimensions.bizygomatic_width == pytest.approx(
            modification.dimensions.bizygomatic_width
        )
        assert fresh_dimensions.facial_width == pytest.approx(
            modification.dimensions.facial_width
        )
        assert fresh_dimensions.facial_height == pytest.approx(
            modification.dimensions.facial_height
        )

    def test_contract_and_serialization(self):
        modification = widen_zygions(_facial_landmarks(), 0.02)

        assert modification.component_type == "landmark_modification"
        assert modification.is_valid()

        data = modification.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["enabled"] is True
        assert data["landmarks"]["points"]["left_zygion"] == [
            0.14,
            0.42,
            0.10,
        ]
        assert data["measurements"]["bizygomatic_width"] == (
            pytest.approx(0.72)
        )
        assert data["dimensions"]["bizygomatic_width"] == (
            pytest.approx(13.5)
        )
        assert data["landmark_report"]["changes"][0]["name"] == (
            "left_zygion"
        )
        assert len(data["landmark_report"]["changes"]) == 2
        assert len(data["landmark_report"]["preserved"]) == 17
        assert len(data["dimension_report"]["changes"]) == 2
        assert len(data["proportion_report"]["changes"]) == 3


class TestCranialLandmarkModification:

    def test_widen_euryons_dimension_report(self):
        modification = widen_euryons(_cranial_landmarks(), 0.02)

        assert modification.dimensions.cranial_width == (
            pytest.approx(8.8)
        )
        assert modification.dimensions.cranial_breadth == (
            pytest.approx(8.8)
        )
        assert modification.dimensions.cranial_circumference == (
            pytest.approx(_ramanujan(0.44, 0.95) * 10.0)
        )
        assert modification.dimension_report.changed_names() == [
            "cranial_width",
            "cranial_breadth",
            "cranial_circumference",
        ]

    def test_widen_euryons_facial_invariance(self):
        # Mirror of H4.14-C: a cranial landmark move leaves the
        # facial trio of the head model exactly as it was.
        modification = widen_euryons(_cranial_landmarks(), 0.02)

        for name in (
            "facial_height",
            "bizygomatic_width",
            "bigonial_width",
        ):
            assert (
                name
                in modification.dimension_report.preserved_names()
            )
            assert not modification.dimension_report.has_changed(name)

    def test_widen_euryons_proportion_report(self):
        modification = widen_euryons(_cranial_landmarks(), 0.02)

        assert modification.proportions.cephalic_index == (
            pytest.approx(8.8 / 19.0 * 100.0)
        )
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

    def test_widen_euryons_matches_widen_cranial(self):
        # Bottom-up (move the euryons) and top-down (widen the
        # cranial width) produce the same model, circumference
        # included: the Ramanujan perimeter is homogeneous, so
        # R(4.4, 9.5) == 10 * R(0.44, 0.95).
        fixture = _cranial_landmarks()
        bottom_up = widen_euryons(fixture, 0.02)

        measurements = cranial_measurements(fixture)
        scale = cranial_scale_factor(measurements, 19.0)
        head = head_dimensions_from_cranial_measurements(
            FaceDimensions(),
            measurements,
            scale,
        )
        top_down = widen_cranial(head, 0.4)

        assert top_down.dimensions.cranial_width == pytest.approx(8.8)
        assert bottom_up.dimensions.cranial_width == pytest.approx(
            top_down.dimensions.cranial_width
        )
        assert bottom_up.dimensions.cranial_breadth == pytest.approx(
            top_down.dimensions.cranial_breadth
        )
        assert (
            bottom_up.dimensions.cranial_circumference
            == pytest.approx(
                top_down.dimensions.cranial_circumference
            )
        )
        assert (
            bottom_up.dimensions.neurocranial_height
            == pytest.approx(
                top_down.dimensions.neurocranial_height
            )
        )
        assert bottom_up.proportion_report.changed_names() == (
            top_down.proportion_report.changed_names()
        )

    def test_cranial_landmark_report(self):
        modification = widen_euryons(_cranial_landmarks(), 0.02)
        report = modification.landmark_report

        assert report.changed_names() == [
            "left_euryon",
            "right_euryon",
        ]
        assert len(report.preserved_names()) == 8
        assert (
            set(report.changed_names())
            | set(report.preserved_names())
            == set(CRANIAL_POINTS)
        )

    def test_move_vertex_changes_vault_height(self):
        modification = modify_cranial_landmarks(
            _cranial_landmarks(),
            {"vertex": (0.0, -0.03, 0.0)},
            operation="raise vertex",
        )

        assert modification.dimensions.neurocranial_height == (
            pytest.approx(4.6)
        )
        assert modification.dimensions.cranial_height == (
            pytest.approx(22.6)
        )
        assert modification.dimension_report.changed_names() == [
            "cranial_height",
            "neurocranial_height",
        ]
        assert (
            len(modification.dimension_report.preserved_names()) == 8
        )
        assert modification.proportion_report.changed_names() == [
            "cranial_height_to_width",
            "face_to_head_height",
            "neurocranium_to_face_height",
        ]
        assert modification.proportion_report.preserved_names() == [
            "cephalic_index",
            "cranial_depth_to_width",
            "face_to_head_width",
            "bizygomatic_to_bigonial",
        ]

    def test_cranial_rejects_invalid_inputs(self):
        with pytest.raises(ValueError, match="CranialLandmarks"):
            modify_cranial_landmarks(
                "landmarks",
                {"vertex": (0.0, 0.0, 0.0)},
                operation="bad",
            )

        with pytest.raises(ValueError, match="non-empty dict"):
            modify_cranial_landmarks(
                _cranial_landmarks(),
                {},
                operation="bad",
            )

        with pytest.raises(ValueError, match="not present"):
            modify_cranial_landmarks(
                _cranial_landmarks(),
                {"menton": (0.0, 0.0, 0.0)},
                operation="bad",
            )

        with pytest.raises(ValueError, match="exactly three"):
            modify_cranial_landmarks(
                _cranial_landmarks(),
                {"vertex": (1.0, 2.0)},
                operation="bad",
            )

        with pytest.raises(ValueError, match="target_cranial_length"):
            modify_cranial_landmarks(
                _cranial_landmarks(),
                {"vertex": (0.0, 0.0, 0.0)},
                operation="bad",
                target_cranial_length=0.0,
            )

    def test_cranial_contract_and_serialization(self):
        modification = widen_euryons(_cranial_landmarks(), 0.02)

        assert (
            modification.component_type
            == "cranial_landmark_modification"
        )
        assert modification.is_valid()

        data = modification.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["dimensions"]["cranial_width"] == pytest.approx(
            8.8
        )
        assert data["landmarks"]["points"]["left_euryon"] == [
            0.06,
            0.30,
            -0.10,
        ]
        assert len(data["landmark_report"]["changes"]) == 2
        assert len(data["landmark_report"]["preserved"]) == 8
        assert len(data["dimension_report"]["changes"]) == 3
        assert len(data["proportion_report"]["changes"]) == 4