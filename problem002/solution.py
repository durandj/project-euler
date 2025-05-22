def fibonacci(seed1: int, seed2: int):
    a = seed1
    b = seed2

    yield a
    yield b

    while True:
        a, b = b, a + b

        yield b


def solution() -> int:
    result = 0
    for value in fibonacci(1, 2):
        if value > 4_000_000:
            break

        if value % 2 == 0:
            result += value

    return result


print(solution())
