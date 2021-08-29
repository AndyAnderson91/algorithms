import unittest
from algorithms.linked_lists import SinglyLinkedList, DoublyLinkedList


def create_singly_and_doubly_linked_lists_test_cases(linked_list_class):
    """
    SinglyLinkedList and DoublyLinkedList have slightly different implementation,
    but same output for most of the methods.
    It's reasonable to have common test package.
    """

    class SinglyAndDoublyLinkedListTestCase(unittest.TestCase):
        """
        Common TestCase package.
        """
        def setUp(self):
            self.linked_list = linked_list_class()
            self.elements = ('a', 'b', 'c', 'd')
            self.length = len(self.elements)
            self.out_of_range_indexes = [i for i in range(-self.length - 5, self.length + 6) if abs(i) > self.length]

        def test_create_linked_list_with_not_iterable_argument(self):
            """
            Checks if TypeError is raised if argument is not iterable.
            """
            self.assertRaises(TypeError, linked_list_class, 12345)

        def test_create_linked_list_with_iterable_argument(self):
            """
            Checks if __init__ method implemented correctly.
            """
            self.assertEqual(len(linked_list_class([1, 2, 3, 4, 5])), 5)

        def test_empty_list_repr(self):
            """
            Checks if empty list representation is correct.
            """
            self.assertEqual(self.linked_list.__repr__(), '«»')

        def test_iter(self):
            """
            Checks if __iter__ method implemented correctly.
            """
            self.linked_list = linked_list_class(self.elements)
            for j, node_data in enumerate(self.linked_list):
                self.assertEqual(node_data, self.elements[j])

        def test_contains(self):
            """
            Checks if __contains__ method implemented correctly.
            """
            self.linked_list = linked_list_class(self.elements)
            for data in self.elements:
                self.assertTrue(data in self.linked_list)

        def test_len(self):
            """
            Checks if __len__ method implemented correctly.
            """
            self.linked_list = linked_list_class(self.elements)
            self.assertEqual(len(self.linked_list), 4)

        def test_getitem_by_index_in_range(self):
            """
            Checks if __getitem__ method returns element by required existing index.
            """
            self.linked_list = linked_list_class(self.elements)
            for i in range(self.length):
                self.assertEqual(self.linked_list[i], self.elements[i])

        def test_getitem_by_index_out_of_range(self):
            """
            Checks if __getitem__ method raises IndexError if required index is out of range.
            """
            self.linked_list = linked_list_class(self.elements)
            for i in self.out_of_range_indexes:
                self.assertRaises(IndexError, self.linked_list.__getitem__, i)

        def test_setitem_by_index_in_range(self):
            """
            Checks if __setitem__ method overwrites element by required existing index.
            """
            self.linked_list = linked_list_class(self.elements)
            for i in range(self.length):
                self.linked_list[i] = 'New data'
                self.assertEqual(self.linked_list[i], 'New data')

        def test_setitem_by_index_out_of_range(self):
            """
            Checks if __setitem__ method raises IndexError if required index is out of range.
            """
            self.linked_list = linked_list_class(self.elements)
            for i in self.out_of_range_indexes:
                self.assertRaises(IndexError, self.linked_list.__setitem__, i, 'New data')

        def test_add_to_empty_list(self):
            """
            Checks if list.first link points to element added in empty list.
            """
            self.linked_list.add('Hello')
            self.assertEqual(self.linked_list.first.value, 'Hello')

        def test_insert_in_correct_order(self):
            """
            Checks if elements are inserted in correct order.
            """
            self.linked_list = linked_list_class(self.elements)
            node, i = self.linked_list.first, 0
            while node:
                self.assertEqual(node.value, self.elements[i])
                node = node.next
                i += 1

        def test_insert_by_positive_index_in_range(self):
            """
            Checks if element is inserted before required existing positive index.
            """
            self.linked_list = linked_list_class(self.elements)
            for pos_index in range(1, self.length):
                self.linked_list.insert('e', pos_index)
                self.assertEqual(self.linked_list._get_node(pos_index-1).next.value, 'e')
                self.linked_list.pop(pos_index)

        def test_insert_by_positive_index_out_of_range(self):
            """
            Checks if element is inserted in the end of the list if required positive index doesn't exist.
            """
            self.linked_list = linked_list_class(self.elements)
            for pos_index in range(self.length, self.length + 5):
                self.linked_list.insert('e', pos_index)
                self.assertEqual(self.linked_list._get_node(self.length - 1).next.value, 'e')
                self.linked_list.pop(self.length)

        def test_insert_by_zero_index(self):
            """
            Checks if element is added to the front of the list.
            """
            self.linked_list = linked_list_class(self.elements)
            self.linked_list.insert('e', 0)
            self.assertEqual(self.linked_list.first.value, 'e')

        def test_insert_by_negative_index_in_range(self):
            """
            Checks if element is added before required existing negative index.
            """
            self.linked_list = linked_list_class(self.elements)
            for neg_index in range(-self.length, 0):
                self.linked_list.insert('e', neg_index)
                self.assertEqual(self.linked_list[neg_index - 1], 'e')
                self.linked_list.pop(neg_index - 1)

        def test_insert_by_negative_index_out_of_range(self):
            """
            Checks if element is added in the front of the list.
            """
            self.linked_list = linked_list_class(self.elements)
            for neg_index in range(-self.length - 5, -self.length):
                self.linked_list.insert('e', neg_index)
                self.assertEqual(self.linked_list.first.value, 'e')
                self.linked_list.pop(0)

        def test_pop_without_index(self):
            """
            Checks default pop method behavior.
            By default, first element is removed from list and returned.
            """
            self.linked_list = linked_list_class(self.elements)
            for j in range(self.length):
                popped = self.linked_list.pop()
                self.assertEqual(popped, self.elements[j])

        def test_pop_by_index_in_range(self):
            """
            Checks if element is removed from list and returned by required existing index.
            """
            self.linked_list = linked_list_class(self.elements)
            for j in range(-self.length, self.length):
                popped = self.linked_list.pop(j)
                self.assertEqual(popped, self.elements[j])
                if j >= 0:
                    self.linked_list.insert(popped, j)
                elif j == -1:
                    self.linked_list.insert(popped, self.length - 1)
                else:
                    self.linked_list.insert(popped, j + 1)

        def test_pop_by_index_out_of_range(self):
            """
            Checks if IndexError is raised if pop method receives index out of range.
            """
            self.linked_list = linked_list_class(self.elements)
            for i in self.out_of_range_indexes:
                self.assertRaises(IndexError, self.linked_list.pop, i)

    return SinglyAndDoublyLinkedListTestCase


