import math


known_primes = [2, 3]


def is_prime(value: int) -> bool:
    midpoint = math.sqrt(value)

    for p in known_primes:
        if p > midpoint:
            break

        if value % p == 0:
            return False

    return True


def prime_sieve():
    for p in known_primes:
        yield p

    candidate = known_primes[-1] + 2
    while True:
        if is_prime(candidate):
            known_primes.append(candidate)
            yield candidate

        candidate += 2


def solution(max_value: int) -> int:
    result = 0
    for p in prime_sieve():
        if p > max_value:
            break

        result += p

    return result


print("< 10 =>", solution(10))
print("< 2,000,000", solution(2_000_000))
