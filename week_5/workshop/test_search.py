import unittest

from main_sol import breath_first_search, depth_first_search

class TestSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.testGraph = {
            'A': ('B', 'C'),
            'B': ('A', 'D', 'E', 'F'),
            'C': ('A', 'F'),
            'D': ('B'),
            'E': ('B', 'F'),
            'F': ('B','C', 'E'),
            'G': ()
        }

    def test_dept_first_search(self):
        result = depth_first_search(self.testGraph, "B", "F")
        self.assertEqual(result, ['B', 'F'])

        result = depth_first_search(self.testGraph, "A", "G")
        self.assertIsNone(result)

    def test_breath_first_search(self):
        result = breath_first_search(self.testGraph, "B", "F")
        self.assertEqual(result, ['B', 'F'])

        result = breath_first_search(self.testGraph, "A", "G")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
