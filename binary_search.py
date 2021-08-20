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
