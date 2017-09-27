import XD.my_functions as my
import re
import unionfind
from tqdm import tqdm

first_line = True
nodes = list()
index = 0
for line in open('large_files/clustering_big.txt'):
    if first_line:
        first_line = False
        n, max_spacing = line.split()
        print(n, 'nodes')
        print(max_spacing, 'bits for each nodes')
        continue

    index += 1
    line = re.sub(r'\s+', '', line)
    nodes.append((index, line))


u = unionfind.unionfind(len(nodes))