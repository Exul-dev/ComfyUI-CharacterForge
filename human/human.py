from __future__ import annotations

from typing import Any

from core.entity import Entity
from core.validation import validate_entity

from .base.semantic import SemanticComponent
from .identity.human_identity import HumanIdentity
from .demographics.human_demographics import HumanDemographics


class Human(Entity):
    """
    CharacterForge Human Engine root entity.

    Human is a real Domain Core Entity specialization.

    The Domain Core owns:
        - entity_id
        - core identity
        - state
        - variants
        - metadata

    The Human Engine owns typed semantic components:
        - human identity
        - demographics
        - anatomy
        - face
        - skin
        - hair
        - eyes
        - expression
        - pose
        - clothing
        - accessories
        - materials
        - condition
        - context
        - behavior
        - voice
        - measurements
        - relationships
        - variation
        - transformation
        - reference sheet

    Components are represented by real Python classes and are
    composed into Human rather than flattened into dictionaries.
    """

    HUMAN_ENTITY_TYPE = "human"

    def __init__(
        self,
        *,
        name: str = "",
        human_identity: HumanIdentity | None = None,
        demographics: HumanDemographics | None = None,
    ) -> None:
        # Domain Core remains authoritative.
        super().__init__()

        self.identity.entity_type = self.HUMAN_ENTITY_TYPE

        if name:
            self.identity.name = name

        # Human-specific identity layer.
        self.human_identity = (
            human_identity
            or HumanIdentity(name=name)
        )

        # Human demographic layer.
        self.demographics = (
            demographics
            or HumanDemographics()
        )

        # Registry of typed semantic components.
        self._components: dict[
            str,
            SemanticComponent,
        ] = {}

        self.register_component(
            "human_identity",
            self.human_identity,
        )

        self.register_component(
            "demographics",
            self.demographics,
        )

    def register_component(
        self,
        name: str,
        component: SemanticComponent,
    ) -> None:
        """
        Register a typed Human Engine component.

        Components must be actual CharacterForge semantic classes.
        Arbitrary dictionaries are not accepted.
        """

        if not name or not name.strip():
            raise ValueError(
                "component name must be non-empty"
            )

        if not isinstance(
            component,
            SemanticComponent,
        ):
            raise TypeError(
                "Human components must inherit from "
                "SemanticComponent"
            )

        if name in self._components:
            raise ValueError(
                f"Human component already registered: {name}"
            )

        self._components[name] = component

    def get_component(
        self,
        name: str,
    ) -> SemanticComponent:
        return self._components[name]

    def has_component(
        self,
        name: str,
    ) -> bool:
        return name in self._components

    def component_names(self) -> tuple[str, ...]:
        return tuple(sorted(self._components))

    def validate(self) -> None:
        """
        Validate both Domain Core and Human Engine layers.

        The existing Domain Core validator accepts the canonical
        serialized representation, so the Entity is converted to
        its Domain Core dictionary before validation.
        """

        # Domain Core validation.
        validate_entity(super().to_dict())

        # Human Engine validation.
        for component in self._components.values():
            component.validate()

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize Domain Core plus Human Engine layers.
        """

        data = super().to_dict()

        data["human_engine"] = {
            "engine": "human",
            "version": "1.0",
            "components": {
                name: component.to_dict()
                for name, component
                in self._components.items()
            },
        }

        return data

    def describe(self) -> dict[str, Any]:
        """
        Return a machine-readable description of this Human.
        """

        return {
            "entity_id": self.entity_id,
            "entity_type": self.identity.entity_type,
            "name": self.identity.name,
            "components": self.component_names(),
            "component_count": len(
                self._components
            ),
        }
