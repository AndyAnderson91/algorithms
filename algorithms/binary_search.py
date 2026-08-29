"""
Binary search algorithm implementation (iterative and recursive versions).
Return index of searched value in a sorted array.
Return None if value is not present.
"""


def binary_search_iterative(array, value):
    if not array:
        return None

    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end)//2
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            end = mid - 1
        else:
            start = mid + 1

    return None


def binary_search_recursive(array, value, start=0, end=None):
    if not array:
        return None

    if end is None:
        end = len(array) - 1

    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == value:
        return mid
    elif array[mid] > value:
        return binary_search_recursive(array, value, start, mid - 1)
    else:
        return binary_search_recursive(array, value, mid + 1, end)
