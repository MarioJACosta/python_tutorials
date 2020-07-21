# input
# 5
# 10 40 30 50 20
# 1 2 3 4 5

if __name__ == "__main__":

    n = int(input())
    x = list(map(int, input().rstrip().split()))
    w = list(map(int, input().rstrip().split()))

    mean = 0
    for i in range(n):
        mean = mean + (x[i] * w[i])

    print("{:.1f}".format(mean/sum(w)))
