from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .arms import Arms
from .legs import Legs
from .pelvis import Pelvis
from .back import Back
from .body_fat import BodyFat
from .body_type import BodyType, Height, Proportions
from .chest import Chest
from .musculature import Musculature
from .neck import Neck
from .ribcage import RibCage
from .shoulders import Shoulders
from .torso import Torso


class HumanAnatomy(AnatomyComponent):
    component_type = "human_anatomy"

    def __init__(
        self,
        *,
        body_type=None,
        height=None,
        proportions=None,
        musculature=None,
        body_fat=None,
        neck=None,
        shoulders=None,
        torso=None,
        chest=None,
        ribcage=None,
        back=None,
        arms=None,
        pelvis=None,
        legs=None,
    ):
        super().__init__()

        self.body_type = body_type or BodyType()
        self.height = height or Height()
        self.proportions = proportions or Proportions()
        self.musculature = musculature or Musculature()
        self.body_fat = body_fat or BodyFat()
        self.neck = neck or Neck()
        self.shoulders = shoulders or Shoulders()
        self.torso = torso or Torso()
        self.chest = chest or Chest()
        self.ribcage = ribcage or RibCage()
        self.back = back or Back()
        self.arms = arms or Arms()
        self.pelvis = pelvis or Pelvis()
        self.legs = legs or Legs()

        self.validate()

    def validate(self):
        super().validate()

        for component in (
            self.body_type,
            self.height,
            self.proportions,
            self.musculature,
            self.body_fat,
            self.neck,
            self.shoulders,
            self.torso,
            self.chest,
            self.ribcage,
            self.back,
            self.arms,
            self.pelvis,
            self.legs,
        ):
            component.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "body_type": self.body_type.to_dict(),
            "height": self.height.to_dict(),
            "proportions": self.proportions.to_dict(),
            "musculature": self.musculature.to_dict(),
            "body_fat": self.body_fat.to_dict(),
            "neck": self.neck.to_dict(),
            "shoulders": self.shoulders.to_dict(),
            "torso": self.torso.to_dict(),
            "chest": self.chest.to_dict(),
            "ribcage": self.ribcage.to_dict(),
            "back": self.back.to_dict(),
            "arms": self.arms.to_dict(),
            "pelvis": self.pelvis.to_dict(),
            "legs": self.legs.to_dict(),
        }
