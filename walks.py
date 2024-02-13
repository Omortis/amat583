import networkx as nx
import matplotlib.pyplot as plt
import pprint

pp = pprint.PrettyPrinter(indent=4)

edge_list = [(1, 2), (2, 3), (3, 4), (2, 4)]

G = nx.Graph()
G.add_edges_from(edge_list)

walks = nx.number_of_walks(G, 3)
total_walks = sum(sum(tgts.values()) for _, tgts in walks.items())
pp.pprint(walks)
print(f"total walks of length 3: {total_walks}")

nx.draw_spring(G, with_labels=True)
plt.show()

