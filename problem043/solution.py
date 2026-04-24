import itertools


def tuple_to_int(digits: tuple[int, ...]) -> int:
    return sum(
        10**i * d
        for i, d in enumerate(reversed(digits))
    )


def main() -> None:
    primes = [2, 3, 5, 7, 11, 13, 17]

    result = 0
    for digits in itertools.permutations(list(range(10))):
        if digits[0] == 0:
            continue

        match = True
        for i in range(len(primes)):
            sub = 100 * digits[i + 1] + 10 * digits[i + 2] + digits[i + 3]
            p = primes[i]

            if sub % p != 0:
                match = False
                break

        if match:
            n = tuple_to_int(digits)
            result += n

    print(result)


if __name__ == "__main__":
    main()
