from typing import List

def binary_search(a: List[int], n: int) -> int: #Victory
    l_len = (len(a) - 1); mid = l_len // 2; look_in = (0, l_len);
    while True:
        if mid <= 1: return 0;
        elif a[mid] == n:
            return mid
        elif a[mid] < n: look_in = (mid + 1, look_in[1]);
        elif a[mid] > n: look_in = (look_in[0], mid);
        mid = ((look_in[1] + look_in[0]) // 2)