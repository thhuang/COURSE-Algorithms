import XD.my_functions as my

G = my.Graph('large_files/g3.txt', different_length_direct=True)
#G = my.Graph('large_files/g_test01.txt', different_length_direct=True)
#G = my.Graph('large_files/dijkstraData.txt', different_length=True)

G.johnson_all_pairs_shortest_path()

