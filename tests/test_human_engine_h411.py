import unittest

from human.anatomy import Head, HeadDimensions, HeadProportions


class TestHumanEngineH411(unittest.TestCase):
    def test_head_dimensions_defaults(self):
        dimensions = HeadDimensions()

        self.assertEqual(dimensions.cranial_height, 22.0)
        self.assertEqual(dimensions.cranial_width, 15.0)
        self.assertEqual(dimensions.cranial_depth, 19.0)

    def test_head_dimensions_reject_non_positive(self):
        with self.assertRaises(ValueError):
            HeadDimensions(cranial_width=0)

    def test_head_proportions_defaults(self):
        proportions = HeadProportions()

        self.assertEqual(proportions.cephalic_index, 78.0)
        self.assertGreater(proportions.face_to_head_height, 0)

    def test_head_proportions_reject_non_positive(self):
        with self.assertRaises(ValueError):
            HeadProportions(cephalic_index=0)

    def test_head_contains_morphometric_core(self):
        head = Head()

        self.assertIsInstance(head.dimensions, HeadDimensions)
        self.assertIsInstance(head.proportions, HeadProportions)
        self.assertIsNotNone(head.face)

    def test_head_serializes_morphometric_core(self):
        head = Head()
        data = head.to_dict()

        self.assertIn("dimensions", data)
        self.assertIn("proportions", data)
        self.assertIn("face", data)


if __name__ == "__main__":
    unittest.main()
