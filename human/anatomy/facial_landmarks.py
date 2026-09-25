from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class FacialLandmarks(AnatomyComponent):
    """Canonical anatomical facial landmark coordinates.

    Coordinates are normalized to the face bounding box:
    x and y are in the 0..1 range, while depth is expressed
    relative to the normalized facial depth.
    """

    component_type = "facial_landmarks"

    VALID_LANDMARKS = (
        "trichion",
        "glabella",
        "nasion",
        "pronasale",
        "subnasale",
        "labiale_superius",
        "stomion",
        "labiale_inferius",
        "gnathion",
        "left_zygion",
        "right_zygion",
        "left_gonion",
        "right_gonion",
        "left_endocanthion",
        "right_endocanthion",
        "left_exocanthion",
        "right_exocanthion",
        "left_cheilion",
        "right_cheilion",
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
                    f"Unknown facial landmark: {name!r}."
                )

            if not isinstance(point, (tuple, list)) or len(point) != 3:
                raise ValueError(
                    f"Facial landmark {name!r} must contain "
                    "exactly three coordinates."
                )

            x, y, z = (float(value) for value in point)

            if not 0.0 <= x <= 1.0:
                raise ValueError(
                    f"Facial landmark {name!r} x coordinate "
                    "must be between 0 and 1."
                )

            if not 0.0 <= y <= 1.0:
                raise ValueError(
                    f"Facial landmark {name!r} y coordinate "
                    "must be between 0 and 1."
                )

            if not -1.0 <= z <= 1.0:
                raise ValueError(
                    f"Facial landmark {name!r} z coordinate "
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
