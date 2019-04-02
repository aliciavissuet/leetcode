def perms(N):
    possible = []
    if len(N) <= 1:
        return [N]
    last = N.pop()
    prev = perms(N)
    newList = list(map(lambda x: add_last(x, last), prev))
    return newList


def add_last(l, el):
    # el = str(el)
    print(l, el)
    result = []
    for i in range(len(l)):
        result.append(l[:i]+[el]+l[i:])
    return list(map(lambda x: int(('').join(x)), result))


def is_power(N):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2
    return True


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        if N == 1:
            return True
        str_n = list(str(N))
        n_arr = list(map(lambda x: int(x), str_n))
        permuts = perms(n_arr)
        for arr in permuts:
            if is_power(arr):
                return True
        return False
