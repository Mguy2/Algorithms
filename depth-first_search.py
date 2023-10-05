from typing import List, Tuple

def dfs(start_id: int, end_id: int, data: List[Tuple[int, List[int]]]) -> List[int]:
    seen = set(); stack = [(start_id, [start_id])]; data = {key: item for key, item in data}
    while stack:
        check, path = stack.pop()
        if check == end_id: return path
        if check not in seen: stack.extend([(c_id, path + [c_id]) for c_id in data.get(check, []) if c_id not in seen.add(check).__dir__()])
