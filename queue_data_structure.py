from linked_lists import DoublyLinkedList


class Queue(DoublyLinkedList):
    """
    Queue can be considered as a special case of DoublyLinkedList.
    Inherited methods: __init__, __iter__, get.
    Overridden methods: __repr__, add, pop.
    New methods: is_empty, front, rear.
    """
    def __repr__(self):
        """
        String representation of all nodes in Queue.
        """
        nodes = []
        for node in self:
            nodes.append(str(node))
        # Arrow shows on the front of the Queue.
        return '«' + ' <-- '.join(nodes) + '»'

    def add(self, data):
        """
        Adds element to the end of Queue.
        """
        super().add(data, self.length)

    def pop(self):
        """
        Removes first element from Queue and returns it.
        If Queue is empty, IndexError is raised.
        """
        if not self.first:
            raise IndexError('Empty Queue')

        return super().pop(0)

    def is_empty(self):
        """
        Returns True if Queue is empty, False otherwise.
        """
        return not bool(self.first)

    def front(self):
        """
        Returns first element of Queue.
        Returns None if Queue is empty.
        """
        return self.first

    def rear(self):
        """
        Returns last element of Queue.
        Returns None if Queue is empty.
        """
        return self.last
