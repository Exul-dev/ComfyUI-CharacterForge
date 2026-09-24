from __future__ import annotations

from .semantic import SemanticComponent


class Reproducible(SemanticComponent):
    """
    Component whose semantic representation can be reproduced
    deterministically from explicit configuration.
    """

    seed: int | None = None

    def set_seed(self, seed: int | None) -> None:
        if seed is not None and not isinstance(seed, int):
            raise TypeError("seed must be int or None")

        self.seed = seed
