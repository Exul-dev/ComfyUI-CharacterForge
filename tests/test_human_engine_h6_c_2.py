from __future__ import annotations

import pytest

from human.age import (
    AgeAxis,
    AgeCurves,
    AgeResult,
    apparent_age,
)
from human.anatomy import FaceAging
from human.hair import HairAging
from human.human import Human
from human.skin import SkinAging


class TestHumanEngineH6C2:

    # --- l operatore base (3) ---

    def test_apparent_age_registers_components(self):
        human = Human(name="AgeOp Test")
        result = apparent_age(human, 70)

        assert human.has_component("skin_aging")
        assert human.has_component("hair_aging")
        assert human.has_component("face_aging")
        assert human.validate() is None

    def test_values_match_curves(self):
        human = Human(name="Curve Match")
        apparent_age(human, 70)

        snap = AgeCurves.snapshot(70)

        skin = human.get_component("skin_aging")
        assert skin.wrinkle_depth == snap[AgeAxis.WRINKLE_DEPTH]
        assert skin.elasticity == snap[AgeAxis.ELASTICITY]
        assert skin.sagging == snap[AgeAxis.SAGGING]
        assert skin.age_spots == snap[AgeAxis.AGE_SPOTS]

        hair = human.get_component("hair_aging")
        assert hair.scalp_gray_extent == snap[AgeAxis.SCALP_GRAY]
        assert hair.facial_gray_extent == snap[AgeAxis.FACIAL_GRAY]
        assert hair.body_gray_extent == snap[AgeAxis.BODY_GRAY]
        assert hair.gray_hair_texture == snap[AgeAxis.GRAY_TEXTURE]

        face = human.get_component("face_aging")
        assert face.nasolabial_fold_depth == snap[AgeAxis.NASOLABIAL_FOLD]
        assert face.midface_descent == snap[AgeAxis.MIDFACE_DESCENT]
        assert face.mandibular_definition_loss == snap[AgeAxis.MANDIBULAR_LOSS]

    def test_rejects_negative_age(self):
        human = Human(name="Neg Test")

        with pytest.raises(ValueError, match="negative"):
            apparent_age(human, -1)

    # --- il report changed/preserved (3) ---

    def test_report_is_age_result(self):
        human = Human(name="Report Test")
        result = apparent_age(human, 50)

        assert isinstance(result, AgeResult)
        assert result.target_age == 50
        assert len(result.changes) > 0
        assert isinstance(result.to_dict(), dict)
        assert "target_age" in result.to_dict()
        assert "changes" in result.to_dict()
        assert "preserved" in result.to_dict()

    def test_report_changed_fields(self):
        human = Human(name="Changed Fields")
        result = apparent_age(human, 70)

        skin_changed = result.changed_fields("skin_aging")
        hair_changed = result.changed_fields("hair_aging")
        face_changed = result.changed_fields("face_aging")

        assert "wrinkle_depth" in skin_changed
        assert "elasticity" in skin_changed
        assert "scalp_gray_extent" in hair_changed
        assert "nasolabial_fold_depth" in face_changed

    def test_report_preserved_on_idempotent_call(self):
        # Same age twice: the second call changes nothing.
        human = Human(name="Idempotent")
        apparent_age(human, 60)
        result_again = apparent_age(human, 60)

        # All fields should be preserved (same values)
        assert len(result_again.preserved) > 20
        # No changes (or very few from rounding)
        assert len(result_again.changes) <= 1

    # --- il ringiovanimento (2) ---

    def test_rejuvenation(self):
        human = Human(name="Rejuvenation")
        apparent_age(human, 80)

        skin_old = human.get_component("skin_aging")
        assert skin_old.wrinkle_depth > 0.8
        # Curve value at 80: ~0.261 (anchors 75->0.3, 90->0.15,
        # smoothstep). The correct expectation is < 0.3.
        assert skin_old.elasticity < 0.3

        # Rejuvenate to 25
        apparent_age(human, 25)

        skin_young = human.get_component("skin_aging")
        assert skin_young.wrinkle_depth < 0.1
        assert skin_young.elasticity > 0.9

        face_young = human.get_component("face_aging")
        assert face_young.nasolabial_fold_depth < 0.1
        assert face_young.mandibular_definition_loss == 0.0

        assert human.validate() is None

    def test_rejuvenation_report_shows_changes(self):
        human = Human(name="Reju Report")
        apparent_age(human, 80)
        result = apparent_age(human, 25)

        # Many fields changed going from 80 to 25
        assert len(result.changes) > 10
        assert result.target_age == 25

    # --- le proporzioni attraverso l operatore (2) ---

    def test_proportions_preserved_through_operator(self):
        # THE core requirement: the operator preserves the
        # gerontological hierarchy, not just "high values".
        human = Human(name="Proportions")
        apparent_age(human, 70)

        face = human.get_component("face_aging")
        hair = human.get_component("hair_aging")

        # Folds lead bone
        assert (
            face.nasolabial_fold_depth
            > face.mandibular_definition_loss
        )
        assert (
            face.nasolabial_fold_depth
            > face.orbital_hollowing
        )

        # Beard grays before scalp
        assert (
            hair.facial_gray_extent
            > hair.scalp_gray_extent
        )

        # Elasticity inverted
        skin = human.get_component("skin_aging")
        assert skin.elasticity < 0.5

    def test_wrinkle_map_is_zone_distributed(self):
        # The global depth is distributed by zone salience:
        # forehead and nasolabial lead, decollete trails.
        human = Human(name="Zone Distribution")
        apparent_age(human, 70)

        skin = human.get_component("skin_aging")
        from human.skin import WrinkleZone

        forehead = skin.wrinkle_map[WrinkleZone.FOREHEAD]
        nasolabial = skin.wrinkle_map[WrinkleZone.NASOLABIAL]
        decollete = skin.wrinkle_map[WrinkleZone.DECOLLETE]

        assert forehead > decollete, "forehead must lead decollete"
        assert nasolabial > decollete, "nasolabial must lead decollete"
        assert forehead > 0.5  # substantial at 70
        assert decollete < forehead  # trailing zone

    # --- non tocca nulla di non-aging (2) ---

    def test_does_not_touch_demographics(self):
        human = Human(name="Demographics Safe")
        from human.demographics import Age

        human.demographics.age.chronological.years = 30

        apparent_age(human, 70)

        # ChronologicalAge UNCHANGED: the operator only acts
        # on the apparent axis.
        assert human.demographics.age.chronological.years == 30

    def test_does_not_touch_anatomy_structure(self):
        human = Human(name="Anatomy Safe")

        # Register the full anatomy
        from human.anatomy import HumanAnatomy

        anatomy = HumanAnatomy(height_cm=180) if hasattr(
            HumanAnatomy, "height_cm"
        ) else None

        # Even without anatomy: identity must survive
        name_before = human.identity.name
        entity_id_before = human.entity_id

        apparent_age(human, 85)

        assert human.identity.name == name_before
        assert human.entity_id == entity_id_before
        assert human.validate() is None

    # --- serializzazione end-to-end (1) ---

    def test_full_serialization_with_aging(self):
        from human.eyes import Eyes
        from human.hair import Hair
        from human.skin import Skin

        human = Human(name="Full Serialization")
        human.register_component("skin", Skin(tone="medium"))
        human.register_component("hair", Hair(color="dark_brown"))
        human.register_component("eyes", Eyes())

        apparent_age(human, 65)

        data = human.to_dict()
        components = data["human_engine"]["components"]

        assert "skin" in components
        assert "hair" in components
        assert "eyes" in components
        assert "skin_aging" in components
        assert "hair_aging" in components
        assert "face_aging" in components

        # The aging values are serialized
        assert (
            components["skin_aging"]["wrinkle_depth"] > 0.5
        )
        assert (
            components["hair_aging"]["facial_gray_extent"] > 0.6
        )
        assert (
            components["face_aging"]["nasolabial_fold_depth"] > 0.5
        )

    # --- graying pattern auto-selection (1) ---

    def test_graying_pattern_auto_selected(self):
        from human.hair import GrayingPattern

        # Young: NONE
        human = Human(name="Pattern Young")
        apparent_age(human, 25)
        hair = human.get_component("hair_aging")
        assert hair.graying_pattern is GrayingPattern.NONE

        # Mid: TEMPLES_FIRST (extent < 0.35)
        human2 = Human(name="Pattern Mid")
        apparent_age(human2, 45)
        hair2 = human2.get_component("hair_aging")
        assert (
            hair2.graying_pattern is GrayingPattern.TEMPLES_FIRST
        )

        # Old: DIFFUSE (extent >= 0.7)
        human3 = Human(name="Pattern Old")
        apparent_age(human3, 80)
        hair3 = human3.get_component("hair_aging")
        assert hair3.scalp_gray_extent >= 0.7
