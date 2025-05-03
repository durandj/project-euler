def solution(exponent: int) -> int:
    value = 1 << exponent
    str_value = str(value)

    return sum([int(i) for i in str_value])


print("solution(15) =>", solution(15))
print("solution(1_000) =>", solution(1_000))
