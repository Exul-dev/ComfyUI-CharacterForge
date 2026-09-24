from __future__ import annotations

from typing import Any

from .demographic_component import DemographicComponent


class PopulationGroup(DemographicComponent):
    """
    Population grouping used as a semantic reference.

    It is not treated as an identity anchor by default.
    """

    component_type = "population_group"

    def __init__(
        self,
        name: str = "unspecified",
    ) -> None:
        super().__init__()

        if not name or not name.strip():
            raise ValueError(
                "Population group cannot be empty"
            )

        self.name = name

    def validate(self) -> None:
        super().validate()

        if not self.name.strip():
            raise ValueError(
                "Population group cannot be empty"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "name": self.name,
        }


class TraitDistribution(DemographicComponent):
    """
    Statistical/probabilistic population trait descriptor.

    This is metadata for generation, not a deterministic rule
    about an individual.
    """

    component_type = "trait_distribution"

    def __init__(
        self,
        traits: dict[str, float] | None = None,
    ) -> None:
        super().__init__()
        self.traits = dict(traits or {})

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.traits, dict):
            raise ValueError(
                "traits must be a dictionary"
            )

        for name, probability in self.traits.items():
            if not isinstance(name, str) or not name.strip():
                raise ValueError(
                    "Trait names must be non-empty strings"
                )

            if not 0.0 <= probability <= 1.0:
                raise ValueError(
                    "Trait probabilities must be between 0 and 1"
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "traits": dict(self.traits),
        }


class PopulationCharacteristics(DemographicComponent):
    """
    Additional population-level characteristics.
    """

    component_type = "population_characteristics"

    def __init__(
        self,
        characteristics: dict[str, Any] | None = None,
    ) -> None:
        super().__init__()

        self.characteristics = dict(
            characteristics or {}
        )

    def validate(self) -> None:
        super().validate()

        if not isinstance(
            self.characteristics,
            dict,
        ):
            raise ValueError(
                "characteristics must be a dictionary"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "characteristics": dict(
                self.characteristics
            ),
        }


class PopulationTraits(DemographicComponent):
    """
    Complete population-traits model.
    """

    component_type = "population_traits"

    def __init__(
        self,
        *,
        group: PopulationGroup | None = None,
        distribution: TraitDistribution | None = None,
        characteristics: PopulationCharacteristics | None = None,
    ) -> None:
        super().__init__()

        self.group = (
            group or PopulationGroup()
        )

        self.distribution = (
            distribution or TraitDistribution()
        )

        self.characteristics = (
            characteristics
            or PopulationCharacteristics()
        )

    def validate(self) -> None:
        super().validate()

        self.group.validate()
        self.distribution.validate()
        self.characteristics.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "group": self.group.to_dict(),
            "distribution": self.distribution.to_dict(),
            "characteristics": (
                self.characteristics.to_dict()
            ),
        }
