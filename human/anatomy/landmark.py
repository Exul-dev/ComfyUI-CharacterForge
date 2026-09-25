from __future__ import annotations

from enum import Enum
from typing import Any

from .anatomy_component import AnatomyComponent
from .coordinate import Coordinate
from .enums import BodySide


class LandmarkStatus(Enum):
    """Epistemic status of a landmark observation."""

    OBSERVED = "observed"
    ESTIMATED = "estimated"
    INFERRED = "inferred"
    UNKNOWN = "unknown"


class LandmarkSource(Enum):
    """Origin of the landmark information."""

    MANUAL = "manual"
    MODEL = "model"
    VISION = "vision"
    CALCULATED = "calculated"
    IMPORTED = "imported"


class Landmark(AnatomyComponent):
    """
    Semantic anatomical landmark.

    A landmark combines:

    - semantic identity;
    - explicit coordinate;
    - optional anatomical side;
    - epistemic status;
    - confidence;
    - information source.
    """

    component_type = "landmark"

    def __init__(
        self,
        *,
        name: str,
        coordinate: Coordinate,
        side: BodySide | None = None,
        status: LandmarkStatus = LandmarkStatus.UNKNOWN,
        confidence: float = 0.0,
        source: LandmarkSource = LandmarkSource.MANUAL,
    ) -> None:
        super().__init__()

        self.name = str(name)
        self.coordinate = coordinate
        self.side = side
        self.status = status
        self.confidence = float(confidence)
        self.source = source

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not self.name.strip():
            raise ValueError(
                "Landmark name must not be empty."
            )

        if not isinstance(self.coordinate, Coordinate):
            raise ValueError(
                "Landmark coordinate must be a Coordinate."
            )

        if self.side is not None and not isinstance(
            self.side,
            BodySide,
        ):
            raise ValueError(
                "Landmark side must be BodySide or None."
            )

        if not isinstance(self.status, LandmarkStatus):
            raise ValueError(
                "Landmark status must be a LandmarkStatus."
            )

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(
                "Landmark confidence must be between 0 and 1."
            )

        if not isinstance(self.source, LandmarkSource):
            raise ValueError(
                "Landmark source must be a LandmarkSource."
            )

        self.coordinate.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "name": self.name,
            "coordinate": self.coordinate.to_dict(),
            "side": (
                self.side.value
                if self.side is not None
                else None
            ),
            "status": self.status.value,
            "confidence": self.confidence,
            "source": self.source.value,
        }