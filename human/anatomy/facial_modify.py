"""Parametric facial modification operators (H4.14-B).

This module turns the H4.14-A modification contract into concrete
facial operators:

- modify_face_dimensions applies explicit deltas to a FaceDimensions
  model, auto-validates the result, rebuilds the derived
  FacialProportions (H4.13-A chain) and produces the two diff
  reports (dimensions and derived proportions);
- semantic wrappers declare their controlled propagation: by the
  H4.13-A convention facial_width follows bizygomatic_width and
  jaw_width follows bigonial_width, so widening operations
  propagate to both properties and the reports declare it.

The core promise, proven by the reports: modifying one region
changes exactly what it must change, and everything else is
certified as preserved.
"""

from __future__ import annotations

import math
from typing import Any

from .anatomy_component import AnatomyComponent
from .face_dimensions import FaceDimensions
from .facial_proportions import FacialProportions
from .facial_morphometry import facial_proportions_from_dimensions
from .modify import ModifyResult, diff_properties

FACIAL_DIMENSION_PROPERTIES: tuple[str, ...] = (
    "facial_height",
    "facial_width",
    "facial_depth",
    "upper_face_height",
    "mid_face_height",
    "lower_face_height",
    "forehead_width",
    "bizygomatic_width",
    "bigonial_width",
    "jaw_width",
    "chin_width",
    "chin_height",
)

FACIAL_PROPORTION_PROPERTIES: tuple[str, ...] = (
    "upper_to_mid_ratio",
    "mid_to_lower_ratio",
    "width_to_height_ratio",
    "forehead_to_cheek_ratio",
    "cheek_to_jaw_ratio",
    "jaw_to_chin_ratio",
)


class FacialModification(AnatomyComponent):
    """Composite outcome of a parametric facial modification.

    Bundles the modified FaceDimensions, the rederived
    FacialProportions and the two ModifyResult reports (dimensions
    and derived proportions) that certify what changed and what
    survived.
    """

    component_type = "facial_modification"

    def __init__(
        self,
        *,
        dimensions: FaceDimensions,
        proportions: FacialProportions,
        dimension_report: ModifyResult,
        proportion_report: ModifyResult,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.dimensions = dimensions
        self.proportions = proportions
        self.dimension_report = dimension_report
        self.proportion_report = proportion_report

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.dimensions, FaceDimensions):
            raise ValueError(
                "FacialModification dimensions must be "
                "FaceDimensions."
            )

        if not isinstance(self.proportions, FacialProportions):
            raise ValueError(
                "FacialModification proportions must be "
                "FacialProportions."
            )

        for name, report in (
            ("dimension_report", self.dimension_report),
            ("proportion_report", self.proportion_report),
        ):
            if not isinstance(report, ModifyResult):
                raise ValueError(
                    f"FacialModification {name} must be a "
                    "ModifyResult."
                )

        self.dimensions.validate()
        self.proportions.validate()
        self.dimension_report.validate()
        self.proportion_report.validate()

        allowed_dimensions = set(FACIAL_DIMENSION_PROPERTIES)
        for name in (
            self.dimension_report.changed_names()
            + self.dimension_report.preserved_names()
        ):
            if name not in allowed_dimensions:
                raise ValueError(
                    "FacialModification dimension_report contains "
                    f"unknown property {name!r}."
                )

        allowed_proportions = set(FACIAL_PROPORTION_PROPERTIES)
        for name in (
            self.proportion_report.changed_names()
            + self.proportion_report.preserved_names()
        ):
            if name not in allowed_proportions:
                raise ValueError(
                    "FacialModification proportion_report contains "
                    f"unknown property {name!r}."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "dimensions": self.dimensions.to_dict(),
            "proportions": self.proportions.to_dict(),
            "dimension_report": self.dimension_report.to_dict(),
            "proportion_report": self.proportion_report.to_dict(),
        }


