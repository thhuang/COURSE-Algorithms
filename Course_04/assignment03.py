import os
import sys
from math import sqrt, floor, inf
from tqdm import tqdm
from time import time

# load data
filename = 'large_files/nn.txt'
#filename = 'large_files/nn_test01.txt'
try:
    file = open(filename, 'r')
    n = int(file.readline())
    print(n, 'vertices')
except Exception as e:
    print(e)
    os.system('ls')
    sys.exit()

X = list()
Y = list()
for line in file:
    line = line.split()
    X.append(float(line[1]))
    Y.append(float(line[2]))

S = set(range(n))
A = 0
v = 0
S.remove(v)
t0 = time()
while len(S):
    D = list()
    nearest = inf
    for i in S:
        d = (X[i] - X[v])**2 + (Y[i] - Y[v])**2
        if d < nearest:
            nearest = d
            w = i
    A += sqrt(nearest)
    S.remove(w)
    v = w

A += sqrt((X[0] - X[v])**2 + (Y[0] - Y[v])**2)
print('Answer:', floor(A))
print('running time:', round(time() - t0, 2), 'sec')