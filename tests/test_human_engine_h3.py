import unittest

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
from human import Human
from human.base.semantic import SemanticComponent

from human.demographics import (
    HumanDemographics,
    DemographicComponent,
    Sex,
    BiologicalSex,
    SexCharacteristics,
    Gender,
    GenderIdentity,
    GenderExpression,
    Age,
    ChronologicalAge,
    DevelopmentalStage,
    ApparentAge,
    Ethnicity,
    PrimaryEthnicity,
    SecondaryEthnicity,
    Ancestry,
    AncestralRegion,
    AncestralComponents,
    PopulationTraits,
    PopulationGroup,
    TraitDistribution,
    PopulationCharacteristics,
)


class TestHumanEngineH3(unittest.TestCase):

    def test_demographic_component_inheritance(self):
        component = DemographicComponent()

        self.assertIsInstance(component, SemanticComponent)
        self.assertEqual(component.component_type, "demographic")

    def test_sex_hierarchy(self):
        sex = Sex()

        self.assertIsInstance(sex, DemographicComponent)
        self.assertIsInstance(sex.biological, BiologicalSex)
        self.assertIsInstance(
            sex.characteristics,
            SexCharacteristics,
        )

    def test_gender_hierarchy(self):
        gender = Gender()

        self.assertIsInstance(gender, DemographicComponent)
        self.assertIsInstance(
            gender.identity,
            GenderIdentity,
        )
        self.assertIsInstance(
            gender.expression,
            GenderExpression,
        )

    def test_age_hierarchy(self):
        age = Age()

        self.assertIsInstance(age, DemographicComponent)
        self.assertIsInstance(
            age.chronological,
            ChronologicalAge,
        )
        self.assertIsInstance(
            age.developmental_stage,
            DevelopmentalStage,
        )
        self.assertIsInstance(
            age.apparent,
            ApparentAge,
        )

        age.chronological.years = 39
        age.validate()

        self.assertEqual(
            age.chronological.years,
            39,
        )

    def test_ethnicity_hierarchy(self):
        ethnicity = Ethnicity()

        self.assertIsInstance(
            ethnicity,
            DemographicComponent,
        )
        self.assertIsInstance(
            ethnicity.primary,
            PrimaryEthnicity,
        )
        self.assertIsInstance(
            ethnicity.secondary,
            SecondaryEthnicity,
        )

    def test_ancestry_hierarchy(self):
        ancestry = Ancestry()

        self.assertIsInstance(
            ancestry,
            DemographicComponent,
        )
        self.assertIsInstance(
            ancestry.regions,
            AncestralComponents,
        )

        region = AncestralRegion(
            name="Test Region",
            proportion=0.5,
        )

        ancestry.regions.add(region)
        ancestry.validate()

        self.assertEqual(
            len(ancestry.regions.regions),
            1,
        )

    def test_population_traits_hierarchy(self):
        traits = PopulationTraits()

        self.assertIsInstance(
            traits,
            DemographicComponent,
        )
        self.assertIsInstance(
            traits.group,
            PopulationGroup,
        )
        self.assertIsInstance(
            traits.distribution,
            TraitDistribution,
        )
        self.assertIsInstance(
            traits.characteristics,
            PopulationCharacteristics,
        )

    def test_human_demographics_composition(self):
        demographics = HumanDemographics()

        self.assertIsInstance(
            demographics,
            SemanticComponent,
        )
        self.assertIsInstance(
            demographics.sex,
            Sex,
        )
        self.assertIsInstance(
            demographics.gender,
            Gender,
        )
        self.assertIsInstance(
            demographics.age,
            Age,
        )
        self.assertIsInstance(
            demographics.ethnicity,
            Ethnicity,
        )
        self.assertIsInstance(
            demographics.ancestry,
            Ancestry,
        )
        self.assertIsInstance(
            demographics.population_traits,
            PopulationTraits,
        )

        demographics.validate()

    def test_human_contains_demographics(self):
        human = Human(
            name="H3 Test Human",
        )

        self.assertIsInstance(
            human.demographics,
            HumanDemographics,
        )

        self.assertTrue(
            human.has_component("demographics")
        )

        self.assertIs(
            human.get_component("demographics"),
            human.demographics,
        )

    def test_human_demographics_serialization(self):
        human = Human(
            name="Serialization Test",
        )

        data = human.to_dict()

        self.assertIn(
            "human_engine",
            data,
        )

        components = data["human_engine"]["components"]

        self.assertIn(
            "demographics",
            components,
        )

        demographics = components["demographics"]

        self.assertEqual(
            demographics["component_type"],
            "human_demographics",
        )

        self.assertIn(
            "sex",
            demographics,
        )
        self.assertIn(
            "gender",
            demographics,
        )
        self.assertIn(
            "age",
            demographics,
        )
        self.assertIn(
            "ethnicity",
            demographics,
        )
        self.assertIn(
            "ancestry",
            demographics,
        )
        self.assertIn(
            "population_traits",
            demographics,
        )

    def test_invalid_age_is_rejected(self):
        age = Age()

        age.chronological.years = -1

        with self.assertRaises(ValueError):
            age.validate()

    def test_invalid_ancestry_proportion_is_rejected(self):
        with self.assertRaises(ValueError):
            AncestralRegion(
                name="Invalid Region",
                proportion=1.5,
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)



