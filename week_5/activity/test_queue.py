import unittest

from queue import Queue
from queue_count import Queue as CQueue

class QueueTests(unittest.TestCase):
    def setUp(self):
        self.queues = [Queue(3), CQueue(3)]

    def test_length(self):
        for queue in self.queues:
            self.assertEqual(len(queue), 0)
            queue.enqueue("A")
            self.assertEqual(len(queue), 1)
            queue.dequeue()
            self.assertEqual(len(queue), 0)

    def test_order(self):
        for queue in self.queues:
            queue.enqueue("A")
            queue.enqueue("B")
            queue.enqueue("C")

            self.assertEqual(queue.dequeue(), "A")
            self.assertEqual(queue.dequeue(), "B")
            self.assertEqual(queue.dequeue(), "C")

            with self.assertRaises(AssertionError):
                queue.dequeue()

    def test_max(self):
        for queue in self.queues:
            queue.enqueue("A")
            queue.enqueue("B")
            queue.enqueue("C")

            with self.assertRaises(AssertionError):
                queue.enqueue("D")

if __name__ == "__main__":
    unittest.main()
