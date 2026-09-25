"""Body aging model (Human Engine, H6-B — Age Engine).

The Age Engine's last layer: HOW the body ages below the
face. The axes follow the gerontological literature:

- SARCOPENIA: muscle mass loss — strength drops EARLIER and
  FASTER than mass (the real mass/strength dissociation,
  two separate axes, never conflated);
- FAT REDISTRIBUTION: subcutaneous fat shifts visceral —
  same weight, different silhouette;
- POSTURAL STOOPING: the kyphotic curve, late to arrive;
- STATURE LOSS: proportional (0..1 of the loss potential),
  not absolute centimeters — this layer is RELATIVE;
- BODY SKIN THINNING: the body skin thins with age —
  separate from SkinAging.thinning (which owns the visible
  face/decollete surface: same sign, different layer, the
  documented project split).

Soft integrations (documented, never enforced): the operator
sets these values; they COMPLEMENT Musculature.level,
BodyFat.distribution and Height without ever mutating them —
the anatomy bricks stay independent, the aging layer rides
on top.
"""

from __future__ import annotations

from typing import Any

from ..base.semantic import SemanticComponent


class BodyAging(SemanticComponent):
    """Six-axis body aging state.

    SemanticComponent (not AnatomyComponent): this is not
    anatomy structure — it is the aging STATE that rides on
    top of it (same placement decision as the aging layers:
    registered, optional, composable).
    """

    component_type = "body_aging"

    VALID_AXES = (
        "muscle_mass_loss",
        "strength_loss",
        "fat_redistribution",
        "postural_stooping",
        "stature_loss",
        "body_skin_thinning",
    )

    def __init__(
        self,
        *,
        muscle_mass_loss: float = 0.0,
        strength_loss: float = 0.0,
        fat_redistribution: float = 0.0,
        postural_stooping: float = 0.0,
        stature_loss: float = 0.0,
        body_skin_thinning: float = 0.0,
        enabled: bool = True,
    ) -> None:
        super().__init__(enabled=enabled)

        self.muscle_mass_loss = float(muscle_mass_loss)
        self.strength_loss = float(strength_loss)
        self.fat_redistribution = float(fat_redistribution)
        self.postural_stooping = float(postural_stooping)
        self.stature_loss = float(stature_loss)
        self.body_skin_thinning = float(body_skin_thinning)

        self.validate()

    def validate(self) -> None:
        super().validate()

        for name in self.VALID_AXES:
            value = getattr(self, name)

            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"BodyAging {name} must be between 0 and 1."
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "muscle_mass_loss": self.muscle_mass_loss,
            "strength_loss": self.strength_loss,
            "fat_redistribution": self.fat_redistribution,
            "postural_stooping": self.postural_stooping,
            "stature_loss": self.stature_loss,
            "body_skin_thinning": self.body_skin_thinning,
        }