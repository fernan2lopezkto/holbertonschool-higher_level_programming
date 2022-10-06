#!/usr/bin/python3
""" base tests """
import unittest
from models.base import Base


class test_bass(unittest.TestCase):
    """ class for testing
    """

    def test_Base(self):
        a = Base(5)
        self.assertEqual(a, 1)

if __name__ == '__main__':
    unittest.main()
