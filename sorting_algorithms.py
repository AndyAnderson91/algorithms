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


def merge_sort(arr):

    def merge(arr1, arr2):
        i, j = 0, 0
        result = []
        while i < len(arr1) or j < len(arr2):
            if i >= len(arr1):
                result += arr2[j:]
                j = len(arr2)
            elif j >= len(arr2):
                result += arr1[i:]
                i = len(arr1)
            elif arr1[i] > arr2[j]:
                result.append(arr2[j])
                j += 1
            else:
                result.append(arr1[i])
                i += 1
        return result

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

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
