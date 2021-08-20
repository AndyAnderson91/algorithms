"""
This module contains 2 data structures:
SinglyLinkedList and DoublyLinkedList.
"""


class SinglyLinkedList:
    """
    Linear collection of elements where each element points to the next one.
    If there is no next element, it points to None.
    Supported methods: __init__, __iter__, __contains__, __repr__, __len__,
    __getitem__, __setitem__, get, add, insert, pop.
    """

    class Node:
        """
        SinglyLinkedList element.
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
        Contains it's length and link to the first element.
        If iterable is provided, adds elements to the list in a given order.
        Means ('a', 'b', 'c') will be added as 'a' --> 'b' --> 'c'.
        Raises TypeError if non-iterable object is provided.
        """
        self.first = None
        self._length = 0

        if iter(iterable):
            for i in range(len(iterable) - 1, -1, -1):
                self.insert(iterable[i], 0)

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

    def __getitem__(self, index):
        """
        Returns node by required index.
        Unlike get() method, raise IndexError if index is out of range.
        """
        # Checks if index is out of range.
        if not (-self._length <= index <= self._length - 1):
            raise IndexError('List index is out of range')
        else:
            return self.get(index)

    def __setitem__(self, index, data):
        """
        Overwrites node with required index by provided data.
        If required index is out of range, raise IndexError if index is out of range.
        """
        if not (-self._length <= index <= self._length - 1):
            raise IndexError('List index is out of range')
        else:
            self.get(index).data = data

    def __repr__(self):
        """
        String representation of all nodes in the SinglyLinkedList.
        """
        nodes_str = []
        for node in self:
            node_str = "'{}'".format(node.data) if isinstance(node.data, str) else str(node.data)
            nodes_str.append(node_str)

        return '«' + ' --> '.join(nodes_str) + '»'

    def get(self, index):
        """
        Basically behaves the same as dict.get() in python.
        Returns node by required index.
        Positive, zero and negative indexes are supported.
        Returns None if node with required index doesn't exist.
        """
        # Checks if index is out of range.
        if not (-self._length <= index <= self._length - 1):
            return None

        # Converts negative indexes to positive.
        if index < 0:
            index = index + self._length

        # Gets required node.
        cur_node = self.first
        for i in range(index):
            cur_node = cur_node.next

        return cur_node

    def add(self, data):
        """
        Adds element in the front of the list.
        Unlike insert method, doesn't support indexing.
        """
        self.first = self.Node(data, self.first)
        self._length += 1

    def insert(self, data, index):
        """
        Basically behaves the same as list.insert() in python.
        Inserts element before index.
        Positive, zero and negative indexes are supported.
        """
        # If index is bigger than length of the list, element is inserted in the end.
        if index > self._length:
            index = self._length
        # Negative index which is in range converts to positive.
        elif -self._length < index < 0:
            index = self._length + index
        # if index is less than -length of the list, element is inserted at the front.
        elif index <= -self._length:
            index = 0

        # None if there is no next node.
        next_node = self.get(index)

        new_node = self.Node(data, next_node)

        # If element is inserted in front,
        # overwrites 'first' link of the SinglyLinkedList.
        if index == 0:
            self.first = new_node

        # Otherwise overwrites 'next' link of the previous element.
        else:
            prev_node = self.get(index - 1)
            prev_node.next = new_node

        self._length += 1

    def pop(self, index=0):
        """
        Basically behaves the same as list.pop() in python.
        Removes the node at required index from the list and returns it.
        Positive, zero and negative indexes are supported.
        If node with required index doesn't exist, IndexError will be raised.
        If index is not provided, first element will be removed and returned.
        """
        if self._length == 0:
            raise IndexError('List is empty.')
        elif not (-self._length <= index <= self._length - 1):
            raise IndexError('Linked list index is out of range.')

        # Converts negative indexes to positive.
        if index < 0:
            index = index + self._length

        node_to_remove = self.get(index)

        # If popped element is first, overwrites 'first' link of the SinglyLinkedList.
        if index == 0:
            self.first = node_to_remove.next

        # Otherwise overwrites 'next' link of previous element.
        else:
            prev_node = self.get(index - 1)
            prev_node.next = node_to_remove.next

        self._length -= 1

        return node_to_remove


