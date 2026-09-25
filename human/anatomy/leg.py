from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .ankle import Ankle
from .enums import BodySide
from .foot import Foot
from .knee import Knee
from .lower_leg import LowerLeg
from .thigh import Thigh


class Leg(AnatomyComponent):
    """Represents one complete human leg.

    Unlike the upper-limb model (which shares segments between the
    two arms), each leg owns its own segments and joints, and every
    sided sub-component must match the leg side: bilateral
    asymmetry stays representable.
    """

    component_type = "leg"

    def __init__(
        self,
        *,
        side: BodySide,
        thigh: Thigh | None = None,
        knee: Knee | None = None,
        lower_leg: LowerLeg | None = None,
        ankle: Ankle | None = None,
        foot: Foot | None = None,
    ) -> None:
        super().__init__()

        self.side = side
        self.thigh = thigh or Thigh()
        self.knee = knee or Knee(side=side)
        self.lower_leg = lower_leg or LowerLeg()
        self.ankle = ankle or Ankle(side=side)
        self.foot = foot or Foot(side=side)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Leg side must be a BodySide value.")

        if not isinstance(self.thigh, Thigh):
            raise ValueError("Leg thigh must be a Thigh instance.")

        if not isinstance(self.knee, Knee):
            raise ValueError("Leg knee must be a Knee instance.")

        if not isinstance(self.lower_leg, LowerLeg):
            raise ValueError(
                "Leg lower_leg must be a LowerLeg instance."
            )

        if not isinstance(self.ankle, Ankle):
            raise ValueError("Leg ankle must be an Ankle instance.")

        if not isinstance(self.foot, Foot):
            raise ValueError("Leg foot must be a Foot instance.")

        if self.knee.side is not self.side:
            raise ValueError(
                "Leg knee side must match the leg side."
            )

        if self.ankle.side is not self.side:
            raise ValueError(
                "Leg ankle side must match the leg side."
            )

        if self.foot.side is not self.side:
            raise ValueError(
                "Leg foot side must match the leg side."
            )

        self.thigh.validate()
        self.knee.validate()
        self.lower_leg.validate()
        self.ankle.validate()
        self.foot.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "thigh": self.thigh.to_dict(),
            "knee": self.knee.to_dict(),
            "lower_leg": self.lower_leg.to_dict(),
            "ankle": self.ankle.to_dict(),
            "foot": self.foot.to_dict(),
        }