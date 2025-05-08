import datetime


def solution() -> int:
    result = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            d = datetime.datetime(year, month, 1)
            if d.weekday() == 6:  # 6 == Sunday
                result += 1

    return result


print(solution())
