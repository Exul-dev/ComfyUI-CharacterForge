"""Hair aging model (Human Engine, H6-A2 — Age Engine).

The Age Engine's second layer: HOW hair color ages.

Design decisions:

- GRAYING IS PROGRESSIVE, not binary: extent is a continuous
  0..1 scale (full color -> salt-and-pepper -> white), and the
  PATTERN says WHERE it advances first (temples-first is the
  classic male sequence, diffuse the classic even one — a real
  taxonomy, like Norwood for loss);
- PER-REGION INDEPENDENCE: the beard often grays BEFORE the
  scalp (a real male trait), and body hair can stay dark. Three
  independent extents: scalp, facial, body — three dials on one
  phenomenon;
- gray_hair_texture: white hair is coarser and wire-like — a
  separate axis, because texture and color age independently;
- DEFAULT IS AGE-NEUTRAL (pattern: glabrous, clean-shaven,
  age-neutral skin): full color, no texture change;
- NOTHING is driven by ChronologicalAge (Age Engine principle:
  this layer answers to ApparentAge only, and even then only
  through explicit values or H6-C profiles — never implicitly).
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from ..base.semantic import SemanticComponent


class GrayingPattern(Enum):
    """Where gray advances first (a real, documented sequence)."""

    NONE = "none"
    TEMPLES_FIRST = "temples_first"
    DIFFUSE = "diffuse"
    SALT_PEPPER = "salt_pepper"
    PATCHY = "patchy"
    ROOT_SHADOW = "root_shadow"


class HairAging(SemanticComponent):
    """Progressive, per-region hair graying state."""

    component_type = "hair_aging"

    def __init__(
        self,
        *,
        graying_pattern: GrayingPattern = GrayingPattern.NONE,
        scalp_gray_extent: float = 0.0,
        facial_gray_extent: float = 0.0,
        body_gray_extent: float = 0.0,
        gray_hair_texture: float = 0.0,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.graying_pattern = graying_pattern
        self.scalp_gray_extent = float(scalp_gray_extent)
        self.facial_gray_extent = float(facial_gray_extent)
        self.body_gray_extent = float(body_gray_extent)
        self.gray_hair_texture = float(gray_hair_texture)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(
            self.graying_pattern,
            GrayingPattern,
        ):
            raise ValueError(
                "HairAging graying_pattern must be a "
                "GrayingPattern value."
            )

        for name in (
            "scalp_gray_extent",
            "facial_gray_extent",
            "body_gray_extent",
            "gray_hair_texture",
        ):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"HairAging {name} must be between 0 and 1."
                )

        # Consistency (soft, documented): a pattern of NONE with
        # extents > 0 is a plausible state (color washed out
        # everywhere evenly — EXTENSIVE bleaching reads as
        # diffuse). No hard constraint: patterns and extents are
        # two independent axes, documented, never enforced.

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "graying_pattern": self.graying_pattern.value,
            "scalp_gray_extent": self.scalp_gray_extent,
            "facial_gray_extent": self.facial_gray_extent,
            "body_gray_extent": self.body_gray_extent,
            "gray_hair_texture": self.gray_hair_texture,
        }