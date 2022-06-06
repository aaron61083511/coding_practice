def selection_sort_array(arr):
    n = len(arr)
    for start in range(n):
        min_index = start
        for pointer in range(start+1, n):
            if arr[pointer] < arr[min_index]:
                min_index = pointer
        arr[start], arr[min_index] = arr[min_index], arr[start]
    return arr

print(selection_sort_array([1, 10, 5, 2, 2, 3, 8]))
