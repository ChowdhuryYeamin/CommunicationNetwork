import random
import networkx as nx
import matplotlib.pyplot as plt

edges = [
    (0, 1, {"weight": 5}),
    (0, 2, {"weight": 5}),
    (1, 3, {"weight": 20}),
    (2, 3, {"weight": 20}),
    (0, 3, {"weight": 35}),
    
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

if nx.has_path(G, src_node, dest_node):
    H = G.copy()
    num_sent = 0
    
    while num_sent < num_packets :
        valid = True
        if nx.has_path(H, src_node, dest_node):
            path = nx.shortest_path(H, src_node, dest_node, weight="weight", method="dijkstra")
            for u, v in zip(path[:-1], path[1:]):
                print(u , v)
                if H.nodes[u]['energy'] < H[u][v]['weight']:
                    valid = False
                    print( H.nodes[u]['energy'])
                    print( H[u][v]['weight'])
                    print("removing edge" , u , v)
                    H.remove_edge(u , v)
                    break
                
            if valid == True:
                for u, v in zip(path[:-1], path[1:]):
                    H.nodes[u]['energy'] -= H[u][v]['weight']
                    print("energy " , u , ":", H.nodes[u]['energy'] )
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
    num_sent = 0
    
    while num_sent < num_packets:
        valid = True
        if nx.has_path(G, src_node, dest_node):
            paths = list(nx.all_simple_paths(G, source=src_node, target=dest_node))
            path = random.choice(paths) 

            for u, v in zip(path[:-1], path[1:]):
                print(u , v)
                if G.nodes[u]['energy'] <  G[u][v]['weight']:
                    valid = False
                    print( G.nodes[u]['energy'])
                    print( G[u][v]['weight'])
                    print("removing edge" , u , v)
                    G.remove_edge(u , v)
                    break

            if valid == True:
                for u, v in zip(path[:-1], path[1:]):
                    G.nodes[u]['energy'] -= G[u][v]['weight']
                    print("energy " , u , ":", G.nodes[u]['energy'] )
                num_sent += 1
                print(path)
        else:
            print("There is no path between the source and destination nodes.")
            break
else:
    print("There is no path between the source and destination nodes.")

            
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
    

               
    

