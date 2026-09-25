from __future__ import annotations

import inspect

import pytest

import human.anatomy as anatomy_module
from human.anatomy import (
    BodySide,
    Finger,
    Foot,
    Heel,
    HumanAnatomy,
    Knee,
    Toe,
)


class TestHumanEngineH418C:

    # --- Knee arricchito (5) ---

    def test_knee_enriched_defaults(self):
        knee = Knee(side=BodySide.LEFT)

        assert knee.is_valid()
        assert knee.component_type == "knee"
        assert knee.patella_prominence == 0.5
        assert knee.patella_width == 5.0
        assert knee.alignment == "neutral"
        assert knee.popliteal_depth == 0.4

    def test_knee_legacy_contract_intact(self):
        knee = Knee(side=BodySide.RIGHT, flexion=90.0, rotation=10.0)

        assert knee.flexion == 90.0
        assert knee.rotation == 10.0

        with pytest.raises(ValueError, match="Knee flexion"):
            Knee(flexion=-0.1)

        with pytest.raises(ValueError, match="Knee rotation"):
            Knee(rotation=45.1)

        with pytest.raises(ValueError, match="Knee width"):
            Knee(width=0.0)

        with pytest.raises(ValueError, match="Knee circumference"):
            Knee(circumference=-1.0)

        with pytest.raises(ValueError, match="Knee prominence"):
            Knee(prominence=1.1)

        with pytest.raises(ValueError, match="side"):
            Knee(side="left")

    def test_knee_alignment_enum(self):
        for alignment in ("neutral", "genu_valgum", "genu_varum"):
            assert Knee(alignment=alignment).is_valid()

        with pytest.raises(ValueError, match="Invalid knee alignment"):
            Knee(alignment="knock_kneed")

    def test_knee_new_params_validation(self):
        with pytest.raises(ValueError, match="patella_prominence"):
            Knee(patella_prominence=1.5)

        with pytest.raises(ValueError, match="patella_width"):
            Knee(patella_width=0.0)

        with pytest.raises(ValueError, match="popliteal_depth"):
            Knee(popliteal_depth=-0.1)

        assert Knee(
            patella_prominence=0.0,
            popliteal_depth=1.0,
        ).is_valid()

    def test_knee_serialization_includes_new_fields(self):
        data = Knee(
            side=BodySide.LEFT,
            alignment="genu_varum",
            patella_prominence=0.8,
        ).to_dict()

        assert data["alignment"] == "genu_varum"
        assert data["patella_prominence"] == 0.8
        assert data["patella_width"] == 5.0
        assert data["popliteal_depth"] == 0.4

    # --- Heel (3) ---

    def test_heel_defaults(self):
        heel = Heel()

        assert heel.is_valid()
        assert heel.component_type == "heel"
        assert heel.width == 5.5
        assert heel.height == 7.0
        assert heel.projection == 0.5
        assert heel.achilles_thickness == 0.5
        assert heel.fat_pad_thickness == 0.5
        assert heel.calcaneal_prominence == 0.4

    def test_heel_validation(self):
        with pytest.raises(ValueError, match="Heel width"):
            Heel(width=0.0)

        with pytest.raises(ValueError, match="Heel height"):
            Heel(height=-1.0)

        for field in (
            "projection",
            "achilles_thickness",
            "fat_pad_thickness",
            "calcaneal_prominence",
        ):
            with pytest.raises(ValueError, match=field):
                Heel(**{field: 1.5})

        assert Heel(
            projection=0.0, calcaneal_prominence=1.0
        ).is_valid()

    def test_heel_serialization(self):
        data = Heel(achilles_thickness=0.9).to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "heel"
        assert data["achilles_thickness"] == 0.9
        assert data["calcaneal_prominence"] == 0.4

    # --- Foot composito (5) ---

    def test_foot_composite_with_independent_plantar_width(self):
        foot = Foot(side=BodySide.RIGHT)

        assert foot.is_valid()
        assert isinstance(foot.heel, Heel)
        # legacy plantar width stays independent of Heel structure
        assert foot.heel_width == 6.0
        assert foot.heel.width == 5.5

    def test_foot_custom_heel(self):
        foot = Foot(
            side=BodySide.LEFT,
            heel=Heel(achilles_thickness=0.9, height=8.0),
        )

        assert foot.heel.achilles_thickness == 0.9
        assert foot.heel.height == 8.0
        assert foot.is_valid()

    def test_foot_rejects_wrong_heel_type(self):
        with pytest.raises(ValueError, match="heel must be"):
            Foot(heel="back")

    def test_foot_serialization_nested(self):
        data = Foot(side=BodySide.RIGHT).to_dict()

        assert data["heel"]["component_type"] == "heel"
        assert data["heel"]["fat_pad_thickness"] == 0.5
        assert data["heel_width"] == 6.0
        assert data["toes"]["hallux"]["type"] == "hallux"

    def test_foot_mutation_heel_invalidates(self):
        foot = Foot()

        foot.heel.projection = 9.0
        assert not foot.is_valid()

    # --- Toe parity certification (1) ---

    def test_toe_matches_finger_detail_standard(self):
        # Meticulosità also means knowing when NOT to add: Toe
        # already sits at the Finger detail standard (the richest
        # per-unit component of the project). Certified by
        # constructor signature parity.
        toe_params = set(
            inspect.signature(Toe.__init__).parameters
        ) - {"self"}
        finger_params = set(
            inspect.signature(Finger.__init__).parameters
        ) - {"self"}

        assert len(toe_params) == len(finger_params)
        assert toe_params == finger_params

    # --- HumanAnatomy end-to-end (2) ---

    def test_anatomy_knee_and_heel_detail(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()
        assert anatomy.legs.left.knee.alignment == "neutral"
        assert (
            anatomy.legs.right.foot.heel.component_type == "heel"
        )

    def test_anatomy_knee_heel_serialization(self):
        data = HumanAnatomy().to_dict()

        left_knee = data["legs"]["left"]["knee"]
        right_heel = data["legs"]["right"]["foot"]["heel"]

        assert left_knee["patella_width"] == 5.0
        assert left_knee["alignment"] == "neutral"
        assert right_heel["achilles_thickness"] == 0.5
        assert right_heel["calcaneal_prominence"] == 0.4

    # --- export (1) ---

    def test_package_exports_h418c(self):
        assert hasattr(anatomy_module, "Heel")
        assert "Heel" in anatomy_module.__all__