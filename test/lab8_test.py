import sys
import os
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.lab8 import load_network_data, calculate_optimal_cable_length


class TestTelecomNetwork(unittest.TestCase):

    def test_load_network_data(self):
        test_csv_path = os.path.join(SCRIPT_DIR, "../src/communication_wells.csv")
        network = load_network_data(test_csv_path)
        connections = network.list_all_connections()
        first_connection = connections[0]
        self.assertEqual(len(first_connection), 3)

    def test_optimal_cable_length(self):
        test_csv_path = os.path.join(SCRIPT_DIR, "../src/communication_wells.csv")
        network = load_network_data(test_csv_path)
        min_cable_length = calculate_optimal_cable_length(network)
        self.assertEqual(min_cable_length, 8000)  # Перевірте чи це очікувана довжина

    def test_unconnected_network(self):
        test_csv_path = os.path.join(SCRIPT_DIR, "../src/unconnected_wells.csv")
        network = load_network_data(test_csv_path)
        min_cable_length = calculate_optimal_cable_length(network)
        self.assertEqual(min_cable_length, -1)


if __name__ == '__main__':
    unittest.main()
