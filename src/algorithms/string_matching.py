NUMBER_OF_CHARS = 256


def naive(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        j = 0
        while j < len(pattern):
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == len(pattern):
            return i
    return -1


def rabin_karp(text, pattern, q=239):
    n, m = len(text), len(pattern)
    h = pow(NUMBER_OF_CHARS, m - 1) % q
    p, t = 0, 0
    for i in range(m):  # preprocessing
        p = (NUMBER_OF_CHARS * p + ord(pattern[i])) % q
        t = (NUMBER_OF_CHARS * t + ord(text[i])) % q
    for s in range(n - m + 1):
        if p == t:
            match = True
            for i in range(m):
                if pattern[i] != text[s + i]:
                    match = False
                    break
            if match:
                return s
        if s < n - m:
            t = (t - h * ord(text[s])) % q  # remove letter s
            t = (t * NUMBER_OF_CHARS + ord(text[s + m])) % q  # add letter s+m
            t = (t + q) % q
    return -1


def knuth_morris_pratt(text, pattern):
    n, m = len(text), len(pattern)

    def compute_prefix_function():
        m = len(pattern)
        lps = [0] * m
        length, i = 0, 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_prefix_function()
    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def finite_automata(text, pattern):
    n, m = len(text), len(pattern)

    def get_next_state(state, x):
        if state < m and x == ord(pattern[state]):
            return state + 1
        for ns in range(state, 0, -1):
            if ord(pattern[ns - 1]) == x:
                i = 0
                while i < ns - 1 and pattern[i] == pattern[state - ns + 1 + i]:
                    i += 1
                if i == ns - 1:
                    return ns
        return 0

    tf = [[0 for _ in range(NUMBER_OF_CHARS + 1)] for _ in range(m + 1)]
    for state in range(m + 1):
        for x in range(NUMBER_OF_CHARS + 1):
            z = get_next_state(state, x)
            tf[state][x] = z
    state = 0
    for i in range(n):
        state = tf[state][ord(text[i])]
        if state == m:
            return i - m + 1
    return -1


if __name__ == '__main__':
    text = "AABAABBCAABDAABBCABBAAABA"
    pattern = "ABBA"
    assert naive(text, pattern) == 17
    assert rabin_karp(text, pattern) == 17
    assert knuth_morris_pratt(text, pattern) == 17
    assert finite_automata(text, pattern) == 17
