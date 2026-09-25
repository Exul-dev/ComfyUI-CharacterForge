"""Female genitalia (Human Engine, H4.20).

Structural description at the MammaryRegion standard: the vulva
is described through its bilateral labial structures (majora and
minora — labial asymmetry is the anatomical norm) and the
clitoral structure. The mons pubis already lives in PubicRegion
(H4.19-B) and is not duplicated here.
"""

from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class LabiumMajus(AnatomyComponent):
    """Represents one labium majus (outer lip)."""

    component_type = "labium_majus"

    VALID_SHAPES = (
        "flat",
        "full",
        "drooping",
    )

    def __init__(
        self,
        *,
        side: BodySide,
        length: float = 7.0,
        width: float = 2.0,
        thickness: float = 1.0,
        prominence: float = 0.5,
        pigmentation: float = 0.4,
        shape: str = "full",
    ) -> None:
        super().__init__()

        self.side = side
        self.length = float(length)
        self.width = float(width)
        self.thickness = float(thickness)
        self.prominence = float(prominence)
        self.pigmentation = float(pigmentation)
        self.shape = shape

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError(
                "LabiumMajus side must be a BodySide value."
            )

        for name in ("length", "width", "thickness"):
            value = getattr(self, name)

            if value <= 0:
                raise ValueError(
                    f"LabiumMajus {name} must be greater than "
                    "zero."
                )

        for name in ("prominence", "pigmentation"):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"LabiumMajus {name} must be between 0 and 1."
                )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid labium majus shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "length": self.length,
            "width": self.width,
            "thickness": self.thickness,
            "prominence": self.prominence,
            "pigmentation": self.pigmentation,
            "shape": self.shape,
        }


class LabiumMinus(AnatomyComponent):
    """Represents one labium minus (inner lip).

    protrusion_beyond_majora is how far the inner lip reads past
    the outer — a real and variable morphological trait.
    """

    component_type = "labium_minus"

    def __init__(
        self,
        *,
        side: BodySide,
        length: float = 4.5,
        width: float = 1.2,
        protrusion_beyond_majora: float = 0.3,
    ) -> None:
        super().__init__()

        self.side = side
        self.length = float(length)
        self.width = float(width)
        self.protrusion_beyond_majora = float(
            protrusion_beyond_majora
        )

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError(
                "LabiumMinus side must be a BodySide value."
            )

        if self.length <= 0:
            raise ValueError(
                "LabiumMinus length must be greater than zero."
            )

        if self.width <= 0:
            raise ValueError(
                "LabiumMinus width must be greater than zero."
            )

        if not 0.0 <= self.protrusion_beyond_majora <= 1.0:
            raise ValueError(
                "LabiumMinus protrusion_beyond_majora must be "
                "between 0 and 1."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "length": self.length,
            "width": self.width,
            "protrusion_beyond_majora": (
                self.protrusion_beyond_majora
            ),
        }


class ClitoralStructure(AnatomyComponent):
    """Represents the externally visible clitoral structure."""

    component_type = "clitoral_structure"

    def __init__(
        self,
        *,
        glans_size: float = 0.3,
        hood_coverage: float = 0.6,
        prominence: float = 0.3,
    ) -> None:
        super().__init__()

        self.glans_size = float(glans_size)
        self.hood_coverage = float(hood_coverage)
        self.prominence = float(prominence)

        self.validate()

    def validate(self) -> None:
        super().validate()

        for name in ("glans_size", "hood_coverage", "prominence"):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"ClitoralStructure {name} must be between "
                    "0 and 1."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "glans_size": self.glans_size,
            "hood_coverage": self.hood_coverage,
            "prominence": self.prominence,
        }


class Vulva(AnatomyComponent):
    """Composite vulva: bilateral labia + clitoral structure."""

    component_type = "vulva"

    def __init__(
        self,
        *,
        labia_majora_left: LabiumMajus | None = None,
        labia_majora_right: LabiumMajus | None = None,
        labia_minora_left: LabiumMinus | None = None,
        labia_minora_right: LabiumMinus | None = None,
        clitoral: ClitoralStructure | None = None,
    ) -> None:
        super().__init__()

        self.labia_majora_left = (
            labia_majora_left
            or LabiumMajus(side=BodySide.LEFT)
        )
        self.labia_majora_right = (
            labia_majora_right
            or LabiumMajus(side=BodySide.RIGHT)
        )
        self.labia_minora_left = (
            labia_minora_left
            or LabiumMinus(side=BodySide.LEFT)
        )
        self.labia_minora_right = (
            labia_minora_right
            or LabiumMinus(side=BodySide.RIGHT)
        )
        self.clitoral = clitoral or ClitoralStructure()

        self.validate()

    def validate(self) -> None:
        super().validate()

        pairs = (
            ("labia_majora_left", BodySide.LEFT),
            ("labia_majora_right", BodySide.RIGHT),
        )

        for name, expected_side in pairs:
            value = getattr(self, name)

            if not isinstance(value, LabiumMajus):
                raise ValueError(
                    f"Vulva {name} must be a LabiumMajus "
                    "instance."
                )

            if value.side is not expected_side:
                raise ValueError(
                    f"Vulva {name} must have "
                    f"{expected_side.value} side."
                )

        minora_pairs = (
            ("labia_minora_left", BodySide.LEFT),
            ("labia_minora_right", BodySide.RIGHT),
        )

        for name, expected_side in minora_pairs:
            value = getattr(self, name)

            if not isinstance(value, LabiumMinus):
                raise ValueError(
                    f"Vulva {name} must be a LabiumMinus "
                    "instance."
                )

            if value.side is not expected_side:
                raise ValueError(
                    f"Vulva {name} must have "
                    f"{expected_side.value} side."
                )

        if not isinstance(self.clitoral, ClitoralStructure):
            raise ValueError(
                "Vulva clitoral must be a ClitoralStructure "
                "instance."
            )

        for value in (
            self.labia_majora_left,
            self.labia_majora_right,
            self.labia_minora_left,
            self.labia_minora_right,
            self.clitoral,
        ):
            value.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "labia_majora_left": self.labia_majora_left.to_dict(),
            "labia_majora_right": (
                self.labia_majora_right.to_dict()
            ),
            "labia_minora_left": self.labia_minora_left.to_dict(),
            "labia_minora_right": (
                self.labia_minora_right.to_dict()
            ),
            "clitoral": self.clitoral.to_dict(),
        }


class FemaleGenitalia(AnatomyComponent):
    """Composite female genitalia (pattern MammaryRegion).

    The mons pubis lives in PubicRegion and is not duplicated.
    """

    component_type = "female_genitalia"

    def __init__(
        self,
        *,
        vulva: Vulva | None = None,
    ) -> None:
        super().__init__()

        self.vulva = vulva or Vulva()

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.vulva, Vulva):
            raise ValueError(
                "FemaleGenitalia vulva must be a Vulva instance."
            )

        self.vulva.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "vulva": self.vulva.to_dict(),
        }