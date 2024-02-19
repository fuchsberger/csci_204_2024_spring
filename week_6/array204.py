# Implement the Array ADT using array capabilities of the ctype module
import ctypes

class Array:
    # Create an array with 'size' elements
    def __init__( self, size ):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()

        # Initialize each element
        self.clear( None )

    # Return the size of the array
    def __len__( self ):
        return self._size

    # Get the content of the indexed element
    def __getitem__( self, index ):
        assert index >=0 and index < len( self ), \
            "Array subscript out of range"
        return self._elements[ index ]

    # Set the value of the array element at the given index
    def __setitem__( self, index, value ):
        assert index >=0 and index < len( self ), \
            "Array subscript out of range"
        self._elements[ index ] = value

    # Clear the array by setting each element to the given value
    def clear( self, value ):
        for i in range( len( self ) ):
            self._elements[ i ] = value

    # Return the array's iterator for traversing the elements
    def __iter__( self ):
        return _ArrayIterator( self._elements )

# An iterator for the Array ADT
class _ArrayIterator:

    def __init__( self, the_array ):
        self._array_ref = the_array
        self._cur_ndx = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self._cur_ndx < len( self._array_ref ):
            entry = self._array_ref[ self._cur_ndx ]
            self._cur_ndx += 1
            return entry
        else:
            raise StopIteration
