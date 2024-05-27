# test_module.py

import unittest
import horizon.module as module

class TestModule(unittest.TestCase):

    # NumPy Function Tests
    def test_matrix(self):
        self.assertEqual(module.matrix([[1, 2], [3, 4]]).tolist(), [[1, 2], [3, 4]])

    def test_ghost(self):
        self.assertEqual(module.ghost((2, 2)).tolist(), [[0, 0], [0, 0]])

    def test_squad(self):
        self.assertEqual(module.squad((2, 2)).tolist(), [[1, 1], [1, 1]])

    # Add more tests for other functions...

if __name__ == '__main__':
    unittest.main()
