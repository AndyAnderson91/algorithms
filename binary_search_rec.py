def binary_search_recursive(arr, k, start=0, end=None):
    """
    Recursive version.
    """
    if not arr:
        return None

    # First function calling requires arr and k arguments.
    # Start and end arguments are 0 and len(arr) by default.
    end = end or len(arr)

    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        end = mid - 1
    elif arr[mid] < k:
        start = mid + 1

    return binary_search_recursive(arr, k, start, end)
