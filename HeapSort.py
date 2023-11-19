def heapify(arr, n, i, key):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if left child exists and is greater than the root
    if left_child < n and arr[i][key] < arr[left_child][key]:
        largest = left_child

    # Check if right child exists and is greater than the largest so far
    if right_child < n and arr[largest][key] < arr[right_child][key]:
        largest = right_child

    # Swap the root if needed
    if largest != i:
        arr[i][key], arr[largest][key] = arr[largest][key], arr[i][key]

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest, key)


def heap_sort(arr, key):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i][key], arr[0][key] = arr[0][key], arr[i][key]  # Swap
        heapify(arr, i, 0, key)

    return arr