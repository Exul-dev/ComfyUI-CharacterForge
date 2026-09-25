from __future__ import annotations

from typing import Any, Iterable

from .anatomy_component import AnatomyComponent
from .coordinate_system import CoordinateSystem
from .landmark import Landmark
from .landmark_relation import LandmarkRelation


class LandmarkGraph(AnatomyComponent):
    """Semantic graph of anatomical landmarks and their relations.

    The graph turns isolated landmarks and relations into a coherent
    structure:

    - landmarks are unique by name;
    - relations can only reference landmarks present in the graph;
    - duplicate relations (including mirrored undirected ones) are
      rejected;
    - an optional shared coordinate system constrains the coordinate
      space of every landmark in the graph.
    """

    component_type = "landmark_graph"

    def __init__(
        self,
        landmarks: Iterable[Landmark] | None = None,
        relations: Iterable[LandmarkRelation] | None = None,
        coordinate_system: CoordinateSystem | None = None,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.landmarks: dict[str, Landmark] = {}
        self.relations: list[LandmarkRelation] = []
        self.coordinate_system = coordinate_system

        for landmark in landmarks or []:
            self.add_landmark(landmark)

        for relation in relations or []:
            self.add_relation(relation)

        self.validate()

    def add_landmark(self, landmark: Landmark) -> Landmark:
        """Add a landmark to the graph, keyed by its name."""

        if not isinstance(landmark, Landmark):
            raise ValueError(
                "LandmarkGraph landmark must be a Landmark."
            )

        landmark.validate()

        if landmark.name in self.landmarks:
            raise ValueError(
                f"LandmarkGraph already contains a landmark "
                f"named '{landmark.name}'."
            )

        if (
            self.coordinate_system is not None
            and landmark.coordinate.space is not self.coordinate_system.space
        ):
            raise ValueError(
                "LandmarkGraph landmark coordinate space must match "
                "the graph coordinate system space."
            )

        self.landmarks[landmark.name] = landmark
        return landmark

    def add_relation(self, relation: LandmarkRelation) -> LandmarkRelation:
        """Add a relation between two landmarks of the graph."""

        if not isinstance(relation, LandmarkRelation):
            raise ValueError(
                "LandmarkGraph relation must be a LandmarkRelation."
            )

        relation.validate()

        for endpoint in (relation.landmark_a, relation.landmark_b):
            if endpoint not in self.landmarks:
                raise ValueError(
                    f"LandmarkGraph relation references unknown "
                    f"landmark '{endpoint}'."
                )

        for existing in self.relations:
            if self._same_relation(existing, relation):
                raise ValueError(
                    "LandmarkGraph already contains an equivalent "
                    f"relation between '{relation.landmark_a}' and "
                    f"'{relation.landmark_b}'."
                )

        self.relations.append(relation)
        return relation

    @staticmethod
    def _same_relation(
        first: LandmarkRelation,
        second: LandmarkRelation,
    ) -> bool:
        if first.relation_type is not second.relation_type:
            return False

        if first.directed != second.directed:
            return False

        if (
            first.landmark_a == second.landmark_a
            and first.landmark_b == second.landmark_b
        ):
            return True

        if (
            not first.directed
            and first.landmark_a == second.landmark_b
            and first.landmark_b == second.landmark_a
        ):
            return True

        return False

    def get_landmark(self, name: str) -> Landmark | None:
        """Return the landmark with the given name, if present."""

        return self.landmarks.get(name)

    def landmark_names(self) -> list[str]:
        """Return the sorted list of landmark names."""

        return sorted(self.landmarks)

    def validate(self) -> None:
        super().validate()

        if self.coordinate_system is not None and not isinstance(
            self.coordinate_system,
            CoordinateSystem,
        ):
            raise ValueError(
                "LandmarkGraph coordinate_system must be a "
                "CoordinateSystem or None."
            )

        if self.coordinate_system is not None:
            self.coordinate_system.validate()

        for landmark in self.landmarks.values():
            landmark.validate()

            if self.landmarks.get(landmark.name) is not landmark:
                raise ValueError(
                    "LandmarkGraph landmarks must be keyed by "
                    "their own name."
                )

            if (
                self.coordinate_system is not None
                and landmark.coordinate.space
                is not self.coordinate_system.space
            ):
                raise ValueError(
                    "LandmarkGraph landmark coordinate space must match "
                    "the graph coordinate system space."
                )

        seen: list[LandmarkRelation] = []

        for relation in self.relations:
            relation.validate()

            for endpoint in (relation.landmark_a, relation.landmark_b):
                if endpoint not in self.landmarks:
                    raise ValueError(
                        f"LandmarkGraph relation references unknown "
                        f"landmark '{endpoint}'."
                    )

            for previous in seen:
                if self._same_relation(previous, relation):
                    raise ValueError(
                        "LandmarkGraph contains duplicate relations."
                    )

            seen.append(relation)

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "coordinate_system": (
                self.coordinate_system.to_dict()
                if self.coordinate_system is not None
                else None
            ),
            "landmarks": [
                self.landmarks[name].to_dict()
                for name in sorted(self.landmarks)
            ],
            "relations": [
                relation.to_dict() for relation in self.relations
            ],
        }