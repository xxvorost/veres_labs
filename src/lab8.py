import csv


class TelecomNetwork:
    def __init__(self):
        self.network_nodes = {}
        self.component_size = {}
        self.network_edges = []

    def add_well_connection(self, well1, well2, distance):
        if well1 not in self.network_nodes:
            self.network_nodes[well1] = well1
            self.component_size[well1] = 0
        if well2 not in self.network_nodes:
            self.network_nodes[well2] = well2
            self.component_size[well2] = 0
        self.network_edges.append((well1, well2, distance))

    def locate_supervisor(self, well):
        if self.network_nodes[well] != well:
            self.network_nodes[well] = self.locate_supervisor(self.network_nodes[well])
        return self.network_nodes[well]

    def connect_wells(self, well1, well2):
        leader1 = self.locate_supervisor(well1)
        leader2 = self.locate_supervisor(well2)

        if leader1 != leader2:
            if self.component_size[leader1] < self.component_size[leader2]:
                self.network_nodes[leader1] = leader2
            elif self.component_size[leader1] > self.component_size[leader2]:
                self.network_nodes[leader2] = leader1
            else:
                self.network_nodes[leader1] = leader2
                self.component_size[leader2] += 1

    def list_all_connections(self):
        return self.network_edges

    def are_all_wells_connected(self):
        supervisors = set(self.locate_supervisor(well) for well in self.network_nodes)
        return len(supervisors) == 1


def calculate_optimal_cable_length(network):
    all_connections = sorted(network.list_all_connections(), key=lambda con: con[2])
    optimal_connections = []

    for connection in all_connections:
        well1, well2, distance = connection
        if network.locate_supervisor(well1) != network.locate_supervisor(well2):
            optimal_connections.append(connection)
            network.connect_wells(well1, well2)

    total_cable_length = sum(distance for _, _, distance in optimal_connections)
    return total_cable_length if network.are_all_wells_connected() else -1


def load_network_data(filepath):
    network = TelecomNetwork()
    with open(filepath, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            if len(row) == 3:
                well1, well2, distance = row
                network.add_well_connection(well1, well2, int(distance))

    return network
