import os
import sys

# open file
try:
    file = open('large_files/mwis.txt', 'r')
    header = file.readline().strip()
    print(header, 'symbols')
except Exception as e:
    print(e)
    os.system('ls')
    sys.exit()

# initialization
maximum_weight = list()
index = 0
for weight in file:
    index += 1

