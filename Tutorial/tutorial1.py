import networkx as nx
import matplotlib.pyplot as plt  # Since we are not using a notebook we will import like this


G = nx.Graph()

# give each a node a 'name', which is a letter in this case.
G.add_node('a')

# the add_nodes_from method allows adding nodes from a sequence, in this case a list
nodes_to_add = ['1','2','3','4','5','6']
G.add_nodes_from(nodes_to_add)

D = nx.DiGraph()

D.add_edges_from([(1,2),(2,3),(3,2),(3,4),(3,5),(4,5),(4,6),(5,6),(6,4),(4,2)])
print(D.has_edge(5,4))

nx.draw(D, with_labels=True,
        node_color='yellow')


# draw the graph
plt.show()