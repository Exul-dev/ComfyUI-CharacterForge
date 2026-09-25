import unittest

from human.anatomy import (
    BodySide,
    CheekStructure,
    Chin,
    Face,
    FaceDimensions,
    FacialLandmarks,
    FacialProportions,
    FacialSymmetry,
    Forehead,
    Jaw,
)


class TestHumanEngineH410(unittest.TestCase):
    def test_face_dimensions_defaults(self):
        dimensions = FaceDimensions()
        self.assertEqual(dimensions.facial_height, 18.0)
        self.assertEqual(dimensions.bizygomatic_width, 14.0)

    def test_face_dimensions_reject_non_positive(self):
        with self.assertRaises(ValueError):
            FaceDimensions(facial_width=0)

    def test_facial_proportions_defaults(self):
        proportions = FacialProportions()
        self.assertGreater(proportions.cheek_to_jaw_ratio, 0)

    def test_facial_proportions_reject_non_positive(self):
        with self.assertRaises(ValueError):
            FacialProportions(jaw_to_chin_ratio=0)

    def test_forehead(self):
        forehead = Forehead(
            height=6.5,
            width=13.0,
            shape="prominent",
        )
        self.assertEqual(forehead.shape, "prominent")

    def test_cheeks_are_bilateral(self):
        left = CheekStructure(side=BodySide.LEFT, prominence=0.8)
        right = CheekStructure(side=BodySide.RIGHT, prominence=0.4)
        self.assertIs( left.side, BodySide.LEFT)
        self.assertIs(right.side, BodySide.RIGHT)
        self.assertNotEqual(left.prominence, right.prominence)

    def test_jaw_is_bilateral(self):
        left = Jaw(side=BodySide.LEFT, gonial_angle=118)
        right = Jaw(side=BodySide.RIGHT, gonial_angle=130)
        self.assertEqual(left.side, BodySide.LEFT)
        self.assertEqual(right.side, BodySide.RIGHT)
        self.assertNotEqual(left.gonial_angle, right.gonial_angle)

    def test_chin(self):
        chin = Chin(
            width=4.5,
            projection=2.8,
            shape="prominent",
        )
        self.assertEqual(chin.shape, "prominent")

    def test_symmetry(self):
        symmetry = FacialSymmetry(
            global_symmetry=0.94,
            upper_face=0.96,
            mid_face=0.92,
            lower_face=0.95,
        )
        self.assertEqual(symmetry.global_symmetry, 0.94)

    def test_landmarks(self):
        landmarks = FacialLandmarks(
            points={
                "glabella": (0.50, 0.31, 0.10),
                "pronasale": (0.50, 0.52, 0.30),
                "gnathion": (0.50, 0.91, 0.02),
            }
        )
        self.assertEqual(len(landmarks.points), 3)

    def test_landmarks_reject_unknown_name(self):
        with self.assertRaises(ValueError):
            FacialLandmarks(
                points={"unknown": (0.5, 0.5, 0.0)}
            )

    def test_face_contains_morphometric_core(self):
        face = Face()
        self.assertIsInstance(face.dimensions, FaceDimensions)
        self.assertIsInstance(face.proportions, FacialProportions)
        self.assertIsInstance(face.forehead, Forehead)
        self.assertIsInstance(face.left_cheek, CheekStructure)
        self.assertIsInstance(face.right_cheek, CheekStructure)
        self.assertIsInstance(face.left_jaw, Jaw)
        self.assertIsInstance(face.right_jaw, Jaw)
        self.assertIsInstance(face.chin, Chin)
        self.assertIsInstance(face.facial_symmetry, FacialSymmetry)
        self.assertIsInstance(face.landmarks, FacialLandmarks)

    def test_face_enforces_bilateral_sides(self):
        with self.assertRaises(ValueError):
            Face(
                left_cheek=CheekStructure(side=BodySide.RIGHT)
            )

        with self.assertRaises(ValueError):
            Face(
                right_jaw=Jaw(side=BodySide.LEFT)
            )

    def test_face_serializes_morphometric_core(self):
        face = Face(
            left_cheek=CheekStructure(
                side=BodySide.LEFT,
                prominence=0.75,
            ),
            landmarks=FacialLandmarks(
                points={"glabella": (0.5, 0.3, 0.1)}
            ),
        )
        data = face.to_dict()

        self.assertIn("dimensions", data)
        self.assertIn("proportions", data)
        self.assertIn("forehead", data)
        self.assertIn("left_cheek", data)
        self.assertIn("right_cheek", data)
        self.assertIn("left_jaw", data)
        self.assertIn("right_jaw", data)
        self.assertIn("chin", data)
        self.assertIn("facial_symmetry", data)
        self.assertIn("landmarks", data)
        self.assertEqual(
            data["left_cheek"]["side"],
            "left",
        )


if __name__ == "__main__":
    unittest.main()
