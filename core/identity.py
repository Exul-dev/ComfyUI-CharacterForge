"""
Identity
========

Identità persistente di un'entità CharacterForge.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


@dataclass
class Identity:
    """Stable semantic identity of a CharacterForge entity."""

    identity_id: str = field(
        default_factory=lambda: f"identity_{uuid4().hex}"
    )
    name: str = ""
    entity_type: str = ""
    anchors: dict[str, Any] = field(default_factory=dict)
    identity_properties: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    version: int = 1

    def to_dict(self) -> dict[str, Any]:
        """Return a deterministic-friendly plain representation."""
        return {
            "identity_id": self.identity_id,
            "name": self.name,
            "entity_type": self.entity_type,
            "anchors": self.anchors,
            "identity_properties": self.identity_properties,
            "created_at": self.created_at,
            "version": self.version,
        }
