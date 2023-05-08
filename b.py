import random
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Ask the user for the number of nodes
num_nodes = int(input("Enter the number of nodes: "))

# Step 2: Create a graph with random edges
G = nx.DiGraph()
for i in range(1, num_nodes+1):
    G.add_node(i, energy=200)
for i in range(1, num_nodes+1):
    for j in range(1, num_nodes+1):
        if i != j and random.random() < 0.5:
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
for i in range(num_packets):
    path = nx.shortest_path(G, src_node, dest_node, weight="weight", method="dijkstra")
    for j in range(len(path)-1):
        u, v = path[j], path[j+1]
        if G.nodes[u]['energy'] - G[u][v]['weight'] < 0:
            # Avoid the node with zero energy by setting the weights of all outgoing edges to infinity
            for x in G.successors(u):
                G[u][x]['weight'] = 100000000
            print(f"Node {u} has run out of energy and will be avoided.")
            break
        else:
            print(u , " -> " , v , " : " , G[u][v]['weight'])
            G.nodes[u]['energy'] -= G[u][v]['weight']
    else:
        # Packet reached destination successfully
        print(f"Packet {i+1} reached the destination through path {path}")
        continue

    # Packet encountered a node with zero energy and did not reach destination
    print(f"Packet {i+1} encountered a node with zero energy and could not reach the destination.")

node_energy = nx.get_node_attributes(G, 'energy')
total_energy_after = sum(node_energy.values())
print(f"Total energy of nodes after sending packets: {total_energy_after}")

# Step 7: Display the final graph with node energies as labels
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
node_energy = nx.get_node_attributes(G, 'energy')
nx.draw_networkx_labels(G, pos, labels={n: f"Energy: {node_energy[n]}" for n in G.nodes()}, font_color='red')

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
