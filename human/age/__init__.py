"""The Age Engine (Human Engine, H6).

Where age becomes appearance. The engine's layers:

- the VOCABULARY (H6-A): SkinAging, HairAging, FaceAging —
  the ~44 dials of age, spread over three layers;
- the CURVES (H6-C1, this package): AgeCurves, the matrix
  age -> axis values, each axis with its real onset, slope
  and shape (gerontology, not invention);
- the OPERATOR (H6-C2): apparent_age(), the one-dial API that
  configures every aging component proportionally — with a
  changed/preserved report;
- TRAJECTORIES (H6-D): age_at(t), coherent forward/backward
  time travel for one identity;
- the BODY (H6-B): musculature, fat, stature aging.

Principle: complex underneath, simple on top. The eventual
ComfyUI node exposes ONE dial (the age); everything in this
package makes that one dial truthful.
"""

from .curves import AgeCurves, AgeAxis
from .operator import (
    AgeResult,
    FieldChange,
    apparent_age,
)

__all__ = [
    "AgeCurves",
    "AgeAxis",
    "AgeResult",
    "FieldChange",
    "apparent_age",
]
