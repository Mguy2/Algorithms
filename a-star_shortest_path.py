from typing import List, Tuple, Dict, Callable
from math import sqrt

class Graph:
    def __init__(self):
        self.nodes: Dict[Tuple[int, int], int] = {}
        self.edges: Dict[Tuple[int, int], Dict[Tuple[int, int], int]] = {}
        self.max: List[Tuple[Tuple[int, int], int]] = [((0, 0), 0), ((0, 0), 0)]

    def add_node(self, node_id: Tuple[int, int], weight: int):
        self.nodes[node_id] = weight
        if weight > self.max[0][1]:
            self.max = [(node_id, weight), self.max[0]]
        elif weight > self.max[1][1]:
            self.max[1] = (node_id, weight)

    def add_edge(self, source_id: Tuple[int, int], end_id: Tuple[int, int], cost: int):
        if source_id not in self.edges:
            self.edges[source_id] = {}
        self.edges[source_id][end_id] = cost
        if end_id not in self.edges:
            self.edges[end_id] = {}
        self.edges[end_id][source_id] = cost

    def astar_shortest_path(self, source_id: Tuple[int, int], end_id: Tuple[int, int], heuristic: Callable):
        open_set = [(0, source_id)]
        hist = {}
        g_score = {source_id: 0}
        while open_set:
            f_score, current_node = min(open_set, key=lambda x: x[0])
            if current_node == end_id:
                path, node = [current_node], current_node
                while node in hist:
                    node = hist[node]
                    path.insert(0, node)
                return path
            open_set.remove((f_score, current_node))
            for neighbor, cost in self.edges[current_node].items():
                tentative_g = g_score[current_node] + cost
                if tentative_g < g_score.get(neighbor, float("inf")):
                    hist[neighbor] = current_node
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, end_id)
                    open_set.append((f_score, neighbor))

def heuristic(u: Tuple[int, int], v: Tuple[int, int]) -> float:
    return ((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2) ** 0.5

def shortest_path(nodes_l: List[Tuple[Tuple[int, int], int]], edges_l: List[Tuple[Tuple[int, int], Tuple[int, int], int]]) -> List[Tuple[int, int]]:
    graph = Graph()
    for node, weight in nodes_l:
        graph.add_node(node, weight)
    for source, end, cost in edges_l:
        graph.add_edge(source, end, cost)
    start, end = graph.max[0][0], graph.max[1][0]
    path = graph.astar_shortest_path(start, end, heuristic)
    return path
