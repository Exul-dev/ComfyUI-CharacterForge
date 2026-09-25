"""The Clothing Engine (Human Engine, H7).

The first RELATIONAL layer of CharacterForge: garments do not
describe the character — they describe WHAT COVERS him/her.
A glove knows it covers a hand. A jacket knows it covers
torso and arms.

- the VOCABULARY (H7-A): GarmentType, CoverageRegion,
  Garment — the building blocks;
- the COMPOSITION (H7-B): Outfit — a named collection of
  garments with coherence checking (conflicts detected,
  never rejected) and preset factories;
- the INTEGRATION (H7-C): registration on Human, coexistence
  with anatomy + appearance + aging.

Principle: complex underneath, simple on top.
"""

from .garment import (
    CoverageRegion,
    Garment,
    GarmentFit,
    GarmentLayer,
    GarmentMaterial,
    GarmentState,
    GarmentType,
)
from .outfit import (
    Outfit,
    OutfitPreset,
)

__all__ = [
    "GarmentType",
    "CoverageRegion",
    "GarmentLayer",
    "GarmentFit",
    "GarmentMaterial",
    "GarmentState",
    "Garment",
    "Outfit",
    "OutfitPreset",
]