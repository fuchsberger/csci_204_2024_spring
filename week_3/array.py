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


# Implementation of the Array2D ADT using an array of arrays
class Array2D:
    # Create a 2-D array of size num_rows X num_cols
    def __init__( self, num_rows, num_cols ):
        # Create a 1-D array to store an array reference for each row
        self._the_rows = Array( num_rows )

        # Create the 1-D arrays for each rows of the 2-D array
        for i in range( num_rows ):
            self._the_rows[ i ] = Array( num_cols )

    # Return the number of rows in the 2-D array
    def num_rows( self ):
        return len( self._the_rows )

    # Return the number of cols in the 2-D array
    def num_cols( self ):
        return len( self._the_rows[0] )

    # Clear the array by setting every element to the given value
    def clear( self, value ):
        for row in range( self.num_rows() ):
            self._the_rows[ row ].clear( value )

    # Get the content of the element at position [i, j]
    def __getitem__( self, ndx_tuple ):
        assert len( ndx_tuple ) == 2, "Invalid number of array subscriptts."
        row = ndx_tuple[ 0 ]
        col = ndx_tuple[ 1 ]
        assert row >= 0 and row < self.num_rows() \
            and col >= 0 and col < self.num_cols(), \
            "Array subscripts out of range."

        the1dArray = self._the_rows[ row ]
        return the1dArray[ col ]

    # Set the content of the element at position [i, j]
    def __setitem__( self, ndx_tuple, value ):
        assert len( ndx_tuple ) == 2, "Invalid number of array subscriptts."
        row = ndx_tuple[ 0 ]
        col = ndx_tuple[ 1 ]
        assert row >= 0 and row < self.num_rows() \
            and col >= 0 and col < self.num_cols(), \
            "Array subscripts out of range."

        the1dArray = self._the_rows[ row ]
        the1dArray[ col ] = value
