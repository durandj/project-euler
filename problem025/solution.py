import math


def fibonacci_sequence(a: int, b: int):
    yield a
    yield b

    while True:
        a, b = b, a + b

        yield b


def solution() -> int:
    for iteration, value in enumerate(fibonacci_sequence(1, 1)):
        digits = math.ceil(math.log10(value))
        if digits >= 1_000:
            return iteration + 1

    return -1


print("solution() =>", solution())
