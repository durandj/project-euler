def solution(max: int) -> int:
    return sum([i for i in range(1, max) if i % 3 == 0 or i % 5 == 0])


print("< 10 =>", solution(10))
print("< 1,000 =>", solution(1_000))
