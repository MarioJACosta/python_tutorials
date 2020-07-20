# https://www.hackerrank.com/challenges/write-a-function/submissions/code/163364560


def is_leap(year):
    leap = False

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return leap

    if year % 4 == 0:
        return True

    return leap


if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))
