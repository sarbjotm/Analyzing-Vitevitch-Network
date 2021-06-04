import networkx as nx
import matplotlib.pyplot as plt  # Since we are not using a notebook we will import like this


def main():
    graph = nx.read_adjlist('../Datasets/vitevitch.adjlist')
    connected = is_connected(graph)
    avg_short_path = shortest_path(graph)
    deg_asrt = assortativity(graph)
    removed_nodes = disconnected(graph)
    density = network_density(graph.number_of_nodes(), graph.number_of_edges())
    reduce_density = reduce_least_density(removed_nodes)
    removed_components = components(removed_nodes)
    print(f"The truth value of connectedness is {connected} \n"
          f"The average shortest path in our network is {avg_short_path} \n"
          f"The degree of assortativity is {deg_asrt} \n"
          f"If we remove the nodes {removed_nodes} our graph will become disconnected \n"
          f"The Current density of our network is {density} \n"
          f"Removing the nodes {removed_nodes} resuls in densitys of {reduce_density} respectively \n"
          f"The list of components are as followed:  \n "
          f"\t - {removed_components[0]} \n"
          f"\t - {removed_components[1]} \n"
          f"\t - {removed_components[2]} \n"
          f"\t - {removed_components[3]} \n"
          f"\t - {removed_components[4]} \n")
    print(len(removed_components))


def components(nodes_list):
    return_components = []
    for nodes in nodes_list:
        graph_r = nx.read_adjlist('../Datasets/vitevitch.adjlist')
        graph_r.remove_node(nodes)
        return_components.append(list(nx.connected_components(graph_r)))
    return return_components


def reduce_least_density(nodes_list):
    difference = 0
    min_node = []
    for nodes in nodes_list:
        graph_r = nx.read_adjlist('../Datasets/vitevitch.adjlist')
        graph_r.remove_node(nodes)
        density = nx.density(graph_r)
        min_node.append(density)
    return min_node


def network_density(N, L):
    numerator = 2 * L
    denominator = N * (N - 1)
    return numerator / denominator


def disconnected(graph):
    return_nodes = []
    for node in list(graph.nodes()):
        graph_r = nx.read_adjlist('../Datasets/vitevitch.adjlist')
        graph_r.remove_node(node)
        if not nx.is_connected(graph_r):
            return_nodes.append(node)
            nx.draw(graph_r,
                    with_labels=True,
                    node_color='black',
                    node_size=18,
                    font_size=8,
                    verticalalignment='baseline',
                    edge_color='grey')
            plt.title(f"Removed node {node}")
            plt.savefig(f'{node}.png')
            plt.show()

    return return_nodes


def shortest_path(G):
    return nx.average_shortest_path_length(G)


def is_connected(G):
    return nx.is_connected(G)


def assortativity(G):
    return nx.degree_assortativity_coefficient(G)


if __name__ == '__main__':
    main()
