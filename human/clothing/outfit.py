"""Outfit model (Human Engine, H7-B — Clothing Engine).

An Outfit is a COMPOSED entity: a named collection of
garments treated as a unit. Its core capability is the
COHERENCE CHECK: which garments conflict with each other
(same region, same layer, same side), and which body regions
are left uncovered.

Design decisions:

- conflicts are DETECTED, never REJECTED: an incoherent
  outfit is representable (a costume, a mistake, a state).
  The conflicts() method exposes the information; the
  caller decides. The same "preset is a starting point,
  never a cage" principle of the whole project;
- uncovered_regions() is the bridge to everything below:
  it tells the appearance layer, the aging layer and the
  future generation compiler WHICH parts of the body are
  actually visible;
- presets (from_preset) are FACTORIES: named starting
  points that remain fully hand-tunable afterwards.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from ..base.semantic import SemanticComponent
from .garment import (
    CoverageRegion,
    Garment,
    GarmentLayer,
    GarmentMaterial,
    GarmentType,
)


class OutfitPreset(Enum):
    """Named outfit starting points."""

    CASUAL = "casual"
    FORMAL = "formal"
    SPORT = "sport"
    WINTER = "winter"
    SUMMER = "summer"
    BUSINESS = "business"


def _build_preset_garments(
    preset: OutfitPreset,
) -> list[Garment]:
    """Build the garment list for a named preset."""

    builders: dict[OutfitPreset, list[dict[str, Any]]] = {
        OutfitPreset.CASUAL: [
            {
                "name": "casual tee",
                "garment_type": GarmentType.TOP,
                "coverage": {
                    CoverageRegion.TORSO,
                    CoverageRegion.ARMS,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.COTTON,
                "color": "white",
            },
            {
                "name": "casual jeans",
                "garment_type": GarmentType.BOTTOM,
                "coverage": {
                    CoverageRegion.LEGS,
                    CoverageRegion.WAIST,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.DENIM,
                "color": "blue",
            },
            {
                "name": "casual sneakers",
                "garment_type": GarmentType.SHOES,
                "coverage": {
                    CoverageRegion.FEET,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.SYNTHETIC,
                "color": "white",
            },
        ],
        OutfitPreset.FORMAL: [
            {
                "name": "dress shirt",
                "garment_type": GarmentType.TOP,
                "coverage": {
                    CoverageRegion.TORSO,
                    CoverageRegion.ARMS,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.COTTON,
                "color": "white",
            },
            {
                "name": "suit trousers",
                "garment_type": GarmentType.BOTTOM,
                "coverage": {
                    CoverageRegion.LEGS,
                    CoverageRegion.WAIST,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.WOOL,
                "color": "navy",
            },
            {
                "name": "suit jacket",
                "garment_type": GarmentType.OUTERWEAR,
                "coverage": {
                    CoverageRegion.TORSO,
                    CoverageRegion.ARMS,
                },
                "layer": GarmentLayer.OUTER,
                "material": GarmentMaterial.WOOL,
                "color": "navy",
            },
            {
                "name": "derby shoes",
                "garment_type": GarmentType.SHOES,
                "coverage": {CoverageRegion.FEET},
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.LEATHER,
                "color": "brown",
            },
        ],
        OutfitPreset.SPORT: [
            {
                "name": "sport tee",
                "garment_type": GarmentType.TOP,
                "coverage": {
                    CoverageRegion.TORSO,
                    CoverageRegion.ARMS,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.SYNTHETIC,
                "color": "gray",
            },
            {
                "name": "sport shorts",
                "garment_type": GarmentType.BOTTOM,
                "coverage": {
                    CoverageRegion.LEGS,
                    CoverageRegion.WAIST,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.SYNTHETIC,
                "color": "black",
            },
        ],
        OutfitPreset.WINTER: [
            {
                "name": "thermal base",
                "garment_type": GarmentType.TOP,
                "coverage": {
                    CoverageRegion.TORSO,
                    CoverageRegion.ARMS,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.SYNTHETIC,
                "color": "black",
            },
            {
                "name": "wool sweater",
                "garment_type": GarmentType.TOP,
                "coverage": {
                    CoverageRegion.TORSO,
                    CoverageRegion.ARMS,
                },
                "layer": GarmentLayer.MID,
                "material": GarmentMaterial.WOOL,
                "color": "olive",
            },
            {
                "name": "insulated pants",
                "garment_type": GarmentType.BOTTOM,
                "coverage": {
                    CoverageRegion.LEGS,
                    CoverageRegion.WAIST,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.SYNTHETIC,
                "color": "gray",
            },
            {
                "name": "parka",
                "garment_type": GarmentType.OUTERWEAR,
                "coverage": {
                    CoverageRegion.TORSO,
                    CoverageRegion.ARMS,
                },
                "layer": GarmentLayer.OUTER,
                "material": GarmentMaterial.SYNTHETIC,
                "color": "olive",
            },
            {
                "name": "winter boots",
                "garment_type": GarmentType.SHOES,
                "coverage": {
                    CoverageRegion.FEET,
                    CoverageRegion.ANKLES,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.LEATHER,
                "color": "brown",
            },
            {
                "name": "wool scarf",
                "garment_type": GarmentType.SCARF,
                "coverage": {CoverageRegion.NECK},
                "layer": GarmentLayer.MID,
                "material": GarmentMaterial.WOOL,
                "color": "beige",
            },
        ],
        OutfitPreset.SUMMER: [
            {
                "name": "linen shirt",
                "garment_type": GarmentType.TOP,
                "coverage": {
                    CoverageRegion.TORSO,
                    CoverageRegion.ARMS,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.LINEN,
                "color": "beige",
            },
            {
                "name": "linen shorts",
                "garment_type": GarmentType.BOTTOM,
                "coverage": {
                    CoverageRegion.LEGS,
                    CoverageRegion.WAIST,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.LINEN,
                "color": "beige",
            },
            {
                "name": "sandals",
                "garment_type": GarmentType.SHOES,
                "coverage": {CoverageRegion.FEET},
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.LEATHER,
                "color": "brown",
            },
        ],
        OutfitPreset.BUSINESS: [
            {
                "name": "business shirt",
                "garment_type": GarmentType.TOP,
                "coverage": {
                    CoverageRegion.TORSO,
                    CoverageRegion.ARMS,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.COTTON,
                "color": "white",
            },
            {
                "name": "chinos",
                "garment_type": GarmentType.BOTTOM,
                "coverage": {
                    CoverageRegion.LEGS,
                    CoverageRegion.WAIST,
                },
                "layer": GarmentLayer.BASE,
                "material": GarmentMaterial.COTTON,
                "color": "beige",
            },
            {
                "name": "blazer",
                "garment_type": GarmentType.OUTERWEAR,
                "coverage": {
                    CoverageRegion.TORSO,
                    CoverageRegion.ARMS,
                },
                "layer": GarmentLayer.OUTER,
                "material": GarmentMaterial.WOOL,
                "color": "navy",
            },
            {
                "name": "belt",
                "garment_type": GarmentType.BELT,
                "coverage": {CoverageRegion.WAIST},
                "layer": GarmentLayer.MID,
                "material": GarmentMaterial.LEATHER,
                "color": "brown",
            },
        ],
    }

    return [
        Garment(**kwargs) for kwargs in builders[preset]
    ]


class Outfit(SemanticComponent):
    """A named collection of garments with coherence checking."""

    component_type = "outfit"

    def __init__(
        self,
        *,
        name: str = "untitled outfit",
        garments: list[Garment] | None = None,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.name = str(name)
        self.garments: list[Garment] = list(garments or [])

        self.validate()

    @classmethod
    def from_preset(
        cls,
        preset: OutfitPreset,
        name: str | None = None,
        **garment_overrides: Any,
    ) -> "Outfit":
        """Build an Outfit from a named preset.

        The preset is a starting point: every garment can be
        replaced, removed or tuned afterwards.
        """

        if not isinstance(preset, OutfitPreset):
            raise ValueError(
                "Outfit.from_preset preset must be an OutfitPreset."
            )

        garments = _build_preset_garments(preset)

        outfit_name = (
            name if name is not None else f"preset: {preset.value}"
        )

        return cls(name=outfit_name, garments=garments)

    def validate(self) -> None:
        super().validate()

        if not self.name.strip():
            raise ValueError(
                "Outfit name must not be empty."
            )

        seen_names: list[str] = []

        for garment in self.garments:
            if not isinstance(garment, Garment):
                raise ValueError(
                    "Outfit garments must be Garment instances."
                )

            garment.validate()

            if garment.name in seen_names:
                raise ValueError(
                    f"Outfit contains duplicate garment name: "
                    f"{garment.name!r}."
                )

            seen_names.append(garment.name)

    def add(self, garment: Garment) -> Garment:
        """Add a garment (atomic: rejected add leaves no trace).

        The garment is appended only after the resulting list
        passes validation: a rejected add never leaves the
        outfit in a dirty state.
        """

        if not isinstance(garment, Garment):
            raise ValueError(
                "Outfit garments must be Garment instances."
            )

        self.garments.append(garment)

        try:
            self.validate()
        except ValueError:
            self.garments.pop()
            raise

        return garment

    def remove(self, garment_name: str) -> Garment | None:
        """Remove a garment by name, if present."""

        for index, garment in enumerate(self.garments):
            if garment.name == garment_name:
                return self.garments.pop(index)

        return None

    def get(self, garment_name: str) -> Garment | None:
        """Return a garment by name, if present."""

        for garment in self.garments:
            if garment.name == garment_name:
                return garment

        return None

    @staticmethod
    def conflicting(
        garment_a: Garment,
        garment_b: Garment,
    ) -> bool:
        """Return True if two garments conflict.

        Conflict: same region, same layer, same side. A
        t-shirt (base) and a jacket (outer) on TORSO do NOT
        conflict — they stack. Two base-layer tops DO.
        """

        if garment_a.layer is not garment_b.layer:
            return False

        if garment_a.side != garment_b.side:
            return False

        return bool(
            garment_a.coverage & garment_b.coverage
        )

    def conflicts(self) -> list[tuple[Garment, Garment]]:
        """All conflicting pairs in the outfit."""

        pairs: list[tuple[Garment, Garment]] = []

        for i, garment_a in enumerate(self.garments):
            for garment_b in self.garments[i + 1 :]:
                if self.conflicting(garment_a, garment_b):
                    pairs.append((garment_a, garment_b))

        return pairs

    def covered_regions(self) -> set[CoverageRegion]:
        """The union of all regions covered by the outfit."""

        covered: set[CoverageRegion] = set()

        for garment in self.garments:
            covered |= garment.coverage

        return covered

    def uncovered_regions(self) -> set[CoverageRegion]:
        """The body regions left uncovered by the outfit."""

        return set(CoverageRegion) - self.covered_regions()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "name": self.name,
            "garments": [
                garment.to_dict() for garment in self.garments
            ],
        }
