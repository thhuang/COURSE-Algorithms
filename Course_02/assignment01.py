import XD.my_functions as my
import random

G = my.Graph('large_files/SCC_test01.txt')
#G = my.Graph('large_files/SCC.txt')

#s = random.choice(list(G.vertices.keys()))
#print('s = ' + str(s) + ', ' + str(G.vertices[s]))

G.dfs_loop()


