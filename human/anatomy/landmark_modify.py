"""Bottom-up landmark modification operators (H4.14-D).

While H4.14-B/C modify the dimensional model directly (top-down),
this module propagates modifications from the landmark level
(bottom-up): moving an anatomical point re-executes the whole
H4.13 derivation chain — measurements, dimensions, proportions —
and the reports certify what changed and what survived at every
level.

- modify_facial_landmarks applies explicit (dx, dy, dz) moves to
  FacialLandmarks and cascades through the facial derivation
  chain. The physical scale is anchored to the ORIGINAL facial
  height, so landmark moves translate into physical dimension
  changes;
- modify_cranial_landmarks does the same for CranialLandmarks
  through the cranial chain, keeping the facial trio of the head
  model untouched (cross invariance, mirroring H4.14-C);
- semantic wrappers (widen_zygions, lower_gnathion,
  advance_pronasale, widen_euryons) declare their propagation;
- the equivalence tests prove that the top-down and bottom-up
  paths produce the same model: moving the zygions in landmark
  space and widening the bizygomatic width in dimension space
  agree exactly.
"""

from __future__ import annotations

import math
from typing import Any

from .anatomy_component import AnatomyComponent
from .cranial_landmarks import CranialLandmarks
from .face_dimensions import FaceDimensions
from .facial_landmarks import FacialLandmarks
from .facial_morphometry import (
    FacialMeasurements,
    face_dimensions_from_measurements,
    facial_measurements,
    facial_proportions_from_dimensions,
    facial_scale_factor,
)
from .facial_modify import (
    FACIAL_DIMENSION_PROPERTIES,
    FACIAL_PROPORTION_PROPERTIES,
)
from .facial_proportions import FacialProportions
from .head_dimensions import HeadDimensions
from .head_modify import (
    HEAD_DIMENSION_PROPERTIES,
    HEAD_PROPORTION_PROPERTIES,
)
from .head_morphometry import (
    CranialMeasurements,
    cranial_measurements,
    cranial_scale_factor,
    head_dimensions_from_cranial_measurements,
    head_proportions_from_dimensions,
)
from .head_proportions import HeadProportions
from .modify import ModifyResult, PropertyChange, diff_properties


def _require_delta_triple(
    delta: object,
    context: str,
) -> tuple[float, float, float]:
    """Validate a (dx, dy, dz) delta triple."""

    if not isinstance(delta, (tuple, list)) or len(delta) != 3:
        raise ValueError(
            f"{context} deltas must contain exactly three "
            "coordinates."
        )

    values = []

    for component in delta:
        if (
            isinstance(component, bool)
            or not isinstance(component, (int, float))
            or not math.isfinite(float(component))
        ):
            raise ValueError(
                f"{context} delta coordinates must be finite "
                "numbers."
            )

        values.append(float(component))

    return (values[0], values[1], values[2])


def _apply_moves(
    points: dict,
    moves: dict,
    context: str,
) -> dict:
    """Validate the moves mapping and return the new point set."""

    if not isinstance(moves, dict) or not moves:
        raise ValueError(
            f"{context} moves must be a non-empty dict mapping "
            "landmark names to (dx, dy, dz) deltas."
        )

    new_points = dict(points)

    for name, delta in moves.items():
        if name not in points:
            raise ValueError(
                f"{context} landmark {name!r} is not present."
            )

        dx, dy, dz = _require_delta_triple(delta, context)

        x, y, z = points[name]
        new_points[name] = (x + dx, y + dy, z + dz)

    return new_points


def _landmark_report(
    points_before: dict,
    points_after: dict,
    operation: str,
) -> ModifyResult:
    """Build the landmark-level report from the two point sets.

    Points whose coordinates changed become PropertyChange entries
    (before/after tuples); unmoved points become preserved names.
    """

    changes: list[PropertyChange] = []
    preserved: list[str] = []

    for name, before_point in points_before.items():
        after_point = points_after[name]

        if before_point != after_point:
            changes.append(
                PropertyChange(
                    name=name,
                    before=before_point,
                    after=after_point,
                )
            )
        else:
            preserved.append(name)

    return ModifyResult(
        operation=operation,
        changes=changes,
        preserved=preserved,
    )


