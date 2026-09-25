"""Garment model (Human Engine, H7-A — Clothing Engine).

A Garment is the atomic unit of clothing: one item that
covers one or more body regions. The coverage is the
RELATIONAL core: it hooks into the anatomical vocabulary,
not into free-text descriptions.

Design decisions:

- CoverageRegion mirrors the body-region vocabulary used by
  BodyHairRegion (H5-D-3) and the anatomical components:
  the garment layer SPEAKS the body's language;
- GarmentLayer (base / mid / outer) enables stacking: a
  t-shirt (base) under a sweater (mid) under a jacket
  (outer) — all covering TORSO;
- Bilateral garments (gloves, socks, shoes) carry an
  optional side: None = the garment covers both sides
  (or the category doesn't have sides);
- State (new / worn / damaged / dirty) is structural, not
  a dynamic concern: it describes the CURRENT condition;
- The material is semantic (fabric type), not a physical
  simulation — the same philosophy as everything else.
"""

from __future__ import annotations

import math
from enum import Enum
from typing import Any

from ..base.semantic import SemanticComponent


class GarmentType(Enum):
    """The semantic categories of garments."""

    HAT = "hat"
    SCARF = "scarf"
    TOP = "top"
    BOTTOM = "bottom"
    FULL_BODY = "full_body"
    OUTERWEAR = "outerwear"
    GLOVES = "gloves"
    SOCKS = "socks"
    SHOES = "shoes"
    BELT = "belt"
    ACCESSORY = "accessory"


class CoverageRegion(Enum):
    """The body regions a garment can cover.

    This mirrors the anatomical vocabulary (aligned with
    BodyHairRegion of H5-D-3 and the anatomical components)
    so that the clothing layer speaks the body's language.
    """

    HEAD = "head"
    NECK = "neck"
    TORSO = "torso"
    ARMS = "arms"
    HANDS = "hands"
    WAIST = "waist"
    LEGS = "legs"
    FEET = "feet"
    ANKLES = "ankles"


class GarmentLayer(Enum):
    """The stacking layer of a garment."""

    BASE = "base"
    MID = "mid"
    OUTER = "outer"


class GarmentFit(Enum):
    """How the garment fits the body."""

    TIGHT = "tight"
    REGULAR = "regular"
    LOOSE = "loose"
    OVERSIZED = "oversized"


class GarmentMaterial(Enum):
    """The semantic fabric type."""

    COTTON = "cotton"
    WOOL = "wool"
    SILK = "silk"
    LINEN = "linen"
    LEATHER = "leather"
    DENIM = "denim"
    SYNTHETIC = "synthetic"
    KNIT = "knit"
    SUEDE = "suede"
    MIXED = "mixed"


class GarmentState(Enum):
    """The current condition of the garment."""

    NEW = "new"
    WORN = "worn"
    DAMAGED = "damaged"
    DIRTY = "dirty"


class Garment(SemanticComponent):
    """One garment item covering one or more body regions."""

    component_type = "garment"

    VALID_COLORS = (
        "black",
        "white",
        "gray",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "pink",
        "brown",
        "beige",
        "navy",
        "olive",
    )

    def __init__(
        self,
        *,
        name: str,
        garment_type: GarmentType,
        coverage: set[CoverageRegion],
        layer: GarmentLayer = GarmentLayer.BASE,
        fit: GarmentFit = GarmentFit.REGULAR,
        material: GarmentMaterial = GarmentMaterial.COTTON,
        color: str = "black",
        color_hex: str | None = None,
        state: GarmentState = GarmentState.NEW,
        side: str | None = None,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.name = str(name)
        self.garment_type = garment_type
        self.coverage = set(coverage)
        self.layer = layer
        self.fit = fit
        self.material = material
        self.color = color
        self.color_hex = color_hex
        self.state = state
        self.side = side

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not self.name.strip():
            raise ValueError(
                "Garment name must not be empty."
            )

        if not isinstance(self.garment_type, GarmentType):
            raise ValueError(
                "Garment garment_type must be a GarmentType."
            )

        if not self.coverage:
            raise ValueError(
                "Garment coverage must contain at least one "
                "CoverageRegion."
            )

        for region in self.coverage:
            if not isinstance(region, CoverageRegion):
                raise ValueError(
                    "Garment coverage must contain only "
                    "CoverageRegion values."
                )

        if not isinstance(self.layer, GarmentLayer):
            raise ValueError(
                "Garment layer must be a GarmentLayer."
            )

        if not isinstance(self.fit, GarmentFit):
            raise ValueError(
                "Garment fit must be a GarmentFit."
            )

        if not isinstance(self.material, GarmentMaterial):
            raise ValueError(
                "Garment material must be a GarmentMaterial."
            )

        if self.color not in self.VALID_COLORS:
            raise ValueError(
                f"Invalid garment color: {self.color!r}. "
                f"Expected one of {self.VALID_COLORS}."
            )

        if self.color_hex is not None:
            if (
                not isinstance(self.color_hex, str)
                or not self.color_hex.startswith("#")
                or len(self.color_hex) != 7
                or not all(
                    char in "0123456789abcdefABCDEF"
                    for char in self.color_hex[1:]
                )
            ):
                raise ValueError(
                    "Garment color_hex must be a #rrggbb hex "
                    "string or None."
                )

        if not isinstance(self.state, GarmentState):
            raise ValueError(
                "Garment state must be a GarmentState."
            )

        if self.side is not None:
            if self.side not in ("left", "right"):
                raise ValueError(
                    "Garment side must be 'left', 'right' or None."
                )

    def covers(self, region: CoverageRegion) -> bool:
        """Return True if this garment covers the region."""

        return region in self.coverage

    @staticmethod
    def _enum_value(value: Any) -> Any:
        """Safely serialize an enum, or pass through non-enum
        values (robustness against post-construction mutation)."""

        return value.value if hasattr(value, "value") else value

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "name": self.name,
            "garment_type": self._enum_value(self.garment_type),
            "coverage": sorted(
                self._enum_value(region) for region in self.coverage
            ),
            "layer": self._enum_value(self.layer),
            "fit": self._enum_value(self.fit),
            "material": self._enum_value(self.material),
            "color": self.color,
            "color_hex": self.color_hex,
            "state": self._enum_value(self.state),
            "side": self.side,
        }
