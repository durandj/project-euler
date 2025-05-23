def reverse_int(n: int) -> int:
    return int(str(n)[::-1])


def is_reversible(n: int) -> bool:
    s = n + reverse_int(n)

    while s > 0:
        if s % 2 == 0:
            return False

        s //= 10

    return True


def solution(limit: int) -> int:
    return sum([1 for n in range(1, limit) if n % 10 != 0 and is_reversible(n)])


print(solution(1_000_000_000))
