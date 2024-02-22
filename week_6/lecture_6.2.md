# Linked List - Stack Implementation

We did an activity in class to arrive at the following Stack Linked-List implementation.

```python
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
    def __init__(self):
       self.top = None

    def isEmpty(self):
       return self.top == None

    def push(self, item):
        newNode = Node(item)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
       value = self.top.value
       self.top = self.top.next
       return value

    def peek(self):
       return self.top.value

    def __len__(self):
        count = 0

        curr = self.top

        while curr != None:
           count += 1
           curr = curr.next

        return count
```

**Homework** All Operations are currently `O(1)` except `len()` which is `O(n)`. Revise the implementation above using a `count` attribute to make len() also `O(1)`.
