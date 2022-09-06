def leaders(arr, N):
    res = list()
    right_max = arr[N-1]
    res.append(right_max)
    for i in range(N-2, -1, -1):
        if right_max <= arr[i]:
            res.append(arr[i])
            right_max = arr[i]
    res.reverse()
    return res


arr = [16, 17, 4, 3, 5, 2]
print(leaders(arr, len(arr)))
