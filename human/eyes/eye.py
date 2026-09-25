"""Eye appearance component (Human Engine, H5-C).

Appearance layer: Eye is a SemanticComponent (pattern Skin/Hair),
side-required like every bilateral structure of the project.

Design notes:

- heterochromia needs no explicit field: it emerges from the
  bilateral model (left.iris_color != right.iris_color);
- eyebrows are facial hair, not ocular structure: they belong to
  a future facial-hair component;
- pupil size is dynamic (function), not structural appearance:
  it belongs to expression/pose layers.
"""

from __future__ import annotations

from typing import Any

from ..base.semantic import SemanticComponent
from ..anatomy.enums import BodySide


class Eye(SemanticComponent):
    """Surface appearance of one eye."""

    component_type = "eye"

    VALID_IRIS_COLORS = (
        "brown",
        "dark_brown",
        "light_brown",
        "hazel",
        "amber",
        "green",
        "blue",
        "gray",
        "violet",
    )

    VALID_IRIS_PATTERNS = (
        "uniform",
        "ringed",
        "flecked",
        "starburst",
    )

    VALID_SCLERA_TINTS = (
        "white",
        "ivory",
        "bluish",
        "yellowish",
    )

    VALID_LASH_LENGTHS = (
        "short",
        "medium",
        "long",
    )

    VALID_LASH_DENSITIES = (
        "sparse",
        "average",
        "dense",
    )

    def __init__(
        self,
        *,
        side: BodySide,
        iris_color: str = "brown",
        iris_color_hex: str | None = None,
        iris_pattern: str = "uniform",
        sclera_tint: str = "white",
        lash_length: str = "medium",
        lash_density: str = "average",
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.side = side
        self.iris_color = iris_color
        self.iris_color_hex = iris_color_hex
        self.iris_pattern = iris_pattern
        self.sclera_tint = sclera_tint
        self.lash_length = lash_length
        self.lash_density = lash_density

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError(
                "Eye side must be a BodySide value."
            )

        if self.iris_color not in self.VALID_IRIS_COLORS:
            raise ValueError(
                f"Invalid eye iris color: {self.iris_color!r}. "
                f"Expected one of {self.VALID_IRIS_COLORS}."
            )

        if self.iris_color_hex is not None:
            if (
                not isinstance(self.iris_color_hex, str)
                or not self.iris_color_hex.startswith("#")
                or len(self.iris_color_hex) != 7
                or not all(
                    char in "0123456789abcdefABCDEF"
                    for char in self.iris_color_hex[1:]
                )
            ):
                raise ValueError(
                    "Eye iris_color_hex must be a #rrggbb hex "
                    "string or None."
                )

        if self.iris_pattern not in self.VALID_IRIS_PATTERNS:
            raise ValueError(
                f"Invalid eye iris pattern: "
                f"{self.iris_pattern!r}. "
                f"Expected one of {self.VALID_IRIS_PATTERNS}."
            )

        if self.sclera_tint not in self.VALID_SCLERA_TINTS:
            raise ValueError(
                f"Invalid eye sclera tint: {self.sclera_tint!r}. "
                f"Expected one of {self.VALID_SCLERA_TINTS}."
            )

        if self.lash_length not in self.VALID_LASH_LENGTHS:
            raise ValueError(
                f"Invalid eye lash length: "
                f"{self.lash_length!r}. "
                f"Expected one of {self.VALID_LASH_LENGTHS}."
            )

        if self.lash_density not in self.VALID_LASH_DENSITIES:
            raise ValueError(
                f"Invalid eye lash density: "
                f"{self.lash_density!r}. "
                f"Expected one of {self.VALID_LASH_DENSITIES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "iris_color": self.iris_color,
            "iris_color_hex": self.iris_color_hex,
            "iris_pattern": self.iris_pattern,
            "sclera_tint": self.sclera_tint,
            "lash_length": self.lash_length,
            "lash_density": self.lash_density,
        }