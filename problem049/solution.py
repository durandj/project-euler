import itertools
import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    midpoint = math.ceil(math.sqrt(n))
    for q in range(3, midpoint + 1, 2):
        if n % q == 0:
            return False

    return True


def digits_to_number(digits: list[int]) -> int:
    return sum((
        10**(len(digits) - i - 1) * d
        for i, d in enumerate(digits)
    ))


def main() -> None:
    for digits in itertools.combinations_with_replacement(list(range(0, 10)), 4):
        number_permutations = [
            n
            for c in itertools.permutations(digits)
            if (n := digits_to_number(list(c))) > 1_000 and is_prime(n)
        ]

        if len(number_permutations) < 3:
            continue

        number_permutations.sort()

        candidates = [
            (a, b, c)
            for a, b, c in itertools.combinations(number_permutations, 3)
            if b - a == 3330 and c - b == 3330
        ]

        if len(candidates) > 0:
            a, b, c = candidates[0]
            print(f"{a}{b}{c}")


if __name__ == "__main__":
    main()
