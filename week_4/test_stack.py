import unittest

from stack import Stack, StackError, LimitedStack

class StackTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.lStack = LimitedStack(2)

    def test_length(self):
        self.assertEqual(len(self.stack), 0)
        self.stack.push(1)
        self.assertEqual(len(self.stack), 1)
        self.stack.pop()
        self.assertEqual(len(self.stack), 0)

    def test_order(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

        with self.assertRaises(StackError):
            self.stack.pop()

    def test_peek(self):
        # TODO
        self.assertIsNone(self.stack.peek())
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.assertEqual(len(self.stack), 1)

    def test_limited_stack(self):
        self.lStack.push(1)
        self.lStack.push(2)

        with self.assertRaises(StackError):
            self.lStack.push(3)

StackTests()
