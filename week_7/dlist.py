class DNode :
    def __init__( self, data ):
        self.data = data
        self.next = None
        self.prev = None

class DList :
    def __init__(self):
        """Creates a new DList instance.
        """
        self.head = None
        self.tail = None
        self.count = 0

    def __len__(self):
        """Returns the number of nodes in the list.
        """
        return self.count

    def insert_before(self, value):
        """Inserts value as a new node at the head of the list.
        """
        # TODO: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        pass

    def insert_after(self, value):
        """Inserts value as a new node at the tail of the list.
        """
        # TODO: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        pass

    def insert_sorted(self, value):
        """Inserts in the right space assuming ascending order of nodes by data.
        """
        # TODO: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        pass

    def remove(self, value):
        """Removes the first occurance of value in the linked list.
        """
        # TODO: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        pass

    def clear(self, value):
        """Removes all instances of value in the linked list.
        """
        # TODO: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        pass

    def __str__(self):
        """
        Returns the string representation of the linked list similar to how a python list's string representation looks like. For example:
        []
        ["A"]
        [1, 2, 3]
        """
        # TODO: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        return ""

