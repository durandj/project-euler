def solution(max: int) -> int:
    return sum([i for i in range(1, max) if i % 3 == 0 or i % 5 == 0])


print(solution(1_000))
