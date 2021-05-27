import networkx as nx
import matplotlib.pyplot as plt  # Since we are not using a notebook we will import like this


def main():
    SG = nx.read_adjlist('../Datasets/vitevitch.adjlist')

    nx.draw(SG,
            with_labels=True,
            node_color='black',
            node_size=16,
            font_size=10,
            verticalalignment='bottom',
            edge_color='grey',
            )

    plt.show()
    return SG


def number_of_edges(G):
    return G.number_of_edges()


def number_of_nodes(G):
    return G.number_of_nodes()


def number_of_possible_edges(N):
    max_edges = (N * (N - 1)) / 2
    return max_edges


def network_density(N, L):
    numerator = 2 * L
    denominator = N * (N - 1)
    return numerator / denominator


if __name__ == '__main__':
    graph = main()
    edges = number_of_edges(graph)
    nodes = number_of_nodes(graph)
    max_edges_possible = number_of_possible_edges(nodes)
    density = network_density(nodes, edges)
    print(f"The number of edges in our graph is {edges}, and the number of nodes in our graph is {nodes}. \n"
          f"The max amount of edges possible in a undirected graph with {nodes} nodes is {max_edges_possible} \n"
          f"The density of our network is {density}.")
