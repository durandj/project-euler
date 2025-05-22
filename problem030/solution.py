import math


def solution(exponent: int) -> int:
    matches = set()

    digits = 2
    while True:
        max_sum = digits * (9**exponent)
        if math.floor(math.log10(max_sum)) < digits:
            break

        for i in range(10, max_sum + 1):
            sum_of_i = 0
            t = i
            while t > 0:
                sum_of_i += (t % 10) ** exponent
                t = t // 10

            if sum_of_i == i:
                matches.add(i)

        digits += 1

    return sum(matches)


print("solution(4) =>", solution(4))
print("solution(5) =>", solution(5))
