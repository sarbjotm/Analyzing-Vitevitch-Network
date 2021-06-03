import networkx as nx
import matplotlib.pyplot as plt  # Since we are not using a notebook we will import like this


#1/2 Paths ------------
G = nx.Graph()
G.add_nodes_from([1,2,3,4])
G.add_edges_from([(1,2),(2,3),(1,3),(1,4)])
nx.draw(G, with_labels=True)

#Since G is a connected graph, there exists a path for all nodes
# so has_path will be true for all

print(nx.shortest_path_length(G, 3, 4) > nx.shortest_path_length(G, 1, 4))

#3/4 Connected ------------

G = nx.Graph()
G.add_cycle((1,2,3))
G.add_edge(4,5)
nx.draw(G, with_labels=True) #Not connected

G.add_edge(3, 4) #Will make graph connected
print(nx.is_connected(G)) #True
G.remove_edge(1,2)
print(nx.is_connected(G)) #True cause still path exists

#5/6 - directed Components
D = nx.DiGraph()
D.add_edges_from([
    (1,2),
    (2,3),
    (3,2), (3,4), (3,5),
    (4,2), (4,5), (4,6),
    (5,6),
    (6,4),
])

print(nx.has_path(D, 1, 4) and not nx.has_path(D, 4, 1)) #True and not False -> true and true T
print(nx.shortest_path_length(D, 2, 5) > nx.shortest_path_length(D, 5, 2))
#If Strong then also weak