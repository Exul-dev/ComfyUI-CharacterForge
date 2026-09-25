from __future__ import annotations

import math

import pytest

from human.anatomy import (
    LandmarkRelation,
    LandmarkRelationType,
)


class TestHumanEngineH412B:
    def test_relation_type_values(self):
        assert LandmarkRelationType.DISTANCE.value == "distance"
        assert LandmarkRelationType.ANGLE.value == "angle"
        assert (
            LandmarkRelationType.HORIZONTAL_OFFSET.value
            == "horizontal_offset"
        )
        assert (
            LandmarkRelationType.VERTICAL_OFFSET.value
            == "vertical_offset"
        )
        assert LandmarkRelationType.DEPTH_OFFSET.value == "depth_offset"

    def test_distance_relation(self):
        relation = LandmarkRelation(
            landmark_a="left_eye",
            landmark_b="right_eye",
            relation_type=LandmarkRelationType.DISTANCE,
        )

        assert relation.is_valid()
        assert relation.landmark_a == "left_eye"
        assert relation.landmark_b == "right_eye"
        assert relation.relation_type is LandmarkRelationType.DISTANCE

    def test_relation_with_measurement(self):
        relation = LandmarkRelation(
            landmark_a="left_eye",
            landmark_b="right_eye",
            relation_type=LandmarkRelationType.DISTANCE,
            value=0.12,
            unit="normalized",
        )

        assert relation.is_valid()
        assert relation.value == 0.12
        assert relation.unit == "normalized"

    def test_directed_relation(self):
        relation = LandmarkRelation(
            landmark_a="nose",
            landmark_b="mouth",
            relation_type=LandmarkRelationType.VERTICAL_OFFSET,
            value=0.08,
            unit="normalized",
            directed=True,
        )

        assert relation.is_valid()
        assert relation.directed is True

    def test_all_relation_types_are_accepted(self):
        for relation_type in LandmarkRelationType:
            relation = LandmarkRelation(
                landmark_a="landmark_a",
                landmark_b="landmark_b",
                relation_type=relation_type,
            )
            assert relation.is_valid()

    def test_same_landmark_is_rejected(self):
        with pytest.raises(ValueError, match="different"):
            LandmarkRelation(
                landmark_a="nose",
                landmark_b="nose",
                relation_type=LandmarkRelationType.DISTANCE,
            )

    def test_empty_endpoint_is_rejected(self):
        with pytest.raises(ValueError, match="landmark_a"):
            LandmarkRelation(
                landmark_a="",
                landmark_b="mouth",
                relation_type=LandmarkRelationType.DISTANCE,
            )

    def test_invalid_relation_type_is_rejected(self):
        with pytest.raises(ValueError, match="relation_type"):
            LandmarkRelation(
                landmark_a="nose",
                landmark_b="mouth",
                relation_type="vertical_offset",
            )

    def test_non_finite_value_is_rejected(self):
        with pytest.raises(ValueError, match="finite"):
            LandmarkRelation(
                landmark_a="nose",
                landmark_b="mouth",
                relation_type=LandmarkRelationType.VERTICAL_OFFSET,
                value=math.inf,
            )

    def test_negative_distance_is_rejected(self):
        with pytest.raises(ValueError, match="greater than or equal to 0"):
            LandmarkRelation(
                landmark_a="left_eye",
                landmark_b="right_eye",
                relation_type=LandmarkRelationType.DISTANCE,
                value=-0.1,
            )

    def test_empty_unit_is_rejected(self):
        with pytest.raises(ValueError, match="unit"):
            LandmarkRelation(
                landmark_a="nose",
                landmark_b="mouth",
                relation_type=LandmarkRelationType.VERTICAL_OFFSET,
                value=0.1,
                unit="",
            )

    def test_is_valid_detects_mutation(self):
        relation = LandmarkRelation(
            landmark_a="nose",
            landmark_b="chin",
            relation_type=LandmarkRelationType.VERTICAL_OFFSET,
        )

        assert relation.is_valid()

        relation.landmark_a = ""
        assert not relation.is_valid()

    def test_serialization(self):
        relation = LandmarkRelation(
            landmark_a="left_eye",
            landmark_b="right_eye",
            relation_type=LandmarkRelationType.DISTANCE,
            value=0.12,
            unit="normalized",
            directed=False,
        )

        data = relation.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "landmark_relation"
        assert data["enabled"] is True
        assert data["landmark_a"] == "left_eye"
        assert data["landmark_b"] == "right_eye"
        assert data["relation_type"] == "distance"
        assert data["value"] == 0.12
        assert data["unit"] == "normalized"
        assert data["directed"] is False

    def test_relation_is_anatomy_component(self):
        relation = LandmarkRelation(
            landmark_a="nose",
            landmark_b="chin",
            relation_type=LandmarkRelationType.VERTICAL_OFFSET,
        )

        assert relation.component_type == "landmark_relation"
        assert relation.is_valid()