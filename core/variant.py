"""
Variant
=======

Variazione controllata di un'entità senza necessariamente crearne
una nuova identità.
"""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass
class Variant:
    """Controlled variation derived from an entity."""

    variant_id: str = field(
        default_factory=lambda: f"variant_{uuid4().hex}"
    )
    source_entity_id: str = ""
    name: str = ""
    changes: dict[str, Any] = field(default_factory=dict)
    preserves_identity: bool = True
    version: int = 1

    def to_dict(self) -> dict[str, Any]:
        """Return a plain serializable representation."""
        return {
            "variant_id": self.variant_id,
            "source_entity_id": self.source_entity_id,
            "name": self.name,
            "changes": self.changes,
            "preserves_identity": self.preserves_identity,
            "version": self.version,
        }
