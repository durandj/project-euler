import functools
import itertools
import math


def get_proper_divisors(n: int) -> list[int]:
    divisors = {1}
    midpoint = math.ceil(math.sqrt(n))
    for p in range(2, midpoint + 1):
        if n % p == 0:
            divisors.add(p)
            divisors.add(n // p)

    return list(divisors)


@functools.cache
def is_abundant_number(n: int) -> bool:
    divisors = get_proper_divisors(n)
    sum_of_divisors = sum(divisors)

    return sum_of_divisors > n


def solution() -> int:
    abundant_numbers = {n for n in range(12, 28_124) if is_abundant_number(n)}

    number_pairs = itertools.combinations_with_replacement(abundant_numbers, 2)
    abundant_sum_numbers = {n + m for n, m in number_pairs if n + m <= 28_124}

    result = 0
    for n in range(1, 28_123):
        if n not in abundant_sum_numbers:
            result += n

    return result


print("get_proper_divisors(28) =>", get_proper_divisors(28))
print("is_abundant_number(12) =>", is_abundant_number(12))
print("solution() =>", solution())
