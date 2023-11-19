def selection_sort(arr, key):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted portion of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j][key] < arr[min_index][key]:
                min_index = j
        # Swap the minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]