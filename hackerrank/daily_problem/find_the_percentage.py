# https://www.hackerrank.com/challenges/finding-the-percentage/submissions/code/169165972

# input
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    s = sum(student_marks[query_name])
    m = len(student_marks[query_name])
    a = s / m

    print("%.2f" % a)
