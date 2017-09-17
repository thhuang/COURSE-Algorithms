import XD.my_functions as my

#G = my.Graph('large_files/SCC_test01.txt')
G = my.Graph('large_files/SCC.txt')

print('DFS on G_rev')
G.dfs_loop(reverse=True)
print('{:-^50}'.format(''))

print('DFS on G')
G.reset_territory()
G.dfs_loop()
print('{:-^50}'.format(''))

scc = G.scc()

display = 5
for i in range(display - 1):
    print(scc.pop() if len(scc) else '0', end=',')
print(scc.pop() if len(scc) else '0')
