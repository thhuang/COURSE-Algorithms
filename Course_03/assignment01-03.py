import XD.my_functions as my

G = my.Graph('large_files/edges.txt', different_cost=True)

G.prim_mst()
