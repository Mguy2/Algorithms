from typing import List, Tuple

def shortest_path(start_id: int, end_id: int,data: List[Tuple[int, int, List[int]]]) -> List[int]:
    data = {key: (item1, item2) for key, item1, item2 in data}; short_p = {c_id: [] for c_id in data.keys()}
    short_p[start_id] = [start_id]; qu = [start_id];
    while qu:
        current_id = qu.pop(0)
        short_p.update({c_id: short_p[current_id] + [c_id] for c_id in data[current_id][1] if not short_p[c_id] and qu.append(c_id).__dir__()})
    return short_p[end_id]