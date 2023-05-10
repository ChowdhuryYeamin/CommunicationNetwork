import random
import networkx as nx
import matplotlib.pyplot as plt


def create_graph():
    # Step 2: Create a graph with random edges
    num_nodes = int(input("Enter the number of nodes: "))
    G = nx.DiGraph()
    for i in range(1, num_nodes+1):
        G.add_node(i, energy=200)
    for i in range(1, num_nodes+1):
        for j in range(i+1, num_nodes+1):
            if random.random() < 0.5:
                weight = random.randint(5, 20)
                G.add_edge(i, j, weight=weight, directed=True)

    return G

    

def display_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    node_energy = nx.get_node_attributes(G, 'energy')
    nx.draw_networkx_labels(G, pos, labels={n: f"Energy: {node_energy[n]}" for n in G.nodes()}, font_color='red')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

def Dijkstra(G, src_node , dest_node , num_packets):
    
    print("\nDijkstra:\n")
    total_energy_before = sum(nx.get_node_attributes(G, 'energy').values())
    print(f"Total energy of nodes before sending packets: {total_energy_before} joules")

    node_energy = nx.get_node_attributes(G, 'energy')
    print("Energies at nodes:" , node_energy)

    if nx.has_path(G, src_node, dest_node):
        H = G.copy()
        num_sent = 0
        
        print("\n")
        while num_sent < num_packets :
            valid = True
            if nx.has_path(H, src_node, dest_node):
                path = nx.shortest_path(H, src_node, dest_node, weight="weight", method="dijkstra")
                
                for u, v in zip(path[:-1], path[1:]):
                    
                    if H.nodes[u]['energy'] < H[u][v]['weight']:
                        valid = False
                        print("\nEnergy available at" , u,  ":" , H.nodes[u]['energy'])
                        print("Energy required for " , u,  "to " , v , ":" , H[u][v]['weight'])
                        print("Thus removing edge" , u , v)
                        print("\n")
                        H.remove_edge(u , v)
                        break
                    
                if valid == True:
                    num_sent += 1
                    print("Path taken by packet ", num_sent , ":" ,path)
                    for u, v in zip(path[:-1], path[1:]):
                        
                        H.nodes[u]['energy'] -= H[u][v]['weight']
                        print("Energy " , u , ":", H.nodes[u]['energy'] , "     Energy required to send packet from" , u , "to" , v , ":" , H[u][v]['weight'] )
                        
                    
            else:
                print("There is no path between the source and destination nodes.\n")
                break
    else:
        print("There is no path between the source and destination nodes.\n")
    
    node_energy = nx.get_node_attributes(H, 'energy')
    total_energy_after = sum(node_energy.values())
    print(f"\nTotal energy of nodes after sending packets: {total_energy_after} joules")

    print("Packets sent before all paths with avaiable energy is exhausted:" , num_sent)
    display_graph(H)

def nonOptimal(G, src_node , dest_node , num_packets):
    print("\nNon-Optimal:\n")

    total_energy_before = sum(nx.get_node_attributes(G, 'energy').values())
    print(f"Total energy of nodes before sending packets: {total_energy_before} joules")

    node_energy = nx.get_node_attributes(G, 'energy')
    print("Energies at nodes:" , node_energy)
    print("\n")

           
    if nx.has_path(G, src_node, dest_node):
        num_sent = 0
        
        while num_sent < num_packets:
            valid = True
            if nx.has_path(G, src_node, dest_node):
                paths = list(nx.all_simple_paths(G, source=src_node, target=dest_node))
                path = random.choice(paths) 

                for u, v in zip(path[:-1], path[1:]):
              
                    if G.nodes[u]['energy'] <  G[u][v]['weight']:
                        valid = False
                        print("\nEnergy available at" , u,  ":" , G.nodes[u]['energy'])
                        print("Energy required for " , u,  "to " , v , ":" , G[u][v]['weight'])
                        print("Thus removing edge" , u , v)
                        print("\n")
                        G.remove_edge(u , v)
                        break

                if valid == True:
                    num_sent += 1
                    print("Path taken by packet ", num_sent , ":" ,path)
                    for u, v in zip(path[:-1], path[1:]):
                        G.nodes[u]['energy'] -= G[u][v]['weight']
                        print("Energy " , u , ":", G.nodes[u]['energy'] , "     Energy required to send packet from" , u , "to" , v , ":" , G[u][v]['weight'] )
                    
            else:
                print("There is no path between the source and destination nodes.")
                break
    else:
        print("There is no path between the source and destination nodes.")
    
    display_graph(G)

                
    node_energy = nx.get_node_attributes(G, 'energy')
    total_energy_after = sum(node_energy.values())
    print(f"\nTotal energy of nodes after sending packets: {total_energy_after} joules")

    print("Packets sent before all paths with avaiable energy is exhausted:" , num_sent)


if __name__ == '__main__':
    G = create_graph()
    display_graph(G)

    # Step 4: Ask the user for the source and destination nodes and the number of packets to send
    src_node = int(input("Enter the source node: "))
    dest_node = int(input("Enter the destination node: "))
    num_packets = int(input("Enter the number of packets to send: "))

    if not nx.has_path(G, src_node, dest_node):
        print("There is no path between the source and destination nodes. Please choose another path")
        src_node = int(input("Enter the source node: "))
        dest_node = int(input("Enter the destination node: "))
        num_packets = int(input("Enter the number of packets to send: "))

    Dijkstra(G , src_node , dest_node , num_packets)
    
    display_graph(G)
    nonOptimal(G , src_node , dest_node , num_packets)