from __future__ import annotations

from typing import Any

from .demographic_component import DemographicComponent


class ChronologicalAge(DemographicComponent):
    """
    Chronological age in years.
    """

    component_type = "chronological_age"

    def __init__(self, years: float = 0.0) -> None:
        super().__init__()

        if years < 0:
            raise ValueError("Age cannot be negative")

        self.years = float(years)

    def validate(self) -> None:
        super().validate()

        if self.years < 0:
            raise ValueError("Age cannot be negative")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "years": self.years,
        }


class DevelopmentalStage(DemographicComponent):
    """
    Semantic developmental stage.

    This is intentionally independent from apparent age.
    """

    component_type = "developmental_stage"

    VALID_VALUES = (
        "prenatal",
        "infant",
        "child",
        "adolescent",
        "young_adult",
        "adult",
        "middle_aged_adult",
        "older_adult",
        "unspecified",
    )

    def __init__(
        self,
        value: str = "unspecified",
    ) -> None:
        super().__init__()

        if value not in self.VALID_VALUES:
            raise ValueError(
                f"Invalid developmental stage: {value!r}"
            )

        self.value = value

    def validate(self) -> None:
        super().validate()

        if self.value not in self.VALID_VALUES:
            raise ValueError(
                f"Invalid developmental stage: {self.value!r}"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "value": self.value,
        }


class ApparentAge(DemographicComponent):
    """
    Perceived visual age used for generation.

    It is deliberately separate from chronological age.
    """

    component_type = "apparent_age"

    def __init__(
        self,
        years: float | None = None,
    ) -> None:
        super().__init__()

        if years is not None and years < 0:
            raise ValueError(
                "Apparent age cannot be negative"
            )

        self.years = (
            None if years is None else float(years)
        )

    def validate(self) -> None:
        super().validate()

        if self.years is not None and self.years < 0:
            raise ValueError(
                "Apparent age cannot be negative"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "years": self.years,
        }


class Age(DemographicComponent):
    """
    Complete Human age model.
    """

    component_type = "age"

    def __init__(
        self,
        *,
        chronological: ChronologicalAge | None = None,
        developmental_stage: DevelopmentalStage | None = None,
        apparent: ApparentAge | None = None,
    ) -> None:
        super().__init__()

        self.chronological = (
            chronological or ChronologicalAge()
        )

        self.developmental_stage = (
            developmental_stage or DevelopmentalStage()
        )

        self.apparent = apparent or ApparentAge()

    def validate(self) -> None:
        super().validate()

        self.chronological.validate()
        self.developmental_stage.validate()
        self.apparent.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "chronological": self.chronological.to_dict(),
            "developmental_stage": (
                self.developmental_stage.to_dict()
            ),
            "apparent": self.apparent.to_dict(),
        }
