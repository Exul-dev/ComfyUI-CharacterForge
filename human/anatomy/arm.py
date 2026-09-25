from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .elbow import Elbow
from .enums import BodySide
from .forearm import Forearm
from .hand import Hand
from .upper_arm import UpperArm
from .wrist import Wrist


class Arm(AnatomyComponent):
    """Represents one complete human arm.

    Each arm owns its own segments and joints, and every sided
    sub-component (elbow, wrist, hand) must match the arm side:
    bilateral asymmetry stays representable, mirroring the Leg
    model of H4.15-B.
    """

    component_type = "arm"

    def __init__(
        self,
        *,
        side: BodySide,
        upper_arm: UpperArm | None = None,
        elbow: Elbow | None = None,
        forearm: Forearm | None = None,
        wrist: Wrist | None = None,
        hand: Hand | None = None,
    ) -> None:
        super().__init__()

        self.side = side
        self.upper_arm = upper_arm or UpperArm()
        self.elbow = elbow or Elbow(side=side)
        self.forearm = forearm or Forearm()
        self.wrist = wrist or Wrist(side=side)
        self.hand = hand or Hand(side=side)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError("Arm side must be a BodySide value.")

        if not isinstance(self.upper_arm, UpperArm):
            raise ValueError(
                "Arm upper_arm must be an UpperArm instance."
            )

        if not isinstance(self.elbow, Elbow):
            raise ValueError("Arm elbow must be an Elbow instance.")

        if not isinstance(self.forearm, Forearm):
            raise ValueError(
                "Arm forearm must be a Forearm instance."
            )

        if not isinstance(self.wrist, Wrist):
            raise ValueError("Arm wrist must be a Wrist instance.")

        if not isinstance(self.hand, Hand):
            raise ValueError("Arm hand must be a Hand instance.")

        if self.elbow.side is not self.side:
            raise ValueError(
                "Arm elbow side must match the arm side."
            )

        if self.wrist.side is not self.side:
            raise ValueError(
                "Arm wrist side must match the arm side."
            )

        if self.hand.side is not self.side:
            raise ValueError(
                "Arm hand side must match the arm side."
            )

        self.upper_arm.validate()
        self.elbow.validate()
        self.forearm.validate()
        self.wrist.validate()
        self.hand.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "upper_arm": self.upper_arm.to_dict(),
            "elbow": self.elbow.to_dict(),
            "forearm": self.forearm.to_dict(),
            "wrist": self.wrist.to_dict(),
            "hand": self.hand.to_dict(),
        }