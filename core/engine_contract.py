"""
CharacterForge Domain Core
Engine Contract
================

Contratto comune per tutti gli Engine semantici CharacterForge.

Gli Engine concreti potranno implementare Human, Creature,
Object, Nature, Environment, Camera, Transformation e
Reference Sheet senza modificare il Domain Core.

Il contratto non contiene logica di generazione immagini.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from .contracts import EntityContract


class EngineContractError(ValueError):
    """Errore relativo a un Engine Contract."""


class EngineContract(ABC):
    """
    Interfaccia base per un CharacterForge Engine.

    Ogni Engine deve:
    - avere un identificatore stabile;
    - dichiarare il proprio entity_type;
    - fornire il relativo EntityContract;
    - poter validare una configurazione;
    - poter costruire un payload semantico.
    """

    engine_id: str = ""
    entity_type: str = ""

    def __init__(self) -> None:
        if not self.engine_id:
            raise EngineContractError(
                f"{type(self).__name__} must define engine_id"
            )

        if not self.entity_type:
            raise EngineContractError(
                f"{type(self).__name__} must define entity_type"
            )

    @property
    @abstractmethod
    def contract(self) -> EntityContract:
        """Restituisce il contratto dell'entità gestita."""
        raise NotImplementedError

    @abstractmethod
    def validate_config(self, config: dict[str, Any]) -> None:
        """
        Valida una configurazione semantica dell'Engine.

        Deve sollevare EngineContractError quando la configurazione
        non rispetta il contratto.
        """
        raise NotImplementedError

    @abstractmethod
    def build_payload(self, config: dict[str, Any]) -> dict[str, Any]:
        """
        Costruisce il payload semantico dell'Engine.

        Il risultato deve essere un dizionario serializzabile.
        """
        raise NotImplementedError

    def describe(self) -> dict[str, Any]:
        """Restituisce i metadati pubblici dell'Engine."""
        return {
            "engine_id": self.engine_id,
            "entity_type": self.entity_type,
            "contract": self.contract.to_dict(),
        }


__all__ = [
    "EngineContract",
    "EngineContractError",
]
