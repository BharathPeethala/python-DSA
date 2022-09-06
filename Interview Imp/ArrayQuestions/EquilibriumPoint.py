arr = [1, 3, 5, 2, 2]
total_sum = sum(arr)
left_sum = 0
equilibrium_point = -1
for i, num in enumerate(arr):
    total_sum -= num
    if left_sum == total_sum:
        equilibrium_point = i
        break
    left_sum += num

print(equilibrium_point)
