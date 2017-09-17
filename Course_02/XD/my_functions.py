from tqdm import tqdm
from time import sleep


class Stack:
    def __init__(self):
        self._storage = []

    def push(self, item):
        self._storage.append(item)

    def pop(self):
        return self._storage.pop()

    def peek(self):
        return self._storage[-1]

    def is_empty(self):
        return len(self._storage) == 0


class Graph:
    def __init__(self, filename):
        self._vertices = dict()
        self._vertices_rev = dict()  # reversal
        self._territory = dict()
        self._edges = list()
        self._leader = dict()
        self._finish = dict()
        self._t = 0  # finishing time
        self._s = None  # leader

        for line in tqdm(open(filename)):
            v, w = line.split()
            v = int(v)
            w = int(w)

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



            self._edges.append((v, w))

        sleep(0.1)
        print('n = ' + str(len(self._vertices)) + ', m = ' + str(len(self._edges)))
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

    def reset_territory(self):
        for v in self._territory:
            self._territory[v] = False

    def dfs(self, s, reverse=False):
        self._leader[s] = []
        stk = Stack()
        stk.push(s)

        while not stk.is_empty():
            v = stk.pop()
            print(v)
            if not self.is_explored(v):
                self.explore(v)
                self._leader[s].append(v)
                if reverse:
                    for w in self._vertices_rev[v]:
                        stk.push(w)
                else:
                    for w in self._vertices[v]:
                        stk.push(w)

    def dfs_loop(self, reverse=False):
        for i in reversed(list(self._vertices.keys())):
            if not self.is_explored(i):
                self._s = i
                self.dfs(self._s, reverse)
                #print(str(self._s) + ' leads ' + str(len(self._leader[self._s])))

