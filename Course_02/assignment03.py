import XD.my_functions as my

h = my.Heap()

h.push(3)
h.push(4)
h.push(1)
h.push(6)
h.push(2)
h.push(10)
h.push(5)
print(len(h))
print(h)
while len(h):
    print(h.pop())

print('-----------------------')

h = my.Heap(max_heap=True)
h.push(3)
h.push(4)
h.push(1)
h.push(6)
h.push(2)
h.push(10)
h.push(5)
print(len(h))
print(h)
while len(h):
    print(h.pop())