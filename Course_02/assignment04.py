from tqdm import tqdm
from time import sleep
from time import time

data = set()
for num in tqdm(open('large_files/twoSum.txt')):
    num = int(num)
    data.add(num)

sleep(0.1)
print(len(data), 'numbers')
sleep(0.1)

a = time()
count = 0
#ans = list()
for t in range(-10000, 10001):
    for x in data:
        y = t - x
        if y != x and y in data:
            #ans.append(t)
            count += 1
            break

print(time() - a)
sleep(0.1)
#print('t:', ans)
print(count)