class LandmarkModification(AnatomyComponent):
    """Composite outcome of a bottom-up facial landmark
    modification.

    Bundles the modified FacialLandmarks, the rederived
    measurements, dimensions and proportions, plus the three
    ModifyResult reports (landmarks, dimensions, proportions).
    """

    component_type = "landmark_modification"

    def __init__(
        self,
        *,
        landmarks: FacialLandmarks,
        measurements: FacialMeasurements,
        dimensions: FaceDimensions,
        proportions: FacialProportions,
        landmark_report: ModifyResult,
        dimension_report: ModifyResult,
        proportion_report: ModifyResult,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.landmarks = landmarks
        self.measurements = measurements
        self.dimensions = dimensions
        self.proportions = proportions
        self.landmark_report = landmark_report
        self.dimension_report = dimension_report
        self.proportion_report = proportion_report

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.landmarks, FacialLandmarks):
            raise ValueError(
                "LandmarkModification landmarks must be "
                "FacialLandmarks."
            )

        if not isinstance(self.measurements, FacialMeasurements):
            raise ValueError(
                "LandmarkModification measurements must be "
                "FacialMeasurements."
            )

        if not isinstance(self.dimensions, FaceDimensions):
            raise ValueError(
                "LandmarkModification dimensions must be "
                "FaceDimensions."
            )

        if not isinstance(self.proportions, FacialProportions):
            raise ValueError(
                "LandmarkModification proportions must be "
                "FacialProportions."
            )

        for name, report in (
            ("landmark_report", self.landmark_report),
            ("dimension_report", self.dimension_report),
            ("proportion_report", self.proportion_report),
        ):
            if not isinstance(report, ModifyResult):
                raise ValueError(
                    f"LandmarkModification {name} must be a "
                    "ModifyResult."
                )

        self.landmarks.validate()
        self.measurements.validate()
        self.dimensions.validate()
        self.proportions.validate()

        for report in (
            self.landmark_report,
            self.dimension_report,
            self.proportion_report,
        ):
            report.validate()

        point_names = set(self.landmarks.points)

        for name in (
            self.landmark_report.changed_names()
            + self.landmark_report.preserved_names()
        ):
            if name not in point_names:
                raise ValueError(
                    "LandmarkModification landmark_report contains "
                    f"unknown landmark {name!r}."
                )

        for name in (
            self.dimension_report.changed_names()
            + self.dimension_report.preserved_names()
        ):
            if name not in FACIAL_DIMENSION_PROPERTIES:
                raise ValueError(
                    "LandmarkModification dimension_report contains "
                    f"unknown property {name!r}."
                )

        for name in (
            self.proportion_report.changed_names()
            + self.proportion_report.preserved_names()
        ):
            if name not in FACIAL_PROPORTION_PROPERTIES:
                raise ValueError(
                    "LandmarkModification proportion_report "
                    f"contains unknown property {name!r}."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "landmarks": self.landmarks.to_dict(),
            "measurements": self.measurements.to_dict(),
            "dimensions": self.dimensions.to_dict(),
            "proportions": self.proportions.to_dict(),
            "landmark_report": self.landmark_report.to_dict(),
            "dimension_report": self.dimension_report.to_dict(),
            "proportion_report": self.proportion_report.to_dict(),
        }


