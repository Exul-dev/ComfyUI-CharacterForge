"""Parametric cranial modification operators (H4.14-C).

The cranial counterpart of the facial operators, with the cross
invariance at its core: cranial operations NEVER touch the facial
properties of the head model, and the ModifyResult reports certify
it — modifying the skull leaves the face exactly as it was.

- modify_head_dimensions applies explicit deltas to HeadDimensions,
  auto-validates, rederives the HeadProportions (H4.13-B chain) and
  produces the two diff reports;
- widen_cranial propagates to cranial_breadth (which follows the
  width by the H4.13-B/C convention) and RECALCULATES the cranial
  circumference with the Ramanujan perimeter (H4.13-C), so the
  declared circumference stays coherent with the modified width;
- lengthen_cranial propagates to cranial_length (which follows the
  depth) and recalculates the circumference accordingly;
- adjust_neurocranial_height touches only the vault height.
"""

from __future__ import annotations

import math
from typing import Any

from .anatomy_component import AnatomyComponent
from .head_dimensions import HeadDimensions
from .head_morphometry import (
    head_proportions_from_dimensions,
    ramanujan_perimeter,
)
from .head_proportions import HeadProportions
from .modify import ModifyResult, diff_properties

HEAD_DIMENSION_PROPERTIES: tuple[str, ...] = (
    "cranial_height",
    "cranial_width",
    "cranial_depth",
    "cranial_length",
    "cranial_breadth",
    "cranial_circumference",
    "neurocranial_height",
    "facial_height",
    "bizygomatic_width",
    "bigonial_width",
)

HEAD_PROPORTION_PROPERTIES: tuple[str, ...] = (
    "cephalic_index",
    "cranial_height_to_width",
    "cranial_depth_to_width",
    "face_to_head_height",
    "face_to_head_width",
    "neurocranium_to_face_height",
    "bizygomatic_to_bigonial",
)


