from __future__ import annotations

from enum import Enum


class BodySide(Enum):
    """Semantic side of a bilateral anatomical structure."""

    LEFT = "left"
    RIGHT = "right"


class FingerType(Enum):
    """Semantic type of a human finger."""

    THUMB = "thumb"
    INDEX = "index"
    MIDDLE = "middle"
    RING = "ring"
    LITTLE = "little"
class ToeType(Enum):
    """Semantic type of a human toe."""

    HALLUX = "hallux"
    SECOND = "second"
    THIRD = "third"
    FOURTH = "fourth"
    FIFTH = "fifth"
