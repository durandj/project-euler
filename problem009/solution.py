def is_pythagorean_triple(a: int, b: int, c: int) -> bool:
    return a**2 + b**2 == c**2


def solution(target_sum: int) -> int:
    # It's a 2 here because we have to leave at least room for
    # two 1's, one for b and one for c.
    for a in range(1, target_sum - 2):
        # There needs to be at least a 1 left over for c.
        for b in range(1, target_sum - a - 1):
            c = target_sum - a - b
            if is_pythagorean_triple(a, b, c):
                return a * b * c


print("12 =>", solution(12))
print("1,000 =>", solution(1_000))
