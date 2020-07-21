import os


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamic_array(n, queries):
    # Write your code here
    last_answer = 0
    seq = []
    answer = []

    for _ in range(0, n):
        seq.append([])

    for i in queries:
        q = i[0]  # It can be either 1 or 2
        x = i[1]
        y = i[2]
        index = (x ^ last_answer) % n

        if q == 1:
            seq[index].append(y)
        elif q == 2:
            size = len(seq[index])  # Calculate the size of the sequence at this index
            last_answer = seq[index][y % size]  # Look up the value in this sequence at index y % size
            answer.append(last_answer)

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamic_array(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
