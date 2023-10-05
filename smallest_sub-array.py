from typing import List

def smallest_subarray_length(a: List[int], k: int) -> int:
    a = sorted(a)[::-1]; s = 0
    for i, x in enumerate(a):
        s += x
        if s > k: i += 1; return i
    return 0