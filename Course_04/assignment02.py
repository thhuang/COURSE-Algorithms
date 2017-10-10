import XD.my_functions as my
import matplotlib.pyplot as plt
import os
import sys
import time
from math import inf, floor
from tqdm import tqdm
from itertools import combinations


# load data
#filename = 'large_files/tsp_test01.txt'
filename = 'large_files/tsp.txt'
try:
    file = open(filename, 'r')
    header = file.readline().strip()
    print(header, 'vertices')
except Exception as e:
    print(e)
    os.system('ls')
    sys.exit()
V = list()
for line in file:
    line = line.split()
    V.append(my.Vertex(float(line[0]), float(line[1])))

# set cutoff
X = list()
Y = list()
for v in V:
    X.append(v.x)
    Y.append(v.y)
d_max = ((max(X) - min(X))**2 + (max(Y) - min(Y))**2) ** 0.5
#plt.scatter(X, Y)
#plt.show()
cutoff = 0.3 #float(input('Enter the cutoff: '))
cutoff *= d_max

# initialize
n = len(V)
all_sets = [[]]
A = dict()
for S in combinations(range(n), 1):
    if S != (0,):
        A[(S, 0)] = inf
    else:
        A[(S, 0)] = 0
all_sets.append(A)

# distance matrix
D = list()
for i in range(n):
    D_row = list()
    for j in range(n):
        D_row.append(V[i].distance(V[j]))
    D.append(D_row)

# main loop
time.sleep(0.1)
t_main = time.time()
for m in range(2, n+1):  # m = sub-problem size
    t0 = time.time()
    A_new = dict()
    for S in combinations(range(n), m):
        if S[0] == 0:
            for i in range(1, m):
                j = S[i]
                S_sub = S[:i] + S[i + 1:]
                sub_prob = inf
                for k in S_sub:
                    if D[k][j] < cutoff and (S_sub, k) in A and sub_prob > A[(S_sub, k)] + D[k][j]:
                        sub_prob = A[(S_sub, k)] + D[k][j]
                A_new[(S, j)] = sub_prob
    print(m, round(min(A.values()), 2), round(time.time() - t0, 2))
    if min(A_new.values()) == inf:
        print('Try a larger cutoff!')
        exit()
    A = A_new

time.sleep(0.1)
S = tuple(range(n))
tours = list()
for j in S[1:]:
    tours.append(A[(S, j)] + V[j].distance(V[0]))

print(round(time.time() - t_main, 2))
print('The minimum cost of a traveling salesman tour is', floor(min(tours)))