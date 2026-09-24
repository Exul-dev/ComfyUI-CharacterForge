from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .elbow import Elbow
from .forearm import Forearm
from .hands import Hands
from .shoulders import Shoulders
from .upper_arm import UpperArm
from .wrist import Wrist


class Arms(AnatomyComponent):
    """Composite anatomical component representing the upper limbs."""

    component_type = "arms"

    def __init__(
        self,
        *,
        shoulders: Shoulders | None = None,
        upper_arm: UpperArm | None = None,
        elbow: Elbow | None = None,
        forearm: Forearm | None = None,
        wrist: Wrist | None = None,
        hands: Hands | None = None,
    ) -> None:
        super().__init__()

        self.shoulders = shoulders or Shoulders()
        self.upper_arm = upper_arm or UpperArm()
        self.elbow = elbow or Elbow()
        self.forearm = forearm or Forearm()
        self.wrist = wrist or Wrist()
        self.hands = hands or Hands()

        self.validate()

    def validate(self) -> None:
        super().validate()

        self.shoulders.validate()
        self.upper_arm.validate()
        self.elbow.validate()
        self.forearm.validate()
        self.wrist.validate()
        self.hands.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "shoulders": self.shoulders.to_dict(),
            "upper_arm": self.upper_arm.to_dict(),
            "elbow": self.elbow.to_dict(),
            "forearm": self.forearm.to_dict(),
            "wrist": self.wrist.to_dict(),
            "hands": self.hands.to_dict(),
        }
