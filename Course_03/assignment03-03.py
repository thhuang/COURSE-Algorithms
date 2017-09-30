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
w = int(file.readline())
weight = [0, w]
maximum_weight = [0, w]

# main loop:
# maximum_weight[i] = max{ maximum_weight[i-1], maximum_weight[i-2] + wi }
for w in file:
    maximum_weight.append(max(maximum_weight[-1], maximum_weight[-2] + int(w)))
    weight.append(int(w))
# compute max-weight independent set
mwis = set()
i = 1000
while i > 0:
    if maximum_weight[i - 2] + weight[i] > maximum_weight[i - 1]:
        mwis.add(i)
        i -= 2
    else:
        i -= 1

# compute the answer
ans = ''
for i in [1, 2, 3, 4, 17, 117, 517, 997]:
    if i in mwis:
        ans += '1'
    else:
        ans += '0'
print('Answer:', ans)
