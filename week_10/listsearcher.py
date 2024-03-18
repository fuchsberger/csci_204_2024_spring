"""This is just a list to emulate the behavior of other search structures
such as bst, avl tree, and hash table. The class supports the following
operations.
1. add( key, value )
2. remove( key )
3. iterator
4. search( key )

This class is used primarily for comparing performance with other
data structures.

CSCI 204
Fall 2017
Xiannong Meng
Revised
Spring 2020
Leave the iterative binary search function here.
Students can supply a recursive form of the function.
"""

class LinearSearch:

    def __init__( self ):
        """Create an empty list"""
        self._table = []

    def __len__( self ):
        """Returns the number of elements"""
        return len( self._table )

    def __contains__( self, key ):
        """ Determines if the table contains the given key."""
        return self._search( key ) != -1

    def __iter__( self ):
        """ Returns an iterator for traversing the keys in the map."""
        return _LinearIterator( self._table )

    def add( self, key, value ):
        """Add the (key,value) pair to the table """
        index = self._search( key )
        if index != -1 :  # key is alredy there, update
            self._table[ index ].value = value
        else:             # key is new
            node = _Node( key, value )
            self._table.append( node )

    def remove( self, key ):
        """Remove the node with the 'key'"""
        index = self._search( key )
        if index != -1 :  # key is found
            self._table.pop( index )

    def _search( self, key ):
        """Search for the key and returns the index if found, returns
        -1 if not found."""
        l = len( self._table )
        for i in range( l ):
            if self._table[ i ].key == key :
                return i  # found
        return -1     # not found

    def print( self ):
        """Print all the items"""
        l = len( self._table )
        print( '[', end = '' )
        for i in range( l ):
            print( self._table[ i ].key, end = ', ' )
        print( ']' )

class BinarySearch:

    def __init__( self ):
        """Create an empty list"""
        self._table = []

    def __len__( self ):
        """Returns the number of elements"""
        return len( self._table )

    def __contains__( self, key ):
        """ Determines if the table contains the given key."""
        return self._search( key ) != -1

    def __iter__( self ):
        """ Returns an iterator for traversing the keys in the map."""
        return _LinearIterator( self._table )

    def add( self, key, value ):
        """Add the (key,value) pair to the table
        Keep the listed sorted for binary search"""

        n = len( self._table )
        node = _Node( key, value )
        if n == 0:   # new list
            self._table.append( node )
        else:
            i = 0
            while i < n and key >= self._table[ i ].key :
                i += 1
            # found the location to insert the new node
            self._table.insert( i, node )

    def remove( self, key ):
        """Remove the node with the 'key'"""
        index = self._search( key )
        if index != -1 :  # key is found
            self._table.pop( index )

    def _search( self, key ):
        """Search for the key and returns the index if found, returns
        -1 if not found.
        Since the list is sorted, we can do binary search"""

        l = len( self._table ) - 1
        return self._dbinsearch( 0, l, key )

    def _dbinsearch( self, first, last, key ):
        """Binary search to find the index of the key"""
        while first <= last :
            mid = first + (last - first) // 2
            if self._table[mid].key == key :
                return mid  # found
            elif key < self._table[mid].key :
                last = mid - 1
            else :
                first = mid + 1

        return -1  # not found

    def print( self ):
        """Print all the items"""
        l = len( self._table )
        print( '[', end = '' )
        for i in range( l ):
            print( self._table[ i ].key, end = ', ' )
        print( ']' )

# Storage class for holding the key/value pairs.
class _Node:

  def __init__( self, key, value ):
    """Create the entry with key and value """
    self.key = key
    self.value = value

  def __eq__( self, rhs ):
    """Overload __eq__ so items can be compared using '==' sign"""
    if rhs == None:
      return False
    return ( self.key == rhs.key and self.value == rhs.value )

# Linear iterator
class _LinearIterator:

    def __init__( self, theTable ):
        """Create the data set"""
        self._table = theTable
        self._curIndex = 0

    def __iter__( self ):
        """Return the iterator"""
        return self

    def __next__( self ):
        """Return the next element"""
        if self._curIndex >= len( self._table ) :
            raise StopIteration
        else:
            element = self._table[ self._curIndex ]
            self._curIndex += 1
            return element
