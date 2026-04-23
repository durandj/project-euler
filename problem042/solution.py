KNOWN_TRIANGLE_NUMBERS: set[int] = set()
PREVIOUS_MAX_TRIANGLE_N = 0


def calculate_triangle_number(n: int) -> int:
    return int(0.5 * n * (n + 1))


def is_triangle_number(n: int) -> bool:
    global KNOWN_TRIANGLE_NUMBERS
    global PREVIOUS_MAX_TRIANGLE_N

    while PREVIOUS_MAX_TRIANGLE_N < n:
        PREVIOUS_MAX_TRIANGLE_N += 1
        KNOWN_TRIANGLE_NUMBERS.add(calculate_triangle_number(PREVIOUS_MAX_TRIANGLE_N))

    return n in KNOWN_TRIANGLE_NUMBERS


def word_to_number(word: str) -> int:
    return sum(
        ord(c) - ord("A") + 1
        for c in word
    )


def main() -> None:
    with open("words.txt", "r") as words_file:
        words = [
            word.strip().strip("\"")
            for word in words_file.readline().split(",")
        ]

    triangle_words = 0
    for word in words:
        word_num = word_to_number(word)
        if is_triangle_number(word_num):
            triangle_words += 1

    print(triangle_words)


if __name__ == "__main__":
    main()
