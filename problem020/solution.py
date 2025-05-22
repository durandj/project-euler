import math


def solution(n: int) -> int:
    factorial = math.factorial(n)

    result = 0
    while factorial > 0:
        result += factorial % 10
        factorial = factorial // 10

    return result


print("solution(10) =>", solution(10))
print("solution(100) =>", solution(100))
