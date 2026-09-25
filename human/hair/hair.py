"""Scalp hair appearance component (Human Engine, H5-B / H5-D-1).

Appearance layer: Hair is a SemanticComponent (pattern Skin /
Coordinate), attachable to Human through its component registry.

Strict-input standard (H5-A lesson): values stored raw, no
coercion, bool rejected for graded fields.

H5-D-1 enrichment — full hair control:

- baldness_pattern: medical-standard loss patterns. Norwood II-VII
  (the standard male progression; Norwood I is healthy scalp =
  NONE), Ludwig I-III (the diffuse female pattern), areata
  (patchy), totalis (full scalp loss);
- "shaved" joins the length vocabulary: SHAVED (uniform stubble
  shadow, a choice) is now distinct from BALD (no visible hair);
- style (the CUT: bob, fade, mohawk...) and arrangement (how it
  is CURRENTLY WORN: ponytail, bun...) are two independent axes —
  a cut can be worn many ways;
- diffuse thinning is density 0..1 (present since H5-B, now
  documented as the thinning control).

Soft constraints are documented, never enforced: a bun on a buzz
cut is wrong for grown hair but right for a wig — hard rules
would lie.

Layer note: anatomy carries hair-bearing CAPACITY (Axilla
hair_density, PubicRegion hair_coverage — structural follicle
density); this component carries the VISIBLE STATE (coverage,
styling). Glabrous = anatomy untouched, appearance coverage 0.
"""

from __future__ import annotations

import math
from enum import Enum
from typing import Any

from ..base.semantic import SemanticComponent


class HairBaldnessPattern(Enum):
    """Medical-standard scalp hair loss patterns."""

    NONE = "none"
    NORWOOD_II = "norwood_ii"
    NORWOOD_III = "norwood_iii"
    NORWOOD_IV = "norwood_iv"
    NORWOOD_V = "norwood_v"
    NORWOOD_VI = "norwood_vi"
    NORWOOD_VII = "norwood_vii"
    LUDWIG_I = "ludwig_i"
    LUDWIG_II = "ludwig_ii"
    LUDWIG_III = "ludwig_iii"
    ALOPECIA_AREATA = "alopecia_areata"
    ALOPECIA_TOTALIS = "alopecia_totalis"


class HairStyle(Enum):
    """The cut: what the hair is shaped into."""

    NATURAL = "natural"
    BUZZ_CUT = "buzz_cut"
    CREW_CUT = "crew_cut"
    FADE = "fade"
    UNDERCUT = "undercut"
    FLAT_TOP = "flat_top"
    POMPADOUR = "pompadour"
    MOHAWK = "mohawk"
    BOWL_CUT = "bowl_cut"
    BOB = "bob"
    LOB = "lob"
    PIXIE = "pixie"
    SHAG = "shag"
    MULLET = "mullet"
    WOLF_CUT = "wolf_cut"
    LAYERS = "layers"
    AFRO = "afro"
    DREADLOCKS = "dreadlocks"
    BOX_BRAIDS = "box_braids"
    CORNROWS = "cornrows"
    TWISTS = "twists"


class HairArrangement(Enum):
    """How the hair is currently worn (independent from the cut)."""

    LOOSE = "loose"
    PONYTAIL = "ponytail"
    BUN = "bun"
    TOP_KNOT = "top_knot"
    HALF_UP = "half_up"
    BRAIDED = "braided"
    PIGTAILS = "pigtails"
    PINNED = "pinned"
    SPACE_BUNS = "space_buns"


