"""Age trajectories (Human Engine, H6-D — Age Engine).

A trajectory is a STORY, not a state: the ordered sequence of
apparent ages a character lived through. The trajectory makes
aging and rejuvenation bidirectional and coherent:

- age_at(t): the apparent age at any point t along the
  trajectory (linear between waypoints — the CURVES already
  carry the gerontological shape, the trajectory only carries
  the timeline);
- transit(human, from, to): moves the character along the
  trajectory, invoking apparent_age (the in-place operator) at
  the destination and returning the TransitReport of the
  passage;
- round-trip coherence: 20 -> 70 -> 20 returns to the exact
  starting state — the curves are deterministic, so history is
  REVERSIBLE BY CONSTRUCTION. Rejuvenation inverts the same
  matrix aging followed: it invents nothing.

The trajectory stores waypoints, not snapshots: two characters
with waypoints (0, 20, 45, 70) share the timeline structure
while keeping their own tuning freedom (the operator's
in-place principle).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .curves import AgeAxis, AgeCurves
from .operator import AgeResult, FieldChange, apparent_age


@dataclass
class TransitReport:
    """The report of one trajectory transit."""

    from_age: float
    to_age: float
    result: AgeResult

    @property
    def direction(self) -> str:
        if self.to_age > self.from_age:
            return "aging"
        if self.to_age < self.from_age:
            return "rejuvenating"
        return "stationary"

    @property
    def changes_count(self) -> int:
        return len(self.result.changes)

    def to_dict(self) -> dict[str, Any]:
        return {
            "from_age": self.from_age,
            "to_age": self.to_age,
            "direction": self.direction,
            "changes": len(self.result.changes),
            "preserved": len(self.result.preserved),
        }


class AgeTrajectory:
    """An ordered timeline of apparent ages.

    Waypoints are (t, age) pairs: at trajectory-time t the
    character's apparent age is the given value. Between
    waypoints the age interpolates linearly (the gerontological
    SHAPE comes from the curves, not from here).
    """

    def __init__(
        self,
        waypoints: list[tuple[float, float]] | None = None,
    ) -> None:
        if waypoints is None:
            waypoints = [(0, 0)]

        self.waypoints: list[tuple[float, float]] = []
        self._set_waypoints(waypoints)

    def _set_waypoints(
        self,
        waypoints: list[tuple[float, float]],
    ) -> None:
        validated: list[tuple[float, float]] = []

        for point in waypoints:
            if (
                not isinstance(point, (tuple, list))
                or len(point) != 2
            ):
                raise ValueError(
                    "AgeTrajectory waypoints must be "
                    "(t, age) pairs."
                )

            t, age = point

            if not isinstance(t, (int, float)) or isinstance(t, bool):
                raise ValueError(
                    "AgeTrajectory waypoint t must be a number."
                )

            if not isinstance(age, (int, float)) or isinstance(age, bool):
                raise ValueError(
                    "AgeTrajectory waypoint age must be a number."
                )

            if age < 0:
                raise ValueError(
                    "AgeTrajectory waypoint age cannot be negative."
                )

            validated.append((float(t), float(age)))

        if len(validated) < 1:
            raise ValueError(
                "AgeTrajectory needs at least one waypoint."
            )

        # Sort by t and check for duplicates.
        validated.sort(key=lambda p: p[0])

        for i in range(len(validated) - 1):
            if validated[i][0] == validated[i + 1][0]:
                raise ValueError(
                    "AgeTrajectory waypoint times must be unique."
                )

        self.waypoints = validated

    def age_at(self, t: float) -> float:
        """The apparent age at trajectory time t.

        Linear interpolation between waypoints: the timeline is
        straight, the aging SHAPE lives in the curves.
        """

        if not isinstance(t, (int, float)) or isinstance(t, bool):
            raise ValueError(
                "AgeTrajectory t must be a number."
            )

        points = self.waypoints

        if t <= points[0][0]:
            return points[0][1]

        if t >= points[-1][0]:
            return points[-1][1]

        for i in range(len(points) - 1):
            t_a, age_a = points[i]
            t_b, age_b = points[i + 1]

            if t_a <= t <= t_b:
                span = t_b - t_a

                if span <= 0:
                    return age_b

                ratio = (t - t_a) / span
                return age_a + (age_b - age_a) * ratio

        return points[-1][1]

    def duration(self) -> float:
        """The trajectory time span (last t - first t)."""

        if len(self.waypoints) < 2:
            return 0.0

        return self.waypoints[-1][0] - self.waypoints[0][0]

    def add_waypoint(self, t: float, age: float) -> None:
        """Add a waypoint and re-validate the timeline."""

        self._set_waypoints(
            self.waypoints + [(t, age)]
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "waypoints": [
                {"t": t, "age": age}
                for t, age in self.waypoints
            ],
        }


def transit(
    human: Any,
    trajectory: AgeTrajectory,
    t_from: float,
    t_to: float,
) -> TransitReport:
    """Move a character along a trajectory.

    Computes the apparent ages at t_from and t_to on the given
    trajectory, then moves the character from the former to the
    latter through apparent_age (the in-place operator). The
    TransitReport captures the passage: direction, changes,
    preserved — the STORY of this transit.
    """

    age_from = trajectory.age_at(t_from)
    age_to = trajectory.age_at(t_to)

    # Bring the character to the starting state first (if not
    # already there), without recording it: only the passage is
    # the report's subject.
    apparent_age(human, age_from)

    result = apparent_age(human, age_to)

    return TransitReport(
        from_age=age_from,
        to_age=age_to,
        result=result,
    )


def transit_steps(
    human: Any,
    trajectory: AgeTrajectory,
    t_from: float,
    t_to: float,
    steps: int,
) -> list[TransitReport]:
    """Transit in multiple steps: the animated passage.

    Divides the t interval into the given number of steps and
    transits through each one, collecting the reports: the
    frame-by-frame story of the aging/rejuvenation.
    """

    if not isinstance(steps, int) or isinstance(steps, bool):
        raise ValueError(
            "transit_steps steps must be an integer."
        )

    if steps < 1:
        raise ValueError(
            "transit_steps steps must be at least 1."
        )

    reports: list[TransitReport] = []

    for i in range(steps):
        t_start = t_from + (t_to - t_from) * i / steps
        t_end = t_from + (t_to - t_from) * (i + 1) / steps

        age_start = trajectory.age_at(t_start)
        age_end = trajectory.age_at(t_end)

        apparent_age(human, age_start)
        result = apparent_age(human, age_end)

        reports.append(
            TransitReport(
                from_age=age_start,
                to_age=age_end,
                result=result,
            )
        )

    return reports