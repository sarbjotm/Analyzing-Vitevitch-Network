import collections

import networkx as nx
import matplotlib.pyplot as plt  # Since we are not using a notebook we will import like this
import numpy as np


def main():
    graph = nx.read_adjlist('../Datasets/vitevitch.adjlist')
    nx.draw(graph,
            with_labels=True,
            node_color='black',
            node_size=18,
            font_size=8,
            verticalalignment='baseline',
            edge_color='grey')
    edges = number_of_edges(graph)
    nodes = number_of_nodes(graph)
    max_edges_possible = number_of_possible_edges(nodes)
    density = network_density(nodes, edges)
    max_degree = highest_degree(graph)
    min_degree = lowest_degree(graph)
    mean_degree = average_degree(nodes, edges)
    print(f"The number of edges in our graph is {edges}, and the number of nodes in our graph is {nodes}. \n"
          f"The max amount of edges possible in a undirected graph with {nodes} nodes is {max_edges_possible} \n"
          f"The density of our network is {density}. \n"
          f"The average density of our network is {mean_degree} \n"
          f"The nodes with the minimum degree are:")
    for nodes in min_degree:
        print(f"\t-{nodes} (degree of {graph.degree(nodes)})")
    print(f"The nodes with the maximum grades are: ")
    for nodes in max_degree:
        print(f"\t-{nodes} (degree of {graph.degree(nodes)})")
    plt.savefig('graph.png')
    plt.show()
    histogram_degrees(graph)


def histogram_degrees(G):
    all_degrees = nx.degree_histogram(G)
    axes = plt.gca()
    plt.bar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], all_degrees)
    axes.set_xlim([0, 19])
    axes.xaxis.set_ticks(np.arange(0, 19, 1))
    plt.xlabel("Degree")
    plt.ylabel("Count")
    plt.savefig('histo.png')
    plt.show()


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


def highest_degree(G):
    max_value = 0
    nodes_with_max_value = []
    for node in G.nodes():
        if G.degree(node) > max_value:
            max_value = G.degree(node)

    for node in G.nodes():
        if G.degree(node) == max_value:
            nodes_with_max_value.append(node)

    return nodes_with_max_value


def lowest_degree(G):
    min_value = 1
    nodes_with_min_value = []
    for node in G.nodes():
        if G.degree(node) < min_value:
            min_value = G.degree(node)

    for node in G.nodes():
        if G.degree(node) == min_value:
            nodes_with_min_value.append(node)

    return nodes_with_min_value


def average_degree(N, L):
    return (2 * L) / N


if __name__ == '__main__':
    main()
