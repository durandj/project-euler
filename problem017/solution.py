int_to_english_less_than_20_mapping = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

int_to_english_tens_mapping = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


def int_to_english_str(value: int) -> str:
    # Ignoring the negative numbers

    if value == 0:
        return ""
    elif value < 20:
        return int_to_english_less_than_20_mapping[value]
    elif value < 100:
        tens_value = value // 10
        remainder = value % 10

        tens_str = int_to_english_tens_mapping[tens_value]
        remainder_str = int_to_english_str(remainder)

        return f"{tens_str}-{remainder_str}".strip(" -")
    elif value < 1_000:
        hundreds_value = value // 100
        remainder = value % 100

        hundreds_str = int_to_english_less_than_20_mapping[hundreds_value]
        tens_str = int_to_english_str(remainder)

        return f"{hundreds_str} hundred and {tens_str}".removesuffix(" and ")
    elif value < 1_000_000:
        thousands_value = value // 1_000
        remainder = value % 1_000

        thousands_str = int_to_english_str(thousands_value)
        hundreds_str = int_to_english_str(remainder)

        return f"{thousands_str} thousand {hundreds_str}"

    else:
        raise Exception(f"Value '{value}' is too big")


def solution(max_number: int) -> int:
    strings = [
        int_to_english_str(i).replace(" ", "").replace("-", "")
        for i in range(1, max_number + 1)
    ]

    return sum([len(s) for s in strings])


print("<= 5 =>", solution(5))
print("<= 1,000 =>", solution(1_000))
