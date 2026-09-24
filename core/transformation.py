"""
Transformation
==============

Trasformazione controllata tra configurazioni semantiche.
"""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass
class Transformation:
    """Controlled transformation between entity configurations."""

    transformation_id: str = field(
        default_factory=lambda: f"transformation_{uuid4().hex}"
    )
    source_entity_id: str = ""
    source_state_id: str = ""
    target_state_id: str = ""
    operations: list[dict[str, Any]] = field(default_factory=list)
    reversible: bool = False
    preserves_identity: bool = True
    version: int = 1

    def to_dict(self) -> dict[str, Any]:
        """Return a plain serializable representation."""
        return {
            "transformation_id": self.transformation_id,
            "source_entity_id": self.source_entity_id,
            "source_state_id": self.source_state_id,
            "target_state_id": self.target_state_id,
            "operations": self.operations,
            "reversible": self.reversible,
            "preserves_identity": self.preserves_identity,
            "version": self.version,
        }
