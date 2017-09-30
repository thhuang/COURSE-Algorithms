import XD.my_functions as my

#G = my.Graph('large_files/edges_test01.txt', different_cost=True)
#G = my.Graph('large_files/edges.txt', different_cost=True)
G = my.Graph('large_files/clustering1.txt', different_cost=True)

#G.prim_mst()

#G.kruskal_mst()

G.max_spacing_k_clustering(4)