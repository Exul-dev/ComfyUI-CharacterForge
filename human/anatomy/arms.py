from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .arm import Arm
from .elbow import Elbow
from .enums import BodySide
from .forearm import Forearm
from .hands import Hands
from .shoulders import Shoulders
from .upper_arm import UpperArm
from .wrist import Wrist


class Arms(AnatomyComponent):
    """Composite anatomical component representing the upper limbs.

    Dual-mode model (pattern Shoulders, H4.5):

    - legacy shared model: shoulders, upper_arm, elbow, forearm,
      wrist, hands — the H4.2/H4.3 public API, kept intact for
      compatibility. The shared segments describe both arms with
      one value and cannot represent asymmetry;
    - structured bilateral model: left and right Arm (H4.17), each
      owning its complete side-matched chain (upper_arm, elbow,
      forearm, wrist, hand). Bilateral asymmetry stays
      representable.

    The two models are independent: setting legacy parameters does
    not alter the bilateral arms and vice versa. New code should
    prefer left/right; the shared model is legacy.
    """

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
        left: Arm | None = None,
        right: Arm | None = None,
    ) -> None:
        super().__init__()

        # Legacy shared model (H4.2/H4.3 API).
        self.shoulders = shoulders or Shoulders()
        self.upper_arm = upper_arm or UpperArm()
        self.elbow = elbow or Elbow()
        self.forearm = forearm or Forearm()
        self.wrist = wrist or Wrist()
        self.hands = hands or Hands()

        # Structured bilateral model (H4.17).
        self.left = left or Arm(side=BodySide.LEFT)
        self.right = right or Arm(side=BodySide.RIGHT)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.shoulders, Shoulders):
            raise ValueError(
                "Arms shoulders must be a Shoulders instance."
            )

        if not isinstance(self.upper_arm, UpperArm):
            raise ValueError(
                "Arms upper_arm must be an UpperArm instance."
            )

        if not isinstance(self.elbow, Elbow):
            raise ValueError(
                "Arms elbow must be an Elbow instance."
            )

        if not isinstance(self.forearm, Forearm):
            raise ValueError(
                "Arms forearm must be a Forearm instance."
            )

        if not isinstance(self.wrist, Wrist):
            raise ValueError("Arms wrist must be a Wrist instance.")

        if not isinstance(self.hands, Hands):
            raise ValueError("Arms hands must be a Hands instance.")

        if not isinstance(self.left, Arm):
            raise ValueError("Arms.left must be an Arm instance.")

        if not isinstance(self.right, Arm):
            raise ValueError("Arms.right must be an Arm instance.")

        if self.left.side is not BodySide.LEFT:
            raise ValueError("Arms.left must have BodySide.LEFT.")

        if self.right.side is not BodySide.RIGHT:
            raise ValueError("Arms.right must have BodySide.RIGHT.")

        self.shoulders.validate()
        self.upper_arm.validate()
        self.elbow.validate()
        self.forearm.validate()
        self.wrist.validate()
        self.hands.validate()
        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            # Legacy shared model.
            "shoulders": self.shoulders.to_dict(),
            "upper_arm": self.upper_arm.to_dict(),
            "elbow": self.elbow.to_dict(),
            "forearm": self.forearm.to_dict(),
            "wrist": self.wrist.to_dict(),
            "hands": self.hands.to_dict(),
            # Structured bilateral model.
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }