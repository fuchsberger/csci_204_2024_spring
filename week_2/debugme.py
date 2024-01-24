number = input("Enter an integer: ")

i = 1

while i < number:
    if number % 2 == 0:
        total = total + number
    i = i + 1

print(total)
