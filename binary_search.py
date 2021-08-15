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
