import networkx as nx
import matplotlib.pyplot as plt  # Since we are not using a notebook we will import like this


def main():
    graph = nx.read_adjlist('../Datasets/vitevitch.adjlist')
    connected = is_connected(graph)
    avg_short_path = shortest_path(graph)
    deg_asrt = assortativity(graph)
    print(f"The truth value of connectedness is {connected} \n"
          f"The average shortest path in our network is {avg_short_path} \n"
          f"The degree of assortativity is {deg_asrt}")

    removed_nodes = disconnected(graph)

    print(removed_nodes)


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
