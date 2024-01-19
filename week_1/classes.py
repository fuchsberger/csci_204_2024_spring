# Intro Classes



# class CustomList:
#     def __init__(self, n1 = None, n2 = None, n3 = None):
#         self.n1 = n1
#         self.n2 = n2
#         self.n3 = n3

class CustomList(list):
    def __init__(self, numbers):
        if type(numbers) == list and len(numbers) <= 3:
            self.numbers = numbers
        else:
            raise TypeError

    def append(self, element):
        if len(self.numbers) < 3:
            self.numbers.append(element)
        else:
            raise ValueError


numbers = CustomList([1, 2]) # valid, proceeeds
# numbers = CustomList([1, 2, 3, 4]) # invalid, raises


numbers.append(4)
print(numbers.numbers)

# numbers.append(5)
# print(numbers.numbers)

numbers.pop()

class SportTeam(list):
    def __init__(self, name):
        self._name = name
        self._members = []
