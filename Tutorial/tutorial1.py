import networkx as nx
import matplotlib.pyplot as plt  # Since we are not using a notebook we will import like this


# Exercise 1 Often in the context of trees, a node with degree 1 is called a leaf. Write a function named get_leaves
# that takes a graph as an argument, loops through the nodes, and returns a list of nodes with degree 1.

def get_leaves(G):
    return_list = []
    for node in G.nodes:
        if G.degree(node) == 1:
            return_list.append(node)
    print(return_list)


def main():
    G = nx.Graph()
    G.add_edges_from([
        ('a', 'b'),
        ('a', 'd'),
        ('c', 'd'),
    ])
    nx.draw(G, with_labels=True)
    # plt.show # To show graph/diagram of nodes
    get_leaves(G)


if __name__ == "__main__":
    main()
