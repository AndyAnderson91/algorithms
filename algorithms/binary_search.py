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


def binary_search_recursive(array, value, shift=0):
    # shift is an index of current array's starting element in initial array.
    # for example, for initial array [1, 4, 5, 8, 10] and searched value 8,
    # after first slicing recursive function will receive [8, 10] array and shift=3.
    # This allows to pass only 1 additional argument (shift) instead of 2 (start, end).
    if not array:
        return None

    mid = (len(array) - 1) // 2

    if array[mid] == value:
        return shift + mid
    elif array[mid] > value:
        return binary_search_recursive(array[:mid], value, shift)
    else:
        return binary_search_recursive(array[mid+1:], value, shift+mid+1)
