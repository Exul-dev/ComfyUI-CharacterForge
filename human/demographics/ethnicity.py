from __future__ import annotations

from typing import Any

from .demographic_component import DemographicComponent


class PrimaryEthnicity(DemographicComponent):
    """
    Primary ethnicity descriptor.

    The semantic value remains registry-driven rather than being
    hard-coded to a closed worldwide classification.
    """

    component_type = "primary_ethnicity"

    def __init__(
        self,
        value: str = "unspecified",
    ) -> None:
        super().__init__()

        if not value or not value.strip():
            raise ValueError(
                "Primary ethnicity cannot be empty"
            )

        self.value = value

    def validate(self) -> None:
        super().validate()

        if not self.value.strip():
            raise ValueError(
                "Primary ethnicity cannot be empty"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "value": self.value,
        }


class SecondaryEthnicity(DemographicComponent):
    """
    Optional additional ethnicity descriptor.
    """

    component_type = "secondary_ethnicity"

    def __init__(
        self,
        values: list[str] | None = None,
    ) -> None:
        super().__init__()
        self.values = list(values or [])

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.values, list):
            raise ValueError(
                "Secondary ethnicity values must be a list"
            )

        for value in self.values:
            if not isinstance(value, str) or not value.strip():
                raise ValueError(
                    "Ethnicity values must be non-empty strings"
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "values": list(self.values),
        }


class Ethnicity(DemographicComponent):
    """
    Complete Human ethnicity model.
    """

    component_type = "ethnicity"

    def __init__(
        self,
        *,
        primary: PrimaryEthnicity | None = None,
        secondary: SecondaryEthnicity | None = None,
    ) -> None:
        super().__init__()

        self.primary = (
            primary or PrimaryEthnicity()
        )

        self.secondary = (
            secondary or SecondaryEthnicity()
        )

    def validate(self) -> None:
        super().validate()

        self.primary.validate()
        self.secondary.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "primary": self.primary.to_dict(),
            "secondary": self.secondary.to_dict(),
        }
