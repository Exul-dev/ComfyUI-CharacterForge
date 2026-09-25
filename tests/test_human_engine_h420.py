from __future__ import annotations

import pytest

import human.anatomy as anatomy_module
from human.anatomy import (
    BodySide,
    ClitoralStructure,
    FemaleGenitalia,
    HumanAnatomy,
    LabiumMajus,
    LabiumMinus,
    MaleGenitalia,
    Penis,
    ReproductiveSystem,
    Scrotum,
    Testicle,
    Vulva,
)
from human.anatomy.anatomy_component import AnatomyComponent


class TestHumanEngineH420:

    # --- Testicle/Scrotum (4) ---

    def test_testicle_defaults_and_side(self):
        left = Testicle(side=BodySide.LEFT)

        assert left.is_valid()
        assert left.component_type == "testicle"
        assert left.size == 0.5
        assert left.hang == 0.5

    def test_testicle_requires_side(self):
        with pytest.raises(TypeError):
            Testicle()

        with pytest.raises(ValueError, match="side"):
            Testicle(side="left")

    def test_scrotum_bilateral_asymmetry(self):
        scrotum = Scrotum(
            left=Testicle(side=BodySide.LEFT, hang=0.6, size=0.4),
            right=Testicle(side=BodySide.RIGHT, hang=0.4, size=0.6),
        )

        assert scrotum.is_valid()
        assert scrotum.left.hang != scrotum.right.hang
        assert scrotum.left.size != scrotum.right.size

    def test_scrotum_validation(self):
        with pytest.raises(ValueError, match="Scrotum width"):
            Scrotum(width=0.0)

        with pytest.raises(ValueError, match="tightness"):
            Scrotum(tightness=1.5)

        with pytest.raises(ValueError, match="Invalid scrotum texture"):
            Scrotum(texture="hairy")

        with pytest.raises(ValueError, match="Scrotum.left"):
            Scrotum(left=Testicle(side=BodySide.RIGHT))

    # --- Penis (5) ---

    def test_penis_defaults(self):
        penis = Penis()

        assert penis.is_valid()
        assert penis.component_type == "penis"
        assert penis.length_flaccid == 9.0
        assert penis.length_erect == 13.5
        assert penis.girth_erect == 11.5
        assert penis.glans_shape == "tapered"
        assert penis.circumcision == "uncircumcised"
        assert penis.curvature_direction == "none"
        assert penis.curvature_degree == 0.0
        assert penis.veination == 0.4

    def test_penis_enums(self):
        for shape in ("tapered", "round", "mushroom"):
            assert Penis(glans_shape=shape).is_valid()

        for state in ("circumcised", "uncircumcised"):
            assert Penis(circumcision=state).is_valid()

        for direction in ("none", "up", "down", "left", "right"):
            assert Penis(curvature_direction=direction).is_valid()

        with pytest.raises(ValueError, match="glans shape"):
            Penis(glans_shape="flat")

        with pytest.raises(ValueError, match="circumcision"):
            Penis(circumcision="partial")

        with pytest.raises(ValueError, match="curvature direction"):
            Penis(curvature_direction="sideways")

    def test_penis_dimensions_validation(self):
        with pytest.raises(ValueError, match="length_flaccid"):
            Penis(length_flaccid=0.0)

        with pytest.raises(ValueError, match="length_erect"):
            Penis(length_erect=-1.0)

        with pytest.raises(ValueError, match="girth_erect"):
            Penis(girth_erect=0.0)

    def test_penis_graded_validation(self):
        with pytest.raises(ValueError, match="curvature_degree"):
            Penis(curvature_degree=1.5)

        with pytest.raises(ValueError, match="veination"):
            Penis(veination=-0.1)

        assert Penis(curvature_degree=0.0, veination=1.0).is_valid()

    def test_penis_serialization(self):
        data = Penis(
            length_flaccid=10.0, circumcision="circumcised"
        ).to_dict()

        assert data["schema_version"] == "1.0"
        assert data["component_type"] == "penis"
        assert data["length_flaccid"] == 10.0
        assert data["circumcision"] == "circumcised"

    # --- Labia / Vulva (7) ---

    def test_labium_majus_defaults_and_side(self):
        labium = LabiumMajus(side=BodySide.LEFT)

        assert labium.is_valid()
        assert labium.component_type == "labium_majus"
        assert labium.length == 7.0
        assert labium.width == 2.0
        assert labium.thickness == 1.0
        assert labium.prominence == 0.5
        assert labium.pigmentation == 0.4
        assert labium.shape == "full"

    def test_labium_majus_validation(self):
        with pytest.raises(TypeError):
            LabiumMajus()

        with pytest.raises(ValueError, match="LabiumMajus length"):
            LabiumMajus(side=BodySide.LEFT, length=0.0)

        with pytest.raises(ValueError, match="pigmentation"):
            LabiumMajus(side=BodySide.LEFT, pigmentation=1.5)

        with pytest.raises(ValueError, match="Invalid labium majus shape"):
            LabiumMajus(side=BodySide.LEFT, shape="angular")

    def test_labium_minus_protrusion(self):
        labium = LabiumMinus(side=BodySide.RIGHT)

        assert labium.is_valid()
        assert labium.component_type == "labium_minus"
        assert labium.length == 4.5
        assert labium.width == 1.2
        assert labium.protrusion_beyond_majora == 0.3

        with pytest.raises(ValueError, match="protrusion"):
            LabiumMinus(
                side=BodySide.RIGHT, protrusion_beyond_majora=1.5
            )

    def test_clitoral_structure(self):
        clitoral = ClitoralStructure()

        assert clitoral.is_valid()
        assert clitoral.component_type == "clitoral_structure"
        assert clitoral.glans_size == 0.3
        assert clitoral.hood_coverage == 0.6
        assert clitoral.prominence == 0.3

        with pytest.raises(ValueError, match="hood_coverage"):
            ClitoralStructure(hood_coverage=1.5)

    def test_vulva_bilateral_labial_asymmetry(self):
        vulva = Vulva(
            labia_minora_left=LabiumMinus(
                side=BodySide.LEFT, protrusion_beyond_majora=0.5
            ),
            labia_minora_right=LabiumMinus(
                side=BodySide.RIGHT, protrusion_beyond_majora=0.2
            ),
        )

        assert vulva.is_valid()
        assert (
            vulva.labia_minora_left.protrusion_beyond_majora
            != vulva.labia_minora_right.protrusion_beyond_majora
        )

    def test_vulva_rejects_wrong_sides(self):
        with pytest.raises(ValueError, match="labia_majora_left"):
            Vulva(
                labia_majora_left=LabiumMajus(
                    side=BodySide.RIGHT
                )
            )

        with pytest.raises(ValueError, match="labia_minora_right"):
            Vulva(
                labia_minora_right=LabiumMinus(
                    side=BodySide.LEFT
                )
            )

    def test_vulva_serialization(self):
        data = Vulva().to_dict()

        assert data["component_type"] == "vulva"
        assert (
            data["labia_majora_left"]["component_type"]
            == "labium_majus"
        )
        assert (
            data["clitoral"]["component_type"]
            == "clitoral_structure"
        )

    # --- Composizione ReproductiveSystem (6) ---

    def test_reproductive_system_defaults_empty(self):
        system = ReproductiveSystem()

        assert system.is_valid()
        assert system.component_type == "reproductive_system"
        assert system.male is None
        assert system.female is None

    def test_male_composition(self):
        system = ReproductiveSystem(
            male=MaleGenitalia(
                penis=Penis(length_flaccid=10.0),
                scrotum=Scrotum(),
            )
        )

        assert system.is_valid()
        assert system.male.penis.length_flaccid == 10.0
        assert system.female is None

    def test_female_composition(self):
        system = ReproductiveSystem(
            female=FemaleGenitalia(vulva=Vulva())
        )

        assert system.is_valid()
        assert system.male is None
        assert system.female.vulva.is_valid()

    def test_both_coexist(self):
        system = ReproductiveSystem(
            male=MaleGenitalia(),
            female=FemaleGenitalia(),
        )

        assert system.is_valid()

    def test_reproductive_rejects_wrong_types(self):
        with pytest.raises(ValueError, match="male must be"):
            ReproductiveSystem(male="male")

        with pytest.raises(ValueError, match="female must be"):
            ReproductiveSystem(female="female")

        with pytest.raises(ValueError, match="penis must be"):
            MaleGenitalia(penis="organ")

        with pytest.raises(ValueError, match="vulva must be"):
            FemaleGenitalia(vulva="organ")

    def test_reproductive_serialization_none_handling(self):
        data = ReproductiveSystem(
            male=MaleGenitalia()
        ).to_dict()

        assert data["male"]["component_type"] == "male_genitalia"
        assert data["female"] is None

    # --- HumanAnatomy integration (5) ---

    def test_anatomy_has_empty_reproductive_default(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()
        assert isinstance(
            anatomy.reproductive_system, ReproductiveSystem
        )
        assert anatomy.reproductive_system.male is None
        assert anatomy.reproductive_system.female is None

    def test_anatomy_male_composition(self):
        anatomy = HumanAnatomy(
            reproductive_system=ReproductiveSystem(
                male=MaleGenitalia(
                    penis=Penis(length_flaccid=11.0)
                )
            )
        )

        assert (
            anatomy.reproductive_system.male.penis.length_flaccid
            == 11.0
        )
        assert anatomy.is_valid()

    def test_anatomy_serialization(self):
        anatomy = HumanAnatomy(
            reproductive_system=ReproductiveSystem(
                female=FemaleGenitalia()
            )
        )
        data = anatomy.to_dict()

        assert data["reproductive_system"]["female"][
            "vulva"
        ]["component_type"] == "vulva"
        assert data["reproductive_system"]["male"] is None

    def test_anatomy_deep_mutation_invalidates(self):
        anatomy = HumanAnatomy(
            reproductive_system=ReproductiveSystem(
                male=MaleGenitalia()
            )
        )

        assert anatomy.is_valid()

        anatomy.reproductive_system.male.penis.girth_erect = 0.0
        assert not anatomy.is_valid()

    def test_anatomy_backward_compatible(self):
        anatomy = HumanAnatomy()

        assert anatomy.is_valid()
        assert anatomy.reproductive_system is not None

    # --- export (3) ---

    def test_package_exports_h420(self):
        for name in (
            "MaleGenitalia",
            "Penis",
            "Scrotum",
            "Testicle",
            "FemaleGenitalia",
            "LabiumMajus",
            "LabiumMinus",
            "ClitoralStructure",
            "Vulva",
            "ReproductiveSystem",
        ):
            assert hasattr(anatomy_module, name)
            assert name in anatomy_module.__all__

    def test_all_components_valid(self):
        for component in (
            Testicle(side=BodySide.LEFT),
            Scrotum(),
            Penis(),
            MaleGenitalia(),
            LabiumMajus(side=BodySide.LEFT),
            LabiumMinus(side=BodySide.LEFT),
            ClitoralStructure(),
            Vulva(),
            FemaleGenitalia(),
            ReproductiveSystem(),
        ):
            assert isinstance(component, AnatomyComponent)
            assert component.is_valid()

    def test_asymmetry_is_anatomical_norm(self):
        # The project's bilateral standard applied where the
        # anatomy is bilateral by nature.
        scrotum = Scrotum(
            left=Testicle(side=BodySide.LEFT, hang=0.6),
            right=Testicle(side=BodySide.RIGHT, hang=0.4),
        )
        vulva = Vulva(
            labia_minora_left=LabiumMinus(
                side=BodySide.LEFT, width=1.4
            ),
            labia_minora_right=LabiumMinus(
                side=BodySide.RIGHT, width=1.0
            ),
        )

        assert scrotum.is_valid()
        assert vulva.is_valid()
        assert scrotum.left.hang != scrotum.right.hang
        assert (
            vulva.labia_minora_left.width
            != vulva.labia_minora_right.width
        )