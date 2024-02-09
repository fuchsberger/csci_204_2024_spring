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
        """Should return a string containing elements separate by " > "
        For example: "A > B > C"
        """
        # Comment: does work for city names, (expects all items in iterable to be strings. This is why it didnt work in class for numbers)
        return " > ".join(self.elements)


