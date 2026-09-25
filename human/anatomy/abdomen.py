from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .flanks import Flanks


class Navel(AnatomyComponent):
    """Represents the navel (belly button)."""

    component_type = "navel"

    VALID_SHAPES = (
        "innie",
        "outie",
        "flat",
        "vertical",
        "horizontal",
    )

    def __init__(
        self,
        *,
        depth: float = 0.5,
        size: float = 1.0,
        shape: str = "innie",
        position: float = 0.5,
    ) -> None:
        super().__init__()

        self.depth = float(depth)
        self.size = float(size)
        self.shape = shape
        self.position = float(position)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not 0.0 <= self.depth <= 1.0:
            raise ValueError(
                "Navel depth must be between 0 and 1."
            )

        if self.size <= 0:
            raise ValueError(
                "Navel size must be greater than zero."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid navel shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if not 0.0 <= self.position <= 1.0:
            raise ValueError(
                "Navel position must be between 0 and 1."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "depth": self.depth,
            "size": self.size,
            "shape": self.shape,
            "position": self.position,
        }


class Abdomen(AnatomyComponent):
    """Represents the anatomical abdomen.

    Composite since H4.16-B (flanks) and enriched in H4.19-B with
    the navel and explicit muscular definitions (rectus, linea
    alba, obliques).
    """

    component_type = "abdomen"

    VALID_SHAPES = (
        "flat",
        "average",
        "rounded",
        "sculpted",
    )

    def __init__(
        self,
        *,
        length: float = 25.0,
        width: float = 28.0,
        depth: float = 19.0,
        muscularity: float = 0.5,
        fat_distribution: float = 0.5,
        shape: str = "average",
        flanks: Flanks | None = None,
        navel: Navel | None = None,
        rectus_definition: float = 0.5,
        linea_alba_prominence: float = 0.4,
        oblique_definition: float = 0.5,
    ) -> None:
        super().__init__()

        self.length = float(length)
        self.width = float(width)
        self.depth = float(depth)
        self.muscularity = float(muscularity)
        self.fat_distribution = float(fat_distribution)
        self.shape = shape
        self.flanks = flanks or Flanks()
        self.navel = navel or Navel()
        self.rectus_definition = float(rectus_definition)
        self.linea_alba_prominence = float(linea_alba_prominence)
        self.oblique_definition = float(oblique_definition)

        self.validate()

    def validate(self) -> None:
        super().validate()

        dimensions = {
            "length": self.length,
            "width": self.width,
            "depth": self.depth,
        }

        for name, value in dimensions.items():
            if value <= 0:
                raise ValueError(
                    f"Abdomen {name} must be greater than zero."
                )

        for name in (
            "muscularity",
            "rectus_definition",
            "linea_alba_prominence",
            "oblique_definition",
        ):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Abdomen {name} must be between 0 and 1."
                )

        # fat_distribution keeps its exact H4.16-B legacy message
        # ("fat distribution", with a space): error messages ARE the
        # contract — tests match them.
        if not 0.0 <= self.fat_distribution <= 1.0:
            raise ValueError(
                "Abdomen fat distribution must be between 0 and 1."
            )

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid abdomen shape: {self.shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        if not isinstance(self.flanks, Flanks):
            raise ValueError(
                "Abdomen flanks must be a Flanks instance."
            )

        if not isinstance(self.navel, Navel):
            raise ValueError(
                "Abdomen navel must be a Navel instance."
            )

        self.flanks.validate()
        self.navel.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "length": self.length,
            "width": self.width,
            "depth": self.depth,
            "muscularity": self.muscularity,
            "fat_distribution": self.fat_distribution,
            "shape": self.shape,
            "flanks": self.flanks.to_dict(),
            "navel": self.navel.to_dict(),
            "rectus_definition": self.rectus_definition,
            "linea_alba_prominence": self.linea_alba_prominence,
            "oblique_definition": self.oblique_definition,
        }
