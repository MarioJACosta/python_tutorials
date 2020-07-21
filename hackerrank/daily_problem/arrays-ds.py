# https://www.hackerrank.com/challenges/arrays-ds

# input
# 4
# 1 4 3 2


def reverse_array(a):
    return [i for i in a[::-1]]


if __name__ == '__main__':
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverse_array(arr)

    print(res)
