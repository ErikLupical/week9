"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
from circle import Circle


class TestCircle(unittest.TestCase):
    def test_normal_radius(self):
        c1 = Circle(3)
        c2 = Circle(4)
        expected_radius = 5.0
        result_circle = c1.add_area(c2)
        self.assertEqual(result_circle.radius, expected_radius)

    def test_radius_zero(self):
        c1 = Circle(0)
        c2 = Circle(8)
        result_circle_1 = c1.add_area(c2)
        result_circle_2 = c2.add_area(c1)

        expected_radius = 8.0

        self.assertEqual(result_circle_1.radius, expected_radius)
        self.assertEqual(result_circle_2.radius, expected_radius)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-2)
