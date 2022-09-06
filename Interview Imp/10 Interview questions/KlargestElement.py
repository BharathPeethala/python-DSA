import heapq as heap
# brute force


def brute_force(arr, k):
    for _ in range(k-1):
        arr.remove(max(arr))
    return max(arr)

# sorting approach


def sort_app(arr, k):
    arr.sort()
    return arr[-k]

# heap approach


def heap_approach(arr, k):
    arr = [-i for i in arr]
    heap.heapify(arr)  # n times
    for i in range(k-1):
        heap.heappop(arr)
    return abs(heap.heappop(arr))


print(heap_approach([12, 5, 787, 1, 23], 3))
