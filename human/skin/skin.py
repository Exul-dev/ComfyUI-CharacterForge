"""Skin appearance component (Human Engine, H5-A).

The appearance layer lives BESIDE the anatomy, not inside it:
Skin is a SemanticComponent (pattern Coordinate), attachable to
Human through its component registry (register_component).

Design note — tone vs type: the nominal tone (very_light..
very_dark) is the PERCEIVED color; the Fitzpatrick type (I..VI)
is UV reactivity. The two scales are correlated but independent:
no mapping is enforced (it would be anthropometrically false).
"""

from __future__ import annotations

import math
from enum import Enum
from typing import Any

from ..base.semantic import SemanticComponent


class SkinType(Enum):
    """Fitzpatrick skin phototype."""

    I = "I"
    II = "II"
    III = "III"
    IV = "IV"
    V = "V"
    VI = "VI"


class Skin(SemanticComponent):
    """Surface appearance of the human skin."""

    component_type = "skin"

    VALID_TONES = (
        "very_light",
        "light",
        "medium_light",
        "medium",
        "medium_dark",
        "dark",
        "very_dark",
    )

    VALID_UNDERTONES = (
        "warm",
        "neutral",
        "cool",
    )

    VALID_TEXTURES = (
        "smooth",
        "average",
        "rough",
        "textured",
    )

    VALID_FRECKLE_DENSITIES = (
        "none",
        "light",
        "moderate",
        "heavy",
        "severe",
    )

    def __init__(
        self,
        *,
        tone: str = "medium",
        tone_hex: str | None = None,
        undertone: str = "neutral",
        skin_type: SkinType = SkinType.III,
        texture: str = "average",
        oiliness: float = 0.4,
        hydration: float = 0.6,
        sensitivity: float = 0.3,
        freckle_density: str = "none",
        mole_count: int = 0,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.tone = tone
        self.tone_hex = tone_hex
        self.undertone = undertone
        self.skin_type = skin_type
        self.texture = texture
        self.oiliness = float(oiliness)
        self.hydration = float(hydration)
        self.sensitivity = float(sensitivity)
        self.freckle_density = freckle_density
        self.mole_count = mole_count

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.tone not in self.VALID_TONES:
            raise ValueError(
                f"Invalid skin tone: {self.tone!r}. "
                f"Expected one of {self.VALID_TONES}."
            )

        if self.tone_hex is not None:
            if (
                not isinstance(self.tone_hex, str)
                or not self.tone_hex.startswith("#")
                or len(self.tone_hex) != 7
                or not all(
                    char in "0123456789abcdefABCDEF"
                    for char in self.tone_hex[1:]
                )
            ):
                raise ValueError(
                    "Skin tone_hex must be a #rrggbb hex string "
                    "or None."
                )

        if self.undertone not in self.VALID_UNDERTONES:
            raise ValueError(
                f"Invalid skin undertone: {self.undertone!r}. "
                f"Expected one of {self.VALID_UNDERTONES}."
            )

        if not isinstance(self.skin_type, SkinType):
            raise ValueError(
                "Skin skin_type must be a SkinType value."
            )

        if self.texture not in self.VALID_TEXTURES:
            raise ValueError(
                f"Invalid skin texture: {self.texture!r}. "
                f"Expected one of {self.VALID_TEXTURES}."
            )

        for name in ("oiliness", "hydration", "sensitivity"):
            value = getattr(self, name)

            if not math.isfinite(value):
                raise ValueError(
                    f"Skin {name} must be a finite number."
                )

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Skin {name} must be between 0 and 1."
                )

        if self.freckle_density not in self.VALID_FRECKLE_DENSITIES:
            raise ValueError(
                f"Invalid skin freckle density: "
                f"{self.freckle_density!r}. "
                f"Expected one of {self.VALID_FRECKLE_DENSITIES}."
            )

        if (
            isinstance(self.mole_count, bool)
            or not isinstance(self.mole_count, int)
            or self.mole_count < 0
        ):
            raise ValueError(
                "Skin mole_count must be a non-negative integer."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "tone": self.tone,
            "tone_hex": self.tone_hex,
            "undertone": self.undertone,
            "skin_type": self.skin_type.value,
            "texture": self.texture,
            "oiliness": self.oiliness,
            "hydration": self.hydration,
            "sensitivity": self.sensitivity,
            "freckle_density": self.freckle_density,
            "mole_count": self.mole_count,
        }
