class Queue:
    """
    Implemented as a particular case of Doubly Linked List.
    """
    class Node:
        """
        Queue element.
        Contains data and links to the next and previous elements.
        """
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self, first=None, last=None):
        # Contains links to the first and last elements.
        self.first = first
        self.last = last

    def is_empty(self):
        """
        Returns True if Queue is empty, False otherwise.
        """
        return not bool(self.first)

    def push(self, data):
        """
        Adds element in the end of Queue.
        """
        new_node = self.Node(data, None, self.last)

        if self.last:
            self.last.next = new_node
        else:
            self.first = new_node

        self.last = new_node

    def pop(self):
        """
        Removes element from the beginning of Queue and returns it.
        If Queue is empty, IndexError is raised.
        """
        if not self.first:
            raise IndexError('Empty Queue')

        node_to_pop = self.first
        # Defines new first element of Queue.
        # None if node_to_pop was only one in Queue.
        self.first = node_to_pop.next

        if self.first:
            # Means Queue still not empty.
            # Sets prev link of the new first element to None.
            self.first.prev = None
        else:
            # Means Queue is empty. Sets last link to None.
            self.last = None

        return node_to_pop

    def peek_first(self):
        """
        Returns first element of Queue.
        Returns None if Queue is empty.
        """
        return self.first

    def peek_last(self):
        """
        Returns last element of Queue.
        Returns None if Queue is empty.
        """
        return self.last