class HeadModification(AnatomyComponent):
    """Composite outcome of a parametric cranial modification.

    Bundles the modified HeadDimensions, the rederived
    HeadProportions and the two ModifyResult reports that certify
    what changed and what survived — including the facial
    invariance when the operation is cranial.
    """

    component_type = "head_modification"

    def __init__(
        self,
        *,
        dimensions: HeadDimensions,
        proportions: HeadProportions,
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

        if not isinstance(self.dimensions, HeadDimensions):
            raise ValueError(
                "HeadModification dimensions must be HeadDimensions."
            )

        if not isinstance(self.proportions, HeadProportions):
            raise ValueError(
                "HeadModification proportions must be "
                "HeadProportions."
            )

        for name, report in (
            ("dimension_report", self.dimension_report),
            ("proportion_report", self.proportion_report),
        ):
            if not isinstance(report, ModifyResult):
                raise ValueError(
                    f"HeadModification {name} must be a "
                    "ModifyResult."
                )

        self.dimensions.validate()
        self.proportions.validate()
        self.dimension_report.validate()
        self.proportion_report.validate()

        allowed_dimensions = set(HEAD_DIMENSION_PROPERTIES)
        for name in (
            self.dimension_report.changed_names()
            + self.dimension_report.preserved_names()
        ):
            if name not in allowed_dimensions:
                raise ValueError(
                    "HeadModification dimension_report contains "
                    f"unknown property {name!r}."
                )

        allowed_proportions = set(HEAD_PROPORTION_PROPERTIES)
        for name in (
            self.proportion_report.changed_names()
            + self.proportion_report.preserved_names()
        ):
            if name not in allowed_proportions:
                raise ValueError(
                    "HeadModification proportion_report contains "
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
    dimensions: HeadDimensions,
    deltas: dict[str, float],
) -> dict[str, float]:
    """Validate the deltas mapping and resolve the new values."""

    if not isinstance(deltas, dict) or not deltas:
        raise ValueError(
            "modify_head_dimensions deltas must be a non-empty "
            "dict of property name to numeric delta."
        )

    resolved: dict[str, float] = {}

    for name, delta in deltas.items():
        if name not in HEAD_DIMENSION_PROPERTIES:
            raise ValueError(
                f"Unknown head dimension property: {name!r}."
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


def modify_head_dimensions(
    dimensions: HeadDimensions,
    deltas: dict[str, float],
    *,
    operation: str,
) -> HeadModification:
    """Apply explicit deltas to a HeadDimensions model.

    The new model is auto-validated, the HeadProportions are
    rederived through the H4.13-B chain, and the two ModifyResult
    reports certify what changed and what survived.
    """

    if not isinstance(dimensions, HeadDimensions):
        raise ValueError(
            "modify_head_dimensions requires a HeadDimensions "
            "instance."
        )

    dimensions.validate()

    resolved = _validated_deltas(dimensions, deltas)

    new_values = {
        name: getattr(dimensions, name)
        for name in HEAD_DIMENSION_PROPERTIES
    }
    new_values.update(resolved)

    new_dimensions = HeadDimensions(**new_values)

    old_proportions = head_proportions_from_dimensions(dimensions)
    new_proportions = head_proportions_from_dimensions(
        new_dimensions
    )

    dimension_report = diff_properties(
        dimensions,
        new_dimensions,
        list(HEAD_DIMENSION_PROPERTIES),
        operation=operation,
    )
    proportion_report = diff_properties(
        old_proportions,
        new_proportions,
        list(HEAD_PROPORTION_PROPERTIES),
        operation=operation,
    )

    return HeadModification(
        dimensions=new_dimensions,
        proportions=new_proportions,
        dimension_report=dimension_report,
        proportion_report=proportion_report,
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


def widen_cranial(
    dimensions: HeadDimensions,
    delta: float,
) -> HeadModification:
    """Widen the cranium, propagating to breadth and circumference.

    cranial_breadth follows cranial_width (H4.13-B/C convention)
    and the cranial circumference is recalculated with the
    Ramanujan perimeter so it stays coherent with the new width.
    Facial properties are never touched.
    """

    amount = _positive_finite(delta, "widen_cranial")

    new_width = dimensions.cranial_width + amount
    new_circumference = ramanujan_perimeter(
        new_width / 2.0,
        dimensions.cranial_length / 2.0,
    )

    return modify_head_dimensions(
        dimensions,
        {
            "cranial_width": amount,
            "cranial_breadth": amount,
            "cranial_circumference": (
                new_circumference - dimensions.cranial_circumference
            ),
        },
        operation=f"widen_cranial {amount:+}",
    )


def lengthen_cranial(
    dimensions: HeadDimensions,
    delta: float,
) -> HeadModification:
    """Lengthen the cranium, propagating to length and circumference.

    cranial_length follows cranial_depth (H4.13-B/C convention) and
    the circumference is recalculated accordingly. Facial
    properties are never touched.
    """

    amount = _positive_finite(delta, "lengthen_cranial")

    new_length = dimensions.cranial_depth + amount
    new_circumference = ramanujan_perimeter(
        dimensions.cranial_width / 2.0,
        new_length / 2.0,
    )

    return modify_head_dimensions(
        dimensions,
        {
            "cranial_depth": amount,
            "cranial_length": amount,
            "cranial_circumference": (
                new_circumference - dimensions.cranial_circumference
            ),
        },
        operation=f"lengthen_cranial {amount:+}",
    )


def adjust_neurocranial_height(
    dimensions: HeadDimensions,
    delta: float,
) -> HeadModification:
    """Adjust the vault height without touching anything else."""

    if (
        isinstance(delta, bool)
        or not isinstance(delta, (int, float))
        or not math.isfinite(float(delta))
        or delta == 0
    ):
        raise ValueError(
            "adjust_neurocranial_height delta must be a non-zero "
            "finite number."
        )

    return modify_head_dimensions(
        dimensions,
        {"neurocranial_height": float(delta)},
        operation=f"adjust_neurocranial_height {float(delta):+}",
    )