import unittest
from algorithms.linked_lists import SinglyLinkedList, DoublyLinkedList


def fill_linked_list(linked_list, elements):
    """
    Fills linked list with given elements in reversed order.
    After inserting ('a', 'b', 'c', 'd'), list will be:
    'a' --> 'b' -- > 'c' --> 'd'.
    """
    for i in range(len(elements) - 1, -1, -1):
        linked_list.insert(elements[i], 0)


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

        def test_empty_list_repr(self):
            """
            Checks if empty list representation is correct.
            """
            self.assertEqual(self.linked_list.__repr__(), '«»')

        def test_iter(self):
            """
            Checks if __iter__ method implemented correctly.
            """
            fill_linked_list(self.linked_list, self.elements)
            for j, node in enumerate(self.linked_list):
                self.assertEqual(node.data, self.elements[j])

        def test_contains(self):
            """
            Checks if __contains__ method implemented correctly.
            """
            fill_linked_list(self.linked_list, self.elements)
            for data in self.elements:
                self.assertTrue(data in self.linked_list)

        def test_len(self):
            """
            Checks if __len__ method implemented correctly.
            """
            fill_linked_list(self.linked_list, self.elements)
            self.assertEqual(len(self.linked_list), 4)

        def test_getitem_by_index_in_range(self):
            """
            Checks if __getitem__ method returns element by required existing index.
            """
            fill_linked_list(self.linked_list, self.elements)
            for i in range(self.length):
                self.assertEqual(self.linked_list[i].data, self.elements[i])

        def test_getitem_by_index_out_of_range(self):
            """
            Checks if __getitem__ method raises IndexError if required index is out of range.
            """
            fill_linked_list(self.linked_list, self.elements)
            for i in self.out_of_range_indexes:
                self.assertRaises(IndexError, self.linked_list.__getitem__, i)

        def test_setitem_by_index_in_range(self):
            """
            Checks if __setitem__ method overwrites element by required existing index.
            """
            fill_linked_list(self.linked_list, self.elements)
            for i in range(self.length):
                self.linked_list[i] = 'New data'
                self.assertEqual(self.linked_list[i].data, 'New data')

        def test_setitem_by_index_out_of_range(self):
            """
            Checks if __setitem__ method raises IndexError if required index is out of range.
            """
            fill_linked_list(self.linked_list, self.elements)
            for i in self.out_of_range_indexes:
                self.assertRaises(IndexError, self.linked_list.__setitem__, i, 'New data')

        def test_add_to_empty_list(self):
            """
            Checks if list.first link points to element added in empty list.
            """
            self.linked_list.add('Hello')
            self.assertEqual(self.linked_list.first.data, 'Hello')

        def test_insert_in_correct_order(self):
            """
            Checks if elements are inserted in correct order.
            """
            fill_linked_list(self.linked_list, self.elements)
            node, i = self.linked_list.first, 0
            while node:
                self.assertEqual(node.data, self.elements[i])
                node = node.next
                i += 1

        def test_insert_by_positive_index_in_range(self):
            """
            Checks if element is inserted before required existing positive index.
            """
            fill_linked_list(self.linked_list, self.elements)
            for pos_index in range(1, self.length):
                self.linked_list.insert('e', pos_index)
                self.assertEqual(self.linked_list.get(pos_index-1).next.data, 'e')
                self.linked_list.pop(pos_index)

        def test_insert_by_positive_index_out_of_range(self):
            """
            Checks if element is inserted in the end of the list if required positive index doesn't exist.
            """
            fill_linked_list(self.linked_list, self.elements)
            for pos_index in range(self.length, self.length + 5):
                self.linked_list.insert('e', pos_index)
                self.assertEqual(self.linked_list.get(self.length - 1).next.data, 'e')
                self.linked_list.pop(self.length)

        def test_insert_by_zero_index(self):
            """
            Checks if element is added to the front of the list.
            """
            fill_linked_list(self.linked_list, self.elements)
            self.linked_list.insert('e', 0)
            self.assertEqual(self.linked_list.first.data, 'e')

        def test_insert_by_negative_index_in_range(self):
            """
            Checks if element is added before required existing negative index.
            """
            fill_linked_list(self.linked_list, self.elements)
            for neg_index in range(-self.length, 0):
                self.linked_list.insert('e', neg_index)
                self.assertEqual(self.linked_list.get(neg_index - 1).data, 'e')
                self.linked_list.pop(neg_index - 1)

        def test_insert_by_negative_index_out_of_range(self):
            """
            Checks if element is added in the front of the list.
            """
            fill_linked_list(self.linked_list, self.elements)
            for neg_index in range(-self.length - 5, -self.length):
                self.linked_list.insert('e', neg_index)
                self.assertEqual(self.linked_list.first.data, 'e')
                self.linked_list.pop(0)

        def test_get_by_index_in_range(self):
            """
            Checks if get method returns element by existing index.
            """
            fill_linked_list(self.linked_list, self.elements)
            for j in range(-self.length, self.length):
                self.assertEqual(self.linked_list.get(j).data, self.elements[j])

        def test_get_by_index_out_of_range(self):
            """
            Checks if get method returns None if required index is out of range.
            """
            fill_linked_list(self.linked_list, self.elements)
            for i in self.out_of_range_indexes:
                self.assertIsNone(self.linked_list.get(i))

        def test_pop_without_index(self):
            """
            Checks default pop method behavior.
            By default, first element is removed from list and returned.
            """
            fill_linked_list(self.linked_list, self.elements)
            for j in range(self.length):
                popped = self.linked_list.pop().data
                self.assertEqual(popped, self.elements[j])

        def test_pop_by_index_in_range(self):
            """
            Checks if element is removed from list and returned by required existing index.
            """
            fill_linked_list(self.linked_list, self.elements)
            for j in range(-self.length, self.length):
                popped = self.linked_list.pop(j).data
                self.assertEqual(popped, self.elements[j])
                if j >= 0:
                    self.linked_list.insert(popped, j)
                elif j == -1:
                    self.linked_list.insert(popped, self.length - 1)
                else:
                    self.linked_list.insert(popped, j + 1)

        def test_pop_by_index_out_of_range(self):
            """
            Checks if IndexError is raised if pop method recieves index out of range.
            """
            fill_linked_list(self.linked_list, self.elements)
            for i in self.out_of_range_indexes:
                self.assertRaises(IndexError, self.linked_list.pop, i)

    return SinglyAndDoublyLinkedListTestCase