class SinglyLinkedListTestCase(create_singly_and_doubly_linked_lists_test_cases(SinglyLinkedList)):

    def test_filled_list_repr(self):
        """
        Checks if filled list represented correctly.
        """
        self.linked_list = SinglyLinkedList(('a', (1, 2), 5, 'd'))
        self.assertEqual(self.linked_list.__repr__(), "«'d' --> 5 --> (1, 2) --> 'a'»")

    def test_add_to_filled_list(self):
        self.linked_list = SinglyLinkedList(self.elements)
        self.linked_list.add('Hello')
        self.assertEqual(self.linked_list.first.value, 'Hello')


class DoublyLinkedListTestCase(create_singly_and_doubly_linked_lists_test_cases(DoublyLinkedList)):

    def test_filled_list_repr(self):
        """
        Checks if filled list represented correctly.
        """
        self.linked_list = DoublyLinkedList(('a', (1, 2), 5, 'd'))
        self.assertEqual(self.linked_list.__repr__(), "«'a' <--> (1, 2) <--> 5 <--> 'd'»")

    def test_add_to_filled_list(self):
        """
        Checks if list.last link points to element added to filled list.
        """
        self.linked_list = DoublyLinkedList(self.elements)
        self.linked_list.add('Hello')
        updated_elements = self.elements + ('Hello',)
        for i, node_data in enumerate(self.linked_list):
            self.assertEqual(node_data, updated_elements[i])


if __name__ == '__main__':
    unittest.main()
