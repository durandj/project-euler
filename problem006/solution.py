def solution(max_value: int) -> int:
    sum_of_squares = sum([v**2 for v in range(1, max_value + 1)])
    square_of_sums = sum(range(1, max_value + 1)) ** 2

    return square_of_sums - sum_of_squares


print("10 =>", solution(10))
print("100 =>", solution(100))
