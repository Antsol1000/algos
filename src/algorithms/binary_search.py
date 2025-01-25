def lower_bound(array, x):
    l, r = 0, len(array) - 1
    while l <= r:
        m = (l + r) // 2
        if array[m] < x:
            l = m + 1
        else:
            r = m - 1
    return l


def upper_bound(array, x):
    l, r = 0, len(array) - 1
    while l <= r:
        m = (l + r) // 2
        if array[m] <= x:
            l = m + 1
        else:
            r = m - 1
    return l


if __name__ == '__main__':
    for s in range(1, 100):
        array = [i for i in range(0, s)]
        for i in range(0, s):
            assert lower_bound(array, i) == i
            assert upper_bound(array, i) == i + 1
        for i in range(0, s - 1):
            assert lower_bound(array, i + 0.5) == i + 1
            assert upper_bound(array, i + 0.5) == i + 1
