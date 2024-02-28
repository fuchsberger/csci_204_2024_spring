from random import *
from circular_list_singly_linked import *

def test_insert():
    """ A test program for singly linked list """
    my_list = CircularListSingly()
    nums = [randint(1, 100) for i in range(10)]  # random numbers
    # nums = [i*2+1 for i in range(10)]  # orderly numbers
    print('Nums to be inserted ', nums)
    for x in nums:
        my_list.insert(ListNode(x))

    print('List content (unordered)')
    print(my_list)

def test_insert_ordered():
    """ A test program for singly linked list """
    my_list = CircularListSingly()
    nums = [randint(1, 100) for i in range(10)]  # random numbers
    # nums = [44, 59, 33, 19, 92, 65, 23, 41]
    # nums = [4, 62, 52, 51, 50, 49, 44, 21, 20, 4]
    # nums = [82, 97, 35, 85, 91, 55, 12, 54, 27, 6]
    # nums = [i*2+1 for i in range(10)]  # orderly numbers
    print('Numbers to be inserted')
    print(nums)
    for x in nums:
        my_list.insert_ordered(ListNode(x))

    print('List content (ordered) ')
    print(my_list)

def test_remove():
    """ Test the remove() function
    """
    my_list = CircularListSingly()
    # nums = [randint(1, 100) for i in range(10)]  # random numbers
    nums = [i for i in range(10)]  # orderly numbers
    for x in nums:
        my_list.insert(ListNode(x))

    print('Before removing ...')
    print(my_list)
    my_list.remove(0)
    my_list.remove(1)
    my_list.remove(4)
    print('After removed 0, 1, and 4 ...')
    print(my_list)

def test_len():
    """ Test the len() function """
    my_list = CircularListSingly()
    print('len should be 0 ', len(my_list))

    my_list.insert(ListNode(10))
    print('len should be 1 ', len(my_list))
    my_list.insert(ListNode(40))
    print('len should be 2 ', len(my_list))

    my_list = CircularListSingly()
    nums = [randint(1, 100) for i in range(10)]  # random numbers
    for x in nums:
        my_list.insert(ListNode(x))
    print('len should be 10 ', len(my_list))

    my_list = CircularListSingly()
    nums = [randint(1, 100) for i in range(20)]  # random numbers
    for x in nums:
        my_list.insert(ListNode(x))
    print('len should be 20 ', len(my_list))


#test_insert()
#test_remove()
test_insert_ordered()
test_len()
