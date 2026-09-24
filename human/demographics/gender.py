from __future__ import annotations

from typing import Any

from .demographic_component import DemographicComponent


class GenderIdentity(DemographicComponent):
    """
    Gender identity semantic component.
    """

    component_type = "gender_identity"

    def __init__(
        self,
        value: str = "unspecified",
    ) -> None:
        super().__init__()

        if not value or not value.strip():
            raise ValueError(
                "Gender identity cannot be empty"
            )

        self.value = value

    def validate(self) -> None:
        super().validate()

        if not self.value.strip():
            raise ValueError(
                "Gender identity cannot be empty"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "value": self.value,
        }


class GenderExpression(DemographicComponent):
    """
    Gender expression represented independently from gender identity.
    """

    component_type = "gender_expression"

    def __init__(
        self,
        value: str = "unspecified",
    ) -> None:
        super().__init__()

        if not value or not value.strip():
            raise ValueError(
                "Gender expression cannot be empty"
            )

        self.value = value

    def validate(self) -> None:
        super().validate()

        if not self.value.strip():
            raise ValueError(
                "Gender expression cannot be empty"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "value": self.value,
        }


class Gender(DemographicComponent):
    """
    Complete Human gender component.
    """

    component_type = "gender"

    def __init__(
        self,
        *,
        identity: GenderIdentity | None = None,
        expression: GenderExpression | None = None,
    ) -> None:
        super().__init__()

        self.identity = identity or GenderIdentity()
        self.expression = expression or GenderExpression()

    def validate(self) -> None:
        super().validate()
        self.identity.validate()
        self.expression.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "identity": self.identity.to_dict(),
            "expression": self.expression.to_dict(),
        }
