import unittest

from human.anatomy.face import Face
from human.anatomy.head import Head


class TestHumanEngineH49(unittest.TestCase):

    def test_face_defaults(self):
        face = Face()

        self.assertEqual(face.component_type, "face")
        self.assertEqual(face.shape, "oval")
        self.assertEqual(face.symmetry, 1.0)

    def test_face_custom_geometry(self):
        face = Face(
            height=19.0,
            width=15.0,
            depth=11.0,
            forehead_width=13.0,
            cheekbone_width=15.0,
            jaw_width=13.0,
            jaw_depth=9.0,
        )

        self.assertEqual(face.height, 19.0)
        self.assertEqual(face.width, 15.0)
        self.assertEqual(face.depth, 11.0)
        self.assertEqual(face.cheekbone_width, 15.0)

    def test_face_shape(self):
        face = Face(shape="square")

        self.assertEqual(face.shape, "square")

    def test_face_symmetry(self):
        face = Face(symmetry=0.72)

        self.assertEqual(face.symmetry, 0.72)

    def test_face_invalid_dimension(self):
        with self.assertRaises(ValueError):
            Face(width=0)

    def test_face_invalid_shape(self):
        with self.assertRaises(ValueError):
            Face(shape="invalid")

    def test_face_invalid_symmetry(self):
        with self.assertRaises(ValueError):
            Face(symmetry=1.1)

    def test_head_contains_face(self):
        head = Head()

        self.assertIsInstance(head.face, Face)

    def test_head_custom_face(self):
        face = Face(shape="square", width=15.5)
        head = Head(face=face)

        self.assertIs(head.face, face)
        self.assertEqual(head.face.shape, "square")
        self.assertEqual(head.face.width, 15.5)

    def test_head_serializes_face(self):
        data = Head().to_dict()

        self.assertIn("face", data)
        self.assertEqual(data["face"]["component_type"], "face")
        self.assertEqual(data["face"]["shape"], "oval")


if __name__ == "__main__":
    unittest.main()
