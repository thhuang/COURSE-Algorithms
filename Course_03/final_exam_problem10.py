A = {(1, 1): 0.2, (2, 2): 0.05, (3, 3): 0.17, (4, 4): 0.1, (5, 5): 0.2, (6, 6): 0.03, (7, 7): 0.25}

n = len(A)
for s in range(0, n):
    for i in range(1, n + 1):
        if i + s <= n:
            C_subtrees = list()
            for r in range(i, i + s + 1):
                left = A[(i, r - 1)] if i <= r - 1 else 0
                right = A[(r + 1, i + s)] if r + 1 <= i + s else 0
                C_subtrees.append(left + right)
            A[(i, i + s)] = sum([A[(k, k)] for k in range(i, i + s + 1)]) + min(C_subtrees)

print(A[(1, n)])
