class Queue:
    """
    Linear collection of elements built on the FIFO (first in - first out) principle.
    Supported methods: __init__, __iter__, __contains__, __len__, __repr__, enqueue, dequeue, is_empty, front, rear.
    """

    class Node:
        """
        doubly linked list element.
        """
        def __init__(self, data, prev_node=None, next_node=None):
            """
            Contains data and links to the previous and next nodes.
            """
            self.data = data
            self.prev = prev_node
            self.next = next_node

        def __repr__(self):
            """
            String representation of contained data.
            """
            return "'{}'".format(self.data) if isinstance(self.data, str) else str(self.data)

    def __init__(self):
        """
        Contains its length and links to the first and last elements.
        """
        self.first = None
        self.last = None
        self._length = 0

    def __iter__(self):
        """
        Traversal implementation.
        """
        cur_node = self.first
        while cur_node:
            yield cur_node
            cur_node = cur_node.next

    def __contains__(self, item):
        """
        Returns True if item in singly linked list. Otherwise False.
        """
        for node in self:
            if node.data == item:
                return True

        return False

    def __len__(self):
        """
        Returns number of nodes.
        """
        return self._length

    def __repr__(self):
        """
        String representation of all nodes in the DoublyLinkedList.
        """
        nodes_str = []
        for node in self:
            node_str = "'{}'".format(node.data) if isinstance(node.data, str) else str(node.data)
            nodes_str.append(node_str)

        return '«' + ' <-- '.join(nodes_str) + '»'

    def enqueue(self, data):
        """
        Adds element to the end of Queue.
        """
        prev_node = self.last
        self.last = self.Node(data, prev_node, None)
        # Checks if previous node exists.
        if prev_node:
            prev_node.next = self.last

        # If queue was empty, new node is now first and last node.
        else:
            self.first = self.last

        self._length += 1

    def dequeue(self):
        """
        Removes front element from queue and returns it.
        If Queue is empty, IndexError is raised.
        """
        if not self.first:
            raise IndexError('Empty Queue')

        node_to_remove = self.first

        # Next element becomes 'first'.
        self.first = node_to_remove.next

        # Checks queue won't be empty after dequeue.
        if self.first:
            self.first.prev = None
        # If queue is empty after dequeue, first and last links points to None.
        else:
            self.last = None

        self._length -= 1

        return node_to_remove

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
