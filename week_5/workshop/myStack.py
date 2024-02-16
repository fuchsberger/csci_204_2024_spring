"""
Basic Stack implementation using python list.
DO NOT MODIFY THIS FILE.
"""

class StackError(Exception):
    pass

class Stack:
    def __init__(self):
        self.elements = []

    def __len__(self):
        return len(self.elements)

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if len(self.elements) == 0:
            raise StackError

        return self.elements.pop()

    def peek(self):
        if len(self.elements) == 0:
            return None
        return self.elements[-1]

    def __str__(self):
        return " > ".join(self.elements)


