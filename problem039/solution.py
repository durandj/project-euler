import math


max_p = 1_000

def main() -> None:
    solution = (0, 0)
    # 12 was picked since the smallest right triangle with integer
    # side lengths is the { 3, 4, 5 } triangle which has a perimeter
    # of 12.
    for p in range(12, max_p + 1):
        solutions_for_p = 0
        for a in range(1, p - 3):
            for b in range(1, p - a - 1):
                c = math.sqrt(a**2 + b**2)
                if c != int(c):
                    continue

                if a + b + c != p:
                    continue

                solutions_for_p += 1

        solution = max(solution, (p, solutions_for_p), key=lambda s: s[1])

    print(solution[0])

if __name__ == "__main__":
    main()
