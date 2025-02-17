import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


import unittest
from functions import utils

class TestFindPattern(unittest.TestCase):
    def test_true(self):
        self.assertTrue(utils.find_pattern("TATTTACTFBCSF", r"T[AV]T.T"))
    def test_false(self):
        self.assertFalse(utils.find_pattern("ACTFBCSF", r"T[AV]T.T"))


if __name__ == '__main__':
    unittest.main()