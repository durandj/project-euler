import itertools
import math


def product(*args: int) -> int:
    p = 1
    for v in args:
        p *= v

    return p


def find_dn(n: int) -> int:
    n_adjusted = n
    g = 0
    start = 0
    while True:
        g += 1
        width = g * 9 * 10 ** (g - 1)

        if n_adjusted <= width:
            break

        n_adjusted -= width
        start += width // g

    offset = math.ceil(n_adjusted / g)
    digit = g - 1 - ((n_adjusted - 1) % g)

    num = start + offset
    dn = (num % 10**(digit + 1)) // 10**digit

    return dn


def main() -> None:
    print("dn(1) =>", find_dn(1))
    print("dn(10) =>", find_dn(10))
    print("dn(11) =>", find_dn(11))
    print("dn(12) =>", find_dn(12))
    print("dn(13) =>", find_dn(13))
    print("dn(14) =>", find_dn(14))
    print("dn(15) =>", find_dn(15))
    print("dn(100) =>", find_dn(100))
    print("dn(190) =>", find_dn(190))

    expected = "".join([str(i) for i in range(1, 10_000)])
    actual = "".join([str(find_dn(i + 1)) for i in range(9 + 2 * 90 + 3 * 900 + 4 * 9_000)])
    assert len(expected) == len(actual)

    for expected_batch, actual_batch in zip(itertools.batched(expected, n=15), itertools.batched(actual, n=15)):
        e = "".join(expected_batch)
        a = "".join(actual_batch)
        
        if e != a:
            print(e)
            print(a)
            assert a == e
    assert expected == actual

    print(
        "solution =>",
        product(
            find_dn(1),
            find_dn(10),
            find_dn(100),
            find_dn(1_000),
            find_dn(10_000),
            find_dn(100_000),
            find_dn(1_000_000),
        ),
    )


if __name__ == "__main__":
    main()
