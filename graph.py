
from node import Node
import heapq


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, id, energy, packets_to_send):
        self.nodes[id] = Node(id, energy, packets_to_send)

    def add_edge(self, node1_id, node2_id, distance):
        self.nodes[node1_id].add_connection(self.nodes[node2_id], distance)
        self.nodes[node2_id].add_connection(self.nodes[node1_id], distance)

    def remove_node(self, node_id):
        self.nodes.pop(node_id)
        for node in self.nodes:
            self.nodes[node].remove_connection(self.nodes[node_id])

    def send_packet(self, start_id, end_id):
        path = self.get_shortest_path(start_id, end_id)
        for i in range(len(path) - 1):
            self.nodes[path[i]].send_packet(self.nodes[path[i + 1]])