class Hair(SemanticComponent):
    """Scalp hair surface appearance."""

    component_type = "hair"

    VALID_COLORS = (
        "black",
        "dark_brown",
        "brown",
        "light_brown",
        "dark_blonde",
        "blonde",
        "light_blonde",
        "auburn",
        "red",
        "copper",
        "gray",
        "white",
    )

    VALID_TEXTURES = (
        "straight",
        "wavy",
        "curly",
        "coily",
    )

    VALID_THICKNESSES = (
        "fine",
        "medium",
        "coarse",
    )

    VALID_LENGTHS = (
        "shaved",
        "bald",
        "very_short",
        "short",
        "medium",
        "long",
        "very_long",
    )

    VALID_HAIRLINES = (
        "straight",
        "rounded",
        "widows_peak",
        "high",
        "receding",
    )

    def __init__(
        self,
        *,
        color: str = "brown",
        color_hex: str | None = None,
        texture: str = "straight",
        thickness: str = "medium",
        length: str = "medium",
        density: float = 0.6,
        volume: float = 0.5,
        gloss: float = 0.4,
        hairline: str = "straight",
        baldness_pattern: HairBaldnessPattern = HairBaldnessPattern.NONE,
        style: HairStyle = HairStyle.NATURAL,
        arrangement: HairArrangement = HairArrangement.LOOSE,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.color = color
        self.color_hex = color_hex
        self.texture = texture
        self.thickness = thickness
        self.length = length
        self.density = density
        self.volume = volume
        self.gloss = gloss
        self.hairline = hairline
        self.baldness_pattern = baldness_pattern
        self.style = style
        self.arrangement = arrangement

        self.validate()

    def _validate_graded(self, name: str) -> None:
        """Validate a 0..1 graded field with strict type checks."""

        value = getattr(self, name)

        if isinstance(value, bool) or not isinstance(
            value,
            (int, float),
        ):
            raise ValueError(
                f"Hair {name} must be a number between 0 and 1."
            )

        if not math.isfinite(value):
            raise ValueError(
                f"Hair {name} must be a number between 0 and 1."
            )

        if not 0.0 <= value <= 1.0:
            raise ValueError(
                f"Hair {name} must be a number between 0 and 1."
            )

    def validate(self) -> None:
        super().validate()

        if self.color not in self.VALID_COLORS:
            raise ValueError(
                f"Invalid hair color: {self.color!r}. "
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
                    "Hair color_hex must be a #rrggbb hex string "
                    "or None."
                )

        if self.texture not in self.VALID_TEXTURES:
            raise ValueError(
                f"Invalid hair texture: {self.texture!r}. "
                f"Expected one of {self.VALID_TEXTURES}."
            )

        if self.thickness not in self.VALID_THICKNESSES:
            raise ValueError(
                f"Invalid hair thickness: {self.thickness!r}. "
                f"Expected one of {self.VALID_THICKNESSES}."
            )

        if self.length not in self.VALID_LENGTHS:
            raise ValueError(
                f"Invalid hair length: {self.length!r}. "
                f"Expected one of {self.VALID_LENGTHS}."
            )

        for name in ("density", "volume", "gloss"):
            self._validate_graded(name)

        if self.hairline not in self.VALID_HAIRLINES:
            raise ValueError(
                f"Invalid hair hairline: {self.hairline!r}. "
                f"Expected one of {self.VALID_HAIRLINES}."
            )

        if not isinstance(self.baldness_pattern, HairBaldnessPattern):
            raise ValueError(
                "Hair baldness_pattern must be a "
                "HairBaldnessPattern value."
            )

        if not isinstance(self.style, HairStyle):
            raise ValueError(
                "Hair style must be a HairStyle value."
            )

        if not isinstance(self.arrangement, HairArrangement):
            raise ValueError(
                "Hair arrangement must be a HairArrangement value."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "color": self.color,
            "color_hex": self.color_hex,
            "texture": self.texture,
            "thickness": self.thickness,
            "length": self.length,
            "density": self.density,
            "volume": self.volume,
            "gloss": self.gloss,
            "hairline": self.hairline,
            "baldness_pattern": self.baldness_pattern.value,
            "style": self.style.value,
            "arrangement": self.arrangement.value,
        }