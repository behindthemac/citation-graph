import networkx as nx
import matplotlib.pyplot as plt


# Create a new directed graph
G = nx.DiGraph()

# Add nodes to the graph
G.add_nodes_from(['A', 'B', 'C', 'D'])

# Add edges to the graph (from, to)
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('A', 'C')
G.add_edge('C', 'D')

# Draw the graph
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

plt.show()

