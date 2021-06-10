import networkx as nx
import matplotlib.pyplot as plt  # Since we are not using a notebook we will import like this
import random

def highest_degree(G):
    max_value = 0
    nodes_with_max_value = []
    for node in G.nodes():
        if G.degree(node) > max_value:
            max_value = G.degree(node)

    for node in G.nodes():
        if G.degree(node) == max_value:
            nodes_with_max_value.append(node)

    print(f"Node {nodes_with_max_value} has degree {max_value}")


G = nx.read_edgelist('../Datasets/ia-enron-only.edges', nodetype=int)
print(nx.info(G))
print(nx.is_connected(G)) #Q1
highest_degree(G) #Q2

C = G.copy() #Q5
nodes_to_remove = random.sample(list(C.nodes), 2)
C.remove_nodes_from(nodes_to_remove)
number_of_steps = 25
M = G.number_of_nodes() // number_of_steps
# print(M)
# num_nodes_removed = range(0, G.number_of_nodes(), M)
#
# N = G.number_of_nodes()
# C = G.copy()
# random_attack_core_proportions = []
# for nodes_removed in num_nodes_removed:
#     # Measure the relative size of the network core
#     core = next(nx.connected_components(C))
#     core_proportion = len(core) / N
#     random_attack_core_proportions.append(core_proportion)
#
#     # If there are more than M nodes, select M nodes at random and remove them
#     if C.number_of_nodes() > M:
#         nodes_to_remove = random.sample(list(C.nodes), M)
#         C.remove_nodes_from(nodes_to_remove)
#
# plt.title('Random failure')
# plt.xlabel('Number of nodes removed')
# plt.ylabel('Proportion of nodes in core')
# plt.plot(num_nodes_removed, random_attack_core_proportions, marker='o')
# plt.show()

nodes_sorted_by_degree = sorted(G.nodes, key=G.degree, reverse=True) #Q6
top_degree_nodes = nodes_sorted_by_degree[:M]
print(top_degree_nodes)
N = G.number_of_nodes()
number_of_steps = 25
M = N // number_of_steps

num_nodes_removed = range(0, N, M)
C = G.copy()
targeted_attack_core_proportions = []
for nodes_removed in num_nodes_removed:
    # Measure the relative size of the network core
    core = next(nx.connected_components(C))
    core_proportion = len(core) / N
    targeted_attack_core_proportions.append(core_proportion)

    # If there are more than M nodes, select top M nodes and remove them
    if C.number_of_nodes() > M:
        nodes_sorted_by_degree = sorted(C.nodes, key=C.degree, reverse=True)
        nodes_to_remove = nodes_sorted_by_degree[:M]
        C.remove_nodes_from(nodes_to_remove)

plt.title('Targeted attack')
plt.xlabel('Number of nodes removed')
plt.ylabel('Proportion of nodes in core')
plt.plot(num_nodes_removed, targeted_attack_core_proportions, marker='o')
plt.show()