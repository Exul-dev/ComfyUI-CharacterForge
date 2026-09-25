from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Ear(AnatomyComponent):
    """Represents one anatomical ear (auricular region).

    Landmark anchor: the porion (superior margin of the external
    auditory meatus) — see CranialLandmarks in head_morphometry
    for the coordinate-level counterpart.
    """

    component_type = "ear"

    VALID_SHAPES = (
        "oval",
        "round",
        "triangular",
        "rectangular",
    )

    VALID_LOBE_SIZES = (
        "small",
        "average",
        "large",
    )

    VALID_LOBE_ATTACHMENTS = (
        "attached",
        "free",
    )

    def __init__(
        self,
        *,
        side: BodySide,
        length: float = 6.0,
        width: float = 3.5,
        protrusion: float = 0.3,
        lobe_size: str = "average",
        lobe_attachment: str = "attached",
        shape: str = "oval",
        prominence: float = 0.5,
    ) -> None:
        super().__init__()

        self.side = side
        self.length = float(length)
        self.width = float(width)
        self.protrusion = float(protrusion)
        self.lobe_size = lobe_size
        self.lobe_attachment = lobe_attachment
        self.shape = shape
        self.prominence = float(prominence)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Ear side must be a BodySide value.")

        if self.length <= 0:
            raise ValueError("Ear length must be greater than zero.")

        if self.width <= 0:
            raise ValueError("Ear width must be greater than zero.")

        if not 0.0 <= self.protrusion <= 1.0:
            raise ValueError(
                "Ear protrusion must be between 0 and 1."
            )

        if self.lobe_size not in self.VALID_LOBE_SIZES:
            raise ValueError(
                f"Invalid ear lobe size: {self.lobe_size!r}. "
                f"Expected one of {self.VALID_LOBE_SIZES}."
            )

        if self.lobe_attachment not in self.VALID_LOBE_ATTACHMENTS:
            raise ValueError(
                f"Invalid ear lobe attachment: "
                f"{self.lobe_attachment!r}. "
                f"Expected one of {self.VALID_LOBE_ATTACHMENTS}."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid ear shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if not 0.0 <= self.prominence <= 1.0:
            raise ValueError(
                "Ear prominence must be between 0 and 1."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "length": self.length,
            "width": self.width,
            "protrusion": self.protrusion,
            "lobe_size": self.lobe_size,
            "lobe_attachment": self.lobe_attachment,
            "shape": self.shape,
            "prominence": self.prominence,
        }