import networkx as nx
import random

# Step 1: Ask the user for the number of nodes
num_nodes = int(input("Enter the number of nodes: "))

# Step 2: Create a graph with the given number of nodes
G = nx.complete_graph(num_nodes)

# Step 3: Ask the user for the source and destination nodes
src = int(input("Enter the source node: "))
dest = int(input("Enter the destination node: "))

# Step 4: Initialize a timer variable
timer = 0

# Step 5: Start sending packets between the source and destination nodes
while True:
    # Step 6: Use a shortest path algorithm to find the shortest path
    try:
        path = nx.shortest_path(G, source=src, target=dest)
    except nx.NetworkXNoPath:
        print("No path exists between the source and destination nodes.")
        break
    
    # Step 7: If any node fails, try to reroute the packets
    for i in range(len(path)-1):
        u = path[i]
        v = path[i+1]
        if random.random() < 0.1:
            G.remove_edge(u, v)
            print("Edge ({}, {}) has failed.".format(u, v))
    
    # Step 8: Keep sending packets until the energy runs out
    if not nx.has_path(G, source=src, target=dest):
        print("No path exists between the source and destination nodes.")
        break
    
    # Step 9: Update the timer and continue sending packets
    timer += 1
    
print("The graph was online for {} seconds.".format(timer))
