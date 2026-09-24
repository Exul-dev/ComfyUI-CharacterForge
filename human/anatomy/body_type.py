from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class BodyType(AnatomyComponent):
    """Semantic representation of overall human body type."""

    component_type = "body_type"

    def __init__(self, value: str = "average") -> None:
        super().__init__()

        if not value or not value.strip():
            raise ValueError("Body type cannot be empty")

        self.value = value

    def validate(self) -> None:
        super().validate()

        if not self.value.strip():
            raise ValueError("Body type cannot be empty")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "value": self.value,
        }


class Height(AnatomyComponent):
    """Human height represented in centimeters."""

    component_type = "height"

    def __init__(self, centimeters: float = 170.0) -> None:
        super().__init__()

        centimeters = float(centimeters)

        if centimeters <= 0:
            raise ValueError("Height must be greater than zero")

        self.centimeters = centimeters

    def validate(self) -> None:
        super().validate()

        if self.centimeters <= 0:
            raise ValueError("Height must be greater than zero")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "centimeters": self.centimeters,
        }


class Proportions(AnatomyComponent):
    """Relative anatomical proportions of the human body."""

    component_type = "proportions"

    def __init__(
        self,
        *,
        head_to_body: float = 7.5,
        shoulder_width: float = 1.0,
        torso_length: float = 1.0,
        arm_length: float = 1.0,
        leg_length: float = 1.0,
    ) -> None:
        super().__init__()

        self.head_to_body = float(head_to_body)
        self.shoulder_width = float(shoulder_width)
        self.torso_length = float(torso_length)
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)

        self.validate()

    def validate(self) -> None:
        super().validate()

        values = {
            "head_to_body": self.head_to_body,
            "shoulder_width": self.shoulder_width,
            "torso_length": self.torso_length,
            "arm_length": self.arm_length,
            "leg_length": self.leg_length,
        }

        for name, value in values.items():
            if value <= 0:
                raise ValueError(f"{name} must be greater than zero")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "head_to_body": self.head_to_body,
            "shoulder_width": self.shoulder_width,
            "torso_length": self.torso_length,
            "arm_length": self.arm_length,
            "leg_length": self.leg_length,
        }
