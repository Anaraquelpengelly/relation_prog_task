import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


import unittest
from functions import utils

class TestBFS(unittest.TestCase):

    def test_true(self):
        int_dic = {'A': ['B', 'C'],
                   'B': ['D', 'E'],
                   'C': ['F', 'G'],
                   'D': ['H', 'I'],
                   'E': ['J', 'K'],
                   'F': ['L', 'M'],
                   'G': ['N', 'O'],
                   'H': [], 'I': [], 'J': [], 'K': [],
                   'L': [], 'M': [], 'N': [], 'O': []}
        self.assertEqual(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
                         utils.bfs(int_dic, "A"))



if __name__ == '__main__':
    unittest.main()