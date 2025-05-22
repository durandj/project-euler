import math


def triangle_number_generator():
    running_sum = 0
    i = 1

    while True:
        running_sum += i
        yield running_sum

        i += 1


def factorize(value: int) -> list[int]:
    midpoint = math.ceil(math.sqrt(value))

    factors = set()
    for p in range(1, midpoint):
        if value % p == 0:
            factors.add(p)
            factors.add(value // p)

    return list(factors)


def solution(divisor_count: int) -> int:
    for triangle_number in triangle_number_generator():
        factors = factorize(triangle_number)

        if len(factors) > divisor_count:
            return triangle_number

    return -1


print("5 =>", solution(5))
print("500 =>", solution(500))
