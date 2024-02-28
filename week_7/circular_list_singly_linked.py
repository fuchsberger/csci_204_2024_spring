class CircularListSingly:
    """A user defined singly linked circular list"""
    def __init__(self):
        self.ref = None    # self.ref always points to the end of the list
                           # alternatively we could have it point to the first

    def __str__(self):
        """ String function """
        h = self.ref
        if h == None:
            return 'CList[]'
        s = 'CList[' + str(h.data)
        h = h.next
        while h != self.ref:
            if h != self.ref:
                s += ', '
                s += str(h.data)
            h = h.next

        s += ']'
        return s

    def __len__(self):
        """ Count the number of elements """
        h = self.ref
        if h == None:
            return 0
        if h.next == h:
            return 1
        else:
            h = h.next
            count = 1
            while h != self.ref:
                count += 1
                h = h.next
            return count

    def insert(self, node):
        """ Insert a node with value"""

        if self.ref == None:       # empty list
            self.ref = node
            node.next = self.ref
        else:                       # insert after ref
            node.next = self.ref.next
            self.ref.next = node

    def insert_ordered(self, new_node):
        """Insert the new_node into the list, sorted"""

        if self.ref is None :               # empty list
            self.ref = new_node
            new_node.next = new_node
        elif new_node.data > self.ref.data : # insert in front, past ref
            new_node.next = self.ref.next
            self.ref.next = new_node
            self.ref = new_node              # need to update the ref
        else:  # new_node.data < self.ref.data, need to locate the position
            prev, place = self.find_place(new_node)
            new_node.next = place
            prev.next = new_node

    def find_place(self, node):
        """ Find where the right place for the node in a sorted list
        """
        prev = self.ref
        cur  = self.ref.next
        while cur != self.ref and cur.data < node.data:
            prev = cur
            cur = cur.next
        return prev, cur

    def remove(self, data):
        """Removes the first node with the given data."""
        # TODO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        pass

class ListNode:
    """ The node class for list notes"""
    def __init__(self, data):
        self.data = data
        self.next = None
