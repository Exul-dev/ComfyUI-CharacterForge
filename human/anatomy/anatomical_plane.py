from __future__ import annotations

from enum import Enum
from typing import Any

from .anatomy_component import AnatomyComponent


class AnatomicalPlaneType(Enum):
    """Semantic type of an anatomical plane."""

    MID_SAGITTAL = "mid_sagittal"
    CORONAL = "coronal"
    AXIAL = "axial"
    FRANKFURT = "frankfurt"
    LANDMARK_DEFINED = "landmark_defined"


# Plane types that require exactly three defining landmarks.
_LANDMARK_DEFINED_TYPES = frozenset(
    {
        AnatomicalPlaneType.FRANKFURT,
        AnatomicalPlaneType.LANDMARK_DEFINED,
    }
)

# Number of landmarks required to geometrically define a plane.
_DEFINING_LANDMARKS = 3


class AnatomicalPlane(AnatomyComponent):
    """Semantic anatomical plane.

    Standard orientation planes (mid-sagittal, coronal, axial) are
    defined by the anatomical coordinate system itself and carry no
    defining landmarks. Reference planes (Frankfurt) and custom planes
    are defined by exactly three distinct landmark names, mirroring
    the landmark identifiers used by LandmarkRelation.
    """

    component_type = "anatomical_plane"

    def __init__(
        self,
        plane_type: AnatomicalPlaneType,
        landmark_names: list[str] | None = None,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.plane_type = plane_type

        if landmark_names is None:
            self.landmark_names = None
        else:
            # Copied only when already a list; anything else is kept
            # as-is so that validate() can reject it explicitly.
            self.landmark_names = (
                list(landmark_names)
                if isinstance(landmark_names, list)
                else landmark_names
            )

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.plane_type, AnatomicalPlaneType):
            raise ValueError(
                "AnatomicalPlane plane_type must be an "
                "AnatomicalPlaneType."
            )

        if self.landmark_names is not None:
            if not isinstance(self.landmark_names, list):
                raise ValueError(
                    "AnatomicalPlane landmark_names must be a list "
                    "of strings or None."
                )

            for name in self.landmark_names:
                if not isinstance(name, str) or not name.strip():
                    raise ValueError(
                        "AnatomicalPlane landmark names must be "
                        "non-empty strings."
                    )

            normalized = [name.strip() for name in self.landmark_names]

            if len(set(normalized)) != len(normalized):
                raise ValueError(
                    "AnatomicalPlane defining landmarks must be "
                    "distinct."
                )

        if self.plane_type in _LANDMARK_DEFINED_TYPES:
            if (
                self.landmark_names is None
                or len(self.landmark_names) != _DEFINING_LANDMARKS
            ):
                raise ValueError(
                    f"AnatomicalPlane of type "
                    f"{self.plane_type.value} requires exactly "
                    f"{_DEFINING_LANDMARKS} defining landmark names."
                )
        elif self.landmark_names:
            raise ValueError(
                "Standard anatomical planes are defined by the "
                "coordinate system and must not carry defining "
                "landmarks."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "plane_type": self.plane_type.value,
            "landmark_names": (
                list(self.landmark_names)
                if self.landmark_names is not None
                else None
            ),
        }