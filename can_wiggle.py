def wiggle_sort(arr):
    first = arr.pop((arr.index(min(arr))))

    i = 0
    while i < len(arr)-2:
        arr[i: i+3] = sorted(arr[i: i+3])
        arr[i], arr[i+1], arr[i+2] = arr[i+2], arr[i], arr[i+1]
        i += 2
    if len(arr) % 2 == 1:
        arr[-3], arr[-2], arr[-1] = sorted(arr[-3:])
        arr[-3], arr[-2], arr[-1] = arr[-1], arr[-3], arr[-2]

    else:
        arr[-3], arr[-2], arr[-1] = sorted(arr[-3:])
        arr[-3], arr[-2], arr[-1] = arr[-3], arr[-1], arr[-2]
    return [first] + arr
