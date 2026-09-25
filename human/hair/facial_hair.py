"""Facial hair appearance component (Human Engine, H5-D-2).

Appearance layer (pattern Skin): the beard is modeled PER
ANATOMIC REGION — facial hair grows in zones (a full moustache
with a bare chin exists), so coverage is a per-region map, not
one global value.

Design decisions:

- styles are FACTORIES, not cages: set_style("goatee")
  configures the region coverages of the classic goatee, and
  everything remains hand-tunable afterwards. A preset is a
  starting point;
- color is INDEPENDENT from scalp hair: beard hair often does
  not match (early gray, red on brown) — a real trait;
- default coverage is 0.0 everywhere: the clean-shaven face is
  the neutral state, glabrousness emerges from data;
- neckline height is NECK coverage, not a separate field: the
  beard line IS where neck coverage stops.
"""

from __future__ import annotations

import math
from enum import Enum
from typing import Any

from ..base.semantic import SemanticComponent


class FacialHairRegion(Enum):
    """Anatomic zones of facial hair growth."""

    MOUSTACHE = "moustache"
    CHIN = "chin"
    JAWLINE = "jawline"
    SIDEBURNS = "sideburns"
    NECK = "neck"
    CHEEKS = "cheeks"


class FacialHairLength(Enum):
    """Beard length scale."""

    STUBBLE = "stubble"
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"


class FacialHairGrooming(Enum):
    """Grooming level."""

    NATURAL = "natural"
    TRIMMED = "trimmed"
    SHAPED = "shaped"


class FacialHairStyle(Enum):
    """Named styles: starting points for region coverage.

    Each maps to a factory configuration — never a constraint.
    """

    CLEAN_SHAVEN = "clean_shaven"
    STUBBLE = "stubble"
    MOUSTACHE = "moustache"
    GOATEE = "goatee"
    VAN_DYKE = "van_dyke"
    CHIN_STRIP = "chin_strip"
    FULL_BEARD = "full_beard"
    MUTTON_CHOPS = "mutton_chops"
    SIDEBURNS_ONLY = "sideburns_only"
    BALBO = "balbo"
    ANCHOR = "anchor"


# Style -> region coverage presets (0..1 per region).
_STYLE_PRESETS: dict[FacialHairStyle, dict[FacialHairRegion, float]] = {
    FacialHairStyle.CLEAN_SHAVEN: {
        region: 0.0 for region in FacialHairRegion
    },
    FacialHairStyle.STUBBLE: {
        FacialHairRegion.MOUSTACHE: 0.6,
        FacialHairRegion.CHIN: 0.6,
        FacialHairRegion.JAWLINE: 0.5,
        FacialHairRegion.SIDEBURNS: 0.4,
        FacialHairRegion.NECK: 0.2,
        FacialHairRegion.CHEEKS: 0.3,
    },
    FacialHairStyle.MOUSTACHE: {
        FacialHairRegion.MOUSTACHE: 1.0,
        FacialHairRegion.CHIN: 0.0,
        FacialHairRegion.JAWLINE: 0.0,
        FacialHairRegion.SIDEBURNS: 0.0,
        FacialHairRegion.NECK: 0.0,
        FacialHairRegion.CHEEKS: 0.0,
    },
    FacialHairStyle.GOATEE: {
        FacialHairRegion.MOUSTACHE: 1.0,
        FacialHairRegion.CHIN: 1.0,
        FacialHairRegion.JAWLINE: 0.0,
        FacialHairRegion.SIDEBURNS: 0.0,
        FacialHairRegion.NECK: 0.0,
        FacialHairRegion.CHEEKS: 0.0,
    },
    FacialHairStyle.VAN_DYKE: {
        FacialHairRegion.MOUSTACHE: 1.0,
        FacialHairRegion.CHIN: 1.0,
        FacialHairRegion.JAWLINE: 0.0,
        FacialHairRegion.SIDEBURNS: 0.0,
        FacialHairRegion.NECK: 0.0,
        FacialHairRegion.CHEEKS: 0.0,
    },
    FacialHairStyle.CHIN_STRIP: {
        FacialHairRegion.MOUSTACHE: 0.0,
        FacialHairRegion.CHIN: 0.8,
        FacialHairRegion.JAWLINE: 0.0,
        FacialHairRegion.SIDEBURNS: 0.0,
        FacialHairRegion.NECK: 0.0,
        FacialHairRegion.CHEEKS: 0.0,
    },
    FacialHairStyle.FULL_BEARD: {
        FacialHairRegion.MOUSTACHE: 1.0,
        FacialHairRegion.CHIN: 1.0,
        FacialHairRegion.JAWLINE: 1.0,
        FacialHairRegion.SIDEBURNS: 1.0,
        FacialHairRegion.NECK: 0.7,
        FacialHairRegion.CHEEKS: 1.0,
    },
    FacialHairStyle.MUTTON_CHOPS: {
        FacialHairRegion.MOUSTACHE: 0.0,
        FacialHairRegion.CHIN: 0.0,
        FacialHairRegion.JAWLINE: 0.6,
        FacialHairRegion.SIDEBURNS: 1.0,
        FacialHairRegion.NECK: 0.0,
        FacialHairRegion.CHEEKS: 0.8,
    },
    FacialHairStyle.SIDEBURNS_ONLY: {
        FacialHairRegion.MOUSTACHE: 0.0,
        FacialHairRegion.CHIN: 0.0,
        FacialHairRegion.JAWLINE: 0.0,
        FacialHairRegion.SIDEBURNS: 1.0,
        FacialHairRegion.NECK: 0.0,
        FacialHairRegion.CHEEKS: 0.0,
    },
    FacialHairStyle.BALBO: {
        FacialHairRegion.MOUSTACHE: 1.0,
        FacialHairRegion.CHIN: 0.8,
        FacialHairRegion.JAWLINE: 0.0,
        FacialHairRegion.SIDEBURNS: 0.0,
        FacialHairRegion.NECK: 0.0,
        FacialHairRegion.CHEEKS: 0.0,
    },
    FacialHairStyle.ANCHOR: {
        FacialHairRegion.MOUSTACHE: 1.0,
        FacialHairRegion.CHIN: 0.6,
        FacialHairRegion.JAWLINE: 0.3,
        FacialHairRegion.SIDEBURNS: 0.0,
        FacialHairRegion.NECK: 0.0,
        FacialHairRegion.CHEEKS: 0.0,
    },
}


