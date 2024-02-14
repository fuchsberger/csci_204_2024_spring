## Queue: Python implementation

Several common ways to implement a queue:

**Python list**
- easiest to implement

**Linked list**
- reduces memory wastes by eliminating the extra
capacity created with an array.

**Circular array**
- fast operations with a fixed size queue.

How is the data organized within the Python
list? Remember:
- Add new items to the end of the list.
- Remove items from the front of the list.

```python
class Queue :
  def __init__( self ) :
    self._qlist = list()

  def is_empty( self ) :
    return len(self) == 0

  def __len__( self ) :
    return len(self._qlist)

  def enqueue( self, item ):
    self._qlist.append(item)

  def dequeue( self ):
    assert not self.is_empty(), "Cannot dequeue from an empty queue."
    return self._qlist.pop(0)
```

## Queue Time complexity
| Operation         | Python List     |
| ---------         | --------------- |
| `Queue()`         | O(1)            |
| `len(q)`          | O(1)            |
| `q.is_empty()`    | O(1)            |
| `q.enqueue(x)`    | O(n)*           |
| `x = q.dequeue()` | O(n)*           |

(*) While the `enqueue()` and `dequeue()` operation
themselves are `O(1)`, the queue potentially needs to be
expanded or shrinked, which is `O(n)`.
