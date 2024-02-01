from array import Array2D

f = open("data.txt")

rows = int(f.readline())
cols = int(f.readline())

# for i in range(rows):
#     row = f.readline()
#     grades = row.split()
#     grades = [int(grade) for grade in grades]

myArray = Array2D(rows, cols)

myArray[0, 0] = True

print(myArray)
print(myArray[0, 0])
print(myArray[0, 1])


# python example
# x = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# x[0][1] = 1    
# print(x)

# for i in range(rows):
#     row = f.readline()
#     grades = row.split()
#     grades = [int(grade) for grade in grades]


