# https://www.hackerrank.com/challenges/whats-your-name/submissions/code/165189205

# input
# Ross
# Taylor


def print_full_name(a, b):
    a = a[0:11]
    b = b[0:11]
    print(f"Hello {a} {b}! You just delved into python.")


if __name__ == "__main__":
    a = input()
    b = input()

    print_full_name(a, b)
