from .human import Human

from .base import (
    CharacterForgeObject,
    Identifiable,
    Serializable,
    Validatable,
    SemanticComponent,
    Variantable,
    Transformable,
    Reproducible,
)

from .identity import (
    IdentityAnchor,
    IdentityAnchors,
    DistinctiveTrait,
    DistinctiveTraits,
    IdentityPersistence,
    HumanIdentity,
)

__all__ = [
    "Human",

    "CharacterForgeObject",
    "Identifiable",
    "Serializable",
    "Validatable",
    "SemanticComponent",
    "Variantable",
    "Transformable",
    "Reproducible",

    "IdentityAnchor",
    "IdentityAnchors",
    "DistinctiveTrait",
    "DistinctiveTraits",
    "IdentityPersistence",
    "HumanIdentity",
]
