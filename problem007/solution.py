import math


def is_prime(value: int, primes: list[int]) -> bool:
    midpoint = math.sqrt(value)

    for p in primes:
        if p > midpoint:
            break

        if value % p == 0:
            return False

    return True


def solution(count: int) -> int:
    primes = [2]

    candidate = 3
    while len(primes) < count:
        if is_prime(candidate, primes):
            primes.append(candidate)

        candidate += 2

    return primes[-1]


print("6 =>", solution(6))
print("10,001 =>", solution(10_001))
