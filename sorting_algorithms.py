def selection_sort(arr):
    for i in range(len(arr) - 1):
        # Current iteration's minimum value and it's index.
        cur_min, cur_min_index = arr[i], i

        for j in range(i + 1, len(arr)):
            if arr[j] < cur_min:
                cur_min, cur_min_index = arr[j], j

        arr[i], arr[cur_min_index] = arr[cur_min_index], arr[i]


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
