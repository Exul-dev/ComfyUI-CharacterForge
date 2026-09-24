from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Musculature(AnatomyComponent):
    """Representation of overall muscular development."""

    component_type = "musculature"

    VALID_LEVELS = (
        "very_low",
        "low",
        "average",
        "high",
        "very_high",
    )

    def __init__(
        self,
        level: str = "average",
        *,
        definition: float = 0.5,
        distribution: str = "balanced",
    ) -> None:
        super().__init__()

        if level not in self.VALID_LEVELS:
            raise ValueError(f"Invalid musculature level: {level}")

        self.level = level
        self.definition = float(definition)
        self.distribution = distribution

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.level not in self.VALID_LEVELS:
            raise ValueError(f"Invalid musculature level: {self.level}")

        if not 0.0 <= self.definition <= 1.0:
            raise ValueError("Musculature definition must be between 0 and 1")

        if not self.distribution.strip():
            raise ValueError("Musculature distribution cannot be empty")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "level": self.level,
            "definition": self.definition,
            "distribution": self.distribution,
        }
