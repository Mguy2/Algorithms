from typing import Optional, List, Tuple, Union

def merge_sort(data):
    def quicksort(array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[0]
            left = [x for x in array[1:] if x[1] + x[2] < pivot[1] + pivot[2]]
            right = [x for x in array[1:] if x[1] + x[2] >= pivot[1] + pivot[2]]
            return quicksort(left) + [pivot] + quicksort(right)
    result = quicksort(data)
    return [x[0] for x in result]