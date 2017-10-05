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
plt.scatter(X, Y)
plt.show()
cutoff = float(input('Enter the cutoff: '))
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

# main loop
time.sleep(0.1)
for m in range(2, n+1):  # m = sub-problem size
    t0 = time.time()
    A = dict()
    for S in combinations(range(n), m):
        if S[0] == 0:
            for j in S[1:]:
                sub_prob = list()
                for k in S:
                    if k != j and V[k].distance(V[j]) < cutoff:
                        S_sub = tuple(v for v in S if v != j)
                        if len(S_sub) == 1 or k != 0:
                            sub_prob.append(all_sets[m-1][(S_sub, k)] + V[k].distance(V[j]))
                A[(S, j)] = min(sub_prob) if len(sub_prob) else inf
    print(m, round(min(A.values()), 2), round(time.time() - t0, 2))
    if min(A.values()) == inf:
        print('Try a larger cutoff!')
        exit()
    all_sets.append(A)
    all_sets[m - 1] = []

time.sleep(0.1)
S = tuple(range(n))
tours = list()
for j in S[1:]:
    tours.append(all_sets[n][(S, j)] + V[j].distance(V[0]))

print('The minimum cost of a traveling salesman tour is', min(floor(tours)))

