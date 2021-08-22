class Queue:
    """
    Linear collection of elements built on the FIFO (first in - first out) principle.
    Supported methods: __init__, __iter__, __contains__, __len__, __repr__, enqueue, dequeue, is_empty, front, rear.
    """

    class Node:
        """
        Queue element.
        """
        def __init__(self, data, prev_node=None, next_node=None):
            """
            Contains data and links to the previous and next nodes.
            """
            self.data = data
            self.prev = prev_node
            self.next = next_node

    def __init__(self, iterable=()):
        """
        Contains its length and links to the first and last elements.
        If iterable is provided, adds elements to the queue in a given order,
        means first element in iterable becomes first in queue.
        For example, ('a', 'b', 'c') will be added as 'a' <-- 'b' <-- 'c'.
        Raises TypeError if non-iterable object is provided.
        """
        self.first = None
        self.last = None
        self._length = 0

        if iter(iterable):
            for element in iterable:
                self.enqueue(element)

    def __iter__(self):
        """
        Traversal implementation.
        """
        cur_node = self.first
        while cur_node:
            yield cur_node.data
            cur_node = cur_node.next

    def __contains__(self, item):
        """
        Returns True if item in Queue. Otherwise False.
        """
        for node_data in self:
            if node_data == item:
                return True

        return False

    def __len__(self):
        """
        Returns number of contained items.
        """
        return self._length

    def __repr__(self):
        """
        String representation of all nodes in the Queue.
        """
        nodes_str = []
        for node_data in self:
            node_str = "'{}'".format(node_data) if isinstance(node_data, str) else str(node_data)
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
        Removes front element from queue and returns it's data.
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

        return node_to_remove.data

    def is_empty(self):
        """
        Returns True if Queue is empty, False otherwise.
        """
        return not bool(self.first)

    def front(self):
        """
        Returns first item of the Queue.
        Returns None if Queue is empty.
        """
        return self.first.data

    def rear(self):
        """
        Returns last item of the Queue.
        Returns None if Queue is empty.
        """
        return self.last.data
