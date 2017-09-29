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
        return Symbol(self.name + other.name, self.weight + other.weight)

# open(filename, access, buffering)
try:
    file = open('large_files/huffman.txt', 'r')
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

dictionary = dict()
while len(symbols) > 1:
    left = heapq.heappop(symbols)
    right = heapq.heappop(symbols)
    for n in left.name:
        if dictionary.get(n):
            dictionary[n] = '0' + dictionary[n]
        else:
            dictionary[n] = '0'
    for n in right.name:
        if dictionary.get(n):
            dictionary[n] = '1' + dictionary[n]
        else:
            dictionary[n] = '1'
    heapq.heappush(symbols, left + right)

codes_length = list()
for c in dictionary.values():
    codes_length.append(len(c))
print('Maximum code length:', max(codes_length))
print('Minimum code length:', min(codes_length))