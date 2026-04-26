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


def prime_generator(threshold: int):
    for p in KNOWN_PRIMES:
        if p > threshold:
            break

        yield p


    n = KNOWN_PRIMES[-1] + 2
    while n < threshold:
        if is_prime(n):
            KNOWN_PRIMES.append(n)

            yield n

        n += 2


def sum_with_max(values: list[int], threshold: int) -> int:
    result = 0
    # We're assuming sorted order because of full system knowledge
    for v in reversed(values):
        result += v

        if result > threshold:
            return -1

    return result


def main() -> None:
    longest = (0, 0)

    all_primes = [
        p
        for p in prime_generator(1_000_000)
    ]
    print(f"Found {len(all_primes)} primes")

    # Find where no combination of end primes can be summed to less
    # than 1 million.
    end_j = 0
    for j in range(len(all_primes) - 1, 0, -1):
        i = j - 21
        s = sum_with_max(all_primes[i:j + 1], 1_000_000)
        if s != -1:
            end_j = j

            break

    print(f"Max j value {end_j}")

    for i in range(0, len(all_primes)):
        print(f"loop ({i})")
        for j in range(end_j, 0, -1):
            candidate = sum_with_max(all_primes[i:j + 1], 1_000_000)
            if candidate == -1:
                continue

            if not is_prime(candidate):
                continue

            streak_length = j - i + 1
            if streak_length < 21:
                continue

            longest = max(longest, (candidate, streak_length), key=lambda t: t[1])

    print(longest[0])


if __name__ == "__main__":
    main()
