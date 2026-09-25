from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class Sternum(AnatomyComponent):
    """Represents the sternum (breastbone)."""

    component_type = "sternum"

    VALID_XIPHOID_SHAPES = (
        "pointed",
        "rounded",
        "bifid",
    )

    def __init__(
        self,
        *,
        length: float = 17.0,
        width: float = 2.5,
        angle: float = 0.3,
        prominence: float = 0.4,
        xiphoid_shape: str = "rounded",
    ) -> None:
        super().__init__()

        self.length = float(length)
        self.width = float(width)
        self.angle = float(angle)
        self.prominence = float(prominence)
        self.xiphoid_shape = xiphoid_shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.length <= 0:
            raise ValueError(
                "Sternum length must be greater than zero."
            )

        if self.width <= 0:
            raise ValueError(
                "Sternum width must be greater than zero."
            )

        for name in ("angle", "prominence"):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Sternum {name} must be between 0 and 1."
                )

        if self.xiphoid_shape not in self.VALID_XIPHOID_SHAPES:
            raise ValueError(
                f"Invalid sternum xiphoid shape: "
                f"{self.xiphoid_shape!r}. "
                f"Expected one of {self.VALID_XIPHOID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "length": self.length,
            "width": self.width,
            "angle": self.angle,
            "prominence": self.prominence,
            "xiphoid_shape": self.xiphoid_shape,
        }