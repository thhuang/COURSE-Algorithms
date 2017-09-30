import os
import sys
from time import time

def maximum_value(A, items, i, x):
    vi = items[i - 1][0]
    wi = items[i - 1][1]

    if not (i - 1, x) in A:
        A[(i - 1, x)] = maximum_value(A, items, i - 1, x)

    if x <= wi:
        return A[(i - 1, x)]
    else:
        if not (i - 1, x - wi) in A:
            A[(i - 1, x - wi)] = maximum_value(A, items, i - 1, x - wi)

        case1 = A[(i - 1, x)]
        case2 = A[(i - 1, x - wi)] + vi
        return case1 if case1 > case2 else case2

# open file
try:
    file = open('large_files/knapsack_big.txt', 'r')
    header = file.readline().strip().split()
    print('number of items:', header[1])
    print('knapsack size:', header[0])
except Exception as e:
    print(e)
    os.system('ls')
    sys.exit()

sys.setrecursionlimit(3000)

t = time()

items = list()
for line in file:
    line = line.split()
    items.append((int(line[0]), int(line[1])))

# initialization
W = int(header[0])
n = int(header[1])
A = {(0, x):0 for x in range(0, W + 1)}

print(maximum_value(A, items, n, W))
print('running time:', time() - t, 'sec')