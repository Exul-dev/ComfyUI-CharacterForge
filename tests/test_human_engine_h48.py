from __future__ import annotations

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from human.anatomy import (
    AnatomyComponent,
    Areola,
    BodySide,
    Breast,
    BreastUnit,
    MammaryRegion,
    Nipple,
)


class TestHumanEngineH48(unittest.TestCase):

    def test_breast_is_real_component(self) -> None:
        breast = Breast(
            side=BodySide.LEFT,
            width=14.0,
            height=13.0,
            projection=5.5,
            shape="round",
        )

        self.assertIsInstance(breast, AnatomyComponent)
        self.assertEqual(breast.component_type, "breast")
        self.assertEqual(breast.side, BodySide.LEFT)
        self.assertEqual(breast.shape, "round")
        self.assertTrue(breast.is_valid())

    def test_nipple_is_real_component(self) -> None:
        nipple = Nipple(
            side=BodySide.LEFT,
            diameter=1.2,
            projection=0.7,
            shape="prominent",
        )

        self.assertIsInstance(nipple, AnatomyComponent)
        self.assertEqual(nipple.component_type, "nipple")
        self.assertEqual(nipple.side, BodySide.LEFT)
        self.assertEqual(nipple.shape, "prominent")
        self.assertTrue(nipple.is_valid())

    def test_areola_is_real_component(self) -> None:
        areola = Areola(
            side=BodySide.RIGHT,
            diameter=4.5,
            shape="oval",
        )

        self.assertIsInstance(areola, AnatomyComponent)
        self.assertEqual(areola.component_type, "areola")
        self.assertEqual(areola.side, BodySide.RIGHT)
        self.assertEqual(areola.shape, "oval")
        self.assertTrue(areola.is_valid())

    def test_breast_unit_contains_components(self) -> None:
        unit = BreastUnit(side=BodySide.LEFT)

        self.assertIsInstance(unit.breast, Breast)
        self.assertIsInstance(unit.areola, Areola)
        self.assertIsInstance(unit.nipple, Nipple)
        self.assertEqual(unit.side, BodySide.LEFT)
        unit.validate()

    def test_mammary_region_is_bilateral(self) -> None:
        region = MammaryRegion()

        self.assertEqual(region.left.side, BodySide.LEFT)
        self.assertEqual(region.right.side, BodySide.RIGHT)
        self.assertTrue(region.is_valid())

    def test_mammary_region_supports_asymmetry(self) -> None:
        left = BreastUnit(
            side=BodySide.LEFT,
            breast=Breast(
                side=BodySide.LEFT,
                volume=450.0,
                projection=4.5,
            ),
        )

        right = BreastUnit(
            side=BodySide.RIGHT,
            breast=Breast(
                side=BodySide.RIGHT,
                volume=520.0,
                projection=5.2,
            ),
        )

        region = MammaryRegion(
            left=left,
            right=right,
            symmetry=0.85,
        )

        self.assertEqual(region.left.breast.volume, 450.0)
        self.assertEqual(region.right.breast.volume, 520.0)
        self.assertEqual(region.symmetry, 0.85)

    def test_invalid_breast_dimensions_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Breast(width=0)

        with self.assertRaises(ValueError):
            Breast(volume=0)

        with self.assertRaises(ValueError):
            Breast(projection=0)

    def test_invalid_breast_shape_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Breast(shape="invalid")

    def test_invalid_nipple_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Nipple(diameter=0)

        with self.assertRaises(ValueError):
            Nipple(vertical_position=2)

    def test_invalid_areola_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Areola(width=0)

        with self.assertRaises(ValueError):
            Areola(shape="invalid")

    def test_invalid_mammary_symmetry_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MammaryRegion(symmetry=2)

    def test_serialization(self) -> None:
        region = MammaryRegion()
        data = region.to_dict()

        self.assertEqual(data["component_type"], "mammary_region")
        self.assertIn("left", data)
        self.assertIn("right", data)
        self.assertIn("symmetry", data)
        self.assertEqual(
            data["left"]["breast"]["component_type"],
            "breast",
        )
        self.assertEqual(
            data["left"]["nipple"]["component_type"],
            "nipple",
        )
        self.assertEqual(
            data["left"]["areola"]["component_type"],
            "areola",
        )

    def test_side_consistency_is_enforced(self) -> None:
        with self.assertRaises(ValueError):
            BreastUnit(
                side=BodySide.LEFT,
                breast=Breast(side=BodySide.RIGHT),
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
