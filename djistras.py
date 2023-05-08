import networkx as nx

edges = [
    (3, 2, {"weight": 19}),
    (3, 1, {"weight": 7}),
    (1, 2, {"weight": 9}),
    
]
edge_labels = {
    (3, 2): 19,
    (3, 1): 7,
    (1, 2): 9,
}


G = nx.Graph()
for i in range(1, 5):
    G.add_node(i)
G.add_edges_from(edges)

pos = nx.planar_layout(G)

# This will give us all the shortest paths from node 1 using the weights from the edges.
p1 = nx.shortest_path(G, source=3, weight="weight")

# This will give us the shortest path from node 1 to node 6.
p1to6 = nx.shortest_path(G, source=3, target=2, weight="weight")

# This will give us the length of the shortest path from node 1 to node 6.
length = nx.shortest_path_length(G, source=3, target=2, weight="weight")

print("All shortest paths from 1: ", p1)
print("Shortest path from 1 to 6: ", p1to6)
print("Length of the shortest path: ", length)