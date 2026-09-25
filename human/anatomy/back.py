from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .scapula import Scapulae


class Back(AnatomyComponent):
    """Back anatomical component.

    Enriched in H4.19-C with the bilateral scapulae, the vertebral
    groove, the lumbar fossae and trapezius definition. Legacy
    parameters and error messages preserved verbatim.
    """

    component_type = "back"

    VALID_SHAPES = (
        "straight",
        "defined",
        "athletic",
        "rounded",
    )

    def __init__(
        self,
        *,
        width: float = 31.0,
        length: float = 45.0,
        muscularity: float = 0.5,
        shape: str = "straight",
        spine_groove_depth: float = 0.4,
        lumbar_fossa_depth: float = 0.3,
        trapezius_definition: float = 0.5,
        scapulae: Scapulae | None = None,
    ) -> None:
        super().__init__()
        self.width = float(width)
        self.length = float(length)
        self.muscularity = float(muscularity)
        self.shape = shape
        self.spine_groove_depth = float(spine_groove_depth)
        self.lumbar_fossa_depth = float(lumbar_fossa_depth)
        self.trapezius_definition = float(trapezius_definition)
        self.scapulae = scapulae or Scapulae()

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.width <= 0:
            raise ValueError("Back width must be greater than zero.")

        if self.length <= 0:
            raise ValueError("Back length must be greater than zero.")

        if not 0 <= self.muscularity <= 1:
            raise ValueError("Back muscularity must be between 0 and 1.")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid back shape: {self.shape!r}")

        for name in (
            "spine_groove_depth",
            "lumbar_fossa_depth",
            "trapezius_definition",
        ):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Back {name} must be between 0 and 1."
                )

        if not isinstance(self.scapulae, Scapulae):
            raise ValueError(
                "Back scapulae must be a Scapulae instance."
            )

        self.scapulae.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "width": self.width,
            "length": self.length,
            "muscularity": self.muscularity,
            "shape": self.shape,
            "spine_groove_depth": self.spine_groove_depth,
            "lumbar_fossa_depth": self.lumbar_fossa_depth,
            "trapezius_definition": self.trapezius_definition,
            "scapulae": self.scapulae.to_dict(),
        }