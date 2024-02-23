class UserList:
    """ A user defined singly linked list"""
    def __init__(self):
        self.head = None
        self.tail = None


    def __str__(self):
        """ String function """
        s = '['
        h = self.head
        while h != None:
            s += str(h.data)
            h = h.next
            if h != None:
                s += ', '
        s += ']'
        return s

    def insert_after(self, node):
        """ Insert a node with data at the end of the list
        """
        if self.is_empty() == True:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insert_before(self, node):
        """ Insert a node with data before the head of the list
        """
        pass

    def remove_node(self, target):
        """ Remove the node containing the target
        """
        pass

    def is_empty(self):
        """ Return True if the list is empty, False otherwise.
        """
        return self.head == None

class ListNode:
    """ The node class for list notes"""
    def __init__(self, data):
        self.data = data
        self.next = None
