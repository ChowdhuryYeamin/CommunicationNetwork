import random
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Ask the user for the number of nodes
num_nodes = int(input("Enter the number of nodes: "))

# Step 2: Create a directed graph with the given number of nodes
G = nx.DiGraph()
F = nx.DiGraph()

# Add nodes to the graph with energy levels of 200
for i in range(num_nodes):
    G.add_node(i, energy=200)
    F.add_node(i, energy=200)
   
# Add edges to the graph with random weights between 5 and 20
for u in range(num_nodes):
    for v in range(num_nodes):
        if u != v and random.random() < 0.5:
            w = random.randint(5, 20)
            G.add_edge(u, v, weight=w)
            F.add_edge(u, v, weight=w)


# Step 3: Display the initial graph with node energies as labels
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
node_energy = nx.get_node_attributes(G, 'energy')
nx.draw_networkx_labels(G, pos, labels={n: f"Energy: {node_energy[n]}" for n in G.nodes()}, font_color='red')

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()


pos = nx.spring_layout(F)
nx.draw(F, pos, with_labels=True, font_weight='bold')
node_energy = nx.get_node_attributes(F, 'energy')
nx.draw_networkx_labels(F, pos, labels={n: f"Energy: {node_energy[n]}" for n in F.nodes()}, font_color='red')

edge_labels = nx.get_edge_attributes(F, 'weight')
nx.draw_networkx_edge_labels(F, pos, edge_labels=edge_labels)
plt.show()

# Step 4: Ask the user for the source and destination nodes and the number of packets to send
src_node = int(input("Enter the source node: "))
dest_node = int(input("Enter the destination node: "))
num_packets = int(input("Enter the number of packets to send: "))

# Check if the source node has any outgoing edges
if not list(G.successors(src_node)):
    raise ValueError(f"Node {src_node} does not have any outgoing edges.")

# Step 5: Send packets from source to destination
energy_remaining = sum(nx.get_node_attributes(G, 'energy').values())
for i in range(num_packets):
    current_node = src_node
    path = [src_node]
    while current_node != dest_node:
        neighbors = list(G.successors(current_node))
        if not neighbors:
            break
        next_node = random.choice(neighbors)
        energy = G[current_node][next_node]['weight']
        if G.nodes[current_node]['energy'] >= energy:
            G.nodes[current_node]['energy'] -= energy
            current_node = next_node
            path.append(current_node)
    energy_remaining = sum(nx.get_node_attributes(G, 'energy').values())
    if energy_remaining <= 0:
        break
    print(f"Packet {i+1}: {path}")

# Step 6: Remove nodes with zero energy from the graph
G.remove_nodes_from([n for n, d in G.nodes(data=True) if d['energy'] <= 0])

# Step 7: Display the final graph with node energies as labels
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
node_energy = nx.get_node_attributes(G, 'energy')
nx.draw_networkx_labels(G, pos, labels={n: f"Energy: {node_energy[n]}" for n in G.nodes()}, font_color='red')

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()


pos = nx.spring_layout(F)
nx.draw(F, pos, with_labels=True, font_weight='bold')
node_energy = nx.get_node_attributes(F, 'energy')
nx.draw_networkx_labels(F, pos, labels={n: f"Energy: {node_energy[n]}" for n in F.nodes()}, font_color='red')

edge_labels = nx.get_edge_attributes(F, 'weight')
nx.draw_networkx_edge_labels(F, pos, edge_labels=edge_labels)
plt.show()

# Step 8: Display the total energy before and after sending the packets
print(f"Total energy before sending packets: {num_nodes*200}")
# Step 8: Display the total energy before and after sending the packets
energy_remaining = sum(nx.get_node_attributes(G, 'energy').values())
print(f"Total energy after sending packets: {energy_remaining}")



shortest_path = nx.shortest_path(F, source=src_node, target=dest_node, weight='weight')
for i in range(num_packets):
    current_node = src_node
    path = [src_node]
    for next_node in shortest_path[1:]:
        energy = F[current_node][next_node]['weight']
        if F.nodes[current_node]['energy'] >= energy:
            F.nodes[current_node]['energy'] -= energy
            current_node = next_node
            path.append(current_node)
        else:
            break
    else:
        # If the loop completed without hitting the "break" statement, the packet has reached its destination
        print(f"Packet {i+1}: {path}")
    energy_remaining = sum(nx.get_node_attributes(F, 'energy').values())
    if energy_remaining <= 0:
        break

# Step 6: Remove nodes with zero energy from the graph
F.remove_nodes_from([n for n, d in F.nodes(data=True) if d['energy'] <= 0])

# Step 7: Display the final graph with node energies as labels
pos = nx.spring_layout(F)
nx.draw(F, pos, with_labels=True, font_weight='bold')
node_energy = nx.get_node_attributes(F, 'energy')
nx.draw_networkx_labels(F, pos, labels={n: f"Energy: {node_energy[n]}" for n in F.nodes()}, font_color='red')

edge_labels = nx.get_edge_attributes(F, 'weight')
nx.draw_networkx_edge_labels(F, pos, edge_labels=edge_labels)
plt.show()

# Step 8: Display the total energy before and after sending the packets
print(f"Total energy before sending packets: {num_nodes*200}")
# Step 8: Display the total energy before and after sending the packets
energy_remaining = sum(nx.get_node_attributes(F, 'energy').values())
print(f"Total energy after sending packets: {energy_remaining}")