__author__ = "Marco Antonio Carcano"
__version__ = '1.0.0'

# from .foolistitem import FoolistItem
from .foolistitem import FoolistItem


class Foolist():
    """
    Object used to implement a list of FoolistItem 
    """
    def __init__(self):
        """
        Initialize the list by setting its head to None
        """
        self.head = None

    def __iter__(self):
        """
        Iterate throughout the list
        """
        node = self.head
        while node is not None:
            yield node
            node = node._next

    def append(self, name, enabled=False):
        """
        Append a FoolistItem to the list
        """
        if self.head is None:
            self.head = FoolistItem(name, enabled)
            return
        for current_node in self:
            pass
        current_node.next = FoolistItem(name, enabled)

    def remove(self, name):
        """
        Removes an item from the list
        """
        for f in self:
            if f.name == name:
                if f == self.head:
                    self.head = f._next
                else:    
                    hold._next = f._next
                del f
                break
            else:
                hold = f

    def __repr__(self):
        """
        Implements the representation of the list
        """
        nodes = []
        for node in self:
            nodes.append(node._name)
        return " -> ".join(nodes)
