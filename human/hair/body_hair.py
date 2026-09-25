"""Body hair appearance component (Human Engine, H5-D-3).

Appearance layer (pattern FacialHair): body hair is modeled PER
REGION, on the Ferriman-Gallwey zones — the medical standard for
androgenic hair distribution (the same source that gave the
project Norwood and Ludwig for scalp loss).

Design decisions:

- GLABROUS = coverage 0.0 everywhere: a state that emerges from
  data, never a flag. The smooth character and the hairy
  character are the same component with different numbers;
- color and texture are SHARED across regions: body hair is
  uniform in reality (unlike the beard, which may differ from
  the scalp);
- NO style presets: body hair has no named-style tradition like
  beards do — only individual patterns. Presets exist where a
  tradition exists.

Layer note: anatomy carries follicle CAPACITY (Axilla
hair_density, PubicRegion hair_coverage); this component carries
the VISIBLE body distribution.
"""

from __future__ import annotations

import math
from enum import Enum
from typing import Any

from ..base.semantic import SemanticComponent


class BodyHairRegion(Enum):
    """Anatomic zones of body hair (Ferriman-Gallwey-based)."""

    CHEST = "chest"
    ABDOMEN = "abdomen"
    BACK = "back"
    SHOULDERS = "shoulders"
    ARMS = "arms"
    FOREARMS = "forearms"
    HANDS = "hands"
    BUTTOCKS = "buttocks"
    THIGHS = "thighs"
    LEGS = "legs"
    FEET = "feet"


class BodyHair(SemanticComponent):
    """Per-region body hair appearance."""

    component_type = "body_hair"

    VALID_TEXTURES = (
        "straight",
        "wavy",
        "curly",
        "coily",
    )

    def __init__(
        self,
        *,
        coverage: dict[BodyHairRegion, float] | None = None,
        color: str = "brown",
        color_hex: str | None = None,
        texture: str = "straight",
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        if coverage is None:
            coverage = {
                region: 0.0 for region in BodyHairRegion
            }

        self.coverage = dict(coverage)
        self.color = color
        self.color_hex = color_hex
        self.texture = texture

        self.validate()

    def validate(self) -> None:
        super().validate()

        required = set(BodyHairRegion)

        if set(self.coverage.keys()) != required:
            raise ValueError(
                "BodyHair coverage must define every "
                "BodyHairRegion exactly once."
            )

        for region, value in self.coverage.items():
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or not 0.0 <= value <= 1.0
            ):
                raise ValueError(
                    f"BodyHair coverage for {region.value} "
                    "must be a number between 0 and 1."
                )

        if not self.color:
            raise ValueError(
                "BodyHair color must not be empty."
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
                    "BodyHair color_hex must be a #rrggbb hex "
                    "string or None."
                )

        if self.texture not in self.VALID_TEXTURES:
            raise ValueError(
                f"Invalid body hair texture: {self.texture!r}. "
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
            "texture": self.texture,
        }