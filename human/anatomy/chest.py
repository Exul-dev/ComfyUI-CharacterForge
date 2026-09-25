from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .sternum import Sternum


class Chest(AnatomyComponent):
    """Thoracic chest component.

    Enriched in H4.19-B with explicit pectoral definitions and
    the sternum as a sub-component. Legacy parameters and error
    messages preserved.
    """

    component_type = "chest"

    VALID_SHAPES = (
        "flat",
        "average",
        "broad",
        "defined",
        "barrel",
    )

    def __init__(
        self,
        *,
        width: float = 32.0,
        height: float = 28.0,
        projection: float = 12.0,
        shape: str = "average",
        pectoral_definition: float = 0.5,
        pectoral_separation: float = 0.4,
        sternum: Sternum | None = None,
    ) -> None:
        super().__init__()
        self.width = float(width)
        self.height = float(height)
        self.projection = float(projection)
        self.shape = shape
        self.pectoral_definition = float(pectoral_definition)
        self.pectoral_separation = float(pectoral_separation)
        self.sternum = sternum or Sternum()

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.width <= 0:
            raise ValueError("Chest width must be greater than zero.")

        if self.height <= 0:
            raise ValueError("Chest height must be greater than zero.")

        if self.projection <= 0:
            raise ValueError("Chest projection must be greater than zero.")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid chest shape: {self.shape!r}")

        for name in ("pectoral_definition", "pectoral_separation"):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Chest {name} must be between 0 and 1."
                )

        if not isinstance(self.sternum, Sternum):
            raise ValueError(
                "Chest sternum must be a Sternum instance."
            )

        self.sternum.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "width": self.width,
            "height": self.height,
            "projection": self.projection,
            "shape": self.shape,
            "pectoral_definition": self.pectoral_definition,
            "pectoral_separation": self.pectoral_separation,
            "sternum": self.sternum.to_dict(),
        }