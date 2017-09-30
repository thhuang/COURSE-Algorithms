import os
import sys
from time import time

# open file
try:
    file = open('large_files/knapsack1.txt', 'r')
    header = file.readline().strip().split()
    print('number of items:', header[1])
    print('knapsack size:', header[0])
except Exception as e:
    print(e)
    os.system('ls')
    sys.exit()

t = time()

items = list()
for line in file:
    line = line.split()
    items.append((int(line[0]), int(line[1])))

# initialization
W = int(header[0])
n = int(header[1])
A = {(0, x):0 for x in range(0, W + 1)}

for i in range(1, n + 1):
    vi = items[i - 1][0]
    wi = items[i - 1][1]
    for x in range(0, W + 1):
        if x >= wi and A[(i - 1, x - wi)] + vi > A[(i - 1, x)]:
            A[(i, x)] = A[(i - 1, x - wi)] + vi
        else:
            A[(i, x)] = A[(i - 1, x)]

print(A[n, W])
print('running time:', time() - t, 'sec')