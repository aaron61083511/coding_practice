# https://towardsdatascience.com/quicksort-in-python-dbefa7dcf9cc
def quick_sort_array(arr, low, high):
    mid = low + (high - low)//2
    arr[mid], arr[high] = arr[high], arr[mid]
    if low < high:
        pivot_position = partition(arr, low, high)
        # pivot_position = partition2(arr, low, high)
        quick_sort_array(arr, low, pivot_position-1)
        quick_sort_array(arr, pivot_position + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    pointer = low-1

    for i in range(low, high):
        if arr[i] <= pivot:
            pointer += 1
            arr[i], arr[pointer] = arr[pointer], arr[i]
    arr[high], arr[pointer+1] = arr[pointer+1], arr[high]
    return pointer+1

def partition2(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end
    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and arr[high] >= pivot:
            high = high - 1
        # Opposite process of the one above
        while low <= high and arr[low] <= pivot:
            low = low + 1
        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            # The loop continues
        else:
            # We exit out of the loop
            break
    arr[start], arr[high] = arr[high], arr[start]
    return high

data = [1, 10, 5, 2, 3, 8]
quick_sort_array(data, 0, len(data)-1)
print(data)

