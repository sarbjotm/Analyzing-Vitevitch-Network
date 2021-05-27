import networkx as nx
import matplotlib.pyplot as plt  # Since we are not using a notebook we will import like this

SG = nx.read_adjlist('../Datasets/vitevitch.adjlist')

nx.draw(SG,
        with_labels=True,
        node_color='black',
        node_size=16,
        font_size=10,
        verticalalignment='bottom',
        edge_color='grey'
        )

plt.show()
