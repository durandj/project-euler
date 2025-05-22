import math


def is_matching_number(n: int) -> bool:
    t = n

    result = 0
    while t > 0:
        p = t % 10
        result += math.factorial(p)

        t //= 10

    return result == n


def solution() -> int:
    return sum([n for n in range(3, 100_000) if is_matching_number(n)])


print(solution())
