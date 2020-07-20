# https://www.hackerrank.com/challenges/find-a-string

# input
# ABCDCDC
# CDC


def count_substring(string, substring):
    return sum([1 for i in range(len(string) - len(substring) + 1) if string[i:i + len(substring)] == substring])


if __name__ == "__main__":
    string = input()
    substring = input()

    print(count_substring(string, substring))
