import random
import networkx as nx
import matplotlib.pyplot as plt

# Step 2: Create a graph with random edges
num_nodes = int(input("Enter the number of nodes: "))
G = nx.Graph()
for i in range(1, num_nodes+1):
    G.add_node(i, energy=200)
for i in range(1, num_nodes+1):
    for j in range(i+1, num_nodes+1):
        if random.random() < 0.5:
            weight = random.randint(5, 20)
            G.add_edge(i, j, weight=weight)

# Step 3: Display the initial graph with node energies as labels
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
node_energy = nx.get_node_attributes(G, 'energy')
nx.draw_networkx_labels(G, pos, labels={n: f"Energy: {node_energy[n]}" for n in G.nodes()}, font_color='red')

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

# Step 4: Ask the user for the source and destination nodes and the number of packets to send
src_node = int(input("Enter the source node: "))
dest_node = int(input("Enter the destination node: "))
num_packets = int(input("Enter the number of packets to send: "))

# Print total energy of nodes before sending packets
total_energy_before = sum(node_energy.values())
print(f"Total energy of nodes before sending packets: {total_energy_before}")

# Send packets between src and dest
H = G.copy()
path_true = True
path = [src_node]
num_sent = 0
while path[-1] != dest_node and len(path) > 0:
    curr_node = path[-1]
    outgoing_edges = H.edges(curr_node)
    if len(outgoing_edges) > 0:
        chosen_edge = None
        chosen_edge_weight = float('inf')
        for u, v in outgoing_edges:
            edge_weight = H[u][v]['weight']
            if edge_weight < chosen_edge_weight:
                chosen_edge = (u, v)
                chosen_edge_weight = edge_weight
        if chosen_edge_weight < float('inf'):
            path.append(chosen_edge[1])
            H.nodes[chosen_edge[0]]['energy'] -= chosen_edge_weight
            H[chosen_edge[0]][chosen_edge[1]]['weight'] = 100000
            num_sent += 1
        else:
            path.pop()
    else:
        path.pop()

if path[-1] == dest_node:
    print(path)
else:
    print("There is no path between the source and destination nodes.")

# Calculate total energy after sending packets
node_energy = nx.get_node_attributes(H, 'energy')
total_energy_after = sum(node_energy.values())
print(f"Total energy of nodes after sending packets: {total_energy_after}")

print("Packets sent before all paths with available energy are exhausted:", num_sent)

# Step 7: Display the final graph with node energies as labels
pos = nx.spring_layout(H)
nx.draw(H, pos, with_labels=True, font_weight='bold')
node_energy = nx.get_node_attributes(H, 'energy')
nx.draw_networkx_labels(H, pos, labels={n: f"Energy: {node_energy[n]}" for n in H.nodes()}, font_color='red')

edge_labels = nx.get_edge_attributes(H, 'weight')
nx.draw_networkx_edge_labels(H, pos, edge_labels=edge_labels)
plt.show()