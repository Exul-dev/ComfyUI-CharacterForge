from __future__ import annotations

from typing import Any

from .demographic_component import DemographicComponent


class BiologicalSex(DemographicComponent):
    """
    Biological sex classification used by the Human Engine.

    This is deliberately represented as semantic data rather than
    hard-coded into anatomy or gender.
    """

    component_type = "biological_sex"

    VALID_VALUES = (
        "female",
        "male",
        "intersex",
        "unspecified",
    )

    def __init__(self, value: str = "unspecified") -> None:
        super().__init__()

        if value not in self.VALID_VALUES:
            raise ValueError(
                f"Invalid biological sex: {value!r}"
            )

        self.value = value

    def validate(self) -> None:
        super().validate()

        if self.value not in self.VALID_VALUES:
            raise ValueError(
                f"Invalid biological sex: {self.value!r}"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "value": self.value,
        }


class SexCharacteristics(DemographicComponent):
    """
    Additional semantic characteristics associated with sex.

    The model intentionally remains extensible rather than forcing
    anatomy into this component.
    """

    component_type = "sex_characteristics"

    def __init__(
        self,
        characteristics: dict[str, Any] | None = None,
    ) -> None:
        super().__init__()
        self.characteristics = characteristics or {}

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.characteristics, dict):
            raise ValueError(
                "characteristics must be a dictionary"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "characteristics": dict(self.characteristics),
        }


class Sex(DemographicComponent):
    """
    Complete Human sex component.
    """

    component_type = "sex"

    def __init__(
        self,
        *,
        biological: BiologicalSex | None = None,
        characteristics: SexCharacteristics | None = None,
    ) -> None:
        super().__init__()

        self.biological = biological or BiologicalSex()
        self.characteristics = (
            characteristics or SexCharacteristics()
        )

    def validate(self) -> None:
        super().validate()
        self.biological.validate()
        self.characteristics.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "biological": self.biological.to_dict(),
            "characteristics": self.characteristics.to_dict(),
        }
