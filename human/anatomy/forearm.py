from __future__ import annotations

from .anatomy_component import AnatomyComponent


class Forearm(AnatomyComponent):
    """Represents the forearm anatomical structure.

    H4.4 foundation, enriched in H4.19-D (brachioradialis and
    ulna definition, vascularity) and in H5-D-3 with
    flexor_definition — completing the soft-tissue trio that the
    other three limb segments carry, for four-segment parity (9
    parameters each). The anterior flexor mass is the visible
    bulk of the forearm. Legacy constructor checks (eager, exact
    messages) preserved verbatim.
    """

    component_type = "forearm"

    VALID_SHAPES = (
        "slender",
        "average",
        "athletic",
        "muscular",
        "robust",
    )

    def __init__(
        self,
        *,
        length: float = 26.0,
        circumference: float = 24.0,
        width: float = 7.5,
        depth: float = 7.0,
        shape: str = "average",
        brachioradialis_definition: float = 0.4,
        ulna_definition: float = 0.4,
        flexor_definition: float = 0.4,
        vascularity: float = 0.3,
    ) -> None:
        super().__init__()

        if length <= 0:
            raise ValueError("Forearm length must be greater than zero.")

        if circumference <= 0:
            raise ValueError("Forearm circumference must be greater than zero.")

        if shape not in self.VALID_SHAPES:
            raise ValueError(
                f"Invalid forearm shape: {shape!r}. "
                f"Expected one of {self.VALID_SHAPES}."
            )

        self.length = float(length)
        self.circumference = float(circumference)
        self.width = float(width)
        self.depth = float(depth)
        self.shape = shape
        self.brachioradialis_definition = float(brachioradialis_definition)
        self.ulna_definition = float(ulna_definition)
        self.flexor_definition = float(flexor_definition)
        self.vascularity = float(vascularity)

        self.validate()

    def validate(self) -> None:
        super().validate()

        if self.length <= 0:
            raise ValueError("Forearm length must be greater than zero.")

        if self.circumference <= 0:
            raise ValueError("Forearm circumference must be greater than zero.")

        if self.width <= 0:
            raise ValueError("Forearm width must be greater than zero.")

        if self.depth <= 0:
            raise ValueError("Forearm depth must be greater than zero.")

        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid forearm shape: {self.shape!r}.")

        for name in (
            "brachioradialis_definition",
            "ulna_definition",
            "flexor_definition",
            "vascularity",
        ):
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Forearm {name} must be between 0 and 1."
                )

    def to_dict(self) -> dict:
        return {
            **super().to_dict(),
            "length": self.length,
            "circumference": self.circumference,
            "width": self.width,
            "depth": self.depth,
            "shape": self.shape,
            "brachioradialis_definition": self.brachioradialis_definition,
            "ulna_definition": self.ulna_definition,
            "flexor_definition": self.flexor_definition,
            "vascularity": self.vascularity,
        }