#!/usr/bin/env python3
'''
Std. no: XXXXXXX
'''

from typing import List, Tuple

def min_spanning_tree(nodes_l, edges_l):
    edges_l.sort(key=lambda x: x[2])
    parent = list(range(len(nodes_l)))
    tree = []
    for edge in edges_l:
        u, v, weight = edge
        if parent[u-1] != parent[v-1]:
            tree.append((u, v, weight))
            old_parent, new_parent = parent[u-1], parent[v-1]
            for i in range(len(parent)):
                if parent[i] == old_parent:
                    parent[i] = new_parent
    return tree
