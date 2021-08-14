class SinglyLinkedList:
    """
    Linear collection of elements where each element points to the next one.
    If there is no next element, it points to None.
    Supported methods: get, add, pop, show_nodes.
    """

    class Node:
        """
        Singly Linked list element.
        """

        def __init__(self, data, next=None):
            """
            Contains data and link to the next node.
            By default next is None.
            """
            self.next = next
            self.data = data

        def __repr__(self):
            return str(self.data)

    def __init__(self):
        """
        Singly Linked List contains its length and link to the first element.
        """
        self.first = None
        self.length = 0

    def add(self, data, index=None):
        """
        Basically behaves the same as list.insert() in python with
        only positive and zero indexes supported.
        Possible to call without providing index argument,
        in this case behaves the same as list.append().
        For example, if current Singly Linked List contains 3 elements,
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
            raise IndexError('List index out of range')

        next_node = self.get(index)
        new_node = self.Node(data, next_node)

        if index > 0:
            # Means new node isn't first.
            prev_node = self.get(index - 1)
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

        """

        if not (-self.length <= index <= self.length - 1):
            # Checks if index is out of range.
            return None

        if index < 0:
            index = index + self.length

        cur_node = self.first
        for i in range(index):
            cur_node = cur_node.next

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
            raise IndexError('Linked list index is out of range.')

        if index < 0:
            index = index + self.length

        deleted_node = self.get(index)

        if index > 0:
            # Means deleted node isn't first one.
            prev_node = self.get(index - 1)
            prev_node.next = deleted_node.next
        else:
            # If it was first, now we need new 'first'.
            self.first = deleted_node.next

        self.length -= 1

        return deleted_node

    def show_nodes(self):
        """
        Returns array with all elements in LinkedList.
        """
        nods = []

        if self.first:
            cur_node = self.first
            while cur_node:
                nods.append(cur_node)
                cur_node = cur_node.next

        return nods
