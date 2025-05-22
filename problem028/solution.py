import math


def solution(size: int) -> int:
    result = 0

    n = 1
    spiral_size = 3
    while n <= size * size:
        result += n

        if n == spiral_size * spiral_size:
            spiral_size += 2

        n += spiral_size - 1

    return result


print("solution(5) =>", solution(5))
print("solution(1_001) =>", solution(1_001))
