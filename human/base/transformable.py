from __future__ import annotations

from .semantic import SemanticComponent


class Transformable(SemanticComponent):
    """
    Component capable of participating in transformations.
    """

    def get_transformation_payload(self) -> dict:
        return {}
