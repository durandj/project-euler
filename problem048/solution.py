def modular_add(a: int, b: int, m: int) -> int:
    return (a + b) % m


def modular_multiply(a: int, b: int, m: int) -> int:
    return (a * b) % m


def modular_exp(b: int, e: int, m: int) -> int:
    assert e > 0, "only positive exponents supported"

    result = b
    for _ in range(e - 1):
        result = modular_multiply(result, b, m)

    return result


def main() -> None:
    m = 10**10

    result = 0
    for i in range(1, 1_000 + 1):
        result = modular_add(result, modular_exp(i, i, m), m)

    print(result)


if __name__ == "__main__":
    main()