class FacialHair(SemanticComponent):
    """Per-region facial hair appearance."""

    component_type = "facial_hair"

    VALID_TEXTURES = (
        "straight",
        "wavy",
        "curly",
        "coily",
    )

    def __init__(
        self,
        *,
        coverage: dict[FacialHairRegion, float] | None = None,
        color: str = "brown",
        color_hex: str | None = None,
        length: FacialHairLength = FacialHairLength.STUBBLE,
        grooming: FacialHairGrooming = (
            FacialHairGrooming.NATURAL
        ),
        texture: str = "straight",
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        if coverage is None:
            coverage = {
                region: 0.0 for region in FacialHairRegion
            }

        self.coverage = dict(coverage)
        self.color = color
        self.color_hex = color_hex
        self.length = length
        self.grooming = grooming
        self.texture = texture

        self.validate()

    @classmethod
    def from_style(
        cls,
        style: FacialHairStyle,
        **overrides: Any,
    ) -> "FacialHair":
        """Build a FacialHair from a named style preset.

        The preset configures region coverages; any other
        parameter can be overridden — and the result remains
        hand-tunable. A preset is a starting point, not a cage.
        """

        return cls(
            coverage=dict(_STYLE_PRESETS[style]),
            **overrides,
        )

    def set_style(self, style: FacialHairStyle) -> None:
        """Reconfigure this component's coverages to a preset."""

        self.coverage = dict(_STYLE_PRESETS[style])
        self.validate()

    def validate(self) -> None:
        super().validate()

        required = set(FacialHairRegion)

        if set(self.coverage.keys()) != required:
            raise ValueError(
                "FacialHair coverage must define every "
                "FacialHairRegion exactly once."
            )

        for region, value in self.coverage.items():
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or not 0.0 <= value <= 1.0
            ):
                raise ValueError(
                    f"FacialHair coverage for {region.value} "
                    "must be a number between 0 and 1."
                )

        if not self.color:
            raise ValueError(
                "FacialHair color must not be empty."
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
                    "FacialHair color_hex must be a #rrggbb hex "
                    "string or None."
                )

        if not isinstance(self.length, FacialHairLength):
            raise ValueError(
                "FacialHair length must be a FacialHairLength "
                "value."
            )

        if not isinstance(self.grooming, FacialHairGrooming):
            raise ValueError(
                "FacialHair grooming must be a "
                "FacialHairGrooming value."
            )

        if self.texture not in self.VALID_TEXTURES:
            raise ValueError(
                f"Invalid facial hair texture: {self.texture!r}. "
                f"Expected one of {self.VALID_TEXTURES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "coverage": {
                region.value: value
                for region, value in sorted(
                    self.coverage.items(),
                    key=lambda item: item[0].value,
                )
            },
            "color": self.color,
            "color_hex": self.color_hex,
            "length": self.length.value,
            "grooming": self.grooming.value,
            "texture": self.texture,
        }