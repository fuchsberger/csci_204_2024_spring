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

class LimitedStack(Stack):
    def __init__(self, max):
        self.max = max
        super().__init__()
