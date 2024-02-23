# Size, IDs, Aliases, Nodes and Linked Lists

> **Reminder:** There is a gradescope homework open on Gradescope and due Wednesday evening.

### Determining size
Every object in python takes up space in memory. We can determine the size of an object in two ways:

```python
x = 0
print(x.__sizeof__())
```
```python
import sys
x = 0
print(sys.getsizeof(x))
```
**Activity:** Determine the size of x using both approaches. What do you notice?

> `getsizeof()` calls the object’s sizeof method and adds an additional garbage collector overhead if the object is managed by the garbage collector.

#### Activity
First take a look at the the `array204.py` file we implemented earlier.
Run the function on both an empty array and a filled array:

```python
import sys

arr1 = Array(3)
arr2 = Array(3)

arr2[0] = True
arr2[1] = 23
arr2[2] = "Hello"

print(sys.getsizeof(arr1))
print(sys.getsizeof(arr2))
```
**What do you observe?**

Finally complete the following function that takes an array and a (valid) index and returns the size of that slot:

```python
def array_size(arr, idx):
  # TODO: Returns the byte size of a given element in an array at a given index.
  pass
```

Test this function on `arr1[0]`, `arr2[0]`, and `arr2[2]`. What do you observe?

### IDs and Aliases
To find an object in memory python uses memory addresses that we refer in Python to via IDs:
```python
x = 0
print(id(x))
```

When we create and assign a value variable we really do three things:
- reserve the appropriate amount of space in memory
- modify that space to contain the variable's value
- we add the variables name and the memory address of the reserved space to a internal table so python can find and use it.

Thus when we are creating an **alias**, both variables names are added to the reference table while only one memory location is actually occupied.

#### Activity
First run the following program:
```python
a = 5
b = a
print(a, b)
a = 6
print(a, b)
```
Next, run the follwing program:
```python
a = []
b = a
print(a, b)
a.append(1)
print(a, b)
```

What did you observe and how can we explain that behavior?

### Nodes

A node is a custom ADT that usually stores a value and a reference to another node.
Depending on the use case more attributes may be available:
```python
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
```

#### Activity
1. Ceate a few nodes (values 'A', 'B', and 'c') and connect them together.
2. Create a loop that loops through the connected sequence of nodes and prints their value.

**Activity Solution:**
```python
n1 = Node("A")
n2 = Node("B")
n3 = Node("C")

n1.next = n2
n2.next = n3

curr = n1

while curr != None:
    print(curr.value)
    curr = curr.next
```
