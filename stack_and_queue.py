"""
Stack and Queue classes.
Stack implementation is based on singly linked list,
while Queue is implemented via doubly linked list.

Stack usage example:
-------
>> s = Stack([False, 3, 'elem'])
>> s
«False -- 3 -- 'elem'»
>> s.push('fresh')                     # «False -- 3 -- 'elem' -- 'fresh'»
>> s.pop()                             # «False -- 3 -- 'elem'»
'fresh'
>> s.peek()
'elem'
>> s.is_empty()
False
>> False in s
True
>> len(s)
3

Queue usage example:
-------
>> q = Queue(['one', 2, None])
>> q
«'one' <-- 2 <-- None»
>> q.enqueue({'english': 'en'})              # «'one' <-- 2 <-- None <-- {'english': 'en'}»
>> q.dequeue()                               # «2 <-- None <-- {'english': 'en'}»
'one'
>> q.front()
2
>> q.rear()
{'english': 'en'}
>> q.is_empty()
False
>> 2 in q
True
>> len(q)
3
"""
from linked_lists import SLLNode, DLLNode, LLCommonMethods


class Stack(LLCommonMethods):
    """
    Linear collection of elements built on the LIFO (last in - first out) principle.
    Inherited methods: _build_linked_list, __len__, __contains__.
    Self methods: __init__, __iter__, push, pop, is_empty, peek.
    """

    def __init__(self, iterable=()):
        self.top = None
        self._length = 0

        self._build_linked_list(iterable, self.push)

    def __iter__(self):
        cur_node = self.top
        while cur_node:
            yield cur_node.value
            cur_node = cur_node.next

    def __repr__(self):
        values_repr = []
        for node_value in self:
            # Makes str data to be represented in single quotes.
            value_repr = "'{}'".format(node_value) if isinstance(node_value, str) else str(node_value)
            values_repr.append(value_repr)

        # Top element of the stack is displayed on the right side.
        return '«' + ' -- '.join(reversed(values_repr)) + '»'

    def push(self, value):
        """
        Adds element on the top of the stack.
        """
        self.top = SLLNode(value, self.top)
        self._length += 1

    def pop(self):
        """
        Removes top element from the stack and returns it's value.
        If stack is empty, IndexError is raised.
        """
        if not self.top:
            raise IndexError('Empty stack')

        node_to_remove = self.top
        self.top = node_to_remove.next
        self._length -= 1

        return node_to_remove.value

    def is_empty(self):
        return not bool(self.top)

    def peek(self):
        """
        Returns top element's value.
        Returns None if Stack is empty.
        """
        return self.top.value if self.top is not None else None


class Queue(LLCommonMethods):
    """
    Linear collection of elements built on the FIFO (first in - first out) principle.
    inherited methods: _build_linked_list, __iter__, __len__, __contains__, __repr__.
    Self methods: __init__, enqueue, dequeue, is_empty, front, rear.
    """

    def __init__(self, iterable=()):
        self.first = None
        self.last = None
        self._length = 0

        self._build_linked_list(iterable, self.enqueue)

    def __repr__(self):
        return super().__repr__().replace('{*}', '<--')

    def enqueue(self, value):
        """
        Adds element to the end of Queue.
        """
        prev_node = self.last
        self.last = DLLNode(value, prev_node, None)
        if prev_node:
            prev_node.next = self.last
        else:
            self.first = self.last

        self._length += 1

    def dequeue(self):
        """
        Removes front element from queue and returns it's value.
        If Queue is empty, IndexError is raised.
        """
        if not self.first:
            raise IndexError('Empty Queue')

        node_to_remove = self.first

        self.first = node_to_remove.next

        if self.first:
            self.first.prev = None
        else:
            self.last = None

        self._length -= 1

        return node_to_remove.value

    def is_empty(self):
        return not bool(self.first)

    def front(self):
        """
        Returns first element's value.
        Returns None if queue is empty.
        """
        return self.first.value if self.first is not None else None

    def rear(self):
        """
        Returns last element's value.
        Returns None if queue is empty.
        """
        return self.last.value if self.last is not None else None
