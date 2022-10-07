#!/usr/bin/python3 
""" test rectangle module """
import unittest
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):
    """ class test rectangle """

    def test_w_1_h_2(self):
        result = Rectangle(1, 2)
        self.assertEqual(result.width, 1)
        self.assertEqual(result.height, 2)
 
    def test_more_argument(self):
        result = Rectangle(1, 2, 3)
        self.assertEqual(result.width, 1)
        self.assertEqual(result.height, 2)
        self.assertEqual(result.x, 3)

    def test_more_more_argument(self):
        result = Rectangle(1, 2, 3, 4)
        self.assertEqual(result.width, 1)
        self.assertEqual(result.height, 2)
        self.assertEqual(result.x, 3)
        self.assertEqual(result.y, 4)

    def test_string_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_string_second_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

    def test_string_other_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

    def test_string_arg_4(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

    def test_negative_arg_0(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_negative_arg_1(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_zero_arg_0(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def test_zero_arg_1(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_negative_arg_2(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

    def test_area(self):
        e = Rectangle(5, 5)
        self.assertEqual(e.area(), 25)

if __name__ == '__main__':
    unittest.main()
