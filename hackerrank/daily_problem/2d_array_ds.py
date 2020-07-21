# https://www.hackerrank.com/challenges/2d-array

# input
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0


def hourglass_sum(arr):
    max_sum = -63
    for i in range(4):
        for j in range(4):
            hourglass = sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3])
            print(hourglass)

            max_sum = hourglass if hourglass > max_sum else max_sum

    return max_sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)

    print(result)
