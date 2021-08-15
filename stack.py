class Stack:
    """
    Implemented as a particular case of a Singly Linked List.
    """
    class Node:
        """
        Stack element.
        Contains data and address of the next element.
        """
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self, head=None):
        # Contains address of the top element.
        self.head = head

    def is_empty(self):
        """
        Returns True if Stack is empty, False otherwise.
        """
        return not bool(self.head)

    def push(self, data):
        """
        Adds element on the top of the Stack.
        """
        new_node = self.Node(data, self.head)
        self.head = new_node

    def pop(self):
        """
        Removes top element from the Stack and returns it.
        If stack is empty, IndexError is raised.
        """
        if not self.head:
            raise IndexError('Empty Stack')

        node_to_pop = self.head
        self.head = node_to_pop.next
        return node_to_pop

    def peek(self):
        """
        Returns top element of the Stack without removing it.
        Returns None if Queue is empty
        """
        return self.head
