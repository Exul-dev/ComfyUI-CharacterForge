"""Male genitalia (Human Engine, H4.20).

Structural description at the MammaryRegion standard of detail
(H4.8): morphological parameters, bilateral asymmetry where the
anatomy is bilateral (testicular asymmetry is the anatomical
norm), explicit composability. The dynamic states belong to the
future pose/state layers, not here.
"""

from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent
from .enums import BodySide


class Testicle(AnatomyComponent):
    """Represents one testicle.

    Bilateral with per-side hang: testicular asymmetry is the
    anatomical norm and stays representable (pattern MammaryRegion
    / Ear).
    """

    component_type = "testicle"

    # Anatomical naming starts with "Test" — pytest's collection
    # prefix. This class is anatomy, not a test class: explicitly
    # opted out (documented pytest mechanism, keeps the correct
    # anatomical name).
    __test__ = False

    def __init__(
        self,
        *,
        side: BodySide,
        size: float = 0.5,
        hang: float = 0.5,
    ) -> None:
        super().__init__()

        self.side = side
        self.size = float(size)
        self.hang = float(hang)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.side, BodySide):
            raise ValueError(
                "Testicle side must be a BodySide value."
            )

        for name in ("size", "hang"):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Testicle {name} must be between 0 and 1."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "side": self.side.value,
            "size": self.size,
            "hang": self.hang,
        }


class Scrotum(AnatomyComponent):
    """Represents the scrotum with its bilateral contents."""

    component_type = "scrotum"

    VALID_TEXTURES = (
        "smooth",
        "wrinkled",
    )

    def __init__(
        self,
        *,
        width: float = 6.0,
        tightness: float = 0.5,
        rugae: float = 0.5,
        texture: str = "wrinkled",
        left: Testicle | None = None,
        right: Testicle | None = None,
    ) -> None:
        super().__init__()

        self.width = float(width)
        self.tightness = float(tightness)
        self.rugae = float(rugae)
        self.texture = texture
        self.left = left or Testicle(side=BodySide.LEFT)
        self.right = right or Testicle(side=BodySide.RIGHT)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.width <= 0:
            raise ValueError(
                "Scrotum width must be greater than zero."
            )

        for name in ("tightness", "rugae"):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Scrotum {name} must be between 0 and 1."
                )

        if self.texture not in self.VALID_TEXTURES:
            raise ValueError(
                f"Invalid scrotum texture: {self.texture!r}. "
                f"Expected one of {self.VALID_TEXTURES}."
            )

        if not isinstance(self.left, Testicle):
            raise ValueError(
                "Scrotum.left must be a Testicle instance."
            )

        if not isinstance(self.right, Testicle):
            raise ValueError(
                "Scrotum.right must be a Testicle instance."
            )

        if self.left.side is not BodySide.LEFT:
            raise ValueError(
                "Scrotum.left must have BodySide.LEFT."
            )

        if self.right.side is not BodySide.RIGHT:
            raise ValueError(
                "Scrotum.right must have BodySide.RIGHT."
            )

        self.left.validate()
        self.right.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "width": self.width,
            "tightness": self.tightness,
            "rugae": self.rugae,
            "texture": self.texture,
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }


class Penis(AnatomyComponent):
    """Represents the penis (structural dimensions).

    Lengths are the two structural references (flaccid / erect);
    the CURRENT state is a pose/state concern, not anatomy.
    """

    component_type = "penis"

    VALID_GLANS_SHAPES = (
        "tapered",
        "round",
        "mushroom",
    )

    VALID_CIRCUMCISIONS = (
        "circumcised",
        "uncircumcised",
    )

    VALID_CURVATURE_DIRECTIONS = (
        "none",
        "up",
        "down",
        "left",
        "right",
    )

    def __init__(
        self,
        *,
        length_flaccid: float = 9.0,
        length_erect: float = 13.5,
        girth_erect: float = 11.5,
        glans_shape: str = "tapered",
        circumcision: str = "uncircumcised",
        curvature_direction: str = "none",
        curvature_degree: float = 0.0,
        veination: float = 0.4,
    ) -> None:
        super().__init__()

        self.length_flaccid = float(length_flaccid)
        self.length_erect = float(length_erect)
        self.girth_erect = float(girth_erect)
        self.glans_shape = glans_shape
        self.circumcision = circumcision
        self.curvature_direction = curvature_direction
        self.curvature_degree = float(curvature_degree)
        self.veination = float(veination)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.length_flaccid <= 0:
            raise ValueError(
                "Penis length_flaccid must be greater than zero."
            )

        if self.length_erect <= 0:
            raise ValueError(
                "Penis length_erect must be greater than zero."
            )

        if self.girth_erect <= 0:
            raise ValueError(
                "Penis girth_erect must be greater than zero."
            )

        if self.glans_shape not in self.VALID_GLANS_SHAPES:
            raise ValueError(
                f"Invalid penis glans shape: "
                f"{self.glans_shape!r}. "
                f"Expected one of {self.VALID_GLANS_SHAPES}."
            )

        if self.circumcision not in self.VALID_CIRCUMCISIONS:
            raise ValueError(
                f"Invalid penis circumcision: "
                f"{self.circumcision!r}. "
                f"Expected one of {self.VALID_CIRCUMCISIONS}."
            )

        if (
            self.curvature_direction
            not in self.VALID_CURVATURE_DIRECTIONS
        ):
            raise ValueError(
                f"Invalid penis curvature direction: "
                f"{self.curvature_direction!r}. "
                f"Expected one of "
                f"{self.VALID_CURVATURE_DIRECTIONS}."
            )

        if not 0.0 <= self.curvature_degree <= 1.0:
            raise ValueError(
                "Penis curvature_degree must be between 0 and 1."
            )

        if not 0.0 <= self.veination <= 1.0:
            raise ValueError(
                "Penis veination must be between 0 and 1."
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "length_flaccid": self.length_flaccid,
            "length_erect": self.length_erect,
            "girth_erect": self.girth_erect,
            "glans_shape": self.glans_shape,
            "circumcision": self.circumcision,
            "curvature_direction": self.curvature_direction,
            "curvature_degree": self.curvature_degree,
            "veination": self.veination,
        }


class MaleGenitalia(AnatomyComponent):
    """Composite male genitalia (pattern MammaryRegion)."""

    component_type = "male_genitalia"

    def __init__(
        self,
        *,
        penis: Penis | None = None,
        scrotum: Scrotum | None = None,
    ) -> None:
        super().__init__()

        self.penis = penis or Penis()
        self.scrotum = scrotum or Scrotum()

        self.validate()

    def validate(self) -> None:
        super().validate()

        if not isinstance(self.penis, Penis):
            raise ValueError(
                "MaleGenitalia penis must be a Penis instance."
            )

        if not isinstance(self.scrotum, Scrotum):
            raise ValueError(
                "MaleGenitalia scrotum must be a Scrotum "
                "instance."
            )

        self.penis.validate()
        self.scrotum.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "penis": self.penis.to_dict(),
            "scrotum": self.scrotum.to_dict(),
        }
