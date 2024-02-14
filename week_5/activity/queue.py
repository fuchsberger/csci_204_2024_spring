### Array Based Circular Queue Implementation without count
### TODO: Make it work without keeping track of a count attribute.

from array204 import Array

class Queue :
  def __init__( self, max_size ) :
    self._front = 0
    self._back = 0
    self._qarray = Array( max_size + 1 )

  def is_empty( self ) :
    return self._back == self._front

  # A new operation specifically for the circular array.
  def is_full( self ) :
    return (self._back + 1) % len(self._qarray) == self._front

  def __len__( self ) :
    if self._front < self._back:
      return self._back - self._front
    else:
      l = 0
      curr = self._front
      while curr != self._back:
        curr = (curr + 1) % len(self._qarray)
        l += 1

      return l

  def enqueue( self, item ):
    assert not self.is_full(), "Cannot enqueue to a full queue."
    self._back = (self._back + 1) % len(self._qarray)
    self._qarray[self._back] = item

  def dequeue( self ):
    assert not self.is_empty(), "Cannot dequeue from an empty queue."
    self._front = (self._front + 1) % len(self._qarray)
    item = self._qarray[ self._front ]
    return item
