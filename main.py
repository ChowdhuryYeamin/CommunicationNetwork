from node import Node
from graph import Graph

def main():

    number_of_nodes = int(input())
    for i in range(0, number_of_nodes):
        node_id, energy, packets_to_send = input().split()
        while len(node_id) == 0 or len(energy) == 0 or len(packets_to_send) == 0:
            node_id, energy, packets_to_send = input().split()
        energy = int(energy)
        packets_to_send = int(packets_to_send)
        graph.add_node(node_id, energy, packets_to_send)
   

    number_of_edges = int(input())
    while number_of_edges < number_of_nodes - 1:
        number_of_edges = int(input())


    for i in range(0, number_of_edges):
        node1_id, node2_id, distance = input().split()
        while len(node1_id) == 0 or len(node2_id) == 0 or len(distance) == 0:
            node1_id, node2_id, distance = input().split()
        distance = int(distance)
        graph.add_edge(node1_id, node2_id, distance)

    #accoridng to the most energy, sorts the nodes in descending order
    #according to the list of energy, gets the ids of the nodes in order

    list_of_order = []
    for node in graph.nodes:
        list_of_order.append(graph.nodes[node])
   
    list_of_order.sort(key=lambda x: x.energy, reverse=True)
    list_of_order = [node.id for node in list_of_order]


     
if __name__ == "__main__":
    main()