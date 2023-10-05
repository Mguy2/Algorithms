from typing import Optional, List, Tuple, Union

def bubble_sort(data):
    output = list()
    success = 0
    while not success:
        success = 1
        for index, entry in enumerate(data):
            if entry[1] + entry[2] < data[index - 1][1] + data[index - 1][2] and index >= 1:
                data[index] = data[index - 1]
                data[index - 1] = entry
                success = 0
                output = list()
            if success:
                output.append(int(entry[0]))
    return output