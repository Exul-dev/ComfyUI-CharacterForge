from __future__ import annotations

import pytest

from human.age import (
    AgeAxis,
    AgeCurves,
    AgeTrajectory,
    TransitReport,
    apparent_age,
    transit,
    transit_steps,
)
from human.human import Human


class TestHumanEngineH6D:

    # --- waypoints validation (1) ---

    def test_waypoints_validation(self):
        with pytest.raises(ValueError, match="negative"):
            AgeTrajectory(waypoints=[(0, -5)])

        with pytest.raises(ValueError, match="unique"):
            AgeTrajectory(waypoints=[(0, 20), (0, 30)])

        with pytest.raises(ValueError, match="pairs"):
            AgeTrajectory(waypoints=[(0, 20, 40)])

        with pytest.raises(ValueError, match="number"):
            AgeTrajectory(waypoints=[("t", 20)])

        # At least one waypoint
        with pytest.raises(ValueError, match="at least one"):
            AgeTrajectory(waypoints=[])

        # Unsorted input is accepted (sorted internally)
        unsorted = AgeTrajectory(waypoints=[(20, 20), (0, 0)])
        assert unsorted.waypoints[0][0] == 0

    # --- age_at (3) ---

    def test_age_at_identity_trajectory(self):
        life = AgeTrajectory(
            waypoints=[(0, 0), (20, 20), (45, 45), (70, 70)]
        )

        assert life.age_at(0) == 0
        assert life.age_at(20) == 20
        assert life.age_at(35) == 35.0
        assert life.age_at(45) == 45
        assert life.age_at(70) == 70

    def test_age_at_accelerated_trajectory(self):
        # 30 years in 10t, 40 more in another 10t.
        accelerated = AgeTrajectory(
            waypoints=[(0, 0), (10, 30), (20, 70)]
        )

        assert accelerated.age_at(5) == 15.0
        assert accelerated.age_at(15) == 50.0
        assert accelerated.age_at(10) == 30
        assert accelerated.age_at(20) == 70

    def test_age_at_clamps(self):
        life = AgeTrajectory(
            waypoints=[(20, 20), (70, 70)]
        )

        # Below the first and above the last: clamped.
        assert life.age_at(-5) == 20
        assert life.age_at(100) == 70

        # Invalid input
        with pytest.raises(ValueError, match="number"):
            life.age_at("twenty")

    def test_duration(self):
        life = AgeTrajectory(
            waypoints=[(0, 0), (20, 20), (70, 70)]
        )

        assert life.duration() == 70

        single = AgeTrajectory(waypoints=[(5, 30)])
        assert single.duration() == 0.0

    # --- transit (3) ---

    def test_transit_aging(self):
        life = AgeTrajectory(
            waypoints=[(0, 0), (20, 20), (45, 45), (70, 70)]
        )
        human = Human(name="Aging Transit")
        report = transit(human, life, 20, 70)

        assert isinstance(report, TransitReport)
        assert report.from_age == 20
        assert report.to_age == 70
        assert report.direction == "aging"
        assert report.changes_count > 20

        # State matches the curves at 70
        skin = human.get_component("skin_aging")
        assert skin.wrinkle_depth == AgeCurves.value(
            AgeAxis.WRINKLE_DEPTH, 70
        )

    def test_transit_rejuvenating(self):
        life = AgeTrajectory(
            waypoints=[(0, 0), (20, 20), (70, 70)]
        )
        human = Human(name="Rejuvenating")
        transit(human, life, 20, 70)
        report = transit(human, life, 70, 20)

        assert report.direction == "rejuvenating"
        assert report.changes_count > 20

        skin = human.get_component("skin_aging")
        assert skin.wrinkle_depth == AgeCurves.value(
            AgeAxis.WRINKLE_DEPTH, 20
        )
        assert skin.elasticity == AgeCurves.value(
            AgeAxis.ELASTICITY, 20
        )

    def test_transit_stationary(self):
        life = AgeTrajectory(
            waypoints=[(0, 0), (70, 70)]
        )
        human = Human(name="Stationary")
        report = transit(human, life, 40, 40)

        assert report.direction == "stationary"
        assert report.changes_count == 0
        assert len(report.result.preserved) > 20

    # --- LA COERENZA ROUND-TRIP (1) ---

    def test_round_trip_coherence(self):
        # THE bidirectionality proof: 20 -> 70 -> 20 returns
        # to the EXACT starting state. Deterministic curves make
        # history reversible BY CONSTRUCTION.
        life = AgeTrajectory(
            waypoints=[(0, 0), (20, 20), (45, 45), (70, 70)]
        )
        human = Human(name="Round Trip")

        transit(human, life, 20, 70)
        transit(human, life, 70, 20)

        skin = human.get_component("skin_aging")
        hair = human.get_component("hair_aging")
        face = human.get_component("face_aging")

        # Every field back to the 20-year values
        assert skin.wrinkle_depth == AgeCurves.value(
            AgeAxis.WRINKLE_DEPTH, 20
        )
        assert skin.elasticity == AgeCurves.value(
            AgeAxis.ELASTICITY, 20
        )
        assert hair.scalp_gray_extent == AgeCurves.value(
            AgeAxis.SCALP_GRAY, 20
        )
        assert face.nasolabial_fold_depth == (
            AgeCurves.value(AgeAxis.NASOLABIAL_FOLD, 20)
        )
        assert face.mandibular_definition_loss == (
            AgeCurves.value(AgeAxis.MANDIBULAR_LOSS, 20)
        )

        assert human.validate() is None

    # --- transit_steps (3) ---

    def test_transit_steps_progression(self):
        life = AgeTrajectory(
            waypoints=[(0, 0), (20, 20), (70, 70)]
        )
        human = Human(name="Steps")
        steps = transit_steps(human, life, 20, 70, steps=5)

        assert len(steps) == 5
        for step in steps:
            assert step.direction == "aging"

        ages = [step.to_age for step in steps]
        assert ages == sorted(ages)

        # t-division on identity: first step t_end = 30
        # (NOT 26: that confused t with age — fixed lesson).
        assert steps[0].to_age == 30.0
        assert steps[-1].to_age == 70.0

    def test_transit_steps_accelerated_t_vs_age(self):
        # The t-vs-age distinction, tested explicitly.
        accelerated = AgeTrajectory(
            waypoints=[(0, 0), (10, 30), (20, 70)]
        )
        human = Human(name="Accel Steps")
        steps = transit_steps(
            human, accelerated, 0, 20, steps=2
        )

        # Step 1: t 0->10, age 0->30
        assert steps[0].from_age == 0.0
        assert steps[0].to_age == 30.0

        # Step 2: t 10->20, age 30->70
        assert steps[1].from_age == 30.0
        assert steps[1].to_age == 70.0

    def test_transit_steps_validation(self):
        life = AgeTrajectory(waypoints=[(0, 0), (70, 70)])
        human = Human(name="Steps Validation")

        with pytest.raises(ValueError, match="integer"):
            transit_steps(human, life, 0, 70, steps=1.5)

        with pytest.raises(ValueError, match="at least 1"):
            transit_steps(human, life, 0, 70, steps=0)

    # --- struttura report (1) ---

    def test_transit_report_to_dict(self):
        life = AgeTrajectory(waypoints=[(0, 0), (70, 70)])
        human = Human(name="Report Dict")
        report = transit(human, life, 20, 70)

        data = report.to_dict()

        assert data["from_age"] == 20
        assert data["to_age"] == 70
        assert data["direction"] == "aging"
        assert isinstance(data["changes"], int)
        assert isinstance(data["preserved"], int)

    # --- add_waypoint (1) ---

    def test_add_waypoint(self):
        life = AgeTrajectory(waypoints=[(0, 0), (50, 50)])
        life.add_waypoint(25, 30)  # non-linear insertion

        assert life.age_at(25) == 30

        # Duplicate t still rejected after add
        with pytest.raises(ValueError, match="unique"):
            life.add_waypoint(25, 40)

    # --- serializzazione (1) ---

    def test_trajectory_serialization(self):
        life = AgeTrajectory(
            waypoints=[(0, 0), (10, 30), (20, 70)]
        )

        data = life.to_dict()

        assert data["waypoints"] == [
            {"t": 0.0, "age": 0.0},
            {"t": 10.0, "age": 30.0},
            {"t": 20.0, "age": 70.0},
        ]

    # --- integrazione Human completa (1) ---

    def test_full_human_with_trajectory(self):
        # The complete stack: identity + appearance + aging +
        # trajectory — the Age Engine fully integrated.
        from human.eyes import Eyes
        from human.hair import Hair
        from human.skin import Skin

        life = AgeTrajectory(
            waypoints=[(0, 0), (25, 25), (50, 50), (80, 80)]
        )
        human = Human(name="Complete Age")

        human.register_component("skin", Skin(tone="medium"))
        human.register_component(
            "hair", Hair(color="dark_brown")
        )
        human.register_component("eyes", Eyes())

        transit(human, life, 25, 80)

        assert human.validate() is None
        # H6-B: apparent_age now configures body_aging too —
        # the full registry is 9 components (contract evolution,
        # same precedent as Hair VALID_LENGTHS 6 -> 7).
        assert set(human.component_names()) == {
            "human_identity",
            "demographics",
            "skin",
            "hair",
            "eyes",
            "skin_aging",
            "hair_aging",
            "face_aging",
            "body_aging",
        }

        data = human.to_dict()
        components = data["human_engine"]["components"]
        assert components["skin_aging"]["wrinkle_depth"] > 0.7
        assert (
            components["hair_aging"]["facial_gray_extent"] > 0.7
        )

    # --- export (1) ---

    def test_package_exports_h6d(self):
        from human import age as age_pkg

        for name in (
            "AgeTrajectory",
            "TransitReport",
            "transit",
            "transit_steps",
        ):
            assert hasattr(age_pkg, name)
            assert name in age_pkg.__all__
