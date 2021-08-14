def binary_search_rec(arr, k, start=0, end=None):
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

    return binary_search_rec(arr, k, start, end)
