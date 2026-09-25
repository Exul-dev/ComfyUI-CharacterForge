import unittest

from human.anatomy import (
    BodySide,
    Coordinate,
    CoordinateSpace,
    CoordinateSystem,
    Landmark,
    LandmarkSource,
    LandmarkStatus,
)


class TestHumanEngineH412(unittest.TestCase):

    def test_coordinate_space_dimensions(self):
        self.assertEqual(
            CoordinateSpace.IMAGE_2D.dimensions,
            2,
        )

        self.assertEqual(
            CoordinateSpace.NORMALIZED_3D.dimensions,
            3,
        )

        self.assertEqual(
            CoordinateSpace.PHYSICAL_3D.dimensions,
            3,
        )

    def test_coordinate_2d(self):
        coordinate = Coordinate(
            x=0.25,
            y=0.75,
            space=CoordinateSpace.IMAGE_2D,
        )

        self.assertEqual(coordinate.x, 0.25)
        self.assertEqual(coordinate.y, 0.75)
        self.assertIsNone(coordinate.z)

    def test_coordinate_3d_requires_z(self):
        with self.assertRaises(ValueError):
            Coordinate(
                x=0.5,
                y=0.5,
                space=CoordinateSpace.NORMALIZED_3D,
            )

    def test_coordinate_2d_rejects_z(self):
        with self.assertRaises(ValueError):
            Coordinate(
                x=0.5,
                y=0.5,
                z=0.0,
                space=CoordinateSpace.IMAGE_2D,
            )

    def test_anatomical_coordinate_system(self):
        system = CoordinateSystem.anatomical_normalized()

        self.assertEqual(
            system.name,
            "anatomical_normalized",
        )

        self.assertIs(
            system.space,
            CoordinateSpace.NORMALIZED_3D,
        )

        self.assertEqual(
            system.x_axis,
            "left_right",
        )

        self.assertEqual(
            system.y_axis,
            "superior_inferior",
        )

        self.assertEqual(
            system.z_axis,
            "posterior_anterior",
        )

        self.assertEqual(
            system.handedness,
            "right",
        )

    def test_coordinate_system_space_must_match(self):
        system = CoordinateSystem.anatomical_normalized()

        with self.assertRaises(ValueError):
            Coordinate(
                x=0.5,
                y=0.5,
                space=CoordinateSpace.IMAGE_2D,
                system=system,
            )

    def test_landmark_defaults(self):
        coordinate = Coordinate(
            x=0.5,
            y=0.5,
            z=0.0,
            space=CoordinateSpace.NORMALIZED_3D,
        )

        landmark = Landmark(
            name="glabella",
            coordinate=coordinate,
        )

        self.assertEqual(
            landmark.name,
            "glabella",
        )

        self.assertIsNone(
            landmark.side,
        )

        self.assertIs(
            landmark.status,
            LandmarkStatus.UNKNOWN,
        )

        self.assertEqual(
            landmark.confidence,
            0.0,
        )

        self.assertIs(
            landmark.source,
            LandmarkSource.MANUAL,
        )

    def test_landmark_with_observation_metadata(self):
        system = CoordinateSystem.anatomical_normalized()

        coordinate = Coordinate(
            x=0.5,
            y=0.32,
            z=0.08,
            space=CoordinateSpace.NORMALIZED_3D,
            system=system,
        )

        landmark = Landmark(
            name="left_zygion",
            coordinate=coordinate,
            side=BodySide.LEFT,
            status=LandmarkStatus.OBSERVED,
            confidence=0.97,
            source=LandmarkSource.VISION,
        )

        self.assertIs(
            landmark.side,
            BodySide.LEFT,
        )

        self.assertIs(
            landmark.status,
            LandmarkStatus.OBSERVED,
        )

        self.assertEqual(
            landmark.confidence,
            0.97,
        )

        self.assertIs(
            landmark.source,
            LandmarkSource.VISION,
        )

    def test_landmark_rejects_invalid_confidence(self):
        coordinate = Coordinate(
            x=0.5,
            y=0.5,
            z=0.0,
            space=CoordinateSpace.NORMALIZED_3D,
        )

        with self.assertRaises(ValueError):
            Landmark(
                name="glabella",
                coordinate=coordinate,
                confidence=1.1,
            )

    def test_landmark_serialization(self):
        coordinate = Coordinate(
            x=0.5,
            y=0.5,
            z=0.1,
            space=CoordinateSpace.NORMALIZED_3D,
        )

        landmark = Landmark(
            name="glabella",
            coordinate=coordinate,
            status=LandmarkStatus.ESTIMATED,
            confidence=0.8,
            source=LandmarkSource.MODEL,
        )

        data = landmark.to_dict()

        self.assertEqual(
            data["component_type"],
            "landmark",
        )

        self.assertEqual(
            data["status"],
            "estimated",
        )

        self.assertEqual(
            data["source"],
            "model",
        )

        self.assertEqual(
            data["coordinate"]["space"],
            "normalized_3d",
        )

    def test_coordinate_rejects_non_finite_values(self):
        with self.assertRaises(ValueError):
            Coordinate(
                x=float("nan"),
                y=0.5,
                space=CoordinateSpace.IMAGE_2D,
            )

        with self.assertRaises(ValueError):
            Coordinate(
                x=0.5,
                y=float("inf"),
                space=CoordinateSpace.IMAGE_2D,
            )

    def test_landmark_rejects_empty_name(self):
        coordinate = Coordinate(
            x=0.5,
            y=0.5,
            z=0.0,
            space=CoordinateSpace.NORMALIZED_3D,
        )

        with self.assertRaises(ValueError):
            Landmark(
                name="",
                coordinate=coordinate,
            )


if __name__ == "__main__":
    unittest.main()