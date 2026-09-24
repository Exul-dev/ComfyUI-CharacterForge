"""
Metadata
========

Metadati tecnici, schema e provenienza.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class Metadata:
    """Technical and provenance metadata for a domain object."""

    schema_version: str = "1.0"
    source: str = "characterforge"
    provenance: dict[str, Any] = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self) -> dict[str, Any]:
        """Return a plain serializable representation."""
        return {
            "schema_version": self.schema_version,
            "source": self.source,
            "provenance": self.provenance,
            "tags": self.tags,
            "created_at": self.created_at,
        }
