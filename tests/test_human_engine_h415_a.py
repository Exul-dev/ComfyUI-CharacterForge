from __future__ import annotations

import pytest

import human.anatomy as anatomy_module
from human.anatomy import (
    Ankle,
    BodySide,
    Knee,
    LowerLeg,
    Pelvis,
    Thigh,
)
from human.anatomy.anatomy_component import AnatomyComponent


class TestHumanEngineH415A:

    # --- Pelvis ---

    def test_pelvis_defaults(self):
        pelvis = Pelvis()

        assert pelvis.is_valid()
        assert pelvis.component_type == "pelvis"
        assert pelvis.width == 36.0
        assert pelvis.depth == 22.0
        assert pelvis.circumference == 95.0
        assert pelvis.tilt == 0.0
        assert pelvis.shape == "average"
        assert pelvis.iliac_flare == 0.5

    def test_pelvis_tilt_boundaries(self):
        assert Pelvis(tilt=-20.0).is_valid()
        assert Pelvis(tilt=0.0).is_valid()
        assert Pelvis(tilt=20.0).is_valid()

    def test_pelvis_rejects_invalid_tilt(self):
        with pytest.raises(ValueError, match="tilt"):
            Pelvis(tilt=-20.1)

        with pytest.raises(ValueError, match="tilt"):
            Pelvis(tilt=20.1)

    def test_pelvis_rejects_non_positive_dimensions(self):
        with pytest.raises(ValueError, match="Pelvis width"):
            Pelvis(width=0.0)

        with pytest.raises(ValueError, match="Pelvis depth"):
            Pelvis(depth=-1.0)

        with pytest.raises(ValueError, match="Pelvis circumference"):
            Pelvis(circumference=0.0)

    def test_pelvis_rejects_invalid_shape(self):
        with pytest.raises(ValueError, match="Invalid pelvis shape"):
            Pelvis(shape="gigantic")

    def test_pelvis_rejects_invalid_iliac_flare(self):
        with pytest.raises(ValueError, match="iliac flare"):
            Pelvis(iliac_flare=-0.1)

        with pytest.raises(ValueError, match="iliac flare"):
            Pelvis(iliac_flare=1.1)

    def test_pelvis_serialization_and_mutation(self):
        pelvis = Pelvis()

        data = pelvis.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["enabled"] is True
        assert data["component_type"] == "pelvis"
        assert data["width"] == 36.0
        assert data["tilt"] == 0.0
        assert data["shape"] == "average"

        pelvis.tilt = 99.0
        assert not pelvis.is_valid()

    # --- Thigh ---

    def test_thigh_defaults(self):
        thigh = Thigh()

        assert thigh.is_valid()
        assert thigh.component_type == "thigh"
        assert thigh.length == 44.0
        assert thigh.circumference == 56.0
        assert thigh.shape == "average"

    def test_thigh_rejects_non_positive(self):
        with pytest.raises(ValueError, match="Thigh length"):
            Thigh(length=0.0)

        with pytest.raises(ValueError, match="Thigh circumference"):
            Thigh(circumference=-1.0)

    def test_thigh_rejects_invalid_shape(self):
        with pytest.raises(ValueError, match="Invalid thigh shape"):
            Thigh(shape="enormous")

    def test_thigh_serialization_and_mutation(self):
        thigh = Thigh()

        data = thigh.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["length"] == 44.0
        assert data["circumference"] == 56.0
        assert data["shape"] == "average"

        thigh.length = -5.0
        assert not thigh.is_valid()

    # --- Knee ---

    def test_knee_defaults(self):
        knee = Knee()

        assert knee.is_valid()
        assert knee.component_type == "knee"
        assert knee.side is BodySide.RIGHT
        assert knee.flexion == 0.0
        assert knee.rotation == 0.0
        assert knee.width == 10.0
        assert knee.circumference == 37.0
        assert knee.prominence == 0.5

    def test_knee_rejects_invalid_side(self):
        with pytest.raises(ValueError, match="side"):
            Knee(side="left")

        with pytest.raises(ValueError, match="side"):
            Knee(side=None)

    def test_knee_flexion_boundaries(self):
        assert Knee(flexion=0.0).is_valid()
        assert Knee(flexion=75.0).is_valid()
        assert Knee(flexion=150.0).is_valid()

        with pytest.raises(ValueError, match="flexion"):
            Knee(flexion=-0.1)

        with pytest.raises(ValueError, match="flexion"):
            Knee(flexion=150.1)

    def test_knee_rotation_boundaries(self):
        assert Knee(rotation=-45.0).is_valid()
        assert Knee(rotation=0.0).is_valid()
        assert Knee(rotation=45.0).is_valid()

        with pytest.raises(ValueError, match="rotation"):
            Knee(rotation=-45.1)

        with pytest.raises(ValueError, match="rotation"):
            Knee(rotation=45.1)

    def test_knee_rejects_non_positive(self):
        with pytest.raises(ValueError, match="Knee width"):
            Knee(width=0.0)

        with pytest.raises(ValueError, match="Knee circumference"):
            Knee(circumference=-1.0)

    def test_knee_rejects_invalid_prominence(self):
        with pytest.raises(ValueError, match="prominence"):
            Knee(prominence=-0.1)

        with pytest.raises(ValueError, match="prominence"):
            Knee(prominence=1.1)

    def test_knee_serialization_and_mutation(self):
        knee = Knee(side=BodySide.LEFT)

        data = knee.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["side"] == "left"
        assert data["flexion"] == 0.0
        assert data["circumference"] == 37.0

        knee.flexion = 999.0
        assert not knee.is_valid()

    # --- LowerLeg ---

    def test_lower_leg_defaults(self):
        lower = LowerLeg()

        assert lower.is_valid()
        assert lower.component_type == "lower_leg"
        assert lower.length == 42.0
        assert lower.circumference == 36.0
        assert lower.shape == "average"
        assert lower.calf_prominence == 0.5

    def test_lower_leg_rejects_non_positive(self):
        with pytest.raises(ValueError, match="Lower leg length"):
            LowerLeg(length=0.0)

        with pytest.raises(ValueError, match="Lower leg circumference"):
            LowerLeg(circumference=-1.0)

    def test_lower_leg_rejects_invalid_shape(self):
        with pytest.raises(ValueError, match="Invalid lower leg shape"):
            LowerLeg(shape="colossal")

    def test_lower_leg_calf_prominence_range(self):
        assert LowerLeg(calf_prominence=0.0).is_valid()
        assert LowerLeg(calf_prominence=1.0).is_valid()

        with pytest.raises(ValueError, match="calf prominence"):
            LowerLeg(calf_prominence=-0.1)

        with pytest.raises(ValueError, match="calf prominence"):
            LowerLeg(calf_prominence=1.1)

    def test_lower_leg_serialization_and_mutation(self):
        lower = LowerLeg()

        data = lower.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["length"] == 42.0
        assert data["calf_prominence"] == 0.5

        lower.circumference = 0.0
        assert not lower.is_valid()

    # --- Ankle ---

    def test_ankle_defaults(self):
        ankle = Ankle()

        assert ankle.is_valid()
        assert ankle.component_type == "ankle"
        assert ankle.side is BodySide.RIGHT
        assert ankle.width == 7.0
        assert ankle.circumference == 22.0
        assert ankle.thickness == 6.0
        assert ankle.flexion == 0.0
        assert ankle.extension == 0.0
        assert ankle.deviation == 0.0
        assert ankle.prominence == 0.5

    def test_ankle_rejects_invalid_side(self):
        with pytest.raises(ValueError, match="side"):
            Ankle(side="right")

        with pytest.raises(ValueError, match="side"):
            Ankle(side=3)

    def test_ankle_motion_ranges(self):
        assert Ankle(
            flexion=60.0, extension=30.0, deviation=-30.0
        ).is_valid()
        assert Ankle(
            flexion=0.0, extension=0.0, deviation=30.0
        ).is_valid()

        with pytest.raises(ValueError, match="flexion"):
            Ankle(flexion=60.1)

        with pytest.raises(ValueError, match="extension"):
            Ankle(extension=30.1)

        with pytest.raises(ValueError, match="deviation"):
            Ankle(deviation=-30.1)

        with pytest.raises(ValueError, match="deviation"):
            Ankle(deviation=30.1)

    def test_ankle_rejects_non_positive(self):
        with pytest.raises(ValueError, match="Ankle width"):
            Ankle(width=0.0)

        with pytest.raises(ValueError, match="Ankle circumference"):
            Ankle(circumference=-1.0)

        with pytest.raises(ValueError, match="Ankle thickness"):
            Ankle(thickness=0.0)

    def test_ankle_serialization_and_mutation(self):
        ankle = Ankle(side=BodySide.LEFT)

        data = ankle.to_dict()

        assert data["schema_version"] == "1.0"
        assert data["side"] == "left"
        assert data["width"] == 7.0
        assert data["thickness"] == 6.0

        ankle.deviation = 500.0
        assert not ankle.is_valid()

    # --- Integrazione pacchetto ---

    def test_package_exports(self):
        for name in ("Pelvis", "Thigh", "Knee", "LowerLeg", "Ankle"):
            assert hasattr(anatomy_module, name)
            assert name in anatomy_module.__all__

        for component in (Pelvis(), Thigh(), Knee(), LowerLeg(), Ankle()):
            assert isinstance(component, AnatomyComponent)
            assert component.is_valid()

    def test_contract_compliance(self):
        expected_types = {
            Pelvis: "pelvis",
            Thigh: "thigh",
            Knee: "knee",
            LowerLeg: "lower_leg",
            Ankle: "ankle",
        }

        for cls, expected in expected_types.items():
            component = cls()
            data = component.to_dict()

            assert component.component_type == expected
            assert data["component_type"] == expected
            assert data["schema_version"] == "1.0"
            assert data["enabled"] is True