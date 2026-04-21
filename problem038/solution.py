# We know that the seed value can't be greater than 9 digits long
# We know that n > 1

import math


def is_pandigital(value: int) -> bool:
    if math.log10(value) > 9:
        return False

    str_value = str(value)

    return "".join(sorted(str_value)) == "123456789"


def calc_concatenated_product(m: int, n: int) -> int:
    values = [m * i for i in range(1, n + 1)]

    result = 0
    for value in values:
        digit_length = math.ceil(math.log10(value))

        result = result * 10 ** digit_length + value

    return result


max_value = 0
# 10 ^ 4.5 is picked because a base 10, zeroless pandigital number
# must have a length of 9 digits. Because n > 1 that means we have to
# have m and m + 2 as parts of the composite number. If m is already
# more than 4 digits long then m * 2 is also going to be at least 5
# digits long which would exceed the 9 digit length.
# So if we solve log(m) < 9/2 we get m < 10 ^ 4.5
for m in reversed(range(9, math.ceil(10 ** 4.5))):
    max_n = math.ceil((10 ** 4.5) / m)
    for n in reversed(range(2, max_n)):
        concatenated_product = calc_concatenated_product(m, n)
        if not is_pandigital(concatenated_product):
            continue

        if concatenated_product > max_value:
            max_value = concatenated_product

        break

print(max_value)
