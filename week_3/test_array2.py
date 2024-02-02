import unittest
from array2 import Array, Array2D

class ArrayTests(unittest.TestCase):
  def test__init__(self):
    obj = Array(3)
    self.assertIsInstance(obj, Array)

    for element in obj:
      self.assertIsNone(element)

    with self.assertRaises(AssertionError):
      Array(-1)

    with self.assertRaises(TypeError):
      Array()

  def test_other(self):
    obj = Array(3)

    obj[0] = True

    self.assertTrue(obj[0])
    self.assertIsNone(obj[1])
