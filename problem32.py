import math


def divisors(n: int):
    midpoint = math.ceil(math.sqrt(n))
    for i in range(2, midpoint + 1):
        if n % i == 0:
            yield (i, n // i)


def is_pandigital(product: int) -> bool:
    for x, y in divisors(product):
        s = "".join(sorted(f"{product}{x}{y}"))
        if s == "123456789":
            return True

    return False


def solution() -> int:
    return sum([i for i in reversed(range(1_000, 9_999)) if is_pandigital(i)])


print("solution() =>", solution())
