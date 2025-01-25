import random
import time


def fast_power(n, p):
    if p == 0:
        return 1
    if p == 1:
        return n
    if p % 2 == 0:
        return fast_power(n * n, p // 2)
    else:
        return n * fast_power(n * n, (p - 1) // 2)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    old_r, r = (a, b)
    old_s, s = (1, 0)
    old_t, t = (0, 1)

    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

def miller_rabin(number, k=5):
    if number == 2 or number == 3:
        return True
    if number % 2 == 0:
        return False

    def check(a, s, d, n):
        x = fast_power(a, d) % n
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    s = 0
    d = number - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = 2 + int(2 * (number - 4) * random.random())
        if not check(a, s, d, number):
            return False
    return True



if __name__ == '__main__':
    a = 1024 * 7 * 19 * 3 ** 12
    b = 7 * 19 * 5 ** 10 * 3
    gcd1 = gcd(a, b)
    print(f"gcd({a}, {b}) = {gcd1}")
    assert gcd1 == 7 * 19 * 3
    gcd2, x, y = extended_gcd(a, b)
    assert gcd2 == 7 * 19 * 3
    print(f"extended_gcd({a}, {b}) = {gcd2} = {x} * {a} + {y} * {b}")
    assert gcd2 == x * a + y * b

    print("*" * 50)

    for i in range(1, 10):
        start_time = time.time()
        power = fast_power(2, 10 ** i)
        print(f"power of 2^{10 ** i} calculated in {time.time() - start_time} seconds.")
        assert power == 2 ** (10 ** i)
