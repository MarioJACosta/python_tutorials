# input
# 10
# 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
from collections import Counter


def calculate_mean(length, numbers):
    return sum(numbers) / length


def calculate_median(length, numbers):
    data = sorted(numbers)
    index = length // 2

    if length % 2 == 1:
        return data[index]
    else:
        return (data[index] + data[index - 1]) / 2


def calculate_mode(numbers):
    counts = Counter(sorted(numbers))
    mode = [k for k, v in counts.items() if v == max(list(counts.values()))]
    return mode[0]


if __name__ == "__main__":
    length = int(input())

    numbers = list(map(int, input().rstrip().split()))

    print("{:.1f}".format(calculate_mean(length, numbers)))
    print("{:.1f}".format(calculate_median(length, numbers)))
    print(calculate_mode(numbers))
