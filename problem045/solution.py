import math


def calculate_triangle_number(n: int) -> int:
    return n * (n + 1) // 2


def is_triangular_number(v: int) -> bool:
    return (-1 + math.sqrt(1 + 8 * v)) % 2 == 0


def calculate_pentagonal_number(n: int) -> int:
    return n * (3 * n - 1) // 2


def is_pentagonal_number(v: int) -> bool:
    return (1 + math.sqrt(1 + 24 * v)) % 6 == 0


def calculate_hexagonal_number(n: int) -> int:
    return n * (2 * n - 1)


def is_hexagonal_number(v: int) -> bool:
    return (1 + math.sqrt(1 + 8 * v)) % 4 == 0


def main() -> None:
    n = 285
    while True:
        n += 1

        tn = calculate_triangle_number(n)

        pentagonal = is_pentagonal_number(tn)
        hexagonal = is_hexagonal_number(tn)

        if not pentagonal or not hexagonal:
            continue

        print(tn)
        break


if __name__ == "__main__":
    main()
