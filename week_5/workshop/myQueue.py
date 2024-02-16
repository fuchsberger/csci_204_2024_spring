"""
Basic Queue implementation using python list.
DO NOT MODIFY THIS FILE.
"""

class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.elements = []

    def __len__(self):
        return len(self.elements)

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        if len(self.elements) == 0:
            raise QueueError

        return self.elements.pop(0)

    def peek(self):
        if len(self.elements) == 0:
            return None
        return self.elements[-1]

    def __str__(self):
        return " > ".join(self.elements)


