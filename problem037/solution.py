import functools
import math


def truncate_left(value: int) -> int:
    digits = math.floor(math.log10(value))

    return value % 10 ** digits


def truncate_right(value: int) -> int:
    return value // 10


@functools.cache
def is_prime(value: int) -> bool:
    if value <= 1:
        return False
    elif value == 2:
        return True
    elif value % 2 == 0:
        return False

    midpoint = math.ceil(math.sqrt(value)) + 1
    for f in range(3, midpoint):
        if value % f == 0:
            return False

    return True

def is_truncatable_prime(value: int) -> bool:
    if not is_prime(value):
        return False

    left = value
    while left > 0:
        left = truncate_left(left)
        if left != 0 and not is_prime(left):
            return False

    right = value
    while right > 0:
        right = truncate_right(right)
        if right != 0 and not is_prime(right):
            return False

    return True


truncatable_primes = []
i = 11
while len(truncatable_primes) < 11:
    if is_truncatable_prime(i):
        truncatable_primes.append(i)

    i += 2

print(sum(truncatable_primes))
