import matplotlib.pyplot as plt
import networkx as nx
import statistics
import random

from Assignments.A1.A1 import number_of_nodes, number_of_edges, highest_degree, lowest_degree, average_degree, \
    histogram_degrees

from Assignments.A2.A2 import shortest_path


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

    # Create two nodes list
    list_of_nodes = node_list_create(graph)

    list_of_nodes_random = node_list_create(graph)

    list_of_nodes = node_list_sort(list_of_nodes, graph, nodes)
    list_of_nodes = list_of_nodes[0:8]
    random.shuffle(list_of_nodes_random)

    average_path_random = remove_nodes(list_of_nodes_random)

    print(f"Removing two orders in random degree makes the path {average_path_random}")
    print(f"Nodes in decreasing order of degree are {list_of_nodes}")
    connected_print(graph, list_of_nodes)


def connected_print(G, nodes_list):
    for i in range(0, len(nodes_list)):
        for j in range(0, len(nodes_list)):
            if i == j:
                pass
            elif G.has_edge(nodes_list[i], nodes_list[j]):
                print(f"There exists an edge between {nodes_list[i]} {nodes_list[j]}")

        print("\n \n")


def remove_nodes(nodes_list):
    graph_r = nx.read_adjlist('../Datasets/vitevitch.adjlist')
    for i in range(0, 2):
        graph_r.remove_node(nodes_list[i])
    return shortest_path(graph_r)


def node_list_sort(list_of_nodes, graph, nodes):
    for i in range(0, nodes):
        for j in range(i + 1, nodes):
            if graph.degree(list_of_nodes[j]) > graph.degree(list_of_nodes[i]):
                tmp = list_of_nodes[j]
                list_of_nodes[j] = list_of_nodes[i]
                list_of_nodes[i] = tmp
    return list_of_nodes


def node_list_create(G):
    node_list = []
    for node in G.nodes():
        node_list.append(node)
    return node_list


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
