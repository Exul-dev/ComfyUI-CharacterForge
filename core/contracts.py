"""
CharacterForge Domain Core
Schema Contracts
=======================

Contratti semantici per le tipologie di entità supportate
dal Domain Core.

I contratti definiscono il minimo necessario affinché un'entità
possa essere riconosciuta da CharacterForge.

Non contengono logica specifica degli Engine.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class EntityContract:
    """
    Contratto base per una tipologia di entità.

    Attributes:
        entity_type: identificatore stabile della tipologia.
        required_identity_properties: proprietà minime dell'identità.
        required_state_properties: proprietà minime dello stato.
        description: descrizione semantica del contratto.
    """

    entity_type: str
    required_identity_properties: frozenset[str] = field(default_factory=frozenset)
    required_state_properties: frozenset[str] = field(default_factory=frozenset)
    description: str = ""

    def __post_init__(self) -> None:
        if not self.entity_type:
            raise ValueError("entity_type must not be empty")

    def to_dict(self) -> dict[str, Any]:
        """Restituisce una rappresentazione serializzabile del contratto."""
        return {
            "entity_type": self.entity_type,
            "required_identity_properties": sorted(
                self.required_identity_properties
            ),
            "required_state_properties": sorted(
                self.required_state_properties
            ),
            "description": self.description,
        }


# Contratto generico di base.
ENTITY_CONTRACT = EntityContract(
    entity_type="entity",
    description="Generic CharacterForge entity.",
)


__all__ = [
    "EntityContract",
    "ENTITY_CONTRACT",
]
