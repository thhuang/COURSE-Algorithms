import XD.my_functions as my
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

# initialize
n = len(V)
all_sets = [[]]
m = 1
A = dict()
for S in combinations(range(n), m):
    if S != (0,):
        A[(S, 0)] = inf
    else:
        A[(S, 0)] = 0
all_sets.append(A)

# main loop
time.sleep(0.1)
for m in tqdm(range(2, n+1)):  # m = sub-problem size
    A = dict()
    for S in combinations(range(n), m):
        if S[0] == 0:
            for j in S[1:]:
                sub_prob = list()
                for k in S:
                    if k != j:
                        S_sub = tuple(v for v in S if v != j)
                        if len(S_sub) > 1 and k == 0:
                            sub_prob.append(inf)
                        else:
                            sub_prob.append(all_sets[m-1][(S_sub, k)] + V[k].distance(V[j]))
                A[(S, j)] = min(sub_prob)
    all_sets.append(A)
    all_sets[m - 1] = []

time.sleep(0.1)
S = tuple(range(n))
tours = list()
for j in S[1:]:
    tours.append(A[(S, j)] + V[j].distance(V[0]))

print('The minimum cost of a traveling salesman tour is', floor(min(tours)))

