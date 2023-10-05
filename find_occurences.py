from typing import List

def find_occurrences(a: List[int], n: int) -> int: #Victory
    l_len = (len(a) - 1); mid = l_len // 2; look_in = (0, l_len);
    while True:
        if mid <= 1: return 0;
        elif a[mid] == n:
            x = 0; y = 0
            while a[mid + x] == n: x += 1;
            while a[mid - y] == n: y += 1;
            return x + y - 1
        elif a[mid] < n: look_in = (mid + 1, look_in[1]);
        elif a[mid] > n: look_in = (look_in[0], mid);
        mid = ((look_in[1] + look_in[0]) // 2)

# ============================================================================================
# ============================================================================================
# Below some O(N) versions # =================================================================
# ============================================================================================
# ============================================================================================

# def find_occurrences(array: List[int], n: int) -> int:
#     return len([x for x in array[:n*5:-1] if x == n])

# def find_occurrences(array: List[int], n: int) -> int: #0.376s
#     new_dict = dict()
#     for x in array:
#         new_dict[x] = new_dict.get(x, 0) + 1
#     return new_dict[n]

# def find_occurrences(array: List[int], n: int) -> int: #0.4449s
#     new_dict = dict()
#     for x in array:
#         new_dict[x] = new_dict.get(x, 0) + 1
#     return new_dict[n]

# def find_occurrences(array: List[int], n: int) -> int: #0.0099s
#     counter = 0
#     for x in array:
#         if x == n:
#             counter += 1
#     return counter

# def find_occurrences(array: List[int], n: int) -> int: #0.0097s
#     counter = len([x for x in array if x == n])
#     return counter

# def find_occurrences(array: List[int], n: int) -> int: #0.0098s
#     return len([x for x in array if x == n])

# def find_occurrences(array: List[int], n: int) -> int: #0.0106s
#     counter = 0
#     end = len(array)
#     x = 0
#     while x < end:
#         while array[x] == n:
#             counter += 1
#             x += 1
#         if counter > 0:
#             return counter
#         x += 1
        
# def find_occurrences(array: List[int], n: int) -> int: #0.009s
#     counter = 0
#     for x in array[n*5:]:
#         if x == n:
#             counter += 1
#         if x != n and counter > 0:
#             return counter
        
# def find_occurrences(array: List[int], n: int) -> int: #0.0096s
#     i = n * 5
#     j = 1
#     while array[i] < n:
#         i += 1
#     j += i
#     while array[j] == n:
#         j += 1
#     return j - i

# def find_occurrences(array: List[int], n: int) -> int:
#     mid = len(array)
#     while True:
#         mid = mid // 2
#         left, right = array[:mid], array[mid:]
#         if array[mid] > n:
#             array = left
#         else:
#             array = right
#         if array[mid -1] == n or mid <= 1000:
#             return sum(1 for x in array if x == n)

# def find_occurrences(a: List[int], n: int) -> int:
#     return sum([1 for x in a[n*5:n*7] if x == n])

# def find_occurrences(a: List[int], n: int) -> int: # BRANCHLESS (No if statements) #2.47sec
#     c = 0
#     for x in a: c += x == n
#     return c

# def find_occurrences(array: List[int], n: int) -> int: # List Comprehension with sum #2.26sec
#     return sum([1 for x in array if x == n])

# def find_occurrences(array: List[int], n: int) -> int: # List Comprehension with len #2.29sec
#     return len([x for x in array if x == n])

# def find_occurrences(array: List[int], n: int) -> int: # Sum List Comprehension with range(len()) #2.87sec
#     return sum([1 for x in range(len(array)) if array[x] == n])

# def find_occurrences(array: List[int], n: int) -> int: # Len List Comprehension with range(len()) #2.85sec
#     return len([array[x] for x in range(len(array)) if array[x] == n])

# def find_occurrences(array: List[int], n: int) -> int: # For-Loop #2.42 sec
#     counter = 0
#     for x in array:
#         if x == n:
#             counter += 1
#     return counter

# def find_occurrences(array: List[int], n: int) -> int: # For-Loop with range(len()) #2.60 sec
#     counter = 0
#     for x in range(len(array)):
#         if array[x] == n:
#             counter += 1
#     return counter

# def find_occurrences(a: List[int], n: int) -> int: # Branchless While loop (Optimized) #2.34sec
#     c = x = 0; a = a[n*5:]
#     while a[x] <= n: c += a[x] == n; x += 1;
#     return c

# def find_occurrences(a: List[int], n: int) -> int:
#     d = dict()
#     for x in a: d[x] = d.get(x, 0) + 1;
#     return d[n]
        
# def find_occurrences(a: List[int], n: int) -> int:
#     l_len = (len(a) - 1); mid = l_len // 2;
#     while True:
#         if mid <= 1: return 0;
#         elif a[mid] < n: a = a[mid:]; l_len = l_len - mid - 1;
#         elif a[mid] > n: a = a[:mid]; l_len = l_len - mid;
#         elif a[mid] == n:
#             x = 0; y = 0
#             while a[mid + x] == n: x += 1;
#             while a[mid - y] == n: y += 1;
#             return x + y - 1
#         mid = l_len // 2



#PSEUDO:
    #while True (found or explored and not found)
        #if mid is the only element, return
        #if mid is our target:
            #New positional varibles
            #while the current index is still target, move to the right
            #While the current index is still target, move to the left
            # return the sum of times you moved left and right, -1 to account for middle
        #if mid is less than target, next time look on the right side of current mid
        #if mid is more than target, next time look on the left side of current mid
        #calculate mid again, with new numbers. (start index + end index) divided by 2.


# def find_occurrences(array: List[int], n: int) -> int: #0.0795s
#     return len([x for x in array[n:] if x == n])

# def find_occurrences(array: List[int], n: int) -> int: #0.0738s
#     p = [index for index, x in enumerate(array[:n*5:-1]) if x == n]
#     return p[::-1][0] - p[0] + 1

# def find_occurrences(array: List[int], n: int) -> int: 
#     return sum(1 for x in array[n*5:] if x == n)

# def find_occurrences(array: List[int], n: int) -> int: #0.0805s
#     i = 0
#     j = len(array) - 1
#     while array[i] != n or array[j] != n:
#         if array[i] != n:
#             i += 1
#         if array[j] != n:
#             j -= 1
#     return j + 1 - i

# def find_occurrences(array: List[int], n: int) -> int: #0.0092s
#     p = [index for index, x in enumerate(array) if x == n]
#     return p[len(p) -1] - p[0] + 1

# def find_occurrences(array: List[int], n: int) -> int: #0.009s
#     p = [index for index, x in enumerate(array) if x == n]
#     return p[::-1][0] - p[0] + 1

# def find_occurrences(array: List[int], n: int) -> int: #0.2567s
#     return array.count(n)

# def find_occurrences(array: List[int], n: int) -> int: #0.0101s
#     x = 0
#     c = 0
#     while array[x] < n:
#         x += 1
#     while array[x + c] == n:
#         c += 1
#     return c

# def find_occurrences(array: List[int], n: int) -> int: #0.0116s
#     x = 0
#     while array[x] < n:
#         x += 1
#     c = x
#     while array[c] == n:
#         c += 1
#     return c - x

# def find_occurrences(array: List[int], n: int) -> int: #0.0784s
#     x = 0
#     c = 0
#     array = array[n:]
#     while array[x] < n:
#         x += 1
#     while array[x + c] == n:
#         c += 1
#     return c

# def find_occurrences(array: List[int], n: int) -> int: #0.0787s
#     counter = 0
#     for x in array[n:]:
#         if x == n:
#             counter += 1
#         if counter > 0 and x != n:
#             return counter
        
# def find_occurrences(array: List[int], n: int) -> int: #0.081s
#     return len([x for x in array[:n:-1] if x == n])

# def find_occurrences(array: List[int], n: int) -> int: # 0.0807s
#     return len([x for x in array[:n:-1] if x == n])

# def find_occurrences(array: List[int], n: int) -> int: #0.0265s
#     array = array[n*4:]
#     p = [index for index, x in enumerate(array) if x == n]
#     return p[::-1][0] - p[0] + 1