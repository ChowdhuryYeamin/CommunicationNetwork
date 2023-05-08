import sys
import timeit
import networkx as nx
import matplotlib.pyplot as plt
from random import randint

# Define function to generate a random graph
def generate_random_graph(num_nodes, num_edges):
    G = nx.Graph()
    nodes = range(1, num_nodes+1)
    G.add_nodes_from(nodes)
    while G.number_of_edges() < num_edges:
        node1 = randint(1, num_nodes)
        node2 = randint(1, num_nodes)
        if node1 != node2:
            weight = randint(1, 10)
            G.add_edge(node1, node2, weight=weight)
    return G

# Define function to compute energy of a graph
def compute_energy(G):
    energy = 0
    for node1, node2 in G.edges():
        weight = G[node1][node2]['weight']
        energy += weight
    return energy

# Generate a random graph
num_nodes = 10
num_edges = 20
G = generate_random_graph(num_nodes, num_edges)

# Compute energy of initial graph
initial_energy = compute_energy(G)
print("Initial Energy: ", initial_energy)

# Run Brute Force Algorithm
start = timeit.default_timer()
brute_force_energy = sys.maxsize
for path in nx.all_simple_paths(G, source=1, target=num_nodes):
    path_energy = sum([G[path[i]][path[i+1]]['weight'] for i in range(len(path)-1)])
    if path_energy < brute_force_energy:
        brute_force_energy = path_energy
stop = timeit.default_timer()
print("Brute Force Energy: ", brute_force_energy)
print("Brute Force Time: ", stop - start)

# Run Dijkstra's Algorithm
start = timeit.default_timer()
dijkstra_energy = nx.shortest_path_length(G, source=1, target=num_nodes, weight='weight')
stop = timeit.default_timer()
print("Dijkstra's Energy: ", dijkstra_energy)
print("Dijkstra's Time: ", stop - start)

# Compute final energy of graph
final_energy = compute_energy(G)
print("Final Energy: ", final_energy)
