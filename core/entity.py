"""
Entity
======

Entità semantica base di CharacterForge.
"""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from .identity import Identity
from .metadata import Metadata
from .state import State
from .variant import Variant


@dataclass
class Entity:
    """Base semantic entity shared by all CharacterForge engines."""

    entity_id: str = field(
        default_factory=lambda: f"entity_{uuid4().hex}"
    )
    identity: Identity = field(default_factory=Identity)
    state: State | None = None
    variants: dict[str, Variant] = field(default_factory=dict)
    metadata: Metadata = field(default_factory=Metadata)

    def __post_init__(self) -> None:
        """Ensure identity and state refer to this entity."""
        if not self.identity.entity_type:
            self.identity.entity_type = "entity"

        if self.state is None:
            self.state = State(entity_id=self.entity_id)
        elif not self.state.entity_id:
            self.state.entity_id = self.entity_id

    def add_variant(self, variant: Variant) -> None:
        """Register a controlled variant."""
        if variant.source_entity_id and variant.source_entity_id != self.entity_id:
            raise ValueError(
                "Variant source_entity_id does not match this entity."
            )

        if not variant.source_entity_id:
            variant.source_entity_id = self.entity_id

        if variant.variant_id in self.variants:
            raise ValueError(
                f"Variant already exists: {variant.variant_id}"
            )

        self.variants[variant.variant_id] = variant

    def get_variant(self, variant_id: str) -> Variant:
        """Return a registered variant."""
        try:
            return self.variants[variant_id]
        except KeyError as exc:
            raise KeyError(
                f"Unknown variant: {variant_id}"
            ) from exc

    def to_dict(self) -> dict[str, Any]:
        """Return a complete plain representation."""
        return {
            "entity_id": self.entity_id,
            "identity": self.identity.to_dict(),
            "state": self.state.to_dict() if self.state else None,
            "variants": {
                key: value.to_dict()
                for key, value in self.variants.items()
            },
            "metadata": self.metadata.to_dict(),
        }
