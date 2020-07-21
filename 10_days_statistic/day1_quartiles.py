# input
# 9
# 3 7 8 5 12 14 21 13 18
import statistics

if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().rstrip().split()))

    quartiles = sorted(x)
    index = n // 2

    q2 = int(statistics.median(quartiles))
    q1 = int(statistics.median(quartiles[:index]))

    if n % 2 == 0:
        q3 = int(statistics.median(quartiles[index:]))
    else:
        q3 = int(statistics.median(quartiles[index + 1:]))

    print(q1)
    print(q2)
    print(q3)