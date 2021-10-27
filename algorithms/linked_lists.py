"""
Singly and doubly linked lists implementations.
Main classes are SinglyLinkedList and DoublyLinkedList.
Other classes are used as mixins (LLCommonMethods and LLItemAccessMethods) or
as support classes (SLLNode and DLLNode).

Single linked list usage example:
--------
>> sll = SinglyLinkedList([1, 'two', True])
>> sll
«True --> 'two' --> 1»
>> sll.add(25)                      # «25 --> True --> 'two' --> 1»
>> sll.insert('middle', 2)          # «25 --> True --> 'middle' --> 'two' --> 1»
>> sll.pop()                        # «True --> 'middle' --> 'two' --> 1»
25
>> sll.pop(-1)                      # «True --> 'middle' --> 'two'»
1
>> sll[0] = False                   # «False --> 'middle' --> 'two'»
>> sll[1]
'middle'
>> 'two' in sll
True
>> len(sll)
3

Doubly linked list usage example:
--------
>> dll = DoublyLinkedList(['text', 21, (1, 2, 3)])
>> dll
«(1, 2, 3) <--> 21 <--> 'text'»
>> dll.add('start')                 # «'start' <--> (1, 2, 3) <--> 21 <--> 'text'»
>> dll.insert('penultimate', -1)    # «'start' <--> (1, 2, 3) <--> 21 <--> 'penultimate' <--> 'text'»
>> dll.pop()                        # «(1, 2, 3) <--> 21 <--> 'penultimate' <--> 'text'»
'start'
>> dll[0] = ()                      # «() <--> 21 <--> 'penultimate' <--> 'text'»
>> dll[1]
21
>> 34 in dll
False
>> len(dll)
4
"""


class SLLNode:
    """Singly linked list element."""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class DLLNode:
    """Doubly linked list element."""
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev = prev_node
        self.next = next_node


class LLCommonMethods:
    """
    This Class is only used for inheritance.
    Parent class for SinglyLinkedList, DoublyLinkedList, Stack and Queue classes.
    Contains _build_linked_list, __iter__, __len__, __contains__ and __repr__ methods.
    """
    @staticmethod
    def _build_linked_list(iterable, add_function):
        # add_function is one that adds element to linked list in constant time.
        # It's specific for every child class (add for SLL and DLL, push for Stack and enqueue for Queue)
        if iter(iterable):
            for element in iterable:
                add_function(element)

    def __iter__(self):
        cur_node = self._first
        while cur_node:
            yield cur_node.value
            cur_node = cur_node.next

    def __len__(self):
        return self._length

    def __contains__(self, item):
        for node_value in self:
            if node_value == item:
                return True

        return False

    def __repr__(self):
        values_repr = []
        for node_value in self:
            # Makes str data to be represented in single quotes.
            value_repr = "'{}'".format(node_value) if isinstance(node_value, str) else str(node_value)
            values_repr.append(value_repr)

        # {*} will be replaced for appropriate symbol in every child class.
        return '«' + ' {*} '.join(values_repr) + '»'


class LLItemsAccessMethods:
    """
    This Class is only used for inheritance.
    Parent class for SinglyLinkedList and DoublyLinkedList.
    Contains __getitem__ and __setitem__ methods.
    """
    def __getitem__(self, index):
        node = self._get_node(index)
        if node is None:
            raise IndexError('linked list index out of range')
        else:
            return node.value

    def __setitem__(self, index, value):
        node = self._get_node(index)
        if node is None:
            raise IndexError('list index out of range')
        else:
            self._get_node(index).value = value


