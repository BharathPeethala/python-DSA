from bisect import bisect_left, bisect_right
from collections import Counter
import math
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
min_element, max_element = matrix[0][0], matrix[-1][-1]


def less_k(mid_element):
    count = 0
    for row in matrix:
        # print(mid_element)
        count += bisect_right(row, mid_element)
        print(count, mid_element)
    return count


while(min_element < max_element):
    mid_element = (min_element+max_element)//2
    if less_k(mid_element) < k:
        min_element = mid_element+1
    else:
        max_element = mid_element
print(mid_element)


# print(temp)

# sorted(sum(matrix, []))[k-1]
# print(sum(matrix, []))
print(dict(Counter("loveleetcode")))
print(math.log10(45)/math.log10(3))


def binary(n): return format(n, "b").zfill(32)


print(int(str(binary(5))))
