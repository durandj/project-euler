import math


def solution(grid_size: int) -> int:
    n = grid_size * 2
    k = n // 2

    return math.comb(n, k)


print("solution(2) =>", solution(2))
print("solution(20) =>", solution(20))
