#import libraries

import networkx as nx
from matplotlib import pyplot as plt

# create graph with networkx library
G = nx.Graph()

# add 6 nodes
G.add_nodes_from([1,2,3,4,5,6])

# add edges to the graph
G.add_weighted_edges_from([
    (1,2,1),(2,3,6),(3,6,2),(1,4,1),(4,5,4),(5,6,6)])

# create a minimum spanning tree
#T = nx.minimum_spanning_tree(G)

# print the edges of the minimum spanning tree
#print(T.edges(data=True))

# draw graph with edge labels
nx.draw(G, with_labels=True)
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels=nx.get_edge_attributes(G,'weight'))

plt.show()