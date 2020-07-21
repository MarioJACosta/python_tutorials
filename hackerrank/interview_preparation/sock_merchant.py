# input
# 9
# 10 20 20 10 10 30 50 10 20
from collections import Counter


def sock_merchant(n, ar):
    colors = Counter(ar)

    pairs = 0
    for k, v in colors.items():
        pairs += v // 2

    return pairs


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(n, ar)

    print(result)
