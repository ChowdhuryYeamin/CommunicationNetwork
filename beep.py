import random
import networkx as nx
import matplotlib.pyplot as plt

edges = [
    (0, 1, {"weight": 5}),
    (0, 2, {"weight": 5}),
    (1, 3, {"weight": 20}),
    (2, 3, {"weight": 20}),
    
]

G = nx.Graph()
for i in range(0,4):
    G.add_node(i, energy=200)
G.add_edges_from(edges)

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
print(f"Total energy of nodes before sending packets: {total_energy_before} joules")


print("Dijkstra:\n")
H = G.copy()
path_true = True
num_sent = 0

while num_packets > num_sent and nx.has_path(H, src_node, dest_node):
    path = nx.shortest_path(H, src_node, dest_node, weight="weight", method="dijkstra")
    for j in range(len(path)-1):
        u, v = path[j], path[j+1]
        H.nodes[u]['energy'] -= H[u][v]['weight']
        if H.nodes[u]['energy'] < 0:
            path_true = False
            H.nodes[u]['energy'] += H[u][v]['weight']
            H[u][v]['weight'] = 100000
            break
    if path_true:
        num_sent += 1
        print(path)
    else:
        path_true = True

if num_sent == 0:
    print("There is no path between the source and destination nodes.")

node_energy = nx.get_node_attributes(H, 'energy')
total_energy_after = sum(node_energy.values())
print(f"Total energy of nodes after sending packets: {total_energy_after} joules")

print("Packets sent before all paths with avaiable energy is exhausted:" , num_sent)
# Step 7: Display the final graph with node energies as labels
pos = nx.spring_layout(H)
nx.draw(H, pos, with_labels=True, font_weight='bold')
node_energy = nx.get_node_attributes(H, 'energy')
nx.draw_networkx_labels(H, pos, labels={n: f"Energy: {node_energy[n]}" for n in H.nodes()}, font_color='red')

edge_labels = nx.get_edge_attributes(H, 'weight')
nx.draw_networkx_edge_labels(H, pos, edge_labels=edge_labels)
plt.show()


print("Greedy:\n")


if nx.has_path(G, src_node, dest_node):
    paths = list(nx.all_simple_paths(G, source=src_node, target=dest_node))
    num_sent = 0
    while G.nodes[src_node]['energy'] > 0 and num_sent < num_packets:
        path = random.choice(paths)
        for u, v in zip(path[:-1], path[1:]):
            G.nodes[u]['energy'] -= G[u][v]['weight']
            if G.nodes[u]['energy'] < 0:
                for x, y in zip(path[:-1], path[1:]):
                    G.nodes[x]['energy'] += G[x][y]['weight']
                break
        else:
            num_sent += 1
            print(path)

    node_energy = nx.get_node_attributes(G, 'energy')
    total_energy_after = sum(node_energy.values())
    print(f"Total energy of nodes after sending packets: {total_energy_after} joules")

    print("Packets sent before all paths with avaiable energy is exhausted:" , num_sent)
    # Step 7: Display the final graph with node energies as labels
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    node_energy = nx.get_node_attributes(G, 'energy')
    nx.draw_networkx_labels(G, pos, labels={n: f"Energy: {node_energy[n]}" for n in G.nodes()}, font_color='red')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
else:
    print("There is no path between the source and destination nodes.")

               
    

