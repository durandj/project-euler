import functools
import math


@functools.cache
def is_prime(n: int) -> bool:
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n <= 0:
        return False

    midpoint = math.ceil(math.sqrt(n))
    for p in range(3, midpoint + 1, 2):
        if n % p == 0:
            return False

    return True


def solution() -> int:
    results = {}
    for a in range(-999, 1_000):
        for b in range(-1_000, 1_001):
            f = lambda n: (n**2) + (a * n) + b
            n = 0
            while is_prime(f(n)):
                n += 1

            if n > 0:
                results[a * b] = n

    return sorted(results.items(), key=lambda t: t[1], reverse=True)[0][0]


print("is_prime(2) =>", is_prime(2))
print("is_prime(3) =>", is_prime(3))
print("is_prime(11) =>", is_prime(11))
print("is_prime(12) =>", is_prime(12))
print("is_prime(15) =>", is_prime(15))
print("solution() =>", solution())
