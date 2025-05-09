import sys


def str_to_int(s: str) -> int:
    return sum([ord(c) - ord("a") + 1 for c in s.lower()])


def solution(lines: list[str]) -> int:
    lines.sort()

    result = 0
    for row, line in enumerate(lines):
        sanitized_str = line.strip('\n"')

        result += str_to_int(sanitized_str) * (row + 1)

    return result


print("str_to_int(COLIN) =>", str_to_int("COLIN"))


with open(sys.argv[1], "r") as input_file:
    lines = input_file.readlines()[0].split(",")

print("solution() =>", solution(lines))
