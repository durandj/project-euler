import collections
import math
import typing


KNOWN_PRIMES: list[int] = [2, 3]


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    midpoint = math.ceil(math.sqrt(n))
    for p in KNOWN_PRIMES:
        if p > midpoint:
            return True

        if n % p == 0:
            return False

    for q in range(KNOWN_PRIMES[-1], midpoint + 1, 2):
        if n % q == 0:
            return False

    return True


def prime_generator():
    global KNOWN_PRIMES

    for p in KNOWN_PRIMES:
        yield p

    q = KNOWN_PRIMES[-1]
    while True:
        q += 2

        if not is_prime(q):
            continue

        KNOWN_PRIMES.append(q)

        yield q


def prime_factorize(n: int) -> list[int]:
    factors: list[int] = []
    for p in prime_generator():
        if p >= n:
            break

        if n % p == 0:
            factors.append(p)

    return factors


def main() -> None:
    start_point = 644
    target_factors = 4

    def _match(target: int, values: typing.Iterable[tuple[int, list[int]]]) -> bool:
        return all((len(factors) == target for _, factors in values))

    numbers = collections.deque([
        (start_point + i, prime_factorize(start_point + i))
        for i in range(target_factors)
    ])

    while not _match(target_factors, numbers):
        new_n = numbers[-1][0] + 1

        numbers.popleft()
        numbers.append((new_n, prime_factorize(new_n)))

    print([n for n, _ in numbers])


if __name__ == "__main__":
    main()
