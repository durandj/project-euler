import math


def find_divisors(x: int) -> list[int]:
    divisors = []

    midpoint = math.ceil(math.sqrt(x))
    for p in range(1, midpoint + 1):
        if x % p == 0:
            divisors.append(p)
            divisors.append(x // p)

    return divisors


def are_coprime(x: int, y: int) -> bool:
    x_factors = set(find_divisors(x))
    y_factors = set(find_divisors(y))

    common_factors = x_factors.intersection(y_factors)
    gcd = max(common_factors)

    return gcd == 1


def solution() -> int:
    results = {}
    for d in range(2, 1_000):
        if not are_coprime(d, 10):
            continue

        for k in range(1, 1_000):
            if 10**k % d == 1:
                results[d] = math.floor(math.log10(10**k // d)) + 1
                break

    sorted_results = sorted(results.items(), key=lambda t: t[1], reverse=True)

    return sorted_results[0][0]


print("are_coprime(7, 10) =>", are_coprime(7, 10))
print("are_coprime(3, 6) =>", are_coprime(3, 6))
print("solution() =>", solution())
