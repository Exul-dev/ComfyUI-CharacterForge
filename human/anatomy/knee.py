from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Knee(AnatomyComponent):
    """Represents an anatomical knee joint.

    H4.15-A foundation, enriched in H4.18-C with patellar detail,
    frontal alignment (genu valgum / varum) and the popliteal
    fossa depth. Legacy parameters and error messages preserved.
    """

    component_type = "knee"

    VALID_ALIGNMENTS = (
        "neutral",
        "genu_valgum",
        "genu_varum",
    )

    def __init__(
        self,
        *,
        side: BodySide = BodySide.RIGHT,
        flexion: float = 0.0,
        rotation: float = 0.0,
        width: float = 10.0,
        circumference: float = 37.0,
        prominence: float = 0.5,
        patella_prominence: float = 0.5,
        patella_width: float = 5.0,
        alignment: str = "neutral",
        popliteal_depth: float = 0.4,
    ) -> None:
        super().__init__()

        self.side = side
        self.flexion = float(flexion)
        self.rotation = float(rotation)
        self.width = float(width)
        self.circumference = float(circumference)
        self.prominence = float(prominence)
        self.patella_prominence = float(patella_prominence)
        self.patella_width = float(patella_width)
        self.alignment = alignment
        self.popliteal_depth = float(popliteal_depth)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Knee side must be a BodySide value.")

        if not 0.0 <= self.flexion <= 150.0:
            raise ValueError(
                "Knee flexion must be between 0 and 150 degrees."
            )

        if not -45.0 <= self.rotation <= 45.0:
            raise ValueError(
                "Knee rotation must be between -45 and 45 degrees."
            )

        if self.width <= 0:
            raise ValueError("Knee width must be greater than zero.")

        if self.circumference <= 0:
            raise ValueError(
                "Knee circumference must be greater than zero."
            )

        if not 0.0 <= self.prominence <= 1.0:
            raise ValueError("Knee prominence must be between 0 and 1.")

        if not 0.0 <= self.patella_prominence <= 1.0:
            raise ValueError(
                "Knee patella_prominence must be between 0 and 1."
            )

        if self.patella_width <= 0:
            raise ValueError(
                "Knee patella_width must be greater than zero."
            )

        if self.alignment not in self.VALID_ALIGNMENTS:
            raise ValueError(
                f"Invalid knee alignment: {self.alignment!r}. "
                f"Expected one of {self.VALID_ALIGNMENTS}."
            )

        if not 0.0 <= self.popliteal_depth <= 1.0:
            raise ValueError(
                "Knee popliteal_depth must be between 0 and 1."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "flexion": self.flexion,
            "rotation": self.rotation,
            "width": self.width,
            "circumference": self.circumference,
            "prominence": self.prominence,
            "patella_prominence": self.patella_prominence,
            "patella_width": self.patella_width,
            "alignment": self.alignment,
            "popliteal_depth": self.popliteal_depth,
        }