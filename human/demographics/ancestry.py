from __future__ import annotations

from typing import Any

from .demographic_component import DemographicComponent


class AncestralRegion(DemographicComponent):
    """
    Geographic/historical ancestry region.
    """

    component_type = "ancestral_region"

    def __init__(
        self,
        name: str,
        *,
        proportion: float = 1.0,
    ) -> None:
        super().__init__()

        if not name or not name.strip():
            raise ValueError(
                "Ancestral region name cannot be empty"
            )

        if not 0.0 <= proportion <= 1.0:
            raise ValueError(
                "Ancestral proportion must be between 0 and 1"
            )

        self.name = name
        self.proportion = float(proportion)

    def validate(self) -> None:
        super().validate()

        if not self.name.strip():
            raise ValueError(
                "Ancestral region name cannot be empty"
            )

        if not 0.0 <= self.proportion <= 1.0:
            raise ValueError(
                "Ancestral proportion must be between 0 and 1"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "name": self.name,
            "proportion": self.proportion,
        }


class AncestralComponents(DemographicComponent):
    """
    Collection of ancestral regions.
    """

    component_type = "ancestral_components"

    def __init__(
        self,
        regions: list[AncestralRegion] | None = None,
    ) -> None:
        super().__init__()
        self.regions = list(regions or [])

    def add(self, region: AncestralRegion) -> None:
        if not isinstance(region, AncestralRegion):
            raise TypeError(
                "region must be AncestralRegion"
            )

        region.validate()
        self.regions.append(region)

    def validate(self) -> None:
        super().validate()

        for region in self.regions:
            region.validate()

        total = sum(
            region.proportion
            for region in self.regions
        )

        if total > 1.0 + 1e-9:
            raise ValueError(
                "Ancestral proportions cannot exceed 1.0"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "regions": [
                region.to_dict()
                for region in self.regions
            ],
        }


class Ancestry(DemographicComponent):
    """
    Complete Human ancestry model.
    """

    component_type = "ancestry"

    def __init__(
        self,
        *,
        regions: AncestralComponents | None = None,
    ) -> None:
        super().__init__()

        self.regions = (
            regions or AncestralComponents()
        )

    def validate(self) -> None:
        super().validate()
        self.regions.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "regions": self.regions.to_dict(),
        }
