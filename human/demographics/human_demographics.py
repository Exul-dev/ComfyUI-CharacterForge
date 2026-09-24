from __future__ import annotations

from typing import Any

from ..base.semantic import SemanticComponent
from .sex import Sex
from .gender import Gender
from .age import Age
from .ethnicity import Ethnicity
from .ancestry import Ancestry
from .population_traits import PopulationTraits


class HumanDemographics(SemanticComponent):
    """
    Complete demographic layer of a Human.

    All demographic concepts are represented by typed Python objects.
    """

    component_type = "human_demographics"

    def __init__(
        self,
        *,
        sex: Sex | None = None,
        gender: Gender | None = None,
        age: Age | None = None,
        ethnicity: Ethnicity | None = None,
        ancestry: Ancestry | None = None,
        population_traits: PopulationTraits | None = None,
    ) -> None:
        super().__init__()

        self.sex = sex or Sex()
        self.gender = gender or Gender()
        self.age = age or Age()
        self.ethnicity = ethnicity or Ethnicity()
        self.ancestry = ancestry or Ancestry()
        self.population_traits = (
            population_traits or PopulationTraits()
        )

    def validate(self) -> None:
        super().validate()

        self.sex.validate()
        self.gender.validate()
        self.age.validate()
        self.ethnicity.validate()
        self.ancestry.validate()
        self.population_traits.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "sex": self.sex.to_dict(),
            "gender": self.gender.to_dict(),
            "age": self.age.to_dict(),
            "ethnicity": self.ethnicity.to_dict(),
            "ancestry": self.ancestry.to_dict(),
            "population_traits": (
                self.population_traits.to_dict()
            ),
        }
