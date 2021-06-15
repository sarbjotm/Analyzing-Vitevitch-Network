import matplotlib.pyplot as plt
import networkx as nx
import statistics

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
    print(nodes)
    edges = number_of_edges(graph)
    max_degree = highest_degree(graph)
    mean_degree = average_degree(nodes, edges)
    histogram_degrees(graph)
    node_degree_mapping = create_dictionary(graph)
    node_max_between = between(graph)
    max_closeness = closeness(graph, max_degree[0])
    print(f"Our node that has a max degree is {max_degree} \n"
          f"Our max degree is {graph.degree(max_degree[0])} \n"
          f"Our graph has a mean degree of {mean_degree} \n"
          f"Our max betweenness node is {node_max_between[0]} \n"
          f"Our max value for between is {node_max_between[1]} \n"
          f"Max closeness is {max_closeness}"
          )

    betweenness = nx.centrality.betweenness_centrality(graph)
    betweenness_sequence = list(betweenness.values())
    print('Mean betweenness:', statistics.mean(betweenness_sequence))
    mean_closeness = closeness_mean(graph)
    print(f"Mean closeness is {mean_closeness}")


def closeness_mean(G):
    total = 0
    for node in G.nodes():
        total = total + nx.closeness_centrality(G, node)
    total = total / number_of_nodes(G)
    return total


def closeness(G, node):
    return nx.closeness_centrality(G, node)


def between(G):
    return_list = []
    betweenness = nx.centrality.betweenness_centrality(G)
    highest_betweenness_node = max(G.nodes, key=betweenness.get)
    return_list.append(highest_betweenness_node)
    return_list.append(betweenness[highest_betweenness_node])
    return return_list


def create_dictionary(G):
    return_dict = {}
    for nodes in G.nodes():
        return_dict[nodes] = G.degree(nodes)
    return return_dict


if __name__ == '__main__':
    main()
