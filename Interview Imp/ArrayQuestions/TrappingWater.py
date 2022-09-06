arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
n = len(arr)
left = [0]*n
right = [0]*n
left[0] = arr[0]
right[n-1] = arr[n-1]
for i in range(1, n):
    left[i] = max(left[i-1], arr[i])
for i in range(n-2, -1, -1):
    right[i] = max(right[i+1], arr[i])

trappingWater = 0
for i in range(n):
    trappingWater += min(left[i], right[i])-arr[i]

print(trappingWater)
