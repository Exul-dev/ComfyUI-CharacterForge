from __future__ import annotations

import pytest

from human.anatomy import (
    Coordinate,
    CoordinateSpace,
    CoordinateSystem,
    Landmark,
    LandmarkGraph,
    LandmarkRelation,
    LandmarkRelationType,
)


def _landmark(
    name: str,
    x: float = 0.5,
    y: float = 0.5,
    z: float = 0.5,
    space: CoordinateSpace = CoordinateSpace.NORMALIZED_3D,
) -> Landmark:
    if space.dimensions == 2:
        coordinate = Coordinate(x=x, y=y, space=space)
    else:
        coordinate = Coordinate(x=x, y=y, z=z, space=space)
    return Landmark(name=name, coordinate=coordinate)


class TestHumanEngineH412C:

    def test_empty_graph_is_valid(self):
        graph = LandmarkGraph()

        assert graph.is_valid()
        assert graph.landmark_names() == []
        assert graph.relations == []

        data = graph.to_dict()
        assert data["component_type"] == "landmark_graph"
        assert data["landmarks"] == []
        assert data["relations"] == []
        assert data["coordinate_system"] is None

    def test_add_landmark(self):
        graph = LandmarkGraph()
        landmark = graph.add_landmark(_landmark("nasion"))

        assert landmark.name == "nasion"
        assert graph.get_landmark("nasion") is landmark
        assert graph.landmark_names() == ["nasion"]

    def test_duplicate_landmark_name_is_rejected(self):
        graph = LandmarkGraph()
        graph.add_landmark(_landmark("nasion"))

        with pytest.raises(ValueError, match="already contains"):
            graph.add_landmark(_landmark("nasion"))

    def test_add_landmark_rejects_non_landmark(self):
        graph = LandmarkGraph()

        with pytest.raises(ValueError, match="must be a Landmark"):
            graph.add_landmark("nasion")

    def test_add_relation(self):
        graph = LandmarkGraph()
        graph.add_landmark(_landmark("glabella"))
        graph.add_landmark(_landmark("nasion"))

        relation = graph.add_relation(
            LandmarkRelation(
                landmark_a="glabella",
                landmark_b="nasion",
                relation_type=LandmarkRelationType.VERTICAL_OFFSET,
            )
        )

        assert relation in graph.relations
        assert len(graph.relations) == 1

    def test_relation_with_unknown_endpoint_is_rejected(self):
        graph = LandmarkGraph()
        graph.add_landmark(_landmark("glabella"))

        with pytest.raises(ValueError, match="unknown landmark"):
            graph.add_relation(
                LandmarkRelation(
                    landmark_a="glabella",
                    landmark_b="nasion",
                    relation_type=LandmarkRelationType.VERTICAL_OFFSET,
                )
            )

    def test_duplicate_relation_is_rejected(self):
        graph = LandmarkGraph()
        graph.add_landmark(_landmark("left_zygion"))
        graph.add_landmark(_landmark("right_zygion"))
        graph.add_relation(
            LandmarkRelation(
                landmark_a="left_zygion",
                landmark_b="right_zygion",
                relation_type=LandmarkRelationType.DISTANCE,
            )
        )

        with pytest.raises(ValueError, match="equivalent relation"):
            graph.add_relation(
                LandmarkRelation(
                    landmark_a="left_zygion",
                    landmark_b="right_zygion",
                    relation_type=LandmarkRelationType.DISTANCE,
                )
            )

    def test_mirrored_undirected_relation_is_rejected(self):
        graph = LandmarkGraph()
        graph.add_landmark(_landmark("left_zygion"))
        graph.add_landmark(_landmark("right_zygion"))
        graph.add_relation(
            LandmarkRelation(
                landmark_a="left_zygion",
                landmark_b="right_zygion",
                relation_type=LandmarkRelationType.DISTANCE,
            )
        )

        with pytest.raises(ValueError, match="equivalent relation"):
            graph.add_relation(
                LandmarkRelation(
                    landmark_a="right_zygion",
                    landmark_b="left_zygion",
                    relation_type=LandmarkRelationType.DISTANCE,
                )
            )

    def test_mirrored_directed_relation_is_allowed(self):
        graph = LandmarkGraph()
        graph.add_landmark(_landmark("nose"))
        graph.add_landmark(_landmark("mouth"))
        graph.add_relation(
            LandmarkRelation(
                landmark_a="nose",
                landmark_b="mouth",
                relation_type=LandmarkRelationType.VERTICAL_OFFSET,
                directed=True,
            )
        )
        graph.add_relation(
            LandmarkRelation(
                landmark_a="mouth",
                landmark_b="nose",
                relation_type=LandmarkRelationType.VERTICAL_OFFSET,
                directed=True,
            )
        )

        assert len(graph.relations) == 2
        assert graph.is_valid()

    def test_graph_construction_from_iterables(self):
        graph = LandmarkGraph(
            landmarks=[
                _landmark("glabella"),
                _landmark("nasion"),
            ],
            relations=[
                LandmarkRelation(
                    landmark_a="glabella",
                    landmark_b="nasion",
                    relation_type=LandmarkRelationType.VERTICAL_OFFSET,
                )
            ],
        )

        assert graph.is_valid()
        assert len(graph.landmarks) == 2
        assert len(graph.relations) == 1

    def test_construction_rejects_relation_with_unknown_endpoint(self):
        with pytest.raises(ValueError, match="unknown landmark"):
            LandmarkGraph(
                landmarks=[_landmark("glabella")],
                relations=[
                    LandmarkRelation(
                        landmark_a="glabella",
                        landmark_b="nasion",
                        relation_type=LandmarkRelationType.VERTICAL_OFFSET,
                    )
                ],
            )

    def test_coordinate_system_space_mismatch_is_rejected(self):
        system = CoordinateSystem.anatomical_normalized()
        graph = LandmarkGraph(coordinate_system=system)

        mismatched = next(
            space for space in CoordinateSpace if space is not system.space
        )

        with pytest.raises(ValueError, match="space"):
            graph.add_landmark(_landmark("nasion", space=mismatched))

    def test_coordinate_system_accepts_matching_space(self):
        system = CoordinateSystem.anatomical_normalized()
        graph = LandmarkGraph(coordinate_system=system)

        graph.add_landmark(_landmark("nasion", space=system.space))

        assert graph.is_valid()

    def test_is_valid_detects_dangling_relation_after_rename(self):
        graph = LandmarkGraph()
        nose = graph.add_landmark(_landmark("nose"))
        graph.add_landmark(_landmark("chin"))
        graph.add_relation(
            LandmarkRelation(
                landmark_a="nose",
                landmark_b="chin",
                relation_type=LandmarkRelationType.VERTICAL_OFFSET,
            )
        )

        assert graph.is_valid()

        nose.name = "snout"
        assert not graph.is_valid()

    def test_is_valid_detects_duplicate_after_mutation(self):
        graph = LandmarkGraph()
        graph.add_landmark(_landmark("a"))
        graph.add_landmark(_landmark("b"))
        relation = LandmarkRelation(
            landmark_a="a",
            landmark_b="b",
            relation_type=LandmarkRelationType.DISTANCE,
        )
        graph.add_relation(relation)

        graph.relations.append(relation)
        assert not graph.is_valid()

    def test_serialization(self):
        graph = LandmarkGraph(
            landmarks=[
                _landmark("glabella"),
                _landmark("nasion"),
            ],
            relations=[
                LandmarkRelation(
                    landmark_a="glabella",
                    landmark_b="nasion",
                    relation_type=LandmarkRelationType.VERTICAL_OFFSET,
                    value=0.04,
                    unit="normalized",
                )
            ],
        )

        data = graph.to_dict()

        assert data["component_type"] == "landmark_graph"
        assert data["schema_version"] == "1.0"
        assert data["enabled"] is True
        assert data["coordinate_system"] is None
        assert [item["name"] for item in data["landmarks"]] == [
            "glabella",
            "nasion",
        ]
        assert data["relations"][0]["relation_type"] == "vertical_offset"
        assert data["relations"][0]["value"] == 0.04

    def test_end_to_end_facial_graph(self):
        system = CoordinateSystem.anatomical_normalized()
        space = system.space

        graph = LandmarkGraph(
            landmarks=[
                _landmark("glabella", x=0.50, y=0.40, z=0.92, space=space),
                _landmark("nasion", x=0.50, y=0.44, z=0.95, space=space),
                _landmark("left_zygion", x=0.36, y=0.50, z=0.80, space=space),
                _landmark("right_zygion", x=0.64, y=0.50, z=0.80, space=space),
            ],
            coordinate_system=system,
        )

        graph.add_relation(
            LandmarkRelation(
                landmark_a="glabella",
                landmark_b="nasion",
                relation_type=LandmarkRelationType.VERTICAL_OFFSET,
            )
        )
        graph.add_relation(
            LandmarkRelation(
                landmark_a="left_zygion",
                landmark_b="right_zygion",
                relation_type=LandmarkRelationType.DISTANCE,
                value=0.28,
                unit="normalized",
            )
        )

        assert graph.is_valid()
        assert graph.landmark_names() == [
            "glabella",
            "left_zygion",
            "nasion",
            "right_zygion",
        ]
        assert len(graph.relations) == 2
        assert graph.get_landmark("nasion") is not None

        data = graph.to_dict()
        assert data["component_type"] == "landmark_graph"
        assert len(data["landmarks"]) == 4
        assert len(data["relations"]) == 2
        assert data["coordinate_system"] is not None