"""
CharacterForge Domain Core
==========================

Primitive semantiche indipendenti da ComfyUI.
"""

from .entity import Entity
from .identity import Identity
from .state import State
from .variant import Variant
from .transformation import Transformation
from .metadata import Metadata

__all__ = [
    "Entity",
    "Identity",
    "State",
    "Variant",
    "Transformation",
    "Metadata",
]
