from typing import List, Union

def is_min_heap(array: List[int]) -> Union[int, bool]:
    n = len(array)
    for i in range(n):
        if 2 * i + 1 < n and array[2 * i + 1] < array[i] or 2 * i + 2 < n and array[2 * i + 2] < array[i]:
            return False
    return True
