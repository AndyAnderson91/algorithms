class DoublyLinkedList:
    """
    Linear collection of elements where each element points to the next and previous elements.
    If there is no next element, it points to None. Same about previous element.
    Supported methods: get, add, pop, show_nodes.
    """

    class Node:
        """
        Doubly Linked list element.
        """

        def __init__(self, data, prev=None, next=None):
            """
            Contains data and links to the previous and next nodes.
            By default prev and next links are None.
            """
            self.prev = prev
            self.next = next
            self.data = data

        def __repr__(self):
            return str(self.data)

    def __init__(self):
        """
        Doubly Linked List contains its length and links to the first and last elements.
        """
        self.first = None
        self.last = None
        self.length = 0

    def add(self, data, index=None):
        """
        Basically behaves the same as list.insert() in python with
        only positive and zero indexes supported.
        Possible to call without providing index argument,
        in this case behaves the same as list.append().
        For example, if current Double Linked List contains 3 elements,
        available indexes to add new node are:
        0 - new node is inserted in the front of the list.
        1, 2 - node is inserted in a given position. Being there node is moved to 'next'.
        3 or None - new node is inserted to the end of the list.
        Other indexes will raise IndexError.
        """
        if index is None:
            index = self.length

        if index < 0:
            raise IndexError('Negative indexes are not supported in add method.')
        elif not (0 <= index <= self.length):
            raise IndexError('Index is out of range')

        if index == self.length:
            # Adds node to the end of the list.
            prev_node = self.get(index-1)
            new_node = self.Node(data, prev_node, None)
            self.last = new_node
            if prev_node:
                # Means list wasn't empty.
                prev_node.next = new_node
            else:
                # Means list was empty and new node is now first and last node.
                self.first = new_node

        else:
            # Adds node to any existing position.
            next_node = self.get(index)
            prev_node = next_node.prev
            new_node = self.Node(data, prev_node, next_node)
            next_node.prev = new_node
            if prev_node:
                # Means new node isn't first.
                prev_node.next = new_node
            else:
                # Means new node is now first.
                self.first = new_node

        self.length += 1

    def get(self, index):
        """
        Basically behaves the same as dict.get() in python.
        Returns required node by index.
        Returns None if node with such index doesn't exist.
        Positive, zero and negative indexes are supported.
        If index is closer to the start, list traversal is going from the first node,
        otherwise it's going from the last node.
        """

        if not (-self.length <= index <= self.length - 1):
            # Checks if index is out of range.
            return None

        if index < 0:
            index = index + self.length

        if index < self.length - index - 1:
            # Means required element is closer to the start of the list.
            cur_node = self.first
            for i in range(index):
                cur_node = cur_node.next
        else:
            # Means required element is closer to the end of the list or exactly in the middle.
            cur_node = self.last
            for i in range(self.length - index - 1):
                cur_node = cur_node.prev

        return cur_node

    def pop(self, index=None):
        """
        Basically behaves the same as list.pop() in python.
        Removes the node at required index from the list and returns it.
        If index is not provided, last element will be removed and returned.
        Positive, zero and negative indexes are supported.
        If node with such index doesn't exist, IndexError will be raised.
        """

        if index is None:
            index = self.length - 1

        if self.length == 0:
            raise IndexError('List is empty.')
        elif not (-self.length <= index <= self.length - 1):
            raise IndexError('Index is out of range.')

        if index < 0:
            index = index + self.length

        deleted_node = self.get(index)
        if deleted_node.prev:
            # Means deleted node isn't first one.
            deleted_node.prev.next = deleted_node.next
        else:
            # If it was first, defines new 'first'.
            self.first = deleted_node.next
        if deleted_node.next:
            # Means deleted node isn't last one.
            deleted_node.next.prev = deleted_node.prev
        else:
            # Defines new 'last'.
            self.last = deleted_node.prev

        self.length -= 1

        return deleted_node

    def show_nodes(self):
        """
        Returns array with all elements in Doubly Linked List.
        """
        nods = []

        if self.first:
            cur_node = self.first
            while cur_node:
                nods.append(cur_node)
                cur_node = cur_node.next

        return nods
