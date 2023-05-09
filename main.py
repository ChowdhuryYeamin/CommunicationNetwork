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
print(f"Total energy of nodes before sending packets: {total_energy_before} joules")


print("Dijkstra:\n")

if nx.has_path(G, src_node, dest_node):
    H = G.copy()
    num_sent = 0
    while H.nodes[src_node]['energy'] > 0 and num_sent < num_packets:
        if nx.has_path(H, src_node, dest_node):
            path = nx.shortest_path(H, src_node, dest_node, weight="weight", method="dijkstra")
            for u, v in zip(path[:-1], path[1:]):
                w = H.nodes[u]['energy'] - H[u][v]['weight']
                
                if w < 0:
                    H.remove_edge(u , v)
                    break
                else:
                    H.nodes[u]['energy'] -= H[u][v]['weight']
            else:
                num_sent += 1
                print(path)
        else:
            print("There is no path between the source and destination nodes.")
            break
else:
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

# Step 7: Display the final graph with node energies as labels
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
node_energy = nx.get_node_attributes(G, 'energy')
nx.draw_networkx_labels(G, pos, labels={n: f"Energy: {node_energy[n]}" for n in G.nodes()}, font_color='red')

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()


print("Greedy:\n")

if nx.has_path(G, src_node, dest_node):
   
    paths = list(nx.all_simple_paths(G, source=src_node, target=dest_node))
    num_sent = 0
    while G.nodes[src_node]['energy'] > 0 and num_sent < num_packets:
        if nx.has_path(G, src_node, dest_node):
            path = random.choice(paths) 
            current_path = path
            for u, v in zip(path[:-1], path[1:]):
                w = G.nodes[u]['energy'] - G[u][v]['weight']
                
                if w < 0:
                    G.remove_edge(u , v)
                    paths = [p for p in nx.all_simple_paths(G, source=src_node, target=dest_node) if p != path]

                    break
                else:
                    G.nodes[u]['energy'] -= H[u][v]['weight']
            else:
                num_sent += 1
                print(path)
        else:
            print("There is no path between the source and destination nodes.")
            break
else:
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
    

               
    

