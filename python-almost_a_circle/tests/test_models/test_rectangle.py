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

    def test_string_other_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

    def test_string_other_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

if __name__ == '__main__':
    unittest.main()
