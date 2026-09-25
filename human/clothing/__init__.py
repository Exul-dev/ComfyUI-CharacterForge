"""The Clothing Engine (Human Engine, H7).

The first RELATIONAL layer of CharacterForge: garments do not
describe the character — they describe WHAT COVERS him/her.
A glove knows it covers a hand. A jacket knows it covers
torso and arms. This is the architectural novelty of H7:
the coverage regions hook into the anatomy that already
exists, creating the first cross-layer relationship
(garment → body region → anatomical component).

Layers of the engine (built progressively):

- the VOCABULARY (H7-A): GarmentType, CoverageRegion,
  Garment — the building blocks;
- the COMPOSITION (H7-B): Outfit — a collection of garments
  with documented soft coherence rules;
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

__all__ = [
    "GarmentType",
    "CoverageRegion",
    "GarmentLayer",
    "GarmentFit",
    "GarmentMaterial",
    "GarmentState",
    "Garment",
]