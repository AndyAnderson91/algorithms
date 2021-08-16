import unittest


def binary_search_iterative(arr, k):
    """
    Iterative version.
    """
    if not arr:
        return None

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            end = mid - 1
        elif arr[mid] < k:
            start = mid + 1

    return None


def binary_search_recursive(arr, k, shift=0):
    """
    Recursive version.
    """
    if not arr:
        return None

    mid = (len(arr) - 1) // 2

    if arr[mid] == k:
        return shift + mid
    elif arr[mid] > k:
        return binary_search_recursive(arr[:mid], k, shift)
    elif arr[mid] < k:
        return binary_search_recursive(arr[mid+1:], k, shift+mid+1)


def create_test_case(function):
    """
    Iterative and recursive versions have same output,
    So it's reasonable to use same tests on both.
    """
    class BinarySearchTestCase(unittest.TestCase):
        """
        Base binary search testing class.
        Existent elements - required elements that are in list.
        Nonexistent elements - required elements that aren't in list.
        """
        def test_empty_list(self):
            """
            Returns None if list is empty.
            """
            arr = []
            element = 5

            self.assertIsNone(function(arr, element))

        def test_single_element_list(self):
            """
            Returns 0 for existent element.
            Returns None for nonexistent element.
            """
            arr = [3]
            existent_element = 3
            nonexistent_elements = [2, 5]

            self.assertEqual(function(arr, existent_element), 0)

            for element in nonexistent_elements:
                self.assertIsNone(function(arr, element))

        def test_even_len_list(self):
            """
            Returns index (0-based) for existent element.
            Returns None for nonexistent element.
            """
            arr = [-12, -7, 0, 1, 5, 8, 14, 25]
            existent_elements = [-12, 0, 1, 14, 25]
            nonexistent_elements = [-15, -1, 9, 26]

            for element in existent_elements:
                function_index = function(arr, element)
                correct_index = arr.index(element)
                self.assertEqual(function_index, correct_index)

            for element in nonexistent_elements:
                self.assertIsNone(function(arr, element))

        def test_odd_len_list(self):
            """
            Returns index (0-based) for existent element.
            Returns None for nonexistent element.
            """
            arr = [-55, -1, 0, 1, 13, 47, 48]
            existent_elements = [-55, -1, 0, 1, 48]
            nonexistent_elements = [-60, -2, 3, 50]

            for element in existent_elements:
                function_index = function(arr, element)
                correct_index = arr.index(element)
                self.assertEqual(function_index, correct_index)

            for element in nonexistent_elements:
                self.assertIsNone(function(arr, element))

    return BinarySearchTestCase


class IterativeTestCase(create_test_case(binary_search_iterative)):
    """
    Runs all BinarySearchTestCase tests on binary_search_iterative function.
    """
    pass


class RecursiveTestCase(create_test_case(binary_search_recursive)):
    """
    Runs all BinarySearchTestCase tests on binary_search_recursive function.
    """
    pass


if __name__ == '__main__':
    unittest.main()
