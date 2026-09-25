from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Flank(AnatomyComponent):
    """Represents one flank (lateral abdominal region).

    The flank spans ribs to iliac crest: per-side model, the
    love-handle zone stays independently adjustable per side.
    """

    component_type = "flank"

    VALID_SHAPES = (
        "hollow",
        "straight",
        "full",
    )

    def __init__(
        self,
        *,
        side: BodySide,
        width: float = 9.0,
        fullness: float = 0.4,
        definition: float = 0.4,
        love_handle_prominence: float = 0.2,
        shape: str = "straight",
    ) -> None:
        super().__init__()

        self.side = side
        self.width = float(width)
        self.fullness = float(fullness)
        self.definition = float(definition)
        self.love_handle_prominence = float(love_handle_prominence)
        self.shape = shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Flank side must be a BodySide value.")

        if self.width <= 0:
            raise ValueError(
                "Flank width must be greater than zero."
            )

        for name in ("fullness", "definition", "love_handle_prominence"):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Flank {name} must be between 0 and 1."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid flank shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "width": self.width,
            "fullness": self.fullness,
            "definition": self.definition,
            "love_handle_prominence": self.love_handle_prominence,
            "shape": self.shape,
        }