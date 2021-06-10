import matplotlib.pyplot as plt
import networkx as nx

from Assignments.A1.A1 import number_of_nodes, number_of_edges, highest_degree, lowest_degree, average_degree, \
    histogram_degrees


def main():
    graph = nx.read_adjlist('../Datasets/vitevitch.adjlist')
    nx.draw(graph,
            with_labels=True,
            node_color='black',
            node_size=18,
            font_size=8,
            verticalalignment='baseline',
            edge_color='grey')
    plt.show()
    nodes = number_of_nodes(graph)
    edges = number_of_edges(graph)
    max_degree = highest_degree(graph)
    min_degree = lowest_degree(graph)
    mean_degree = average_degree(nodes, edges)
    histogram_degrees(graph)


if __name__ == '__main__':
    main()
