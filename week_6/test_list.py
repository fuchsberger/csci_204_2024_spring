from userlist import UserList, ListNode
from random import randint
#from userlist_imcomplete import UserList, ListNode

def test_insert_after():
    """ A test program for singly linked list """
    my_list = UserList()
    # nums = [randint(1, 100) for i in range(10)]  # random numbers
    nums = [i*2+1 for i in range(10)]  # orderly numbers
    for x in nums:
        my_list.insert_after(ListNode(x))

    print(my_list)


def test_insert_before():
    """ A test program for singly linked list """
    my_list = UserList()
    # nums = [randint(1, 100) for i in range(10)]  # random numbers
    nums = [i*2+1 for i in range(10)]  # orderly numbers
    for x in nums:
        my_list.insert_before(ListNode(x))

    print(my_list)

def test_remove():
    """ Test the remove() function
    """
    my_list = UserList()
    # nums = [randint(1, 100) for i in range(10)]  # random numbers
    nums = [i for i in range(10)]  # orderly numbers
    for x in nums:
        my_list.insert_before(ListNode(x))

    print('Before removing ...')
    print(my_list)
    my_list.remove_node(0)
    my_list.remove_node(9)
    my_list.remove_node(4)
    print('After removed 0, 9, and 4 ...')
    print(my_list)

def test_add_len():
    """Test '+' and len()"""
    my_list = UserList()
    nums = [randint(1, 100) for i in range(10)]  # random numbers
    for x in nums:
        my_list = my_list + ListNode(x)
    print("List generated ...")
    print(my_list)
    print("len of the list (should be 10): " + str(len(my_list)))


print('Test insert_after() ...')
test_insert_after()

print('Test insert_before() ...')
test_insert_before()

print('Test remove() ...')
test_remove()

print('Test add_len() ...')
test_add_len()
