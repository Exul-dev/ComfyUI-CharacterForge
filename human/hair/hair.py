"""Hair appearance component (Human Engine, H5-B).

Appearance layer: Hair is a SemanticComponent (pattern Skin /
Coordinate), attachable to Human through its component registry.

Strict-input standard (from the H5-A mole_count lesson): values
are stored raw — no coercion — and validate() checks types
explicitly. bool is rejected for graded fields, non-numeric
strings raise ValueError (not TypeError).

Design note — bald orthogonality: length describes the CURRENT
scalp coverage; color, texture, thickness and density describe
the hair fiber itself (relevant for stubble, regrowth, future
facial hair). The fields are deliberately independent.
"""

from __future__ import annotations

import math
from typing import Any

from ..base.semantic import SemanticComponent


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
        }