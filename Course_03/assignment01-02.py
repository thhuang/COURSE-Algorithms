import heapq

h = list()

for line in open('large_files/jobs.txt'):
#for line in open('large_files/jobs_test01.txt'):
    line = line.split()
    if len(line) != 2:
        continue
    weight = int(line[0])
    length = int(line[1])
    difference = weight - length
    ratio = weight / length
    h.append((ratio, weight, length))

heapq._heapify_max(h)
completion_time = 0
twct = 0  # total_weighted_completion_times
while len(h):
    job = heapq._heappop_max(h)
    completion_time += job[2]
    twct += job[1] * completion_time
    print(job, completion_time, twct)

print(twct)