from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .gluteal_region import GlutealRegion
from .hips import Hips


class PubicRegion(AnatomyComponent):
    """Represents the pubic region (mons pubis area).

    hair_coverage is structural (0 = none); color and texture
    belong to the future body-hair appearance component. Detail
    level consistent with the MammaryRegion standard.
    """

    component_type = "pubic_region"

    def __init__(
        self,
        *,
        mons_prominence: float = 0.4,
        hair_coverage: float = 0.5,
    ) -> None:
        super().__init__()

        self.mons_prominence = float(mons_prominence)
        self.hair_coverage = float(hair_coverage)

        self.validate()

    def validate(self) -> None:
        super().validate()

        for name in ("mons_prominence", "hair_coverage"):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"PubicRegion {name} must be between 0 and 1."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "mons_prominence": self.mons_prominence,
            "hair_coverage": self.hair_coverage,
        }

class Pelvis(AnatomyComponent):
    """Represents the anatomical pelvis structure."""

    component_type = "pelvis"

    VALID_SHAPES = (
        "narrow",
        "average",
        "broad",
        "wide",
    )

    def __init__(
        self,
        *,
        width: float = 36.0,
        depth: float = 22.0,
        circumference: float = 95.0,
        tilt: float = 0.0,
        shape: str = "average",
        iliac_flare: float = 0.5,
        hips: Hips | None = None,
        gluteal_region: GlutealRegion | None = None,
        pubic_region: PubicRegion | None = None,
    ) -> None:
        super().__init__()

        self.width = float(width)
        self.depth = float(depth)
        self.circumference = float(circumference)
        self.tilt = float(tilt)
        self.shape = shape
        self.iliac_flare = float(iliac_flare)

        self.hips = hips or Hips()
        self.gluteal_region = gluteal_region or GlutealRegion()
        self.pubic_region = pubic_region or PubicRegion()

        self.validate()

    def validate(self) -> None:
        super().validate()

        dimensions = {
            "width": self.width,
            "depth": self.depth,
            "circumference": self.circumference,
        }

        for name, value in dimensions.items():
            if value <= 0:
                raise ValueError(
                    f"Pelvis {name} must be greater than zero."
                )

        if not -20.0 <= self.tilt <= 20.0:
            raise ValueError(
                "Pelvis tilt must be between -20 and 20 degrees."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid pelvis shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if not 0.0 <= self.iliac_flare <= 1.0:
            raise ValueError(
                "Pelvis iliac flare must be between 0 and 1."
            )

        if not isinstance(self.hips, Hips):
            raise ValueError("Pelvis hips must be a Hips instance.")

        if not isinstance(self.gluteal_region, GlutealRegion):
            raise ValueError("Pelvis gluteal_region must be a GlutealRegion instance.")

        self.hips.validate()
        self.gluteal_region.validate()

        if not isinstance(self.pubic_region, PubicRegion):
            raise ValueError("Pelvis pubic_region must be a PubicRegion instance.")

        self.pubic_region.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "width": self.width,
            "depth": self.depth,
            "circumference": self.circumference,
            "tilt": self.tilt,
            "shape": self.shape,
            "iliac_flare": self.iliac_flare,
            "hips": self.hips.to_dict(),
            "gluteal_region": self.gluteal_region.to_dict(),
            "pubic_region": self.pubic_region.to_dict(),
        }
