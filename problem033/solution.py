import functools
import math


@functools.cache
def factorize(n: int) -> set[int]:
    factors = set()
    midpoint = math.ceil(math.sqrt(n))
    for i in range(1, midpoint + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)

    return factors


def find_greatest_common_factor(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return 1

    x_factors = factorize(x)
    y_factors = factorize(y)

    common_factors = x_factors.intersection(y_factors)

    return sorted(common_factors, reverse=True)[0]


def simplify_fraction(n: int, d: int) -> tuple[int, int]:
    gcf = find_greatest_common_factor(n, d)

    return n // gcf, d // gcf


def solution() -> int:
    result_n = 1
    result_d = 1

    for n in range(11, 100):
        for d in range(11, 100):
            if n > d:
                continue

            # Exclude "trivial" cases
            if n == d:
                continue
            elif n % 10 == 0 and d % 10 == 0:
                continue

            n_digit_1, n_digit_2 = n // 10, n % 10
            d_digit_1, d_digit_2 = d // 10, d % 10

            if n_digit_1 == d_digit_1:
                expected_n, expected_d = n % 10, d % 10
            elif n_digit_1 == d_digit_2:
                expected_n, expected_d = n % 10, d // 10
            elif n_digit_2 == d_digit_1:
                expected_n, expected_d = n // 10, d % 10
            elif n_digit_2 == d_digit_2:
                expected_n, expected_d = n // 10, d // 10
            else:
                continue

            expected_n, expected_d = simplify_fraction(expected_n, expected_d)
            actual_n, actual_d = simplify_fraction(n, d)

            # TODO: it's not that the simplified expression matches but that the faction is equivalent to dropping digits
            if expected_n / actual_n == expected_d / actual_d:
                result_n *= actual_n
                result_d *= actual_d

                result_n, result_d = simplify_fraction(result_n, result_d)

    return result_d


print(solution())
