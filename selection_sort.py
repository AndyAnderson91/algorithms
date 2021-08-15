def selection_sort(arr):
    for i in range(len(arr) - 1):
        # Current iteration's min value and it's index.
        cur_min, cur_min_index = arr[i], i

        for j in range(i + 1, len(arr)):
            if arr[j] < cur_min:
                cur_min, cur_min_index = arr[j], j

        arr[i], arr[cur_min_index] = arr[cur_min_index], arr[i]