class CranialLandmarkModification(AnatomyComponent):
    """Composite outcome of a bottom-up cranial landmark
    modification.

    Bundles the modified CranialLandmarks, the rederived
    measurements, head dimensions and proportions, plus the three
    ModifyResult reports.
    """

    component_type = "cranial_landmark_modification"

    def __init__(
        self,
        *,
        landmarks: CranialLandmarks,
        measurements: CranialMeasurements,
        dimensions: HeadDimensions,
        proportions: HeadProportions,
        landmark_report: ModifyResult,
        dimension_report: ModifyResult,
        proportion_report: ModifyResult,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.landmarks = landmarks
        self.measurements = measurements
        self.dimensions = dimensions
        self.proportions = proportions
        self.landmark_report = landmark_report
        self.dimension_report = dimension_report
        self.proportion_report = proportion_report

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.landmarks, CranialLandmarks):
            raise ValueError(
                "CranialLandmarkModification landmarks must be "
                "CranialLandmarks."
            )

        if not isinstance(self.measurements, CranialMeasurements):
            raise ValueError(
                "CranialLandmarkModification measurements must be "
                "CranialMeasurements."
            )

        if not isinstance(self.dimensions, HeadDimensions):
            raise ValueError(
                "CranialLandmarkModification dimensions must be "
                "HeadDimensions."
            )

        if not isinstance(self.proportions, HeadProportions):
            raise ValueError(
                "CranialLandmarkModification proportions must be "
                "HeadProportions."
            )

        for name, report in (
            ("landmark_report", self.landmark_report),
            ("dimension_report", self.dimension_report),
            ("proportion_report", self.proportion_report),
        ):
            if not isinstance(report, ModifyResult):
                raise ValueError(
                    f"CranialLandmarkModification {name} must be "
                    "a ModifyResult."
                )

        self.landmarks.validate()
        self.measurements.validate()
        self.dimensions.validate()
        self.proportions.validate()

        for report in (
            self.landmark_report,
            self.dimension_report,
            self.proportion_report,
        ):
            report.validate()

        point_names = set(self.landmarks.points)

        for name in (
            self.landmark_report.changed_names()
            + self.landmark_report.preserved_names()
        ):
            if name not in point_names:
                raise ValueError(
                    "CranialLandmarkModification landmark_report "
                    f"contains unknown landmark {name!r}."
                )

        for name in (
            self.dimension_report.changed_names()
            + self.dimension_report.preserved_names()
        ):
            if name not in HEAD_DIMENSION_PROPERTIES:
                raise ValueError(
                    "CranialLandmarkModification dimension_report "
                    f"contains unknown property {name!r}."
                )

        for name in (
            self.proportion_report.changed_names()
            + self.proportion_report.preserved_names()
        ):
            if name not in HEAD_PROPORTION_PROPERTIES:
                raise ValueError(
                    "CranialLandmarkModification proportion_report "
                    f"contains unknown property {name!r}."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "landmarks": self.landmarks.to_dict(),
            "measurements": self.measurements.to_dict(),
            "dimensions": self.dimensions.to_dict(),
            "proportions": self.proportions.to_dict(),
            "landmark_report": self.landmark_report.to_dict(),
            "dimension_report": self.dimension_report.to_dict(),
            "proportion_report": self.proportion_report.to_dict(),
        }


def modify_facial_landmarks(
    landmarks: FacialLandmarks,
    moves: dict[str, tuple[float, float, float]],
    *,
    target_facial_height: float = 18.0,
    forehead_width: float = 12.0,
    chin_width: float = 5.0,
    operation: str,
) -> LandmarkModification:
    """Apply (dx, dy, dz) moves to facial landmarks and cascade.

    The physical scale is computed from the ORIGINAL measurements
    (target facial height / original facial height) and reused for
    the modified chain: landmark moves translate into physical
    dimension changes while the normalization anchor stays fixed.
    """

    if not isinstance(landmarks, FacialLandmarks):
        raise ValueError(
            "modify_facial_landmarks requires a FacialLandmarks "
            "instance."
        )

    landmarks.validate()

    new_points = _apply_moves(
        landmarks.points,
        moves,
        "modify_facial_landmarks",
    )
    new_landmarks = FacialLandmarks(points=new_points)

    before_measurements = facial_measurements(landmarks)
    after_measurements = facial_measurements(new_landmarks)

    scale = facial_scale_factor(
        before_measurements,
        target_facial_height,
    )

    before_dimensions = face_dimensions_from_measurements(
        before_measurements,
        scale,
        forehead_width=forehead_width,
        chin_width=chin_width,
    )
    after_dimensions = face_dimensions_from_measurements(
        after_measurements,
        scale,
        forehead_width=forehead_width,
        chin_width=chin_width,
    )

    before_proportions = facial_proportions_from_dimensions(
        before_dimensions
    )
    after_proportions = facial_proportions_from_dimensions(
        after_dimensions
    )

    return LandmarkModification(
        landmarks=new_landmarks,
        measurements=after_measurements,
        dimensions=after_dimensions,
        proportions=after_proportions,
        landmark_report=_landmark_report(
            landmarks.points,
            new_points,
            operation,
        ),
        dimension_report=diff_properties(
            before_dimensions,
            after_dimensions,
            list(FACIAL_DIMENSION_PROPERTIES),
            operation=operation,
        ),
        proportion_report=diff_properties(
            before_proportions,
            after_proportions,
            list(FACIAL_PROPORTION_PROPERTIES),
            operation=operation,
        ),
    )


