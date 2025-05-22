def solution(limit: int) -> int:
    results = set()
    for a in range(2, limit + 1):
        for b in range(2, limit + 1):
            results.add(a**b)

    return len(results)


print("solution(5) =>", solution(5))
print("solution(100) =>", solution(100))
