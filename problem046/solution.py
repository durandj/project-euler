import math


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


def main() -> None:
    n = 7
    while True:
        n += 2

        if is_prime(n):
            continue

        if (n - 1) % 100_000 == 0:
            print(n, len(KNOWN_PRIMES))

        found = False
        for p in prime_generator():
            if p > n - 2:
                found = True

                break

            q = math.sqrt((n - p) / 2.0)
            if q == math.floor(q):
                break

        if found:
            print(n)

            break


if __name__ == "__main__":
    main()
