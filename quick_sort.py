def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller, bigger = [], []
        for element in arr[1:]:
            if element <= pivot:
                smaller.append(element)
            else:
                bigger.append(element)
        return quick_sort(smaller) + [pivot] + quick_sort(bigger)
