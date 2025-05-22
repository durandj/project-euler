def find_sequence_length(seed: int) -> int:
    iterations = 1

    n = seed
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        iterations += 1

    return iterations


def solution() -> int:
    max_seed = 0
    max_length = 0
    for i in range(1, 1_000_000):
        seq_length = find_sequence_length(i)
        if seq_length > max_length:
            max_seed = i
            max_length = seq_length

    return max_seed


print("sample =>", find_sequence_length(13))
print("solution =>", solution())
