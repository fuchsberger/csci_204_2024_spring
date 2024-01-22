# print("Hello World")


x = 5

print(x)


class MyInteger():
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return(f"number is : {self.val}")

a = MyInteger(4)
print(a)
