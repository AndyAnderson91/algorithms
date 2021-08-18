"""
This module contains 2 data structures:
SinglyLinkedList and DoublyLinkedList.
"""


class SinglyLinkedList:
    """
    Linear collection of elements where each element points to the next one.
    If there is no next element, it points to None.
    Supported methods: __init__, __repr__, __iter__, get, add, pop.
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
            return str(self.data)

    def __init__(self):
        """
        Contains it's length and link to the first element. Created empty.
        """
        self.first = None
        self.length = 0

    def __iter__(self):
        """
        Traversal implementation.
        """
        cur_node = self.first
        while cur_node:
            yield cur_node
            cur_node = cur_node.next

    def __repr__(self):
        """
        String representation of all nodes in the SinglyLinkedList.
        """
        nodes = []
        for node in self:
            nodes.append(str(node))

        return '«' + ' --> '.join(nodes) + '»'

    def get(self, index):
        """
        Basically behaves the same as dict.get() in python.
        Returns node by required index.
        Positive, zero and negative indexes are supported.
        Returns None if node with required index doesn't exist.
        """
        # Checks if index is out of range.
        if not (-self.length <= index <= self.length - 1):
            return None

        # Converts negative indexes to positive.
        if index < 0:
            index = index + self.length

        # Gets required node.
        cur_node = self.first
        for i in range(index):
            cur_node = cur_node.next

        return cur_node

    def add(self, data, index=0):
        """
        Basically behaves the same as list.insert() in python.
        Inserts element before index.
        Positive, zero and negative indexes are supported.
        If no index is provided, new element is added in the front of the list.
        """
        # If index is bigger than length of the list, element is added in the end.
        if index > self.length:
            index = self.length
        # Negative index which is in range converts to positive.
        elif -self.length < index < 0:
            index = self.length + index
        # if index is less than -length of the list, element is added at the front.
        elif index <= -self.length:
            index = 0

        # None if there is no next node.
        next_node = self.get(index)

        new_node = self.Node(data, next_node)

        # If element is added in front,
        # overwrites 'first' link of the SinglyLinkedList.
        if index == 0:
            self.first = new_node

        # Otherwise overwrites 'next' link of the previous element.
        else:
            prev_node = self.get(index - 1)
            prev_node.next = new_node

        self.length += 1

    def pop(self, index=0):
        """
        Basically behaves the same as list.pop() in python.
        Removes the node at required index from the list and returns it.
        Positive, zero and negative indexes are supported.
        If node with required index doesn't exist, IndexError will be raised.
        If index is not provided, first element will be removed and returned.
        """
        if self.length == 0:
            raise IndexError('List is empty.')
        elif not (-self.length <= index <= self.length - 1):
            raise IndexError('Linked list index is out of range.')

        # Converts negative indexes to positive.
        if index < 0:
            index = index + self.length

        node_to_remove = self.get(index)

        # If popped element is first, overwrites 'first' link of the SinglyLinkedList.
        if index == 0:
            self.first = node_to_remove.next

        # Otherwise overwrites 'next' link of previous element.
        else:
            prev_node = self.get(index - 1)
            prev_node.next = node_to_remove.next

        self.length -= 1

        return node_to_remove


class DoublyLinkedList:
    """
    Linear collection of elements where each element points to the next and previous elements.
    If there is no next element, it points to None. Same about previous element.
    Supported methods: __init__, __iter__, __repr__, get, add, pop.
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
            return str(self.data)

    def __init__(self):
        """
        Contains its length and links to the first and last elements.
        """
        self.first = None
        self.last = None
        self.length = 0

    def __iter__(self):
        """
        Traversal implementation.
        """
        cur_node = self.first
        while cur_node:
            yield cur_node
            cur_node = cur_node.next

    def __repr__(self):
        """
        String representation of all nodes in the DoublyLinkedList.
        """
        nodes = []
        for node in self:
            nodes.append(str(node))

        return '«' + ' <--> '.join(nodes) + '»'

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
        if not (-self.length <= index <= self.length - 1):
            return None

        # Converts negative indexes to positive.
        if index < 0:
            index = index + self.length

        # Checks if required index is closer to the start of the list.
        if index < self.length - index - 1:
            cur_node = self.first
            for i in range(index):
                cur_node = cur_node.next

        # Required index is closer to the end of the list or exactly in the middle.
        else:
            cur_node = self.last
            for i in range(self.length - index - 1):
                cur_node = cur_node.prev

        return cur_node

    def add(self, data, index=0):
        """
        Basically behaves the same as list.insert() in python.
        Inserts element before index.
        Positive, zero and negative indexes are supported.
        If no index is provided, new element is added in the front of the list.
        """
        # If index is bigger than length of the list, element is added in the end.
        if index > self.length:
            index = self.length
        # Negative index which is in range converts to positive.
        elif -self.length < index < 0:
            index = self.length + index
        # if index is less than -length of the list, element is added at the front.
        elif index <= -self.length:
            index = 0

        # Checks if new node is added to the end of the list.
        if index == self.length:
            prev_node = self.get(index-1)
            new_node = self.Node(data, prev_node, None)
            self.last = new_node
            # Checks if previous node exists.
            if prev_node:
                prev_node.next = new_node
            # Means list was empty and new node is now first and last node.
            else:
                self.first = new_node

        # Adds node to any existing position.
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

        self.length += 1

    def pop(self, index=0):
        """
        Basically behaves the same as list.pop() in python.
        Removes the node at required index from the list and returns it.
        Positive, zero and negative indexes are supported.
        If node with required index doesn't exist, IndexError will be raised.
        If index is not provided, first element will be removed and returned.
        """
        if self.length == 0:
            raise IndexError('List is empty.')
        elif not (-self.length <= index <= self.length - 1):
            raise IndexError('Index is out of range.')

        # Converts negative indexes to positive.
        if index < 0:
            index = index + self.length

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

        self.length -= 1

        return node_to_remove
