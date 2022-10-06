#!/usr/bin/python3
""" unitest module """

import unittest
from models.base import Base



class Test_Base(unittest.TestCase):
    """ class for testing
    """

    def test_Base(self):
        a = 1
        self.assertEqual(a, 1)

if __name__ == '__main__':
    unittest.main()
