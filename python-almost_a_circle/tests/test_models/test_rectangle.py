#!/usr/bin/python3 
""" test rectangle module """
import unittest
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):
    """ class test rectangle """


    """
    all good
    """

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

    def test_5_arguments(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_area(self):
        e = Rectangle(5, 5)
        self.assertEqual(e.area(), 25)

    def test___str__(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        r1 = Rectangle(1, 1, 0, 0)
        self.assertEqual(r1.display(), None)

    def test_display_2(self):
        r1 = Rectangle(1, 1, 1, 0)
        self.assertEqual(r1.display(), None)

    def test_display_3(self):
        r1 = Rectangle(1, 1, 0, 1)
        self.assertEqual(r1.display(), None)

    """
    whit strings in arguments
    """

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

    """
    whit negative arguments
    """
    def test_negative_arg_1(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_negative_arg_2(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

    def test_negative_arg_3(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

    def test_negative_arg_0(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    """
    whit zero arguments
    """

    def test_zero_arg_0(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def test_zero_arg_1(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)


if __name__ == '__main__':
    unittest.main()