class SinglyLinkedList(LLCommonMethods, LLItemsAccessMethods):
    """
    Linear collection of elements where each element (node) has a link to the next one.
    If there is no next element, it points to None.
    Inherited methods: _build_linked_list, __iter__, __len__, __contains__, __repr__,
    __getitem__, __setitem__.
    Self methods: __init__, _get_node, add, insert, pop.
    """

    def __init__(self, iterable=()):
        self._first = None
        self._length = 0

        self._build_linked_list(iterable, self.add)

    def __repr__(self):
        return super().__repr__().replace('{*}', '-->')

    def _get_node(self, index):
        """
        Returns node by required index.
        Returns None if node with required index doesn't exist.
        """
        if not (-self._length <= index <= self._length - 1):
            return None

        # Converts negative indexes to positive.
        index = index + self._length if index < 0 else index

        cur_node = self._first
        for i in range(index):
            cur_node = cur_node.next

        return cur_node

    def add(self, value):
        """Adds element in the front of the list. O(1) time complexity."""
        self._first = SLLNode(value, self._first)
        self._length += 1

    def insert(self, value, index):
        """
        Basically behaves the same as list.insert() in python.
        Inserts element before index.
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

        next_node = self._get_node(index)
        new_node = SLLNode(value, next_node)

        if index == 0:
            self._first = new_node
        else:
            prev_node = self._get_node(index - 1)
            prev_node.next = new_node

        self._length += 1

    def pop(self, index=0):
        """
        Basically behaves the same as list.pop() in python.
        Removes the node at required index from the list and returns it's value.
        If node with required index doesn't exist, IndexError will be raised.
        If index is not provided - remove first node and returns it's value. O(1) time complexity in this case.
        """
        if self._length == 0:
            raise IndexError('List is empty.')
        elif not (-self._length <= index <= self._length - 1):
            raise IndexError('Linked list index is out of range.')

        # Converts negative indexes to positive.
        index = index + self._length if index < 0 else index

        node_to_remove = self._get_node(index)

        if index == 0:
            self._first = node_to_remove.next
        else:
            prev_node = self._get_node(index - 1)
            prev_node.next = node_to_remove.next

        self._length -= 1

        return node_to_remove.value


class DoublyLinkedList(LLCommonMethods, LLItemsAccessMethods):
    """
    Linear collection of elements where each element (node) has links to the next and previous elements.
    If there is no next or previous element, related link points to None.
    Inherited methods: _build_linked_list, __iter__, __len__, __contains__, __repr__,
    __getitem__, __setitem__.
    Self methods: __init__, _get_node, add, insert, pop.
    """
    def __init__(self, iterable=()):
        self._first = None
        self._last = None
        self._length = 0

        self._build_linked_list(iterable, self.add)

    def __repr__(self):
        return super().__repr__().replace('{*}', '<-->')

    def _get_node(self, index):
        """
        Returns node by required index.
        Returns None if node with required index doesn't exist.
        If index is closer to the start, list traversal is going from the first node,
        otherwise it's going from the last node.
        """
        if not (-self._length <= index <= self._length - 1):
            return None

        # Converts negative indexes to positive.
        index = index + self._length if index < 0 else index

        if index < self._length - index - 1:
            cur_node = self._first
            for i in range(index):
                cur_node = cur_node.next
        else:
            cur_node = self._last
            for i in range(self._length - index - 1):
                cur_node = cur_node.prev

        return cur_node

    def add(self, value):
        """Adds element in the front of the list. O(1) time complexity."""
        next_node = self._first
        self._first = DLLNode(value, None, next_node)
        if next_node:
            next_node.prev = self._first
        else:
            self._last = self._first

        self._length += 1

    def insert(self, value, index):
        """
        Basically behaves the same as list.insert() in python.
        Inserts element before index.
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

        if index == self._length:
            prev_node = self._get_node(index-1)
            new_node = DLLNode(value, prev_node, None)
            self._last = new_node
        else:
            next_node = self._get_node(index)
            prev_node = next_node.prev
            new_node = DLLNode(value, prev_node, next_node)
            next_node.prev = new_node

        if prev_node:
            prev_node.next = new_node
        else:
            self._first = new_node

        self._length += 1

    def pop(self, index=0):
        """
        Basically behaves the same as list.pop() in python,
        but by default removes first element instead of last.
        (For more similar behaviour with SinglyLinkedList).
        Removes the node at required index from the list and returns it's value.
        If node with required index doesn't exist, IndexError will be raised.
        If index is not provided - remove last node and returns it's value. O(1) time complexity in this case.
        """
        if self._length == 0:
            raise IndexError('List is empty.')
        elif not (-self._length <= index <= self._length - 1):
            raise IndexError('Index is out of range.')

        # Converts negative indexes to positive.
        index = index + self._length if index < 0 else index

        node_to_remove = self._get_node(index)

        if node_to_remove.prev:
            node_to_remove.prev.next = node_to_remove.next
        else:
            self._first = node_to_remove.next

        if node_to_remove.next:
            node_to_remove.next.prev = node_to_remove.prev
        else:
            self._last = node_to_remove.prev

        self._length -= 1

        return node_to_remove.value
