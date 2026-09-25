from __future__ import annotations

import math
from enum import Enum
from typing import Any

from .anatomy_component import AnatomyComponent


class LandmarkRelationType(Enum):
    """Semantic type of the relation between two landmarks."""

    DISTANCE = "distance"
    ANGLE = "angle"
    HORIZONTAL_OFFSET = "horizontal_offset"
    VERTICAL_OFFSET = "vertical_offset"
    DEPTH_OFFSET = "depth_offset"


class LandmarkRelation(AnatomyComponent):
    """Semantic relation between two anatomical landmarks.

    Endpoints are textual landmark identifiers, not embedded Landmark
    objects. This keeps the relation lightweight, serializable, and ready
    for a future graph representation.
    """

    component_type = "landmark_relation"

    def __init__(
        self,
        landmark_a: str,
        landmark_b: str,
        relation_type: LandmarkRelationType,
        value: float | None = None,
        unit: str | None = None,
        directed: bool = False,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.landmark_a = landmark_a
        self.landmark_b = landmark_b
        self.relation_type = relation_type
        self.value = value
        self.unit = unit
        self.directed = directed

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.landmark_a, str) or not self.landmark_a.strip():
            raise ValueError(
                "LandmarkRelation landmark_a must be a non-empty string."
            )

        if not isinstance(self.landmark_b, str) or not self.landmark_b.strip():
            raise ValueError(
                "LandmarkRelation landmark_b must be a non-empty string."
            )

        if self.landmark_a.strip() == self.landmark_b.strip():
            raise ValueError(
                "LandmarkRelation landmark_a and landmark_b must be "
                "different landmarks."
            )

        if not isinstance(self.relation_type, LandmarkRelationType):
            raise ValueError(
                "LandmarkRelation relation_type must be a LandmarkRelationType."
            )

        if self.value is not None:
            if (
                isinstance(self.value, bool)
                or not isinstance(self.value, (int, float))
                or not math.isfinite(float(self.value))
            ):
                raise ValueError(
                    "LandmarkRelation value must be a finite number or None."
                )

        if self.unit is not None:
            if not isinstance(self.unit, str) or not self.unit.strip():
                raise ValueError(
                    "LandmarkRelation unit must be a non-empty string or None."
                )

        if not isinstance(self.directed, bool):
            raise ValueError(
                "LandmarkRelation directed must be a bool."
            )

        if (
            self.relation_type is LandmarkRelationType.DISTANCE
            and self.value is not None
            and self.value < 0
        ):
            raise ValueError(
                "LandmarkRelation distance value must be "
                "greater than or equal to 0."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "landmark_a": self.landmark_a,
            "landmark_b": self.landmark_b,
            "relation_type": self.relation_type.value,
            "value": self.value,
            "unit": self.unit,
            "directed": self.directed,
        }