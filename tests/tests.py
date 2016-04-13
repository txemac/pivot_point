import unittest
from pivot_point import find_pivot_points


__author__ = 'josebermudez'


class TestPivotPoints(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestPivotPoints, self).__init__(*args, **kwargs)

    def test_none(self):
        self.assertRaises(ValueError, find_pivot_points, array=None)

    def test_array_example(self):
        array = [1, 3, 2, -2, 2, 4]
        self.assertEqual(find_pivot_points(array=array), [2, 3, 4])

    def test_array_without_pivot(self):
        array = [1, 3, 2, -2, 2, 4, 3]
        self.assertEqual(find_pivot_points(array=array), -1)

    def test_array_first_element(self):
        array = [17, 1, -1]
        self.assertEqual(find_pivot_points(array=array), [0])

    def test_array_last_element(self):
        array = [1, -1, 17]
        self.assertEqual(find_pivot_points(array=array), [2])
