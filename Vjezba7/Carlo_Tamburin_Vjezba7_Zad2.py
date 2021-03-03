from time import perf_counter
from math import sqrt
import networkx as nx
import time


class aStarAlgorithm:
    def __init__(self, coords_dict, start_air, end_air):
        self.coords_dict = coords_dict
        self.start_air = start_air
        self.end_air = end_air

    def heuristic(self, coords1, coords2):
        (x1, y1) = self.coords_dict[coords1]
        (x2, y2) = self.coords_dict[coords2]

        distance = sqrt(pow(x1-y1, 2) + pow(x2-y2, 2))
        return distance

    def a_star(self):
        start = time.time()
        graph = nx.read_pajek("airports-astar.net")
        nx.set_node_attributes(graph, self.coords_dict, "coordinates")

        path = nx.astar_path(graph, self.start_air,
                             self.end_air, heuristic=self.heuristic)
        distance = nx.astar_path_length(
            graph, self.start_air, self.end_air, self.heuristic)

        end = time.time()
        completionTime = end-start

        return path, distance, completionTime
