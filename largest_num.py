def largest_num(arr):
    #     strategy: sort each number by their first digit, then by their length (shorter numbers win), then by the number value
    #first: convert each to string
    # new_arr = arr.map(lambda x: str(x))
    # new_arr = arr.sort()

    string_arr = map(lambda x: str(x), special_quick_sort(arr))
    print(''.join(string_arr))


def special_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    mid_i = arr.pop()
    mid_first_digit = int(str(mid_i)[0])
    left = []
    right = []
    for el in arr:
        el_s = str(el)

        first_digit = int(el_s[0])

        if first_digit > mid_first_digit:
            left.append(el)
        elif first_digit < mid_first_digit:
            right.append(el)
        else:
            if len(el_s) < len(str(mid_i)):
                left.append(el)
            elif len(el_s) > len(str(mid_i)):
                right.append(el)
            elif mid_i > el:
                right.append(el)
            else:
                left.append(el)
    left = special_quick_sort(left)
    right = special_quick_sort(right)
    return left + [mid_i] + right
