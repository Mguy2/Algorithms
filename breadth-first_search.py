from typing import List, Tuple

def BFS(start_id: int, end_id: int, data: List[Tuple[int, List[int]]]) -> List[List[int]]:
    paths = []; qu = [(start_id, [start_id])];
    while qu:
        current_id, path = qu.pop(0)
        if current_id == end_id: paths.append(path)
        else:
            connections = [adj_id for entry_id, connected_ids in data if entry_id == current_id for adj_id in connected_ids]
            for c_id in connections:
                if c_id not in path:
                    new_path = path + [c_id]; qu.append((c_id, new_path));
    return paths