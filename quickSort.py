def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    # Partition the array into elements less than and greater than the pivot
    left = [ x for x in arr if x[key] < pivot[key]]
    middle = [x for x in arr if x[key] == pivot[key]]
    right = [x for x in arr if x[key] > pivot[key]]
    # Recursively sort the sub-arrays and combine them with the pivot
    sub_array = quick_sort(left, key) + middle + quick_sort(right, key)
    return sub_array
