x = "hanoi"


print(x[0]) # index

print(x[1:4:2]) # slicing

print(x[:3]) # slicing


def my_len(s):
    if s == "":
        return 0
    else:
        return 1 + my_len(s[1:])

print(my_len("hanoi"))