class SinglyLinkedListTestCase(create_singly_and_doubly_linked_lists_test_cases(SinglyLinkedList)):

    def test_filled_list_repr(self):
        """
        Checks if filled list represented correctly.
        """
        fill_linked_list(self.linked_list, ('a', (1, 2), 5, 'd'))
        self.assertEqual(self.linked_list.__repr__(), "«'a' --> (1, 2) --> 5 --> 'd'»")

    def test_add_to_filled_list(self):
        """
        Checks if list.first link points to element added to filled list.
        """
        fill_linked_list(self.linked_list, self.elements)
        self.linked_list.add('Hello')
        updated_elements = ('Hello',) + self.elements
        for i, node in enumerate(self.linked_list):
            self.assertEqual(node.data, updated_elements[i])


class DoublyLinkedListTestCase(create_singly_and_doubly_linked_lists_test_cases(DoublyLinkedList)):

    def test_filled_list_repr(self):
        """
        Checks if filled list represented correctly.
        """
        fill_linked_list(self.linked_list, ('a', (1, 2), 5, 'd'))
        self.assertEqual(self.linked_list.__repr__(), "«'a' <--> (1, 2) <--> 5 <--> 'd'»")

    def test_add_to_filled_list(self):
        """
        Checks if list.last link points to element added to filled list.
        """
        fill_linked_list(self.linked_list, self.elements)
        self.linked_list.add('Hello')
        updated_elements = self.elements + ('Hello',)
        for i, node in enumerate(self.linked_list):
            self.assertEqual(node.data, updated_elements[i])


if __name__ == '__main__':
    unittest.main()