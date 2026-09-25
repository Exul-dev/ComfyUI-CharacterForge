from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class RibCage(AnatomyComponent):
    """Rib cage component."""

    component_type = "ribcage"

    VALID_SHAPES = (
        "narrow",
        "average",
        "broad",
        "barrel",
    )

    def __init__(
        self,
        *,
        width: float = 30.0,
        depth: float = 20.0,
        shape: str = "average",
    ) -> None:
        super().__init__()
        self.width = float(width)
        self.depth = float(depth)
        self.shape = shape
        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.width <= 0:
            raise ValueError("Rib cage width must be greater than zero.")

        if self.depth <= 0:
            raise ValueError("Rib cage depth must be greater than zero.")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid rib cage shape: {self.shape!r}")

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "width": self.width,
            "depth": self.depth,
            "shape": self.shape,
        }
