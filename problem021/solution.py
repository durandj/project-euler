import math


def d(n: int) -> int:
    result = 0
    midpoint = math.ceil(math.sqrt(n))
    for p in range(1, midpoint):
        if n % p == 0:
            result += p + (n // p if p != 1 else 0)

    return result


def is_amicable_number(n: int) -> bool:
    d_of_n = d(n)
    d_of_d_of_n = d(d_of_n)

    if n == d_of_n:
        return False

    return n == d_of_d_of_n


def solution() -> int:
    result = 0
    for i in range(2, 10_000):
        if is_amicable_number(i):
            result += i

    return result


print("d(220) =>", d(220))
print("d(284) =>", d(284))
print("is_amicable_number(220) =>", is_amicable_number(220))
print("solution() =>", solution())
