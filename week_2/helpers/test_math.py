import unittest
from .math import power
# the . helps tell python to understand that we want
# to import math.py from a local directory, not the
# standard library. Similarily we could have imported
# from a parent directory: ..math

class MathTests(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 0), 1)

        with self.assertRaises(ValueError):
            power(2, -1)

