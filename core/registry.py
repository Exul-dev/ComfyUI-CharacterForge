"""
CharacterForge Domain Core
Entity Registry
================

Registry centrale dei contratti delle entità.

Il Registry non crea né modifica entità.
Mantiene esclusivamente la conoscenza dei contratti
semantici disponibili.
"""

from __future__ import annotations

from typing import Iterator

from .contracts import ENTITY_CONTRACT, EntityContract


class RegistryError(ValueError):
    """Errore relativo al registro delle entità."""


class EntityRegistry:
    """
    Registro dei contratti CharacterForge.

    Il registro è intenzionalmente semplice e deterministico.
    La stessa tipologia non può essere registrata due volte
    senza una sostituzione esplicita.
    """

    def __init__(self) -> None:
        self._contracts: dict[str, EntityContract] = {}

    def register(
        self,
        contract: EntityContract,
        *,
        replace: bool = False,
    ) -> EntityContract:
        """Registra un contratto."""
        entity_type = contract.entity_type

        if entity_type in self._contracts and not replace:
            raise RegistryError(
                f"Entity contract already registered: {entity_type}"
            )

        self._contracts[entity_type] = contract
        return contract

    def unregister(self, entity_type: str) -> EntityContract:
        """Rimuove e restituisce un contratto."""
        try:
            return self._contracts.pop(entity_type)
        except KeyError as exc:
            raise RegistryError(
                f"Entity contract not registered: {entity_type}"
            ) from exc

    def get(self, entity_type: str) -> EntityContract:
        """Restituisce il contratto richiesto."""
        try:
            return self._contracts[entity_type]
        except KeyError as exc:
            raise RegistryError(
                f"Entity contract not registered: {entity_type}"
            ) from exc

    def get_optional(
        self,
        entity_type: str,
    ) -> EntityContract | None:
        """Restituisce il contratto oppure None."""
        return self._contracts.get(entity_type)

    def contains(self, entity_type: str) -> bool:
        """Indica se il contratto è registrato."""
        return entity_type in self._contracts

    def clear(self) -> None:
        """Svuota il registro."""
        self._contracts.clear()

    def __len__(self) -> int:
        return len(self._contracts)

    def __iter__(self) -> Iterator[EntityContract]:
        return iter(self._contracts.values())

    def entity_types(self) -> tuple[str, ...]:
        """Restituisce le tipologie in ordine deterministico."""
        return tuple(sorted(self._contracts))

    def to_dict(self) -> dict[str, dict]:
        """Serializza tutti i contratti."""
        return {
            entity_type: self._contracts[entity_type].to_dict()
            for entity_type in self.entity_types()
        }


def create_default_registry() -> EntityRegistry:
    """
    Crea il Registry iniziale CharacterForge.

    Per ora viene registrato esclusivamente il contratto
    generico 'entity'. Gli Engine verranno aggiunti
    progressivamente nelle rispettive fasi della roadmap.
    """
    registry = EntityRegistry()
    registry.register(ENTITY_CONTRACT)
    return registry


DEFAULT_REGISTRY = create_default_registry()


__all__ = [
    "RegistryError",
    "EntityRegistry",
    "create_default_registry",
    "DEFAULT_REGISTRY",
]
