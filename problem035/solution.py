import functools
import math


@functools.cache
def is_prime(n: int) -> bool:
    midpoint = math.ceil(math.sqrt(n))
    for i in range(2, midpoint + 1):
        if n % i == 0:
            return False

    return True


def rotate_number(n: int) -> int:
    length = math.floor(math.log10(n))
    m = n % 10

    return (n // 10) + (m * 10**length)


def solution() -> int:
    result = 1  # 2 is the first, but we're skipping it
    for n in range(3, 1_000_000, 2):
        if not is_prime(n):
            continue

        length = math.floor(math.log10(n))
        for _ in range(length):
            n = rotate_number(n)

            if not is_prime(n):
                break
        else:
            result += 1

    return result


print(solution())
