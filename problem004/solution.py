def is_palindrome(value: int) -> bool:
    str_value = str(value)

    for i in range(len(str_value) // 2):
        if str_value[i] != str_value[-1 - i]:
            return False

    return True


def solution(digit_size: int) -> int:
    range_min = 10 ** (digit_size - 1)
    range_max = 10**digit_size

    max_palindrome = 0

    for x in range(range_min, range_max):
        for y in range(range_min, range_max):
            product = x * y

            if is_palindrome(product) and max_palindrome < product:
                max_palindrome = product

    return max_palindrome


print("size 2 =>", solution(2))
print("size 3 =>", solution(3))
