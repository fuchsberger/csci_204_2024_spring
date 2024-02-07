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

    def reverse(self):
        """Reverses the elements in the stack.
        Try to do this without making creating a new list.
        """
        pass

    def copy(self):
        """
        Returns a new stack that is a copy of the original stack.
        (You don't need to account for deep copying elements)
        """
        pass

class LimitedStack(Stack):
    """Just like an ordinary stack but raises if the stack is full.
    """
    def __init__(self, max):
        self.max = max
        super().__init__()

class UnlimitedStack(LimitedStack):
    """
    Just like the Limited Stack but should not raise an exception when pushing into a full stack. Instead the oldest element at the bottom of the stack should be kicked out to make room.
    """
    pass
