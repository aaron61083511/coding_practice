def bubble_sort_array(arr):
    n = len(arr)
    if n != 0:
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    else:
        print('empty array')
    return arr

print(bubble_sort_array([1, 10, 5, 2, 2, 3, 8]))
