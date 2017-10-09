import XD.my_functions as my

satisfiability = list()
for i in range(6):

    filename = 'large_files/2sat{0}.txt'.format(i+1)
    G = my.Graph(filename, two_sat=True)

    print('DFS on G_rev')
    G.dfs_loop(reverse=True)
    print('{:-^50}'.format(''))

    print('DFS on G')
    G.reset_territory()
    G.dfs_loop()
    print('{:=^50}'.format(''))
    print()

    satisfiability.append('1' if G.scc(two_sat=True) else '0')

print('Answer: ', end='')
for ans in satisfiability:
    print(ans, end='')
print()