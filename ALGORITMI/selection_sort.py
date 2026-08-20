def selection_sort(arr):
    for i in range(len(arr)):
        indice_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[indice_min]:
                indice_min = j
        if indice_min != i:
            arr[i], arr[indice_min] = arr[indice_min], arr[i]
    return arr