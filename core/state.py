"""
State
=====

Stato corrente di un'entità CharacterForge.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


@dataclass
class State:
    """Current semantic configuration of an entity."""

    state_id: str = field(
        default_factory=lambda: f"state_{uuid4().hex}"
    )
    entity_id: str = ""
    properties: dict[str, Any] = field(default_factory=dict)
    active_variant_id: str | None = None
    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    version: int = 1

    def to_dict(self) -> dict[str, Any]:
        """Return a plain serializable representation."""
        return {
            "state_id": self.state_id,
            "entity_id": self.entity_id,
            "properties": self.properties,
            "active_variant_id": self.active_variant_id,
            "timestamp": self.timestamp,
            "version": self.version,
        }
