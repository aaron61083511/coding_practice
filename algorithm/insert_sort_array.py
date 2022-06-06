def insert_sort_array(arr):
    if len(arr) != 0:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
    else:
        print('empty array')
    return arr

# assert insert_sort_array([1, 10, 5, 2, 2,3,8])
# assert insert_sort_array([])
print(insert_sort_array([1, 10, 5, 2, 2, 3, 8]))
