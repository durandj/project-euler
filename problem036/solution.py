def is_palindrome(s: str) -> bool:
    length = len(s)
    midpoint = length // 2

    for i in range(midpoint + 1):
        if s[i] != s[length - i - 1]:
            return False

    return True


def solution() -> int:
    result = 0
    for n in range(1, 1_000_000, 2):
        str_b10 = str(n)
        str_b2 = bin(n)[2:]

        if is_palindrome(str_b10) and is_palindrome(str_b2):
            result += n

    return result


print(solution())
