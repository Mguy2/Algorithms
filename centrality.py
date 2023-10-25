from typing import List, Tuple, Dict

class Graph:
    def __init__(self):
        self.nodes: List[int] = []
        self.edges: Dict[int, Dict[int, int]] = {}

    def add_node(self, node_id):
        if node_id not in self.nodes:
            self.nodes.append(node_id)
            self.edges[node_id] = {}

    def add_edge(self, source_id, end_id, cost):
        if source_id in self.nodes and end_id in self.nodes:
            self.edges[source_id][end_id] = cost
            self.edges[end_id][source_id] = cost

def betweenness_centrality(graph: Graph):
    pivot = -1
    mcn = 0
    for n in graph.nodes:
        centrality = 0
        if centrality > pivot:
            pivot = centrality
            mcn = n
    return mcn

def most_central(nodes_l, edges_l):
    G = Graph()
    for node in nodes_l:
        G.add_node(node)
    for node1, node2, c in edges_l:
        G.add_edge(node1, node2, c)
    return betweenness_centrality(G)