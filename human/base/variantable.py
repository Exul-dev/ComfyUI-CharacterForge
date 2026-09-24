from __future__ import annotations

from .semantic import SemanticComponent


class Variantable(SemanticComponent):
    """
    Component capable of participating in controlled variants.
    """

    def get_variant_payload(self) -> dict:
        return {}
