# iterative
def bs_i(array, target):
    low = 0
    high = len(array) - 1
    if array is None or len(array) == 0:
        return -1
    while low + 1 < high:
        mid = low + (high-low)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid
        else:
            high = mid
    if array[low] == target:
        return low
    if array[high] == target:
        return high
    return -1

# recursive
def bs_r(array, target):
    low = 0
    high = len(array)-1
    if array is None or len(array) == 0:
        return -1
    if low + 1 < high:
        mid = (high - low)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return mid + bs_r(array[mid:], target)
        else:
            return bs_r(array[:mid], target)
    if array[low] == target:
        return low
    if array[high] == target:
        return high
    return -1



array = [3, 4, 5, 6, 7, 8, 9]
x = 5

result_i = bs_i(array, x)
result_r = bs_r(array, x)
print(result_i)
print(result_r)



