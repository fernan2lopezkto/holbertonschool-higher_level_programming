#!/usr/bin/python3 
""" test rectangle module """
import unittest
from models.square import Square


class Test_rectangle(unittest.TestCase):
    """ class test Square """


    """
    all good
    """

    def test_w_1_h_2(self):
        result = Square(1, 2)
        self.assertEqual(result.size, 1)
        self.assertEqual(result.x, 2)
 
    def test_more_argument(self):
        result = Square(1, 2, 3)
        self.assertEqual(result.size, 1)
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 3)

    def test_more_more_argument(self):
        result = Square(1, 2, 3, 4)
        self.assertEqual(result.size, 1)
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 3)
        self.assertEqual(result.id, 4)

    def test_area(self):
        e = Square(5)
        self.assertEqual(e.area(), 25)

    def test___str__(self):
        r1 = Square(4, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Square] (12) 2/1 - 4")

    """
    whit strings in arguments
    """

    def test_string_arg(self):
        with self.assertRaises(TypeError):
            r = Square("1", 2)

    def test_string_second_arg(self):
        with self.assertRaises(TypeError):
            r = Square(1, "2")

    def test_string_other_arg(self):
        with self.assertRaises(TypeError):
            r = Square(1, 2, "3")

    """
    whit negative arguments
    """
    def test_negative_arg_1(self):
        with self.assertRaises(ValueError):
            r = Square(1, -2)

    def test_negative_arg_2(self):
        with self.assertRaises(ValueError):
            r = Square(1, 2, -3)

    def test_negative_arg_3(self):
        with self.assertRaises(ValueError):
            r = Square(1, 2, -3)

    def test_negative_arg_0(self):
        with self.assertRaises(ValueError):
            r = Square(-1, 2)

    """
    whit zero arguments
    """

    def test_zero_arg_0(self):
        with self.assertRaises(ValueError):
            r = Square(0, 2)


if __name__ == '__main__':
    unittest.main()
