import XD.my_functions as my

#G = my.Graph('large_files/dijkstraData_test01.txt', different_length=True)
#G = my.Graph('large_files/dijkstraData_test02.txt', different_length=True)
#G = my.Graph('large_files/dijkstraData_test03.txt', different_length=True)
G = my.Graph('large_files/dijkstraData.txt', different_length=True)

G.dijkstra_shortest_path(1)


test_vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
for v in test_vertices[:-1]:
    print(G.vertices[v], end=',')
print(G.vertices[test_vertices[-1]])

# 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068