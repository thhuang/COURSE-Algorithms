import re
import unionfind
from tqdm import tqdm

filename = 'large_files/clustering_big.txt'
#filename = 'large_files/clustering_big_test01.txt'

# read input
first_line = True
nodes = dict()
for line in open(filename):
    if first_line:
        first_line = False
        n, max_spacing = line.split()
        max_spacing = int(max_spacing)
        print(n, 'nodes')
        print(max_spacing, 'bits for each nodes')
        continue

    line = re.sub(r'\s+', '', line)
    #line = line.split()
    nodes[line] = 0

# assign node index
for n, i in zip(nodes.keys(), range(len(nodes))):
    nodes[n] = i
clusters = unionfind.unionfind(len(nodes))

def hop(n, i, j):
    if i == j:
        if n[i] == '1':
            return n[:i] + '0' + n[i + 1:]
        else:  # n[i] == '0'
            return n[:i] + '1' + n[i + 1:]
    else:
        if n[i] == '1' and n[j] == '1':
            return n[:i] + '0' + n[i + 1:j] + '0' + n[j + 1:]
        elif n[i] == '1' and n[j] == '0':
            return n[:i] + '0' + n[i + 1:j] + '1' + n[j + 1:]
        elif n[i] == '0' and n[j] == '1':
            return n[:i] + '1' + n[i + 1:j] + '0' + n[j + 1:]
        else:  # n[i] == '0' and n[j] == '0'
            return n[:i] + '1' + n[i + 1:j] + '1' + n[j + 1:]

for u in tqdm(nodes):  # check every nodes
    for i in range(max_spacing):
        for j in range(i, max_spacing):
            v = hop(u, i, j)  # a candidate of neighbors
            if v in nodes:
                clusters.unite(nodes[u], nodes[v])

groups = set()
for i in range(len(nodes)):
    groups.add(clusters.find(i))
print(len(groups))