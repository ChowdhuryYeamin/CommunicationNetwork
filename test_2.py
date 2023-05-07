import networkx as nx
import random
import matplotlib.pyplot as plt
import time

# Step 1: Ask the user for the number of nodes
num_nodes = int(input("Enter the number of nodes: "))


G = nx.complete_graph(num_nodes)
for i in range(num_nodes):
    G.add_node(i, energy=200, packets_to_send=0, packets_received=0)

#Ask the user for source and destination nodes
src = int(input("Enter the source node: "))
dest = int(input("Enter the destination node: "))
#ask the user for the number of packets to send and set the packets_to_send property of the source node to that number
num_packets = int(input("Enter the number of packets to send: "))
G.nodes[src]["packets_to_send"] = num_packets

# Step 4: Initialize a timer variable
timer = 0


while True:
    # Step 6: Use a shortest path algorithm to find the shortest path
    try:
        path = nx.shortest_path(G, source=src, target=dest, method="dijkstra")
        #print each node in the path
        print("The path is: ")
        for i in range(len(path)):
            print(path[i])

    except nx.NetworkXNoPath:
        print("No path exists between the source and destination nodes.")
        break
    
    # Step 7: If any node fails, try to reroute the packets
    # for i in range(len(path)-1):
    #     u = path[i]
    #     v = path[i+1]
    #     if random.random() < 0.1:
    #         G.remove_edge(u, v)
    #         print("Edge ({}, {}) has failed.".format(u, v))

    #if any node in the path has energy == 0 or energy < 20, remove the node from the graph and print the node id
    for i in range(len(path)):
        u = path[i]
        if G.nodes[u]["energy"] == 0 or G.nodes[u]["energy"] < 20:
            G.remove_node(u)
            print("Node {} has failed.".format(u))
            

    
    # Step 8: Keep sending packets until the energy runs out
    if not nx.has_path(G, source=src, target=dest):
        print("No path exists between the source and destination nodes.")
        break
    
    # Step 9: Update the timer and continue sending packets
    timer += 1
    for i in range(len(path)-1):
        u = path[i]
        v = path[i+1]
        G.nodes[u]["energy"] -= 20
        G.nodes[u]["packets_to_send"] -= 1
        G.nodes[v]["energy"] -= 20
        G.nodes[v]["packets_received"] += 1
        for j in range(i+2, len(path)):
            w = path[j]
            G.nodes[w]["energy"] -= 20
            
   



    
    # Step 10: Draw the graph with the packets being sent between the nodes
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    labels = {(i, j): random.randint(1, 100) for i in range(num_nodes) for j in range(num_nodes) if i != j}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Time: {} seconds".format(timer))
    plt.pause(0.5)
    plt.clf()
    

