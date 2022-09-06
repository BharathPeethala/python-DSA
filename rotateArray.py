arr = [1, 2, 3, 4, 5]
print(arr[-1:])
print(arr[:-1])
print(arr[-1:]+arr[:-1])


def solve(arr, n):
    x = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = x


arr2 = [1, 2, 3, 4, 5, 7, 8, 9]
solve(arr2, len(arr2))
print(*arr2)
