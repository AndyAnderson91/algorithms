def bubble_sort(array):
    check_again = True
    i = 0
    while check_again:
        check_again = False
        for j in range(len(array)-i-1):
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
                check_again = True
        i += 1


def selection_sort(array):
    for i in range(len(array) - 1):
        # Current iteration's minimum value and it's index.
        cur_min, cur_min_index = array[i], i

        for j in range(i + 1, len(array)):
            if array[j] < cur_min:
                cur_min, cur_min_index = array[j], j

        array[i], array[cur_min_index] = array[cur_min_index], array[i]


def insertion_sort(array):
    for i in range(1, len(array)):
        k = i
        while k > 0 and array[k] < array[k-1]:
            array[k], array[k-1] = array[k-1], array[k]
            k -= 1


def merge_sort(array):

    def merge(array1, array2):
        i, j = 0, 0
        result = []
        while i < len(array1) or j < len(array2):
            if i >= len(array1):
                result += array2[j:]
                j = len(array2)
            elif j >= len(array2):
                result += array1[i:]
                i = len(array1)
            elif array1[i] > array2[j]:
                result.append(array2[j])
                j += 1
            else:
                result.append(array1[i])
                i += 1
        return result

    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        smaller, bigger = [], []
        for element in array[1:]:
            if element <= pivot:
                smaller.append(element)
            else:
                bigger.append(element)
        return quick_sort(smaller) + [pivot] + quick_sort(bigger)
