### Array Based Circular Queue Implementation
from array204 import Array

class Queue :
  def __init__( self, max_size ) :
    self._count = 0
    self._front = 0
    self._back = max_size - 1
    self._qarray = Array( max_size )

  def is_empty( self ) :
    return self._count == 0

   # A new operation specifically for the circular array.
  def is_full( self ) :
    return self._count == len(self._qarray)

  def __len__( self ) :
    return self._count

  def enqueue( self, item ):
    assert not self.is_full(), "Cannot enqueue to a full queue."
    max_size = len(self._qarray)
    self._back = (self._back + 1) % max_size
    self._qarray[self._back] = item
    self._count += 1

  def dequeue( self ):
    assert not self.is_empty(), "Cannot dequeue from an empty queue."
    item = self._qarray[ self._front ]
    max_size = len(self._qarray)
    self._front = (self._front + 1) % max_size
    self._count -= 1
    return item
