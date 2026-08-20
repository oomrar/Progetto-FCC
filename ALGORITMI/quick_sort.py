def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    
    min_arr = []
    ug_arr = []
    mag_arr = []

    for n in arr:
        if n < pivot:
            min_arr.append(n)
        elif n == pivot:
            ug_arr.append(n)
        else:
            mag_arr.append(n)

    sorted_list = quick_sort(min_arr) + ug_arr + quick_sort(mag_arr)

    return sorted_list


