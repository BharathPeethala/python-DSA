nums = [100, 400, 200, 1, 3, 2]
nums = set(nums)
longConsSeq = 0
for num in nums:
    if num-1 in nums:
        continue
    currentLength = 1
    while num+1 in nums:
        num += 1
        currentLength += 1
    longConsSeq = max(longConsSeq, currentLength)

print(longConsSeq)
