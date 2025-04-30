import math


known_primes = [2, 3]


def is_prime(value: int) -> bool:
    midpoint = math.sqrt(value)

    for p in known_primes:
        if p > value:
            return True

        if value % p == 0:
            return False

    i = known_primes[-1] + 2
    while i < midpoint:
        if value % i == 0:
            return False

        i += 2

    return True


def prime_sieve():
    for p in known_primes:
        yield p

    i = known_primes[-1]
    while True:
        if is_prime(i):
            known_primes.append(i)
            yield i

        i += 2


def find_prime_factors(value: int) -> set[int]:
    remainder = value
    prime_factors = set()
    while remainder > 1:
        for p in prime_sieve():
            if p > remainder:
                break

            if remainder % p == 0:
                q = int(remainder / p)

                prime_factors.add(p)

                if is_prime(q) and q != 1:
                    prime_factors.add(q)

                remainder = q

                break

    return prime_factors


def solution(value: int) -> int:
    return max(find_prime_factors(value))


print("13195 => ", solution(13_195))
print("600851475143 => ", solution(600_851_475_143))
