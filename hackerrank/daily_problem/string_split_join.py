# https://www.hackerrank.com/challenges/python-string-split-and-join/submissions/code/165864248

# input
# this is a string

def split_and_join(line):
    a = line.split(" ")

    return "-".join(a)


if __name__ == "__main__":
    line = input()

    print(split_and_join(line))
