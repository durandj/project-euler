import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    midpoint = math.sqrt(n)

    q = 3
    while q < midpoint:
        if n % q == 0:
            return False

        q += 2

    return True


def prime_sieve():
    yield 2

    n = 3
    while True:
        if is_prime(n):
            yield n

        n += 2


def get_number_length(n: int) -> int:
    return math.ceil(math.log10(n))


def get_nth_digit(n: int, digit: int) -> int:
    return (n % 10**(digit + 1)) // 10**digit


def is_pandigital(value: int) -> bool:
    n = get_number_length(value)

    unique = set[int]()
    for d in range(n):
        unique.add(get_nth_digit(value, d))

    for i in range(1, n + 1):
        if i not in unique:
            return False

    return True


def main() -> None:
    max_pandigital = 0

    for p in prime_sieve():
        if get_number_length(p) >= 10:
            break

        if is_pandigital(p):
            max_pandigital = max(max_pandigital, p)


    print(max_pandigital)


if __name__ == "__main__":
    main()
