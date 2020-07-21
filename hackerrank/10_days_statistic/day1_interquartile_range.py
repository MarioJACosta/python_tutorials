# input
# 6
# 6 12 8 10 20 16
# 5 4 3 2 1 5
import statistics

if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().rstrip().split()))
    f = list(map(int, input().rstrip().split()))

    s = [x[i] for i in range(n) for _ in range(f[i])]

    quartiles = sorted(s)
    index = len(quartiles) // 2

    q2 = int(statistics.median(quartiles))
    q1 = int(statistics.median(quartiles[:index]))

    if n % 2 == 0:
        q3 = int(statistics.median(quartiles[index:]))
    else:
        q3 = int(statistics.median(quartiles[index + 1:]))

    print("{:.1f}".format(q3 - q1))
