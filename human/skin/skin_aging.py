"""Skin aging model (Human Engine, H6-A1 — Age Engine).

The Age Engine's first layer: WHERE age shows on the skin.

Design decisions:

- WRINKLES ARE REGIONAL: a nasolabial fold is not a forehead
  line. The wrinkle_map follows the per-region pattern of
  FacialHair/BodyHair — every WrinkleZone independently
  adjustable, all zones required (the map is complete);
- FOTOAGING IS NOT CRONOAGING: sun damage is a SEPARATE axis
  (sun_damage, and the wrinkle_map itself is neutral about
  WHY a zone is wrinkled). A sailor and an office worker age
  differently — one axis must not dictate the other;
- DEFAULT IS AGE-NEUTRAL: zero everywhere. Youth is the
  neutral state, aging emerges from data (pattern: glabrous
  BodyHair, clean-shaven FacialHair);
- NOTHING IS DRIVEN BY ChronologicalAge: this component is
  hand-steerable (or steered by H6-C age profiles, which
  only ever act on ApparentAge). The Age model found in
  demographics (chronological/developmental/apparent, three
  independent axes) is respected: this layer answers to the
  APPARENT axis only.
"""

from __future__ import annotations

import math
from enum import Enum
from typing import Any

from ..base.semantic import SemanticComponent


class WrinkleZone(Enum):
    """Anatomic zones where wrinkles visibly form."""

    FOREHEAD = "forehead"
    GLABELLA = "glabella"
    CROW_FEET = "crow_feet"
    NASOLABIAL = "nasolabial"
    MARIONETTE = "marionette"
    PERIORAL = "perioral"
    UNDER_EYE = "under_eye"
    NECK = "neck"
    DECOLLETE = "decollete"
    HANDS = "hands"


class SkinAging(SemanticComponent):
    """Per-zone skin aging state."""

    component_type = "skin_aging"

    def __init__(
        self,
        *,
        wrinkle_map: dict[WrinkleZone, float] | None = None,
        wrinkle_depth: float = 0.0,
        elasticity: float = 1.0,
        sagging: float = 0.0,
        thinning: float = 0.0,
        age_spots: float = 0.0,
        vascular_visibility: float = 0.0,
        sun_damage: float = 0.0,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        if wrinkle_map is None:
            wrinkle_map = {
                zone: 0.0 for zone in WrinkleZone
            }

        self.wrinkle_map = dict(wrinkle_map)
        self.wrinkle_depth = float(wrinkle_depth)
        self.elasticity = float(elasticity)
        self.sagging = float(sagging)
        self.thinning = float(thinning)
        self.age_spots = float(age_spots)
        self.vascular_visibility = float(vascular_visibility)
        self.sun_damage = float(sun_damage)

        self.validate()

    def validate(self) -> None:
        super().validate()

        required = set(WrinkleZone)

        if set(self.wrinkle_map.keys()) != required:
            raise ValueError(
                "SkinAging wrinkle_map must define every "
                "WrinkleZone exactly once."
            )

        for zone, value in self.wrinkle_map.items():
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or not 0.0 <= value <= 1.0
            ):
                raise ValueError(
                    f"SkinAging wrinkle_map for "
                    f"{zone.value} must be a number between "
                    "0 and 1."
                )

        # wrinkle_depth: 0..1 (global coherence of line depth)
        if not 0.0 <= self.wrinkle_depth <= 1.0:
            raise ValueError(
                "SkinAging wrinkle_depth must be between "
                "0 and 1."
            )

        # elasticity: 0..1 (1 = youthful full resilience)
        if not 0.0 <= self.elasticity <= 1.0:
            raise ValueError(
                "SkinAging elasticity must be between 0 and 1."
            )

        for name in (
            "sagging",
            "thinning",
            "age_spots",
            "vascular_visibility",
            "sun_damage",
        ):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"SkinAging {name} must be between 0 and 1."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "wrinkle_map": {
                zone.value: value
                for zone, value in sorted(
                    self.wrinkle_map.items(),
                    key=lambda item: item[0].value,
                )
            },
            "wrinkle_depth": self.wrinkle_depth,
            "elasticity": self.elasticity,
            "sagging": self.sagging,
            "thinning": self.thinning,
            "age_spots": self.age_spots,
            "vascular_visibility": self.vascular_visibility,
            "sun_damage": self.sun_damage,
        }