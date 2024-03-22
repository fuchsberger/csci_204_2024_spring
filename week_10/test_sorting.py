import unittest
from sorting import *

class TestSorting(unittest.TestCase):
    def setUp(self) -> None:
        self.sequence = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
        self.goal = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]

    def test_selection_sort(self):
        result = selection_sort(self.sequence)
        self.assertEqual(result, self.goal)

    def test_insertion_sort(self):
        result = insertion_sort(self.sequence)
        self.assertEqual(result, self.goal)

    def test_bubble_sort(self):
        result = bubble_sort(self.sequence)
        self.assertEqual(result, self.goal)

    def test_shell_sort(self):
        result = shell_sort(self.sequence)
        self.assertEqual(result, self.goal)

if __name__ == "__main__":
    unittest.main()
