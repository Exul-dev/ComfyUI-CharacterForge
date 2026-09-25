"""Reproductive system (Human Engine, H4.20).

Architectural decision — COMPOSABILITY over hardcoding: the
system never deduces anatomy from Demographics.sex (the project
separates Sex from Gender by design). Male and female structures
are optional, independently configurable, and may coexist: the
configuration is always explicit.
"""

from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .female_genitalia import FemaleGenitalia
from .male_genitalia import MaleGenitalia


class ReproductiveSystem(AnatomyComponent):
    """Composable reproductive system.

    Empty by default: a fresh HumanAnatomy carries no hardcoded
    anatomy — the caller composes what the character requires.
    """

    component_type = "reproductive_system"

    def __init__(
        self,
        *,
        male: MaleGenitalia | None = None,
        female: FemaleGenitalia | None = None,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.male = male
        self.female = female

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.male is not None and not isinstance(
            self.male,
            MaleGenitalia,
        ):
            raise ValueError(
                "ReproductiveSystem male must be a "
                "MaleGenitalia instance or None."
            )

        if self.female is not None and not isinstance(
            self.female,
            FemaleGenitalia,
        ):
            raise ValueError(
                "ReproductiveSystem female must be a "
                "FemaleGenitalia instance or None."
            )

        if self.male is not None:
            self.male.validate()

        if self.female is not None:
            self.female.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "male": self.male.to_dict() if self.male else None,
            "female": (
                self.female.to_dict() if self.female else None
            ),
        }