from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class CranialLandmarks(AnatomyComponent):
    """Canonical anatomical cranial landmark coordinates.

    Coordinates are normalized to the head bounding box: x (left to
    right) and y (top to bottom, vertex near 0) are in the 0..1
    range, while depth is expressed relative to the normalized
    cranial depth range (-1 back, +1 front).

    This component is deliberately separate from FacialLandmarks:
    the two sets live in different normalizations (face bounding box
    vs head bounding box) and describe different anatomical regions.
    """

    component_type = "cranial_landmarks"

    VALID_LANDMARKS = (
        "vertex",
        "left_euryon",
        "right_euryon",
        "opisthocranion",
        "left_porion",
        "right_porion",
        "left_orbitale",
        "right_orbitale",
        "glabella",
        "nasion",
    )

    def __init__(
        self,
        *,
        points: dict[str, tuple[float, float, float]] | None = None,
    ) -> None:
        super().__init__()

        self.points = dict(points or {})
        self.validate()

    def validate(self) -> None:
        super().validate()

        for name, point in self.points.items():
            if name not in self.VALID_LANDMARKS:
                raise ValueError(
                    f"Unknown cranial landmark: {name!r}."
                )

            if not isinstance(point, (tuple, list)) or len(point) != 3:
                raise ValueError(
                    f"Cranial landmark {name!r} must contain "
                    "exactly three coordinates."
                )

            x, y, z = (float(value) for value in point)

            if not 0.0 <= x <= 1.0:
                raise ValueError(
                    f"Cranial landmark {name!r} x coordinate "
                    "must be between 0 and 1."
                )

            if not 0.0 <= y <= 1.0:
                raise ValueError(
                    f"Cranial landmark {name!r} y coordinate "
                    "must be between 0 and 1."
                )

            if not -1.0 <= z <= 1.0:
                raise ValueError(
                    f"Cranial landmark {name!r} z coordinate "
                    "must be between -1 and 1."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "points": {
                name: list(point)
                for name, point in self.points.items()
            },
        }