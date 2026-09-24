from __future__ import annotations

from typing import Any

from ..base.semantic import SemanticComponent


class IdentityPersistence(SemanticComponent):
    """
    Controls how strongly identity-defining properties are preserved
    across variants, transformations and generated views.
    """

    component_type = "identity_persistence"

    def __init__(
        self,
        *,
        enabled: bool = True,
        strength: float = 1.0,
        preserve_face: bool = True,
        preserve_body: bool = True,
        preserve_hair: bool = True,
        preserve_skin: bool = True,
        preserve_distinctive_traits: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        if not 0.0 <= strength <= 1.0:
            raise ValueError("strength must be between 0 and 1")

        self.strength = float(strength)
        self.preserve_face = bool(preserve_face)
        self.preserve_body = bool(preserve_body)
        self.preserve_hair = bool(preserve_hair)
        self.preserve_skin = bool(preserve_skin)
        self.preserve_distinctive_traits = bool(
            preserve_distinctive_traits
        )

    def validate(self) -> None:
        super().validate()

        if not 0.0 <= self.strength <= 1.0:
            raise ValueError("strength must be between 0 and 1")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "strength": self.strength,
            "preserve_face": self.preserve_face,
            "preserve_body": self.preserve_body,
            "preserve_hair": self.preserve_hair,
            "preserve_skin": self.preserve_skin,
            "preserve_distinctive_traits": (
                self.preserve_distinctive_traits
            ),
        }
