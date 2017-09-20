import XD.my_functions as my
from tqdm import tqdm
from time import sleep

h_low = my.Heap(max_heap=True)
h_high = my.Heap()

medians = list()

for num in tqdm(open('large_files/Median.txt')):

    num = int(num)
    if len(h_low) and h_low.peek() > num:
        h_low.push(num)
    elif len(h_high) and h_high.peek() < num:
        h_high.push(num)
    else:
        h_low.push(num)

    while len(h_low) > len(h_high) + 1:
        h_high.push(h_low.pop())
    while len(h_high) > len(h_low) + 1:
        h_low.push(h_high.pop())

    if len(h_high) > len(h_low):
        medians.append(h_high.peek())
    else:
        medians.append(h_low.peek())

sleep(0.1)
print(sum(medians) % 10000)