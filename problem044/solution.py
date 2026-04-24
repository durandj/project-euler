import math


PREVIOUS_PENTAGONAL_NUMBERS: list[int] = [1]


def calculate_pentagonal_number(n: int) -> int:
    return n * (3 * n - 1) // 2


def is_pentagonal_number(v: int) -> int:
    # The formula for a pentagonal number is a quadratic so we can
    # solve for n using standard methods. The only special casing we
    # need to do is drop the subtraction case since that'll always
    # be a negative number which isn't possible in our situation.
    return (1 + math.sqrt(1 + 24 * v)) % 6 == 0


def main() -> None:
    n = 1
    while True:
        n += 1

        p = calculate_pentagonal_number(n)
        PREVIOUS_PENTAGONAL_NUMBERS.append(p)
        assert n == len(PREVIOUS_PENTAGONAL_NUMBERS)

        found = False
        for q in reversed(PREVIOUS_PENTAGONAL_NUMBERS[:-1]):
            s = p + q
            d = p - q

            assert d > 0

            is_s_pentagonal = is_pentagonal_number(s)
            is_d_pentagonal = is_pentagonal_number(d)
            if not is_s_pentagonal or not is_d_pentagonal:
                continue

            print(d)
            found = True

        if found:
            break


if __name__ == "__main__":
    main()
