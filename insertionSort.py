def insertion_sort(arr, key):
    n = len(arr)
    for i in range(1, n):
        pivot = arr[i]
        j = i - 1
        while j >= 0 and pivot[key] < arr[j][key]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pivot
    return arr