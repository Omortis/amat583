import networkx as nx
import random
import time

timeStart = time.perf_counter()

noOfVertices = 100000
G = nx.Graph()

# Create vertices (0, 1, ..., noOfVertices) of G
for i in range(noOfVertices):
  G.add_node(i)

# Add random edges. The average will be about 4.
for i in range(2 * noOfVertices):
  G.add_edge(random.randint(0, noOfVertices-1),
             random.randint(0, noOfVertices-1))

# Find the shortest path between 2 vertices.
#   Note: nx.shortest_path() uses the 'dijkstra' algorithm.
x = nx.shortest_path(G, 0, 1)

timeEnd = time.perf_counter()
timeDuration = timeEnd - timeStart

print(f"The shortest path between 0 and 1 has length {len(x)-1}")
print(G)
print(f"Generation and analysis took {timeDuration:.3f} seconds")
