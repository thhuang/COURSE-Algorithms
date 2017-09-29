import heapq
import os
import sys

class Symbol():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return '({name},{weight})'.format(name=self.name, weight=self.weight)

    def __add__(self, other):
        return Symbol(left.name + right.name, left.weight + right.weight)

# open(filename, access, buffering)
try:
    file = open('large_files/mwis.txt', 'r')
    header = file.readline().strip()
    print(header, 'symbols')
except Exception as e:
    print(e)
    os.system('ls')
    sys.exit()

symbols = list()
index = 0
for weight in file:
    heapq.heappush(symbols, Symbol([str(index)], int(weight)))
    index += 1

