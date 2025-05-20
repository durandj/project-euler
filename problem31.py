def solution(target: int, units: list[int]) -> int:
    if len(units) == 0:
        return 0
    elif target == 0:
        return 1

    sorted_units = sorted(units, reverse=True)

    current_unit = sorted_units.pop(0)
    if current_unit == 1:
        return 1

    possibilities = target // current_unit
    if len(sorted_units) == 1:
        return possibilities + 1

    return sum(
        [
            solution(target - current_unit * i, sorted_units)
            for i in range(possibilities + 1)
        ]
    )


uk_coins = [
    1,
    2,
    5,
    10,
    20,
    50,
    100,
    200,
]


print("solution(200, uk) =>", solution(200, uk_coins))
