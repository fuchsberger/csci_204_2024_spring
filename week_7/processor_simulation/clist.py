"""
Do not copy code from this file into processor.py. Instead you should build your Processor and Process classes to import and use the content of clist.

Author: Alexander Fuchsberger
Last Revised: 03/01/2024
Class: CSCI 204

DO NOT CHANGE THIS FILE
"""

class CList:
    """ A user defined singly linked list"""
    def __init__(self):
        self.head = None

    def insert(self, node):
        """ Inserts a node after current head and moves head to the node.
        """
        if self.head == None:
            self.head = node
            node.next = node
            node.prev = node
        else:
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            self.head = node

    def remove(self):
        """ Removes and returns the head node and sets the following node to be head. Raises an exception if List is empty.
        """
        if self.head == None:
            raise Exception("Cannot remove a node from an empty list.")

        elif self.head == self.head.next:
            curr = self.head
            self.head = None
            return self.head

        else:
            curr = self.head
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next
            return curr

    def __str__(self):
        """ Stringifys the content of all nodes starting with the head."""
        if self.head == None:
            return "[]"

        elif self.head == self.head.next:
            return f"[{str(self.head.data)}]"

        else:
            s = '['
            current = self.head
            s += str(current.data)
            current = current.next

            while current != self.head:
                s += str(current.data)
                if current.next != self.head:
                    s += ', '
                current = current.next

            s += ']'
            return s

class CNode:
    """ The node class for list notes"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Testcode. Run this file to execute.
if __name__ == "__main__":
    print("Testing Circular List")
    l = CList()
    assert str(l) == '[]'
    l.insert(CNode("A"))
    assert str(l) == '[A]'
    l.insert(CNode("B"))
    assert str(l) == '[BA]'
    l.remove()
    assert str(l) == '[A]'
    l.insert(CNode("C"))
    assert str(l) == '[CA]'
    print("All tests concluded successfully.")
