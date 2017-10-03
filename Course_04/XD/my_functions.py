from tqdm import tqdm
from time import sleep
from math import inf
from collections import deque
from time import time
from copy import deepcopy
import sys
import os
import random
import heapq
import unionfind


class Stack:
    def __init__(self):
        self._storage = []

    def push(self, x):
        self._storage.append(x)

    def pop(self):
        return self._storage.pop()

    def size(self):
        return len(self._storage)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self._storage[-1] if self.size() else None


class Queue:
    def __init__(self, data=None):
        if data:
            self._storage = deque(data)
        else:
            self._storage = deque()
    def push(self, x):
        self._storage.append(x)

    def pop(self):
        return self._storage.popleft()

    def size(self):
        return len(self._storage)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self._storage[0] if self.size() else None


# incorrect!
class Heap:
    def __init__(self, max_heap=False):
        self._storage = []
        self._max_heap = max_heap

    def __len__(self):
        return len(self._storage)

    def __getitem__(self, i):
        return self._storage[i]

    def __setitem__(self, i, x):
        self._storage[i] = x

    def __str__(self):
        return str(self._storage)

    def _swap(self, i, j):
        self[i], self[j] = self[j], self[i]

    def push(self, x):
        self._storage.append(x)
        i = len(self)

        if self._max_heap:
            while i != 1 and self[i - 1] > self[i // 2 - 1]:
                self._swap(i - 1, i // 2 - 1)
                i = i // 2
        else:
            while i != 1 and self[i - 1] < self[i // 2 - 1]:
                self._swap(i - 1, i // 2 - 1)
                i = i // 2

    def pop(self):
        self._swap(-1, 0)
        ans = self._storage.pop()
        i = 1
        if self._max_heap:
            while i * 2 <= len(self):
                if i * 2 == len(self) and self[i - 1] < self[i * 2 - 1]:
                    self._swap(i - 1, i * 2 - 1)
                    i = i * 2
                elif i * 2 < len(self):
                    if self[i * 2 - 1] > self[i * 2]:
                        self._swap(i - 1, i * 2 - 1)
                        i = i * 2
                    else:
                        self._swap(i - 1, i * 2)
                        i = i * 2 + 1
                else:
                    break
        else:
            while i * 2 <= len(self):
                if i * 2 == len(self) and self[i - 1] > self[i * 2 - 1]:
                    self._swap(i - 1, i * 2 - 1)
                    i = i * 2
                elif i * 2 < len(self):
                    if self[i * 2 - 1] < self[i * 2]:
                        self._swap(i - 1, i * 2 - 1)
                        i = i * 2
                    else:
                        self._swap(i - 1, i * 2)
                        i = i * 2 + 1
                else:
                    break
        return ans

    def peek(self):
        return self[0]

    def size(self):
        return len(self._storage)

    def is_empty(self):
        return self.size() == 0


class Graph:
    def __init__(self, filename, edge_list=False, different_length=False, different_cost=False,
                 different_length_direct=False):
        self._vertices = dict()
        self._vertices_rev = dict()  # reversal
        self._territory = dict()
        self._edges = dict()
        self._in_direct_edges = dict()
        self._leader = dict()
        self._finish = dict()
        self._t = 0  # finishing time
        self._s = None  # leader

        if edge_list:
            print('Loading from ' + filename)
            for line in tqdm(open(filename)):
                v, w = line.split()
                v = int(v)
                w = int(w)

                self._edges[v] = w

                # add adjacent list
                if not self._vertices.get(v):
                    self._territory[v] = False
                    self._vertices[v] = [w]
                else:
                    self._vertices[v].append(w)
                if not self._vertices_rev.get(w):
                    self._vertices_rev[w] = [v]
                else:
                    self._vertices_rev[w].append(v)

                # include sink nodes
                if not self._vertices.get(w):
                    self._territory[w] = False
                    self._vertices[w] = []
                if not self._vertices_rev.get(v):
                    self._vertices_rev[v] = []

            sleep(0.1)
            print('n = ' + str(len(self._vertices)) + ', m = ' + str(len(self._edges)))
            print('{:-^50}'.format(''))

        if different_length:
            print('Loading from ' + filename)
            for line in tqdm(open(filename)):
                line = line.split()
                v = int(line[0])
                if len(line) > 1:
                    for e in line[1:]:
                        if ',' in e:
                            w, l = e.split(',')
                            w = int(w)
                            l = int(l)
                            self._vertices[v] = inf  # dijkstra's greedy score
                            self._vertices[w] = inf
                            self._territory[v] = False
                            self._territory[w] = False
                            self._edges[(v, w)] = l
                            if w in self._in_direct_edges.keys():
                                self._in_direct_edges[w].append(v)
                            else:
                                self._in_direct_edges[w] = [v]

            sleep(0.1)
            print('n = ' + str(len(self._vertices)) + ', m = ' + str(len(self._edges)))
            print('{:-^50}'.format(''))

        if different_length_direct:
            try:
                file = open(filename, 'r')
                print('Loading from ' + filename)
                header = file.readline().strip().split()
                #print('n =', header[1])
                #print('m =', header[0])
            except Exception as e:
                print(e)
                os.system('ls')
                sys.exit()

            for line in tqdm(file):
                line = line.split()
                v = int(line[0])
                w = int(line[1])
                l = int(line[2])
                self._vertices[v] = inf  # minimum cost
                self._vertices[w] = inf
                self._territory[v] = False
                self._territory[w] = False
                self._edges[(v, w)] = l
                if w in self._in_direct_edges.keys():
                    self._in_direct_edges[w].append(v)
                else:
                    self._in_direct_edges[w] = [v]


            sleep(0.1)
            print('n = ' + str(len(self._vertices)) + ', m = ' + str(len(self._edges)))
            print('{:-^50}'.format(''))

        if different_cost:
            print('Loading from ' + filename)
            self._pairs = list()
            first_line = True
            for line in tqdm(open(filename)):
                if first_line:
                    first_line = False
                    continue
                line = line.split()
                v = int(line[0])
                w = int(line[1])
                c = int(line[2])
                self._vertices[v] = inf  # minimum cost
                self._vertices[w] = inf  # undirected graph, minimum cost
                self._territory[v] = False
                self._territory[w] = False
                self._edges[(v, w)] = c
                self._edges[(w, v)] = c
                heapq.heappush(self._pairs, (c, (v, w)))

            sleep(0.1)
            print('n = ' + str(len(self._vertices)) + ', m = ' + str(len(self._edges) / 2))
            print('{:-^50}'.format(''))

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges

    def is_explored(self, v):
        return self._territory[v]

    def explore(self, v):
        self._territory[v] = True

    def scc(self):
        scc_size = list()
        for k in self._leader.keys():
            scc_size.append(len(self._leader[k]))
        scc_size.sort()
        return scc_size

    def reset_territory(self):
        for v in self._territory:
            self._territory[v] = False

    def dfs(self, s, reverse=False):
        self._leader[s] = []
        stk = Stack()
        stk.push(s)
        start = Stack()

        while not stk.is_empty():
            v = stk.pop()
            if not self.is_explored(v):
                start.push(v)
                self.explore(v)
                self._leader[s].append(v)
                self._t += 1
                if reverse:
                    for w in self._vertices_rev[v]:
                        stk.push(w)
                else:
                    for w in self._vertices[v]:
                        stk.push(w)
            if reverse:
                while (stk.peek() == None or stk.peek() not in self._vertices_rev[
                    start.peek()]) and not start.is_empty():
                    self._finish[self._t - start.size()] = start.pop()

    def dfs_loop(self, reverse=False):
        keys = list(self._vertices.keys())
        for i in tqdm(reversed(keys)) if reverse else tqdm(reversed(range(len(keys)))):
            if not reverse:
                i = self._finish[i + 1]
            if not self.is_explored(i):
                self._s = i
                self.dfs(self._s, reverse)
        sleep(0.1)
        '''
        if reverse:
            print(self._finish)
        else:
            print(self._leader)
        '''

    def dijkstra_shortest_path(self, s):
        X = set()  # explored vertices
        h = []  # unexplored vertices, heap key = dijkstra's greedy score
        for v in self._vertices.keys():
            heapq.heappush(h, (inf, v))

        def greedy_score(v, w):
            return self._vertices[v] + self._edges[(v, w)]

        def update_score(v, score):
            heapq.heappush(h, (score, v))
            self._vertices[v] = score

        def explore_vertex(v):
            X.add(v)
            self.explore(v)

            for e in self._edges.keys():
                if e[0] == v and not self.is_explored(e[1]):
                    score = greedy_score(v, e[1])
                    if self._vertices[e[1]] > score:
                        update_score(e[1], score)

        def initialize(s):
            for v in self._vertices.keys():
                self._vertices[v] = inf
            self.reset_territory()
            self._vertices[s] = 0
            explore_vertex(s)

        initialize(s)

        while X != set(self._vertices):
            score, v = heapq.heappop(h)
            explore_vertex(v)

    def prim_mst(self):
        X = set()  # explored vertices
        h = []  # unexplored vertices, heap key = minimum cost
        total_cost = 0
        for v in self._vertices.keys():
            heapq.heappush(h, (inf, v))

        def edge_cost(v, w):
            return self._edges[(v, w)]

        def update_cost(v, cost):
            heapq.heappush(h, (cost, v))
            self._vertices[v] = cost

        def explore_vertex(v):
            X.add(v)
            self.explore(v)

            for e in self._edges.keys():
                if e[0] == v and not self.is_explored(e[1]):
                    cost = edge_cost(v, e[1])
                    if self._vertices[e[1]] > cost:
                        update_cost(e[1], cost)

        def initialize():
            s = random.randint(min(self._vertices), max(self._vertices))
            self._vertices[s] = 0
            explore_vertex(s)
            return s

        v = initialize()
        while X != set(self._vertices):
            cost, w = heapq.heappop(h)
            while self._territory[w]:
                cost, w = heapq.heappop(h)
            total_cost += cost
            v = w
            explore_vertex(v)
        print('Total cost:', total_cost)

    def max_spacing_k_clustering(self, k):
        u = unionfind.unionfind(len(self._vertices))
        groups = len(u.groups())
        total_spacing = 0
        while groups > k:
            spacing, pair = heapq.heappop(self._pairs)
            p = pair[0] - 1
            q = pair[1] - 1
            if not u.issame(p, q):
                u.unite(p, q)
                groups -= 1
                total_spacing += spacing

        if k == 1:
            return total_spacing
        else:
            while groups > 1:
                spacing, pair = heapq.heappop(self._pairs)
                p = pair[0] - 1
                q = pair[1] - 1
                if not u.issame(p, q):
                    u.unite(p, q)
                    groups -= 1
                    print(spacing)
                    break

    def kruskal_mst(self):
        print('Total cost:', self.max_spacing_k_clustering(1))

    def bellman_ford_shortest_path(self, s):
        # initialize
        n = len(self._vertices)
        A = {(0, v):inf for v in self._vertices.keys()}
        A[(0, s)] = 0

        # Bellman-Ford algorithm
        for i in range(1, n):
            for v in self._vertices.keys():
                case1 = A[(i - 1, v)]
                case2 = min(A[(i - 1, w)] + self._edges[(w, v)] for w in self._in_direct_edges[v])
                A[(i, v)] = case1 if case1 < case2 else case2

        # check negative cycle
        i = n
        for v in self._vertices.keys():
            case1 = A[(i - 1, v)]
            case2 = min(A[(i - 1, w)] + self._edges[(w, v)] for w in self._in_direct_edges[v])
            if case1 > case2:
                print('There is a negative cycle!')
                sys.exit()

        for v in self._vertices.keys():
            self._vertices[v] = A[(n - 1, v)]

    def johnson_all_pairs_shortest_path(self):
        t1 = time()
        print('0. backup the original graph')
        original_vertices = deepcopy(self._vertices)
        original_edges = deepcopy(self._edges)
        original_in_direct_edges = deepcopy(self._in_direct_edges)
        t2 = time()
        print('\t\trunning time: {0:.2f} sec'.format(t2 - t1))

        t1 = t2
        print('1. Form new graph by add new vertex s and new edges (s, v)')
        s = min(self._vertices.keys()) - 1
        self._vertices[s] = 0
        self._in_direct_edges[s] = []
        for v in list(self._vertices.keys()):
            self._edges[(s, v)] = 0
            if v in self._in_direct_edges.keys():
                self._in_direct_edges[v].append(s)
            else:
                self._in_direct_edges[v] = [s]
        t2 = time()
        print('\t\trunning time: {0:.2f} sec'.format(t2 - t1))

        t1 = t2
        print('2. Run the Bellman-Ford algorithm on new graph with source vertex s')
        self.bellman_ford_shortest_path(s)
        t2 = time()
        print('\t\trunning time: {0:.2f} sec'.format(t2 - t1))

        t1 = t2
        print('3. Define weights for all edges')
        p = deepcopy(self._vertices)  # weights of vertices
        self._vertices = original_vertices
        self._edges = original_edges
        self._in_direct_edges = original_in_direct_edges
        for e in self._edges.keys():
            self._edges[e] += p[e[0]] - p[e[1]]
        t2 = time()
        print('\t\trunning time: {0:.2f} sec'.format(t2 - t1))

        t1 = t2
        print('4. Run Dijkstra\'s algorithm in the original graph')
        SSSP = list()
        for u in tqdm(self._vertices.keys()):
            self.dijkstra_shortest_path(u)
            shortest = inf
            for v in self._vertices.keys():
                distance = self._vertices[v] - p[u] + p[v]
                if distance < shortest: shortest = distance
            SSSP.append(shortest)
            #print('\tsourse: {s}, shortest distance = {d}'.format(s=u, d=shortest))
        t2 = time()
        print('\t\trunning time: {0:.2f} sec'.format(t2 - t1))

        t1 = t2
        print('5. Compute all-pair shortest path distance')
        print('Answer:', min(SSSP))
        t2 = time()
        print('\t\trunning time: {0:.2f} sec'.format(t2 - t1))

def hamming_distance(s1, s2):
    assert len(s1) == len(s2), '{0} and {1} have different length: {2} and {3}'.format(s1, s2, len(s1), len(s2))
    return sum(e1 != e2 for e1, e2 in zip(s1, s2))

