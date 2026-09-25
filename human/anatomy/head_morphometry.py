"""Morphometric derivation layer for the human head.

Extends the H4.13 derivation chain above the face:

- FaceDimensions (derived or declared) become HeadDimensions through
  explicit cranial fallbacks: the canonical facial landmarks do not
  cover the neurocranium, so cranial measurements cannot be derived
  from them yet;
- HeadDimensions become HeadProportions (finally derived, not
  declared).

Design notes:

- cranial_length follows cranial_depth and cranial_breadth follows
  cranial_width, mirroring the declared H4.11 defaults where the
  two pairs are identical (19/19 and 15/15);
- cranial_height_to_width uses the neurocranial height (the vault
  height above the facial plane), which is the anthropometric
  reading that reproduces the declared H4.11 default
  (13/15 = 0.87);
- the cephalic index is the classic breadth/length * 100 ratio: the
  declared H4.11 default (78.0) is the tabulated mesocephalic mean,
  while the value derived from the dimensional defaults is 78.95.
"""

from __future__ import annotations

import math

from .face_dimensions import FaceDimensions
from .head_dimensions import HeadDimensions
from .head_proportions import HeadProportions


def _require_positive_finite(value: object, name: str) -> None:
    """Raise ValueError unless value is a positive finite number."""

    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(float(value))
        or value <= 0
    ):
        raise ValueError(
            f"head_dimensions_from_face_dimensions {name} "
            "must be a positive finite number."
        )


def head_dimensions_from_face_dimensions(
    face_dimensions: FaceDimensions,
    *,
    cranial_height: float = 22.0,
    cranial_width: float = 15.0,
    cranial_depth: float = 19.0,
    cranial_circumference: float = 56.0,
    neurocranial_height: float = 13.0,
) -> HeadDimensions:
    """Build HeadDimensions from facial dimensions plus cranial
    fallbacks.

    The facial measurements (facial height, bizygomatic and bigonial
    widths) are injected from the given FaceDimensions so that the
    head model stays consistent with the derived face. The cranial
    measurements are explicit fallbacks because the canonical facial
    landmarks do not cover the neurocranium. cranial_length follows
    cranial_depth and cranial_breadth follows cranial_width.
    """

    if not isinstance(face_dimensions, FaceDimensions):
        raise ValueError(
            "head_dimensions_from_face_dimensions requires a "
            "FaceDimensions instance."
        )

    face_dimensions.validate()

    fallbacks = {
        "cranial_height": cranial_height,
        "cranial_width": cranial_width,
        "cranial_depth": cranial_depth,
        "cranial_circumference": cranial_circumference,
        "neurocranial_height": neurocranial_height,
    }

    for name, value in fallbacks.items():
        _require_positive_finite(value, name)

    return HeadDimensions(
        cranial_height=float(cranial_height),
        cranial_width=float(cranial_width),
        cranial_depth=float(cranial_depth),
        cranial_length=float(cranial_depth),
        cranial_breadth=float(cranial_width),
        cranial_circumference=float(cranial_circumference),
        neurocranial_height=float(neurocranial_height),
        facial_height=face_dimensions.facial_height,
        bizygomatic_width=face_dimensions.bizygomatic_width,
        bigonial_width=face_dimensions.bigonial_width,
    )


def head_proportions_from_dimensions(
    dimensions: HeadDimensions,
) -> HeadProportions:
    """Derive HeadProportions from HeadDimensions.

    This closes the H4.11 note for the head: proportions are finally
    derived from the dimensional model instead of being declared by
    hand. cranial_height_to_width reads the neurocranial height (the
    vault height above the facial plane), consistent with the
    declared H4.11 default.
    """

    if not isinstance(dimensions, HeadDimensions):
        raise ValueError(
            "head_proportions_from_dimensions requires a "
            "HeadDimensions instance."
        )

    dimensions.validate()

    return HeadProportions(
        cephalic_index=(
            dimensions.cranial_breadth
            / dimensions.cranial_length
            * 100.0
        ),
        cranial_height_to_width=(
            dimensions.neurocranial_height
            / dimensions.cranial_width
        ),
        cranial_depth_to_width=(
            dimensions.cranial_depth / dimensions.cranial_width
        ),
        face_to_head_height=(
            dimensions.facial_height / dimensions.cranial_height
        ),
        face_to_head_width=(
            dimensions.bizygomatic_width
            / dimensions.cranial_width
        ),
        neurocranium_to_face_height=(
            dimensions.neurocranial_height
            / dimensions.facial_height
        ),
        bizygomatic_to_bigonial=(
            dimensions.bizygomatic_width
            / dimensions.bigonial_width
        ),
    )