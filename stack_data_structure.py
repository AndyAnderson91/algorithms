from linked_lists import SinglyLinkedList


class Stack(SinglyLinkedList):
    """
    Stack can be considered as a special case of SinglyLinkedList.
    Inherited methods: __init__, __iter__, get.
    Overridden methods: __repr__, add, pop.
    New methods: is_empty, peek.
    """
    def __repr__(self):
        """
        String representation of all nodes in Queue.
        """
        nodes = []
        for node in self:
            nodes.append(str(node))
        # Arrow shows on element to be taken via 'pop' next.
        return '«' + ' <-- '.join(nodes) + '»'

    def add(self, data):
        """
        Adds element on the top of the Stack.
        """
        super().add(data, 0)

    def pop(self):
        """
        Removes top element from the Stack and returns it.
        If stack is empty, IndexError is raised.
        """
        if not self.first:
            raise IndexError('Empty Stack')

        return super().pop(0)

    def is_empty(self):
        """
        Returns True if Stack is empty, False otherwise.
        """
        return not bool(self.first)

    def peek(self):
        """
        Returns top element of the Stack without removing it.
        Returns None if Stack is empty
        """
        return self.first
