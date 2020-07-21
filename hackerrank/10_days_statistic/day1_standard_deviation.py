# input
# 5
# 10 40 30 50 20
import math


def get_mean(n, x):
    return sum(x) / n


def get_standard_deviation(n, x):
    mean = get_mean(n, x)
    sd = 0

    for i in range(n):
        sd = sd + (x[i] - mean)**2

    return math.sqrt(sd/n)


if __name__ == "__main__":
    n = int(input())

    x = list(map(int, input().rstrip().split()))

    print("{:.1f}".format(get_standard_deviation(n, x)))
