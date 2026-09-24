from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class BodyFat(AnatomyComponent):
    """Representation of body-fat level and distribution."""

    component_type = "body_fat"

    def __init__(
        self,
        percentage: float = 20.0,
        *,
        distribution: str = "balanced",
    ) -> None:
        super().__init__()

        self.percentage = float(percentage)
        self.distribution = distribution

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not 0.0 <= self.percentage <= 100.0:
            raise ValueError("Body fat percentage must be between 0 and 100")

        if not self.distribution.strip():
            raise ValueError("Body fat distribution cannot be empty")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "percentage": self.percentage,
            "distribution": self.distribution,
        }