def modify_cranial_landmarks(
    landmarks: CranialLandmarks,
    moves: dict[str, tuple[float, float, float]],
    *,
    face_dimensions: FaceDimensions | None = None,
    target_cranial_length: float = 19.0,
    cranial_height: float | None = None,
    operation: str,
) -> CranialLandmarkModification:
    """Apply (dx, dy, dz) moves to cranial landmarks and cascade.

    The facial trio of the head model comes from the given
    FaceDimensions (default reference when omitted) and is never
    touched by cranial moves: the cross invariance of H4.14-C,
    mirrored bottom-up. The physical scale is anchored to the
    ORIGINAL cranial length.
    """

    if not isinstance(landmarks, CranialLandmarks):
        raise ValueError(
            "modify_cranial_landmarks requires a CranialLandmarks "
            "instance."
        )

    landmarks.validate()

    face = (
        face_dimensions
        if face_dimensions is not None
        else FaceDimensions()
    )

    new_points = _apply_moves(
        landmarks.points,
        moves,
        "modify_cranial_landmarks",
    )
    new_landmarks = CranialLandmarks(points=new_points)

    before_measurements = cranial_measurements(landmarks)
    after_measurements = cranial_measurements(new_landmarks)

    scale = cranial_scale_factor(
        before_measurements,
        target_cranial_length,
    )

    before_dimensions = head_dimensions_from_cranial_measurements(
        face,
        before_measurements,
        scale,
        cranial_height=cranial_height,
    )
    after_dimensions = head_dimensions_from_cranial_measurements(
        face,
        after_measurements,
        scale,
        cranial_height=cranial_height,
    )

    before_proportions = head_proportions_from_dimensions(
        before_dimensions
    )
    after_proportions = head_proportions_from_dimensions(
        after_dimensions
    )

    return CranialLandmarkModification(
        landmarks=new_landmarks,
        measurements=after_measurements,
        dimensions=after_dimensions,
        proportions=after_proportions,
        landmark_report=_landmark_report(
            landmarks.points,
            new_points,
            operation,
        ),
        dimension_report=diff_properties(
            before_dimensions,
            after_dimensions,
            list(HEAD_DIMENSION_PROPERTIES),
            operation=operation,
        ),
        proportion_report=diff_properties(
            before_proportions,
            after_proportions,
            list(HEAD_PROPORTION_PROPERTIES),
            operation=operation,
        ),
    )


def _positive_finite(delta: object, operation: str) -> float:
    """Validate a strictly positive finite delta."""

    if (
        isinstance(delta, bool)
        or not isinstance(delta, (int, float))
        or not math.isfinite(float(delta))
        or delta <= 0
    ):
        raise ValueError(
            f"{operation} delta must be a positive finite number."
        )

    return float(delta)


def widen_zygions(
    landmarks: FacialLandmarks,
    delta: float,
) -> LandmarkModification:
    """Move both zygions outward, widening the bizygomatic width."""

    amount = _positive_finite(delta, "widen_zygions")

    return modify_facial_landmarks(
        landmarks,
        {
            "left_zygion": (-amount, 0.0, 0.0),
            "right_zygion": (amount, 0.0, 0.0),
        },
        operation=f"widen_zygions {amount:+}",
    )


def lower_gnathion(
    landmarks: FacialLandmarks,
    delta: float,
) -> LandmarkModification:
    """Move the gnathion down (y grows downward), lengthening the
    lower face and the chin height."""

    amount = _positive_finite(delta, "lower_gnathion")

    return modify_facial_landmarks(
        landmarks,
        {"gnathion": (0.0, amount, 0.0)},
        operation=f"lower_gnathion {amount:+}",
    )


def advance_pronasale(
    landmarks: FacialLandmarks,
    delta: float,
) -> LandmarkModification:
    """Move the pronasale forward (z), increasing the facial
    depth."""

    amount = _positive_finite(delta, "advance_pronasale")

    return modify_facial_landmarks(
        landmarks,
        {"pronasale": (0.0, 0.0, amount)},
        operation=f"advance_pronasale {amount:+}",
    )


def widen_euryons(
    landmarks: CranialLandmarks,
    delta: float,
) -> CranialLandmarkModification:
    """Move both euryons outward, widening the cranium."""

    amount = _positive_finite(delta, "widen_euryons")

    return modify_cranial_landmarks(
        landmarks,
        {
            "left_euryon": (-amount, 0.0, 0.0),
            "right_euryon": (amount, 0.0, 0.0),
        },
        operation=f"widen_euryons {amount:+}",
    )