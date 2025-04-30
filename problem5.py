def solution(max_range: int) -> int:
    p = max_range
    if p % 2 == 1:
        p += 1

    while True:
        for q in range(2, max_range + 1):
            if p % q != 0:
                break
        else:
            return p

        p += 2


print("1 to 10 =>", solution(10))
print("1 to 20 =>", solution(20))
