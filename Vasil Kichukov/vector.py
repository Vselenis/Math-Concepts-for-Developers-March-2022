import unittest
import numpy as np


class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.array = np.array([x, y, z])

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

    def dot_product(self, other):
        dot = np.dot(self.array, other.array)
        return dot

    def cross_product(self, other):
        cross = np.cross(self.array, other.array)
        return cross

    def magnitude(self):
        length = np.linalg.norm(self.array)
        return length

    def normalize(self):
        return self / self.magnitude()

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        assert not isinstance(other, Vector)
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        assert not isinstance(other, Vector)
        return Vector(self.x / other, self.y / other, self.z / other)


class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1.0, -2.0, -2.0)
        self.v2 = Vector(3.0, 6.0, 9.0)

    def test_dot_product(self):
        self.assertEqual(self.v1.dot_product(self.v2), -27)

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)

    def test_addition(self):
        sum_vectors = self.v1 + self.v2
        self.assertEqual(getattr(sum_vectors, 'x'), 4.0)

    def test_subtraction(self):
        sub_vectors = self.v1 - self.v2
        self.assertEqual(getattr(sub_vectors, 'x'), -2.0)

    def test_multiplication(self):
        mul_vectors = self.v1 * 2
        self.assertEqual(getattr(mul_vectors, 'y'), -4.0)

    def test_division(self):
        mul_vectors = self.v1 / 2
        self.assertEqual(getattr(mul_vectors, 'z'), -1.0)


if __name__ == "__main__":
    unittest.main()
