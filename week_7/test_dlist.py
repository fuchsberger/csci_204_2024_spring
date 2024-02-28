import unittest
from random import *
from dlist_sol import DList

class Tests(unittest.TestCase):
    def setUp(self):
        self.list = DList()

    def test_insert_after(self):
        """ A test program for singly linked list """
        for x in [i for i in range(10)]:
            self.list.insert_after(x)

        self.assertEqual(str(self.list), "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")

    def test_insert_sorted(self):
        """ A test program for singly linked list """
        for x in [2, 1, 5, 4, 3]:
            self.list.insert_sorted(x)

        self.assertEqual(str(self.list), "[1, 2, 3, 4, 5]")

    def test_insert_before(self):
        """ A test program for singly linked list """
        for x in [i for i in range(10)]:
            self.list.insert_before(x)

        self.assertEqual(str(self.list), "[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]")

    def test_str(self):
        """ Test the __str__() function
        """
        self.assertEqual(str(self.list), "[]")
        self.list.insert_after(1)
        self.assertEqual(str(self.list), "[1]")
        self.list.insert_before(2)
        self.assertEqual(str(self.list), "[2, 1]")

    def test_remove(self):
        """ Test the remove() function
        """
        for x in [i for i in range(10)]:
            self.list.insert_after(x)

        self.assertEqual(str(self.list), "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")

        self.list.remove(0)
        self.list.remove(9)
        self.list.remove(4)

        self.assertEqual(str(self.list), "[1, 2, 3, 5, 6, 7, 8]")


    def test_clear(self):
        """ Test the clear() function
        """
        for x in [i % 2 for i in range(5)]:
            self.list.insert_after(x)

        self.assertEqual(len(self.list), 5)
        self.assertEqual(str(self.list), "[0, 1, 0, 1, 0]")

        self.list.clear(0)

        self.assertEqual(len(self.list), 2)
        self.assertEqual(str(self.list), "[1, 1]")

if __name__ == "__main__":
    unittest.main()
