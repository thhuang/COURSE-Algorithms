import queue
import os
import sys

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
for line in file:
    symbols.append(int(line))

symbols.sort()
q1 = queue.Queue(symbols)
q2 = queue.Queue()