class DoublyLinkedList:
    """
    Linear collection of elements where each element points to the next and previous elements.
    If there is no next element, it points to None. Same about previous element.
    Supported methods: __init__, __iter__, __contains__, __repr__, __len__,
    __getitem__, __setitem__, get, add, insert, pop.
    """

    class Node:
        """
        DoublyLinkedList element.
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

    def __init__(self, iterable=()):
        """
        Contains it's length and link to the first and last elements.
        If iterable is provided, adds elements to the list in a given order.
        Means ('a', 'b', 'c') will be added as 'a' --> 'b' --> 'c'.
        Raises TypeError if non-iterable object is provided.
        """
        self.first = None
        self.last = None
        self._length = 0

        if iter(iterable):
            for i in range(len(iterable) - 1, -1, -1):
                self.insert(iterable[i], 0)

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

    def __getitem__(self, index):
        """
        Returns node by required index.
        Unlike get() method, raise IndexError if index is out of range.
        """
        # Checks if index is out of range.
        if not (-self._length <= index <= self._length - 1):
            raise IndexError('List index is out of range')
        else:
            return self.get(index)

    def __setitem__(self, index, data):
        """
        Overwrites node with required index by provided data.
        If required index is out of range, raise IndexError if index is out of range.
        """
        if not (-self._length <= index <= self._length - 1):
            raise IndexError('List index is out of range')
        else:
            self.get(index).data = data

    def __repr__(self):
        """
        String representation of all nodes in the DoublyLinkedList.
        """
        nodes_str = []
        for node in self:
            node_str = "'{}'".format(node.data) if isinstance(node.data, str) else str(node.data)
            nodes_str.append(node_str)

        return '«' + ' <--> '.join(nodes_str) + '»'

    def get(self, index):
        """
        Basically behaves the same as dict.get() in python.
        Returns node by required index.
        Positive, zero and negative indexes are supported.
        Returns None if node with required index doesn't exist.
        If index is closer to the start, list traversal is going from the first node,
        otherwise it's going from the last node.
        """
        # Checks if index is out of range.
        if not (-self._length <= index <= self._length - 1):
            return None

        # Converts negative indexes to positive.
        if index < 0:
            index = index + self._length

        # Checks if required index is closer to the start of the list.
        if index < self._length - index - 1:
            cur_node = self.first
            for i in range(index):
                cur_node = cur_node.next

        # Required index is closer to the end of the list or exactly in the middle.
        else:
            cur_node = self.last
            for i in range(self._length - index - 1):
                cur_node = cur_node.prev

        return cur_node

    def add(self, data):
        """
        Adds element in the end of the list.
        Unlike insert method, doesn't support indexing.
        """
        prev_node = self.last
        self.last = self.Node(data, prev_node, None)
        # Checks if previous node exists.
        if prev_node:
            prev_node.next = self.last

        # If list was empty, new node is now first and last node.
        else:
            self.first = self.last

        self._length += 1

    def insert(self, data, index):
        """
        Basically behaves the same as list.insert() in python.
        Inserts element before index.
        Positive, zero and negative indexes are supported.
        """
        # If index is bigger than length of the list, element is inserted in the end.
        if index > self._length:
            index = self._length
        # Negative index which is in range converts to positive.
        elif -self._length < index < 0:
            index = self._length + index
        # if index is less than -length of the list, element is inserted at the front.
        elif index <= -self._length:
            index = 0

        # Checks if new node is inserted to the end of the list.
        if index == self._length:
            prev_node = self.get(index-1)
            new_node = self.Node(data, prev_node, None)
            self.last = new_node
            # Checks if previous node exists.
            if prev_node:
                prev_node.next = new_node
            # Means list was empty and new node is now first and last node.
            else:
                self.first = new_node

        # inserts node to any existing position.
        else:
            next_node = self.get(index)
            prev_node = next_node.prev
            new_node = self.Node(data, prev_node, next_node)
            next_node.prev = new_node
            # Checks if previous node exists.
            if prev_node:
                prev_node.next = new_node
            # Means new node is now first.
            else:
                self.first = new_node

        self._length += 1

    def pop(self, index=0):
        """
        Basically behaves the same as list.pop() in python.
        Removes the node at required index from the list and returns it.
        Positive, zero and negative indexes are supported.
        If node with required index doesn't exist, IndexError will be raised.
        If index is not provided, first element will be removed and returned.
        """
        if self._length == 0:
            raise IndexError('List is empty.')
        elif not (-self._length <= index <= self._length - 1):
            raise IndexError('Index is out of range.')

        # Converts negative indexes to positive.
        if index < 0:
            index = index + self._length

        node_to_remove = self.get(index)

        # Checks removed node has previous.
        if node_to_remove.prev:
            node_to_remove.prev.next = node_to_remove.next
        # Means removed node is first one.
        else:
            self.first = node_to_remove.next
        # Checks removed node has next.
        if node_to_remove.next:
            node_to_remove.next.prev = node_to_remove.prev
        # Means removed node is last
        else:
            self.last = node_to_remove.prev

        self._length -= 1

        return node_to_remove
