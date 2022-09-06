from collections import deque


def solve(arr, k, n):
    res = list()
    Qi = deque()
    for i in range(k):
        print(Qi)
        while Qi and arr[i] >= arr[Qi[-1]]:
            print(Qi.pop())
        Qi.append(i)
    print(Qi)
    for i in range(k, n):
        res.append(arr[Qi[0]])
        while Qi and Qi[0] <= i-k:
            Qi.popleft()
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    res.append(arr[Qi[0]])

    return res


arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
print(solve(arr, 4, len(arr)))
