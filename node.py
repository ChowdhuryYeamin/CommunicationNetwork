class Node:
    def __init__(self, id, energy, packets_to_send):
        self.id = id
        self.energy = energy
        self.packets_to_send = packets_to_send
        self.connections = {}

    def add_connection(self, other_node, distance):
        self.connections[other_node.id] = (other_node, distance)

    def get_connection_distance(self, other_node):
        return self.connections[other_node.id][1]

    def send_packet(self, other_node, energy_cost):
        if self.energy >= energy_cost:
            self.energy -= energy_cost
            other_node.receive_packet(self, energy_cost)
        else:
            print(f"Node {self.id} does not have enough energy to send a packet to node {other_node.id}.")

    def receive_packet(self, other_node, energy_cost):
        self.energy -= energy_cost

    def is_alive(self):
        return self.energy > 0
