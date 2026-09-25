"""Parametric modification contract for the Human Engine.

This module introduces the modification layer of H4.14: the
contract that turns "change a value" into "change a value and
prove what changed and what survived".

- PropertyChange records one property transition (before -> after),
  with an explicit tolerance for floating point comparisons;
- ModifyResult is the semantic report of an operation: the list of
  changes and the list of preserved properties. The contract is
  hard: a declared change must really be a change, names are
  unique, and a property is either changed or preserved, never
  both;
- diff_properties compares two anatomy components over an explicit
  set of property names and builds the ModifyResult automatically.

The comparison is deliberately flat: first-level scalar properties.
Non-scalar values (nested components, dicts) are compared with ==
and should be diffed at their own level. Composed diffs are built
on top of this contract by the H4.14 operators.
"""

from __future__ import annotations

import math
from typing import Any

from .anatomy_component import AnatomyComponent

_MISSING = object()


def _value_changed(before: Any, after: Any, tolerance: float) -> bool:
    """Return True when before and after differ beyond tolerance."""

    if isinstance(before, bool) or isinstance(after, bool):
        return before != after

    if isinstance(before, (int, float)) and isinstance(
        after,
        (int, float),
    ):
        return not math.isclose(
            float(before),
            float(after),
            rel_tol=0.0,
            abs_tol=tolerance,
        )

    return before != after


def _require_tolerance(value: object, context: str) -> float:
    """Validate a tolerance and return it as float."""

    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(float(value))
        or value < 0
    ):
        raise ValueError(
            f"{context} tolerance must be a non-negative "
            "finite number."
        )

    return float(value)


class PropertyChange:
    """A single property transition produced by a modification."""

    def __init__(
        self,
        *,
        name: str,
        before: Any,
        after: Any,
        tolerance: float = 1e-9,
    ) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError(
                "PropertyChange name must be a non-empty string."
            )

        self.name = name
        self.before = before
        self.after = after
        self.tolerance = _require_tolerance(
            tolerance,
            "PropertyChange",
        )
        self.changed = _value_changed(
            before,
            after,
            self.tolerance,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "before": self.before,
            "after": self.after,
            "changed": self.changed,
        }


class ModifyResult(AnatomyComponent):
    """Semantic report of a parametric modification.

    A ModifyResult answers the core question of the parametric
    builder: WHAT changed and WHAT survived. Changes and preserved
    properties are mutually exclusive: a property is either in one
    list or in the other, never both, never duplicated.
    """

    component_type = "modify_result"

    def __init__(
        self,
        *,
        operation: str,
        changes: list[PropertyChange] | None = None,
        preserved: list[str] | None = None,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.operation = str(operation)
        self.changes = list(changes or [])
        self.preserved = list(preserved or [])

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not self.operation.strip():
            raise ValueError(
                "ModifyResult operation must be a non-empty string."
            )

        seen_changes: list[str] = []

        for change in self.changes:
            if not isinstance(change, PropertyChange):
                raise ValueError(
                    "ModifyResult changes must contain "
                    "PropertyChange instances."
                )

            if not change.changed:
                raise ValueError(
                    f"ModifyResult change {change.name!r} is declared "
                    "as changed but its values are equal."
                )

            if change.name in seen_changes:
                raise ValueError(
                    "ModifyResult contains duplicate change for "
                    f"{change.name!r}."
                )

            seen_changes.append(change.name)

        seen_preserved: list[str] = []

        for name in self.preserved:
            if not isinstance(name, str) or not name.strip():
                raise ValueError(
                    "ModifyResult preserved names must be "
                    "non-empty strings."
                )

            if name in seen_preserved:
                raise ValueError(
                    "ModifyResult contains duplicate preserved name "
                    f"{name!r}."
                )

            if name in seen_changes:
                raise ValueError(
                    f"ModifyResult property {name!r} is both changed "
                    "and preserved."
                )

            seen_preserved.append(name)

    def changed_names(self) -> list[str]:
        """Return the names of the changed properties, in order."""

        return [change.name for change in self.changes]

    def preserved_names(self) -> list[str]:
        """Return the names of the preserved properties, in order."""

        return list(self.preserved)

    def has_changed(self, name: str) -> bool:
        """Return True when the given property changed."""

        return name in self.changed_names()

    def change_of(self, name: str) -> PropertyChange | None:
        """Return the PropertyChange for a name, if present."""

        for change in self.changes:
            if change.name == name:
                return change

        return None

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "operation": self.operation,
            "changes": [
                change.to_dict() for change in self.changes
            ],
            "preserved": list(self.preserved),
        }


def diff_properties(
    before: AnatomyComponent,
    after: AnatomyComponent,
    names: list[str] | tuple[str, ...],
    *,
    operation: str,
    tolerance: float = 1e-9,
) -> ModifyResult:
    """Compare two components over explicit property names.

    Builds the ModifyResult automatically: properties whose values
    differ beyond the tolerance become PropertyChange entries, the
    others become preserved names.
    """

    if not isinstance(before, AnatomyComponent) or not isinstance(
        after,
        AnatomyComponent,
    ):
        raise ValueError(
            "diff_properties requires anatomy components."
        )

    resolved_tolerance = _require_tolerance(
        tolerance,
        "diff_properties",
    )

    name_list = list(names)

    if not name_list:
        raise ValueError(
            "diff_properties requires at least one property name."
        )

    before.validate()
    after.validate()

    changes: list[PropertyChange] = []
    preserved: list[str] = []
    seen: list[str] = []

    for name in name_list:
        if not isinstance(name, str) or not name.strip():
            raise ValueError(
                "diff_properties property names must be non-empty "
                "strings."
            )

        if name in seen:
            raise ValueError(
                "diff_properties contains duplicate property name "
                f"{name!r}."
            )

        seen.append(name)

        value_before = getattr(before, name, _MISSING)
        value_after = getattr(after, name, _MISSING)

        if value_before is _MISSING or value_after is _MISSING:
            raise ValueError(
                f"Property {name!r} not found on both components."
            )

        if _value_changed(
            value_before,
            value_after,
            resolved_tolerance,
        ):
            changes.append(
                PropertyChange(
                    name=name,
                    before=value_before,
                    after=value_after,
                    tolerance=resolved_tolerance,
                )
            )
        else:
            preserved.append(name)

    return ModifyResult(
        operation=operation,
        changes=changes,
        preserved=preserved,
    )