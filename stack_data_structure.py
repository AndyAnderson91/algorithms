class Stack:
    """
    Linear collection of elements built on the LIFO (last in - first out) principle.
    Supported methods: __init__, __iter__, __contains__, __len__, __repr__, push, pop, is_empty, peek.
    """

    class Node:
        """
        singly linked list element.
        Supported methods: __init__, __repr__.
        """

        def __init__(self, data, next_node=None):
            """
            Contains data and link to the next node.
            """
            self.data = data
            self.next = next_node

        def __repr__(self):
            """
            String representation of contained data.
            """
            return "'{}'".format(self.data) if isinstance(self.data, str) else str(self.data)

    def __init__(self, iterable=()):
        """
        Contains it's length and link to the top element.
        If iterable is provided, adds elements to the stack in a given order,
        means last element in iterable becomes top element of the stack:
        For example, ('a', 'b', 'c') will be added as 'c' <-- 'b' <-- 'a'.
        Raises TypeError if non-iterable object is provided.
        """
        self.top = None
        self._length = 0

        if iter(iterable):
            for element in iterable:
                self.push(element)

    def __iter__(self):
        """
        Traversal implementation.
        """
        cur_node = self.top
        while cur_node:
            yield cur_node
            cur_node = cur_node.next

    def __contains__(self, item):
        """
        Returns True if item in stack. Otherwise False.
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
        String representation of all nodes in the SinglyLinkedList.
        """
        nodes_str = []
        for node in self:
            node_str = "'{}'".format(node.data) if isinstance(node.data, str) else str(node.data)
            nodes_str.append(node_str)

        return '«' + ' <-- '.join(nodes_str) + '»'

    def push(self, data):
        """
        Adds element on the top of the stack.
        """
        self.top = self.Node(data, self.top)
        self._length += 1

    def pop(self):
        """
        Removes top element from the stack and returns it.
        If stack is empty, IndexError is raised.
        """
        if not self.top:
            raise IndexError('Empty stack')

        node_to_remove = self.top
        self.top = node_to_remove.next
        self._length -= 1

        return node_to_remove

    def is_empty(self):
        """
        Returns True if Stack is empty, False otherwise.
        """
        return not bool(self.top)

    def peek(self):
        """
        Returns top element of the Stack without removing it.
        Returns None if Stack is empty.
        """
        return self.top
