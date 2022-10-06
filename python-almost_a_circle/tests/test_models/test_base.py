#!/usr/bin/python3
""" base tests """
import unittest
from models.base import Base


class BaseClass(unittest.TestCase):
    """ Base class """
    def test_negative_id(self):
        result = Base(-12)
        self.assertEqual(result.id, -12)

    def test_auto_assign(self):
        result = Base()
        self.assertEqual(result.id, 1)

    def test_one_to_auto_assign(self):
        result = Base()
        result2 = Base()
        self.assertEqual(result.id, 2)

    def test_id_exists(self):
        result = Base(2)
        self.assertEqual(result.id, 2)

    def test_to_json_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, '[]')

    def test_to_json_brackets(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, '[]')

    def test_from_json_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_brackets(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()