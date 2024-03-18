"""
Test basic search strategies, linear search and binary search.
CSCI 204
Fall 2017
Xiannong MengÍ
Reviewed:
Spring 2024
Alexander Fuchsberger
"""
from listsearcher import LinearSearch as Searcher
# from listsearcher import BinarySearch as Searcher

from time import *
import random

def validate() :
    """Validate the basic operations of searchers"""

    print( 'Performing some basic checking ...' )
    values = [ 9, 5, 10, 0, 6, 11, -1, 1, 2 ]
    print( 'original data ...' )

    mydata = Searcher()

    for v in values:
        print( v, end = ', ' )
        mydata.add( v, v )    # v is both key and data
    print()
    mydata.print()
    print()


    print( 'traversal of the data ...' )
    print( 'the result is (printed in (key, data) pairs) : ', end = '[' )
    for x in mydata:
        print( '(', x.key, ',', x.value, ')', end = ', ' )
    print( ']')

    print( 'search for "9", should be True : ', 9 in mydata )
    print( 'search for "2", should be True: ', 2 in mydata )
    print( 'search for "-1", should be True : ', -1 in mydata )
    print( 'search for "20", should be False : ', 20 in mydata )


    values.remove( 10 )
    mydata.remove( 10 )
    print( 'removing 10 from the data ...')
    print( 'the result should be ', sorted( values ) )
    print( 'the result is (printed in (key, data) pairs) : ', end = '[' )
    for x in mydata:
        print( '(', x.key, ',', x.value, ')', end = ', ' )
    print( ']' )
    mydata.print()

def timing_search( size ):
    """ Measure the time needed for search in n items """

    print( 'Performing add and search in ', size, ' keys...' )
    # First, generate a list of integers
    a = []
    for i in range( size ):
        a.append( random.randint( 1, size ) )

    mydata = Searcher()   # Create a search structure (tree or hash table)
    # record the start time for building the table
    startA = time()
    for i in range( size ):
        # add (key, value) pair to the searcher
        mydata.add( a[i], i )
    # record the finish time for building the table
    finishA = time()

    searchCount = size // 2

    # record the start time for searching
    startB = time()
    # Do search half of the sizes, every key should be in the searcher
    for i in range( searchCount ):
        if not (a[i] in mydata) :
            print( 'search ', a[i], ' failed!!! (shouldnt happen)' )
    # record the finish time for searching
    finishB = time()

    print( 'building time : ', '{0:0.6f}'.format(finishA - startA), ' seconds.' )
    print( 'search time : ', '{0:0.6f}'.format(finishB - startB), ' seconds.' )

def testTiming() :
    """Test the time needed for various search structures"""
    random.seed( 10 )      # any integer to specify the seed

    timing_search( 1000 )   # search in a list of size 1,000
    timing_search( 10000 )  # search in a list of size 10,000


#validate()
testTiming()
