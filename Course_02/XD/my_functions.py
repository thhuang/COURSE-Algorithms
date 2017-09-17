class Stack:
    def __init__(self):
        self._storage = []

    def push(self, item):
        self._storage.append(item)

    def pop(self):
        return self._storage.pop()

    def is_empty(self):
        return len(self._storage) == 0

class Vertex:
    def __init__(self):
        self._label = False

    def label(self):
        self._label = True

    def is_labeled(self):
        return self._label