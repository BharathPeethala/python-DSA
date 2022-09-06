

nums = [1, 7, 4, 9, 2, 5]
inc, dec = 1, 1
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        inc = dec+1
    elif nums[i] < nums[i-1]:
        dec = inc+1
print(max(inc, dec)-1)
