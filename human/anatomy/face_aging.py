"""Facial aging model (Human Engine, H6-A3 — Age Engine).

The Age Engine's third layer: HOW the face's soft tissues,
volumes and contours change with age.

Layer placement (the project's structure/appearance split):
this is ANATOMY — soft-tissue structure, volumes, ptosis —
not surface (SkinAging owns lines and texture). The
nasolabial fold appears in both, deliberately: SkinAging owns
the visible LINE (surface crease), FaceAging owns the FOLD
(tissue depth) — two aspects of one sign, each in its layer.

Twelve independent axes, grouped after the gerontological
literature on facial aging:

- SOFT TISSUE DESCENT: midface fat pads descend, jowls form,
  folds deepen;
- VOLUME LOSS: lips thin, earlobes elongate, temples hollow;
- PTOSIS: brows descend, upper lids drop (soft-integrated with
  Brow.height and Eyelid.upper_exposure: documented, never
  enforced — the components stay independent);
- BONY CONTOUR (the extreme): orbital hollowing, mandibular
  definition loss.

Default is age-neutral (0.0 everywhere — pattern of the whole
Age Engine). Nothing is driven by ChronologicalAge: this layer
answers to ApparentAge values or H6-C profiles only.
"""

from __future__ import annotations

from typing import Any

from .anatomy_component import AnatomyComponent


class FaceAging(AnatomyComponent):
    """Twelve-axis facial aging state."""

    component_type = "face_aging"

    VALID_AXES = (
        "midface_descent",
        "jowl_formation",
        "nasolabial_fold_depth",
        "marionette_fold_depth",
        "cheek_hollowing",
        "lip_volume_loss",
        "earlobe_elongation",
        "temporal_hollowing",
        "brow_descent",
        "upper_lid_ptosis",
        "orbital_hollowing",
        "mandibular_definition_loss",
    )

    def __init__(
        self,
        *,
        midface_descent: float = 0.0,
        jowl_formation: float = 0.0,
        nasolabial_fold_depth: float = 0.0,
        marionette_fold_depth: float = 0.0,
        cheek_hollowing: float = 0.0,
        lip_volume_loss: float = 0.0,
        earlobe_elongation: float = 0.0,
        temporal_hollowing: float = 0.0,
        brow_descent: float = 0.0,
        upper_lid_ptosis: float = 0.0,
        orbital_hollowing: float = 0.0,
        mandibular_definition_loss: float = 0.0,
    ) -> None:
        super().__init__()

        self.midface_descent = float(midface_descent)
        self.jowl_formation = float(jowl_formation)
        self.nasolabial_fold_depth = float(nasolabial_fold_depth)
        self.marionette_fold_depth = float(marionette_fold_depth)
        self.cheek_hollowing = float(cheek_hollowing)
        self.lip_volume_loss = float(lip_volume_loss)
        self.earlobe_elongation = float(earlobe_elongation)
        self.temporal_hollowing = float(temporal_hollowing)
        self.brow_descent = float(brow_descent)
        self.upper_lid_ptosis = float(upper_lid_ptosis)
        self.orbital_hollowing = float(orbital_hollowing)
        self.mandibular_definition_loss = float(
            mandibular_definition_loss
        )

        self.validate()

    def validate(self) -> None:
        super().validate()

        for name in self.VALID_AXES:
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"FaceAging {name} must be between 0 and 1."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "midface_descent": self.midface_descent,
            "jowl_formation": self.jowl_formation,
            "nasolabial_fold_depth": self.nasolabial_fold_depth,
            "marionette_fold_depth": self.marionette_fold_depth,
            "cheek_hollowing": self.cheek_hollowing,
            "lip_volume_loss": self.lip_volume_loss,
            "earlobe_elongation": self.earlobe_elongation,
            "temporal_hollowing": self.temporal_hollowing,
            "brow_descent": self.brow_descent,
            "upper_lid_ptosis": self.upper_lid_ptosis,
            "orbital_hollowing": self.orbital_hollowing,
            "mandibular_definition_loss": (
                self.mandibular_definition_loss
            ),
        }