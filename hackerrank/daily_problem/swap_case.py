# https://www.hackerrank.com/challenges/swap-case/submissions/code/165188791

# input
# HackerRank.com presents "Pythonist 2".


def swap_case(s):
    a = ""
    for c in s:
        a += c.lower() if c.isupper() else c.upper()
    return a


if __name__ == '__main__':
    s = input()

    print(swap_case(s))