def _validated_deltas(
    dimensions: FaceDimensions,
    deltas: dict[str, float],
) -> dict[str, float]:
    """Validate the deltas mapping and resolve the new values."""

    if not isinstance(deltas, dict) or not deltas:
        raise ValueError(
            "modify_face_dimensions deltas must be a non-empty "
            "dict of property name to numeric delta."
        )

    resolved: dict[str, float] = {}

    for name, delta in deltas.items():
        if name not in FACIAL_DIMENSION_PROPERTIES:
            raise ValueError(
                f"Unknown facial dimension property: {name!r}."
            )

        if (
            isinstance(delta, bool)
            or not isinstance(delta, (int, float))
            or not math.isfinite(float(delta))
        ):
            raise ValueError(
                f"Delta for {name!r} must be a finite number."
            )

        resolved[name] = getattr(dimensions, name) + float(delta)

    return resolved


def modify_face_dimensions(
    dimensions: FaceDimensions,
    deltas: dict[str, float],
    *,
    operation: str,
) -> FacialModification:
    """Apply explicit deltas to a FaceDimensions model.

    The new model is auto-validated (positive values enforced by
    FaceDimensions itself), the FacialProportions are rederived
    through the H4.13-A chain, and two ModifyResult reports certify
    exactly what changed and what survived — on the dimensions and
    on the derived proportions.
    """

    if not isinstance(dimensions, FaceDimensions):
        raise ValueError(
            "modify_face_dimensions requires a FaceDimensions "
            "instance."
        )

    dimensions.validate()

    resolved = _validated_deltas(dimensions, deltas)

    new_values = {
        name: getattr(dimensions, name)
        for name in FACIAL_DIMENSION_PROPERTIES
    }
    new_values.update(resolved)

    new_dimensions = FaceDimensions(**new_values)

    old_proportions = facial_proportions_from_dimensions(dimensions)
    new_proportions = facial_proportions_from_dimensions(
        new_dimensions
    )

    dimension_report = diff_properties(
        dimensions,
        new_dimensions,
        list(FACIAL_DIMENSION_PROPERTIES),
        operation=operation,
    )
    proportion_report = diff_properties(
        old_proportions,
        new_proportions,
        list(FACIAL_PROPORTION_PROPERTIES),
        operation=operation,
    )

    return FacialModification(
        dimensions=new_dimensions,
        proportions=new_proportions,
        dimension_report=dimension_report,
        proportion_report=proportion_report,
    )


def widen_bizygomatic(
    dimensions: FaceDimensions,
    delta: float,
) -> FacialModification:
    """Widen the bizygomatic width, propagating to facial_width.

    By the H4.13-A derivation convention facial_width follows the
    bizygomatic width: the propagation is part of the operation and
    is declared in the reports.
    """

    if (
        isinstance(delta, bool)
        or not isinstance(delta, (int, float))
        or not math.isfinite(float(delta))
        or delta <= 0
    ):
        raise ValueError(
            "widen_bizygomatic delta must be a positive finite "
            "number."
        )

    return modify_face_dimensions(
        dimensions,
        {
            "bizygomatic_width": delta,
            "facial_width": delta,
        },
        operation=f"widen_bizygomatic {float(delta):+}",
    )


def widen_jaw(
    dimensions: FaceDimensions,
    delta: float,
) -> FacialModification:
    """Widen the bigonial width, propagating to jaw_width.

    By the H4.13-A derivation convention jaw_width follows the
    bigonial width: the propagation is declared in the reports.
    """

    if (
        isinstance(delta, bool)
        or not isinstance(delta, (int, float))
        or not math.isfinite(float(delta))
        or delta <= 0
    ):
        raise ValueError(
            "widen_jaw delta must be a positive finite number."
        )

    return modify_face_dimensions(
        dimensions,
        {
            "bigonial_width": delta,
            "jaw_width": delta,
        },
        operation=f"widen_jaw {float(delta):+}",
    )


def adjust_facial_height(
    dimensions: FaceDimensions,
    delta: float,
) -> FacialModification:
    """Adjust the facial height without touching anything else."""

    if (
        isinstance(delta, bool)
        or not isinstance(delta, (int, float))
        or not math.isfinite(float(delta))
        or delta == 0
    ):
        raise ValueError(
            "adjust_facial_height delta must be a non-zero "
            "finite number."
        )

    return modify_face_dimensions(
        dimensions,
        {"facial_height": delta},
        operation=f"adjust_facial_height {float(delta):+}",
    )