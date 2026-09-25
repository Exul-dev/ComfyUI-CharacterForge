from __future__ import annotations

import pytest

from human.anatomy import (
    BodySide,
    BreastUnit,
    Head,
    HumanAnatomy,
    MammaryRegion,
)


class TestHumanEngineH418D:

    # --- cablaggio Head (3) ---

    def test_anatomy_has_head(self):
        anatomy = HumanAnatomy()

        assert isinstance(anatomy.head, Head)
        assert anatomy.head.is_valid()
        assert anatomy.head.component_type == "head"

    def test_head_brings_the_whole_face(self):
        anatomy = HumanAnatomy()
        face = anatomy.head.face

        assert face.nose.component_type == "nose"
        assert face.mouth.philtrum.component_type == "philtrum"
        assert face.forehead is not None
        assert face.chin is not None
        assert face.landmarks is not None
        assert anatomy.head.ears.left.side is BodySide.LEFT
        assert anatomy.head.ears.right.side is BodySide.RIGHT

    def test_head_is_optional_and_overridable(self):
        anatomy = HumanAnatomy(
            head=Head(height=24.0, shape="round"),
        )

        assert anatomy.head.height == 24.0
        assert anatomy.head.shape == "round"
        assert anatomy.is_valid()

    # --- cablaggio MammaryRegion (3) ---

    def test_anatomy_has_mammary_region(self):
        anatomy = HumanAnatomy()

        assert isinstance(anatomy.mammary_region, MammaryRegion)
        assert anatomy.mammary_region.is_valid()
        assert anatomy.mammary_region.component_type == "mammary_region"

    def test_mammary_region_is_bilateral(self):
        anatomy = HumanAnatomy()
        region = anatomy.mammary_region

        # The signature is discovered structurally: the region
        # must expose left and right BreastUnits (H4.8 contract).
        assert isinstance(region.left, BreastUnit)
        assert isinstance(region.right, BreastUnit)
        assert region.left.is_valid()
        assert region.right.is_valid()

    def test_mammary_region_is_optional_and_overridable(self):
        anatomy = HumanAnatomy(
            mammary_region=MammaryRegion(),
        )

        assert anatomy.mammary_region.is_valid()
        assert anatomy.is_valid()

    # --- serializzazione completa (2) ---

    def test_serialization_includes_head_and_mammary(self):
        data = HumanAnatomy().to_dict()

        assert data["head"]["component_type"] == "head"
        assert (
            data["head"]["face"]["nose"]["component_type"]
            == "nose"
        )
        assert (
            data["head"]["face"]["mouth"]["philtrum"]["shape"]
            == "average"
        )
        assert data["head"]["ears"]["right"]["side"] == "right"
        assert "mammary_region" in data
        assert (
            data["mammary_region"]["left"]["component_type"]
            == "breast_unit"
        )

    def test_backward_compatible_constructor(self):
        # Pre-H4.18 call style keeps working silently.
        from human.anatomy import BodyType, Height

        anatomy = HumanAnatomy(
            body_type=BodyType("slender"),
            height=Height(175),
        )

        assert anatomy.is_valid()
        assert anatomy.head is not None
        assert anatomy.mammary_region is not None

    # --- mutazioni profonde (2) ---

    def test_deep_mutation_head_invalidates(self):
        anatomy = HumanAnatomy()

        anatomy.head.face.nose.width = 0.0
        assert not anatomy.is_valid()

    def test_deep_mutation_mammary_invalidates(self):
        anatomy = HumanAnatomy()

        # Invalidate through a nested breast unit attribute.
        unit = anatomy.mammary_region.left
        unit.breast.volume = -1.0
        assert not anatomy.is_valid()

    # --- LA TRAVERSATA (1) ---

    def test_complete_human_head_to_toe(self):
        # The certified walk: from the hairline (trichion) to the
        # big toe (hallux), through every station built across the
        # whole Human Engine history.
        anatomy = HumanAnatomy()
        assert anatomy.is_valid()

        head = anatomy.head
        assert head.face.landmarks is not None  # H4.10/H4.12 stations
        assert head.face.nose.bridge == "straight"  # H4.16-A
        assert head.face.mouth.shape == "full"  # H4.16-A
        assert head.ears.left.side is BodySide.LEFT  # H4.16-A

        assert anatomy.neck.circumference == 36.0  # H4.6
        assert anatomy.shoulders.left.side is BodySide.LEFT  # H4.5
        assert anatomy.chest.width == 32.0  # H4.7
        assert anatomy.torso.length == 52.0  # H4.16-B (cm reali)
        assert anatomy.waist.circumference == 80.0  # H4.16-B
        assert anatomy.abdomen.flanks.left.side is BodySide.LEFT  # H4.18-B
        assert anatomy.mammary_region.left.breast is not None  # H4.8 + H4.18-D
        assert anatomy.pelvis.hips.right.side is BodySide.RIGHT  # H4.18-A
        assert (
            anatomy.pelvis.gluteal_region.left.side
            is BodySide.LEFT
        )  # H4.18-A

        left_arm = anatomy.arms.left  # H4.17
        assert left_arm.hand.fingers is not None
        assert len(left_arm.hand.fingers) == 5

        left_leg = anatomy.legs.left  # H4.15 + H4.18-B/C
        assert left_leg.thigh.quad_prominence == 0.5  # H4.18-B
        assert left_leg.knee.alignment == "neutral"  # H4.18-C
        assert left_leg.foot.heel is not None  # H4.18-C
        hallux = left_leg.foot.toes[
            __import__("human.anatomy", fromlist=["ToeType"]).ToeType.HALLUX
        ]
        assert hallux.length == 2.7  # H4.15-B

        # E la serializzazione porta tutto.
        data = anatomy.to_dict()
        assert data["head"]["face"]["mouth"]["philtrum"]["length"] == 1.5
        assert data["legs"]["right"]["foot"]["heel"]["height"] == 7.0

    # --- export/conto componenti (1) ---

    def test_anatomy_component_count(self):
        # 16 componenti pre-H4.18-D + head + mammary_region = 18.
        anatomy = HumanAnatomy()

        components = (
            anatomy.body_type, anatomy.height, anatomy.proportions,
            anatomy.musculature, anatomy.body_fat, anatomy.neck,
            anatomy.shoulders, anatomy.torso, anatomy.chest,
            anatomy.ribcage, anatomy.back, anatomy.waist,
            anatomy.abdomen, anatomy.pelvis, anatomy.arms,
            anatomy.legs, anatomy.head, anatomy.mammary_region,
        )

        assert len(components) == 18
        for component in components:
            assert component.is_valid()